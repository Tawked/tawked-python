"""Retries, idempotency and timeouts, the same in every language.

A failure is *pre-send* when the connection failed before any request byte left (DNS, refused,
TLS handshake, waiting for a pooled connection): the server cannot have acted, so every class
retries it. It is *after-send* for a read timeout, a connection broken after sending, or a 5xx:
the server may have acted, and today's servers release the key on a 5xx, so only ``safe`` and
``idempotent`` calls retry it.

| class        | pre-send | after-send       | 409 idempotency_in_progress | 429 (Retry-After <= 60 s) | key minted |
|--------------|----------|------------------|-----------------------------|---------------------------|------------|
| safe         | retry    | retry            | n/a                         | retry                     | no         |
| idempotent   | retry    | retry, same key  | wait (30 s window)          | retry                     | yes        |
| write_once   | retry    | no: error has key| wait (30 s window)          | retry                     | yes        |
| never        | retry    | no               | no                          | no                        | no         |

A 429 is waited on when its ``Retry-After`` is 60 s or less, whatever its code (the per-key
throttle, Email's per-second ``rate_limited``); a business limit (``daily_cap_reached``,
``spend_cap_reached``, ...) sends no ``Retry-After`` and fails at once, as in @tawked/sdk and
tawked-php.

The sync and async transports share every decision (``_Decider``); only the loop that sleeps and
sends differs.
"""

from __future__ import annotations

import email.utils
import json
import platform
import random
import re
import time
import uuid
from collections.abc import Callable, Mapping, Sequence
from dataclasses import dataclass, field
from typing import Any

import anyio
import httpx

from tawked._errors import (
    ACCOUNT_ERROR_STATUS,
    APIConnectionError,
    APIError,
    APITimeoutError,
    ApprovalRequiredError,
    UnexpectedResponseError,
    error_class_for,
)
from tawked._models import ResponseMeta
from tawked._version import __version__

__all__ = [
    "AsyncTransport",
    "Endpoint",
    "PreparedRequest",
    "RawResponse",
    "RequestOptions",
    "SyncTransport",
]

_KEY_RE = re.compile(r"^[\x21-\x7E]+$")
IN_PROGRESS_STEPS = (1.0, 2.0, 4.0)
IN_PROGRESS_EVERY = 5.0
RETRY_AFTER_CAP = 60.0
CONNECT_TIMEOUT = 10.0


@dataclass(frozen=True)
class Endpoint:
    """One SDK method's contract entry, generated from ``sdk`` (never edited by hand)."""

    id: str
    surface: str
    method: str
    path: str
    retry: str
    idempotency: str | None = None
    key_max: int = 128
    timeout_s: float = 30.0
    secret: bool = False
    body: str = "none"
    params_in: str = "body"
    response: str = "json"
    documented: Mapping[str, int] = field(default_factory=dict)
    approval: bool = False


@dataclass
class RequestOptions:
    idempotency_key: str | None = None
    timeout: float | None = None
    max_retries: int | None = None
    extra_headers: Mapping[str, str] | None = None


def options(
    idempotency_key: str | None = None,
    timeout: float | None = None,
    max_retries: int | None = None,
    extra_headers: Mapping[str, str] | None = None,
) -> RequestOptions:
    return RequestOptions(
        idempotency_key=idempotency_key,
        timeout=timeout,
        max_retries=max_retries,
        extra_headers=extra_headers,
    )


@dataclass
class PreparedRequest:
    """A request ready to send, kept on an :class:`ApprovalRequiredError` for ``wait_and_retry``."""

    endpoint: Endpoint
    path: str
    query: dict[str, Any] | None = None
    json_body: Any = None
    form: dict[str, Any] | None = None
    multipart_data: list[tuple[str, str]] | None = None
    multipart_files: list[tuple[str, tuple[str, bytes, str]]] | None = None
    idempotency_key: str | None = None
    timeout: float = 30.0
    max_retries: int = 2
    extra_headers: dict[str, str] = field(default_factory=dict)
    boundary: str = field(default_factory=lambda: uuid.uuid4().hex)

    def __repr__(self) -> str:
        return f"PreparedRequest({self.endpoint.method} {self.path}, idempotency_key={self.idempotency_key!r})"


@dataclass
class RawResponse:
    status: int
    headers: httpx.Headers
    body: Any
    content: bytes
    meta: ResponseMeta


@dataclass
class _Retry:
    delay: float
    counts: bool = True  # an attempt of max_retries (in-progress waits do not count)


def user_agent(api_version: str) -> str:
    return f"tawked-python/{__version__} ({platform.python_implementation()}/{platform.python_version()}; api {api_version})"


def _backoff(attempt: int) -> float:
    base: float = min(0.5 * (2**attempt), 8.0)
    return base - base * random.uniform(0, 0.25)  # noqa: S311 (jitter, not a secret)


def _retry_after(headers: httpx.Headers) -> float | None:
    value = headers.get("retry-after")
    if value is None:
        return None
    value = value.strip()
    try:
        return max(0.0, float(value))
    except ValueError:
        pass
    try:
        when = email.utils.parsedate_to_datetime(value)
    except (TypeError, ValueError):
        return None
    return max(0.0, when.timestamp() - time.time())


def _after_send_advice(prepared: PreparedRequest, status_5xx: bool = False) -> str | None:
    """What to do after a failure once the request was sent.

    After a timeout or a broken connection the same key gets the first result if it finished. After
    a 5xx the server has released the key unless the call is ``idempotent`` (the key and the effect
    commit together, so nothing was kept): the same key would run it again, so the caller looks first.
    """
    key = prepared.idempotency_key
    if prepared.endpoint.secret:
        return (
            "the request may have been applied and its secret is shown once: find what it made by its id, "
            "then rotate or revoke it"
        )
    if key and status_5xx and prepared.endpoint.retry != "idempotent":
        return (
            f"Idempotency-Key {key}: the request may have been applied, and Tawked released the key on this 5xx, "
            "so the same key runs it again: check whether it took effect (get or list it by its id or reference) "
            "before calling again"
        )
    if key:
        return f"Idempotency-Key {key}: the request may have been applied; to retry safely call again with idempotency_key={key!r}"
    return None


def _in_progress_message(key: str) -> str:
    return f"`Idempotency-Key {key}` is still being processed: call again with `idempotency_key={key!r}` (not a new key) to get its answer."


def validate_key(key: str, max_length: int) -> str:
    key = key.strip()
    if not (1 <= len(key) <= max_length) or not _KEY_RE.match(key):
        raise ValueError(f"`Idempotency-Key` must be 1-{max_length} printable ASCII characters")
    return key


class _Decider:
    """Every retry decision, shared by the sync and the async loop."""

    def __init__(
        self,
        *,
        base_url: str,
        auth_header: str,
        api_version: str,
        max_retries: int,
        in_progress_wait: float,
        default_headers: Mapping[str, str] | None,
        language: str | None = None,
    ) -> None:
        self.base_url = base_url.rstrip("/")
        self._auth_header = auth_header
        self.api_version = api_version
        self.max_retries = max_retries
        self.in_progress_wait = in_progress_wait
        self.default_headers = dict(default_headers or {})
        self.language = language
        self.sleep_log: list[float] = []

    def __repr__(self) -> str:
        return f"{type(self).__name__}(base_url={self.base_url!r})"

    # ------------------------------------------------------------------ building

    def prepare(
        self,
        endpoint: Endpoint,
        path: str,
        options: RequestOptions | None,
        *,
        query: dict[str, Any] | None = None,
        json_body: Any = None,
        form: dict[str, Any] | None = None,
        multipart: tuple[list[tuple[str, str]], list[tuple[str, tuple[str, bytes, str]]]]
        | None = None,
    ) -> PreparedRequest:
        options = options or RequestOptions()
        key: str | None = None
        if endpoint.idempotency is not None:
            if options.idempotency_key is not None:
                key = validate_key(options.idempotency_key, endpoint.key_max)
            elif endpoint.retry in ("idempotent", "write_once"):
                key = str(uuid.uuid4())
        elif options.idempotency_key is not None:
            raise TypeError(f"{endpoint.id} takes no Idempotency-Key")
        max_retries = self.max_retries if options.max_retries is None else options.max_retries
        if max_retries < 0:
            raise ValueError("max_retries cannot be negative")
        headers = {str(k): str(v) for k, v in (options.extra_headers or {}).items()}
        for name, value in headers.items():
            if "\n" in value or "\r" in value or "\n" in name or "\r" in name:
                raise ValueError(f"header {name!r} must be one line")
        return PreparedRequest(
            endpoint=endpoint,
            path=path,
            query=query or None,
            json_body=json_body,
            form=form,
            multipart_data=multipart[0] if multipart else None,
            multipart_files=multipart[1] if multipart else None,
            idempotency_key=key,
            timeout=float(options.timeout if options.timeout is not None else endpoint.timeout_s),
            max_retries=max_retries,
            extra_headers=headers,
        )

    def build(
        self,
        client: httpx.Client | httpx.AsyncClient,
        prepared: PreparedRequest,
        approval: str | None = None,
    ) -> httpx.Request:
        headers: dict[str, str] = {
            "Accept": "application/json",
            "User-Agent": user_agent(self.api_version),
            **self.default_headers,
        }
        if self._auth_header:
            headers["Authorization"] = self._auth_header
        if self.language and prepared.endpoint.surface == "account":
            headers["Accept-Language"] = self.language
        if prepared.idempotency_key is not None:
            headers["Idempotency-Key"] = prepared.idempotency_key
        if approval is not None:
            headers["Tawked-Approval"] = approval
        headers.update(prepared.extra_headers)
        timeout = httpx.Timeout(prepared.timeout, connect=min(CONNECT_TIMEOUT, prepared.timeout))
        url = self.base_url + prepared.path
        params: Any = _query_params(prepared.query) if prepared.query else None
        method = prepared.endpoint.method
        if prepared.json_body is not None:
            content = json.dumps(
                prepared.json_body, ensure_ascii=False, separators=(",", ":")
            ).encode("utf-8")
            headers["Content-Type"] = "application/json"
            return client.build_request(
                method, url, params=params, headers=headers, content=content, timeout=timeout
            )
        if prepared.form is not None:
            return client.build_request(
                method, url, params=params, headers=headers, data=prepared.form, timeout=timeout
            )
        if prepared.multipart_files:
            headers["Content-Type"] = f"multipart/form-data; boundary={prepared.boundary}"
            return client.build_request(
                method,
                url,
                params=params,
                headers=headers,
                data=_as_dict_list(prepared.multipart_data or []),
                files=prepared.multipart_files,
                timeout=timeout,
            )
        if prepared.multipart_data is not None:
            return _multipart_without_files(
                client, prepared, url, params, headers, prepared.multipart_data, timeout
            )
        return client.build_request(method, url, params=params, headers=headers, timeout=timeout)

    # ------------------------------------------------------------------ deciding

    def on_exception(
        self, prepared: PreparedRequest, error: Exception, attempt: int
    ) -> _Retry | TawkedFailure:
        pre_send = isinstance(
            error,
            (
                httpx.ConnectError,
                httpx.ConnectTimeout,
                httpx.PoolTimeout,
                httpx.UnsupportedProtocol,
            ),
        )
        if pre_send:
            if attempt < prepared.max_retries:
                return _Retry(_backoff(attempt))
            return TawkedFailure(
                APIConnectionError(
                    f"could not reach {self.base_url}: {type(error).__name__} (nothing was sent)",
                    idempotency_key=prepared.idempotency_key,
                    sent=False,
                )
            )
        if prepared.endpoint.retry in ("safe", "idempotent") and attempt < prepared.max_retries:
            return _Retry(_backoff(attempt))
        advice = _after_send_advice(prepared)
        cls = APITimeoutError if isinstance(error, httpx.TimeoutException) else APIConnectionError
        what = (
            f"timed out after {prepared.timeout:g} s"
            if cls is APITimeoutError
            else f"the connection broke after sending ({type(error).__name__})"
        )
        message = (
            f"{advice}. {prepared.endpoint.method} {prepared.path} {what}"
            if advice
            else f"{prepared.endpoint.method} {prepared.path} {what}"
        )
        return TawkedFailure(cls(message, idempotency_key=prepared.idempotency_key, sent=True))

    def on_response(
        self,
        prepared: PreparedRequest,
        response: httpx.Response,
        attempt: int,
        waited: float,
        step: int,
    ) -> _Retry | RawResponse | TawkedFailure:
        status = response.status_code
        meta = self.meta(prepared, response)
        if 200 <= status < 300:
            return self._success(prepared, response, meta)
        body = _json_or_none(response)
        code = _code_of(body, status)
        retry = prepared.endpoint.retry
        if (
            status == 409
            and code == "idempotency_in_progress"
            and retry in ("idempotent", "write_once")
            and prepared.idempotency_key
        ):
            delay = IN_PROGRESS_STEPS[step] if step < len(IN_PROGRESS_STEPS) else IN_PROGRESS_EVERY
            remaining = self.in_progress_wait - waited
            if remaining > 0:
                return _Retry(min(delay, remaining), counts=False)
            error = self.error(prepared, response, body, code)
            error.message = _in_progress_message(prepared.idempotency_key)
            error.args = (
                error.message + (f" (request {error.request_id})" if error.request_id else ""),
            )
            return TawkedFailure(error)
        # A 429 is waited on for the Retry-After it names (<= 60 s), whatever its code: the per-key
        # minute, Email's per-second rate_limited, the Account API's throttle. A business limit
        # (daily_cap_reached, spend_cap_reached, ...) sends none and fails at once, as in
        # @tawked/sdk and tawked-php.
        if status == 429 and retry != "never":
            after = _retry_after(response.headers)
            if after is not None and after <= RETRY_AFTER_CAP and attempt < prepared.max_retries:
                return _Retry(after)
        if status >= 500 and retry in ("safe", "idempotent") and attempt < prepared.max_retries:
            return _Retry(_backoff(attempt))
        error = self.error(prepared, response, body, code)
        if status >= 500:
            advice = _after_send_advice(prepared, status_5xx=True)
            if advice:
                error.advice = advice
                error.args = (f"{advice}. {error}",)
        return TawkedFailure(error)

    def meta(self, prepared: PreparedRequest, response: httpx.Response) -> ResponseMeta:
        return ResponseMeta(
            status=response.status_code,
            request_id=response.headers.get("x-request-id"),
            idempotent_replayed=response.headers.get("idempotent-replayed", "").lower() == "true",
            idempotency_key=prepared.idempotency_key,
            headers={k.lower(): v for k, v in response.headers.items()},
            untrusted=response.headers.get("tawked-untrusted-content", "").lower() == "true",
        )

    def _success(
        self, prepared: PreparedRequest, response: httpx.Response, meta: ResponseMeta
    ) -> RawResponse | TawkedFailure:
        if prepared.endpoint.response == "binary":
            return RawResponse(response.status_code, response.headers, None, response.content, meta)
        if not response.content:
            return RawResponse(response.status_code, response.headers, None, b"", meta)
        try:
            body = json.loads(response.content)
        except ValueError:
            return TawkedFailure(
                UnexpectedResponseError(
                    "the answer is not JSON",
                    status=response.status_code,
                    request_id=meta.request_id,
                    body=response.text[:500],
                )
            )
        return RawResponse(response.status_code, response.headers, body, response.content, meta)

    def error(
        self, prepared: PreparedRequest, response: httpx.Response, body: Any, code: str
    ) -> APIError:
        documented: Mapping[str, int] = prepared.endpoint.documented
        if prepared.endpoint.surface == "account":
            documented = {**ACCOUNT_ERROR_STATUS, **documented}
        www = response.headers.get("www-authenticate")
        cls = error_class_for(code, response.status_code, documented, www)
        message = ""
        if isinstance(body, dict):
            raw = body.get("message") or body.get("error_description")
            message = str(raw) if raw is not None else ""
        scope = None
        if www:
            found = re.search(r'scope="([^"]+)"', www)
            scope = found.group(1) if found else None
        error = cls(
            message or code,
            status=response.status_code,
            code=code,
            request_id=response.headers.get("x-request-id"),
            body=body,
            headers=dict(response.headers),
            retry_after=_retry_after(response.headers),
            idempotency_key=prepared.idempotency_key,
            required_scope=scope,
        )
        if isinstance(error, ApprovalRequiredError):
            error.request = prepared
        return error


class TawkedFailure:
    def __init__(self, error: Exception) -> None:
        self.error = error


def _json_or_none(response: httpx.Response) -> Any:
    try:
        return json.loads(response.content) if response.content else None
    except ValueError:
        return None


def _code_of(body: Any, status: int) -> str:
    if isinstance(body, dict) and isinstance(body.get("error"), str):
        return str(body["error"])
    if status == 429:
        return "too_many_requests"
    if status >= 500:
        return "internal_error"
    return f"http_{status}"


def _query_params(query: Mapping[str, Any]) -> list[tuple[str, str]]:
    out: list[tuple[str, str]] = []
    for name, value in query.items():
        _flatten(name, value, out)
    return out


def _flatten(name: str, value: Any, out: list[tuple[str, str]]) -> None:
    if value is None:
        return
    if isinstance(value, bool):
        out.append((name, "true" if value else "false"))
    elif isinstance(value, Mapping):
        for key, item in value.items():
            _flatten(f"{name}[{key}]", item, out)
    elif isinstance(value, Sequence) and not isinstance(value, (str, bytes)):
        for item in value:
            _flatten(f"{name}[]", item, out)
    else:
        out.append((name, str(value)))


def form_fields(values: Mapping[str, Any]) -> list[tuple[str, str]]:
    """A multipart body's text fields; booleans as ``1``/``0`` (Laravel's reading)."""
    out: list[tuple[str, str]] = []
    for name, value in values.items():
        if isinstance(value, bool):
            out.append((name, "1" if value else "0"))
        else:
            _flatten(name, value, out)
    return out


def _as_dict_list(data: Any) -> Any:
    if isinstance(data, list):
        merged: dict[str, Any] = {}
        for key, value in data:
            if key in merged:
                existing = merged[key]
                merged[key] = (
                    [*existing, value] if isinstance(existing, list) else [existing, value]
                )
            else:
                merged[key] = value
        return merged
    return data


def _multipart_without_files(
    client: httpx.Client | httpx.AsyncClient,
    prepared: PreparedRequest,
    url: str,
    params: Any,
    headers: dict[str, str],
    data: Any,
    timeout: httpx.Timeout,
) -> httpx.Request:
    boundary = prepared.boundary
    parts: list[bytes] = []
    for key, value in data or []:
        parts.append(
            f'--{boundary}\r\nContent-Disposition: form-data; name="{key}"\r\n\r\n'.encode()
            + str(value).encode("utf-8")
            + b"\r\n"
        )
    parts.append(f"--{boundary}--\r\n".encode())
    headers = {**headers, "Content-Type": f"multipart/form-data; boundary={boundary}"}
    return client.build_request(
        prepared.endpoint.method,
        url,
        params=params,
        headers=headers,
        content=b"".join(parts),
        timeout=timeout,
    )


class SyncTransport(_Decider):
    def __init__(self, http_client: httpx.Client | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._own = http_client is None
        self.http = http_client or httpx.Client(follow_redirects=False)
        self.sleep: Callable[[float], None] = time.sleep

    def close(self) -> None:
        if self._own:
            self.http.close()

    def send(self, prepared: PreparedRequest, approval: str | None = None) -> RawResponse:
        attempt = 0
        waited = 0.0
        step = 0
        while True:
            request = self.build(self.http, prepared, approval)
            try:
                response = self.http.send(request)
                response.read()
            except httpx.TransportError as error:
                decision: _Retry | RawResponse | TawkedFailure = self.on_exception(
                    prepared, error, attempt
                )
            else:
                decision = self.on_response(prepared, response, attempt, waited, step)
            if isinstance(decision, RawResponse):
                return decision
            if isinstance(decision, TawkedFailure):
                raise decision.error
            self.sleep_log.append(decision.delay)
            self.sleep(decision.delay)
            if decision.counts:
                attempt += 1
            else:
                waited += decision.delay
                step += 1


class AsyncTransport(_Decider):
    def __init__(self, http_client: httpx.AsyncClient | None = None, **kwargs: Any) -> None:
        super().__init__(**kwargs)
        self._own = http_client is None
        self.http = http_client or httpx.AsyncClient(follow_redirects=False)
        self.sleep: Callable[[float], Any] = anyio.sleep

    async def close(self) -> None:
        if self._own:
            await self.http.aclose()

    async def send(self, prepared: PreparedRequest, approval: str | None = None) -> RawResponse:
        attempt = 0
        waited = 0.0
        step = 0
        while True:
            request = self.build(self.http, prepared, approval)
            try:
                response = await self.http.send(request)
                await response.aread()
            except httpx.TransportError as error:
                decision: _Retry | RawResponse | TawkedFailure = self.on_exception(
                    prepared, error, attempt
                )
            else:
                decision = self.on_response(prepared, response, attempt, waited, step)
            if isinstance(decision, RawResponse):
                return decision
            if isinstance(decision, TawkedFailure):
                raise decision.error
            self.sleep_log.append(decision.delay)
            await self.sleep(decision.delay)
            if decision.counts:
                attempt += 1
            else:
                waited += decision.delay
                step += 1
