"""``Tawked`` and ``AsyncTawked``: the product API (``/v1`` with an API key).

The namespaces (``tawked.email.messages``, ``tawked.verify``…) are generated from the contract; this
file wires them to one transport and reads the answers.
"""

from __future__ import annotations

import os
from collections.abc import AsyncIterator, Iterator, Mapping
from types import TracebackType
from typing import Any, TypeVar
from urllib.parse import quote

import httpx

from tawked._generated.contract import API_VERSION, BASE_URL, KEY_PREFIXES
from tawked._generated.resources import AsyncProductNamespaces, ProductNamespaces
from tawked._models import NotGiven, TawkedModel, TawkedParams, build_params, parse_model
from tawked._pagination import Page, Pagination, async_iterate, iterate
from tawked._transport import (
    AsyncTransport,
    Endpoint,
    PreparedRequest,
    RawResponse,
    RequestOptions,
    SyncTransport,
    form_fields,
)
from tawked.attachments import check_attachments, file_part

__all__ = ["AsyncTawked", "Tawked", "key_mode_of"]

M = TypeVar("M", bound=TawkedModel)
I = TypeVar("I")  # noqa: E741

IN_PROGRESS_WAIT = 30.0


def key_mode_of(key: str) -> str:
    """The prefix's name (``live``, ``test``, ``partner``, ``partner_test``, ``account``) or ``unknown``.

    The longest matching prefix wins. There is no "is test key" boolean on purpose: what a test key
    does differs per product (the contract's ``sandbox.notes``).
    """
    best = ("unknown", "")
    for name, prefix in KEY_PREFIXES.items():
        if key.startswith(prefix) and len(prefix) > len(best[1]):
            best = (name, prefix)
    return best[0]


def encode_path(template: str, values: Mapping[str, Any]) -> str:
    path = template
    for name, value in values.items():
        if value is None or isinstance(value, NotGiven) or str(value) == "":
            raise ValueError(f"`{name}` is required in the path {template}")
        path = path.replace("{" + name + "}", quote(str(value), safe=""))
    return path


class _Base:
    """What the sync and async clients share: preparing a request and reading an answer."""

    _transport: SyncTransport | AsyncTransport

    def _prepare(
        self,
        endpoint: Endpoint,
        *,
        path: Mapping[str, Any],
        given: Mapping[str, Any],
        params: type[TawkedParams] | None,
        opts: RequestOptions,
        list_param: tuple[str, Any] | None = None,
        files: tuple[str, ...] = (),
    ) -> PreparedRequest:
        uploads = {
            name: given[name]
            for name in files
            if name in given and not isinstance(given[name], NotGiven)
        }
        values = {k: v for k, v in given.items() if k not in uploads}
        wire = (
            build_params(params, values)
            if params is not None
            else {k: v for k, v in values.items() if not isinstance(v, NotGiven)}
        )
        wire.update(uploads)
        if endpoint.id == "email-send" and isinstance(wire.get("attachments"), list):
            check_attachments(wire["attachments"])
        if list_param is not None:
            name, items = list_param
            wire = {name: [_wire_item(item) for item in items], **wire}
        url = encode_path(endpoint.path, path)
        if endpoint.params_in == "query" or endpoint.method in ("GET", "HEAD"):
            return self._transport.prepare(endpoint, url, opts, query=wire)
        if endpoint.body == "multipart":
            data = {k: v for k, v in wire.items() if k not in files}
            parts = [
                (name, file_part(wire[name], name)) for name in files if wire.get(name) is not None
            ]
            return self._transport.prepare(
                endpoint, url, opts, multipart=(form_fields(data), parts)
            )
        if endpoint.body == "form":
            return self._transport.prepare(
                endpoint, url, opts, form={k: str(v) for k, v in wire.items()}
            )
        if endpoint.body == "none" and not wire:
            return self._transport.prepare(endpoint, url, opts)
        return self._transport.prepare(endpoint, url, opts, json_body=wire)

    @staticmethod
    def _read(model: type[M], raw: RawResponse) -> M:
        return parse_model(model, raw.body if raw.body is not None else {}, raw.meta)

    @staticmethod
    def _page(model: type[M], item: type[I], p: Pagination, raw: RawResponse) -> Page[I]:
        response = parse_model(model, raw.body if raw.body is not None else {}, raw.meta)
        body = raw.body if isinstance(raw.body, dict) else {}
        values = getattr(response, p.items, None)
        items: list[Any] = (
            list(values) if isinstance(values, list) else list(body.get(p.items) or [])
        )
        total = body.get(p.total) if p.total else None
        has_more = body.get(p.has_more) if p.has_more else None
        next_cursor = body.get(p.next) if p.next else None
        return Page(
            items,
            response=response,
            next_cursor=str(next_cursor) if next_cursor is not None else None,
            has_more=bool(has_more) if has_more is not None else None,
            total=int(total) if isinstance(total, int) else None,
            meta=raw.meta,
        )


def _wire_item(item: Any) -> Any:
    if isinstance(item, TawkedParams):
        return item.to_wire()
    if isinstance(item, TawkedModel):
        return item.to_dict()
    return item


def _config(api_key: str | None, base_url: str | None) -> tuple[str, str]:
    key = api_key if api_key is not None else os.environ.get("TAWKED_API_KEY")
    if not key:
        raise ValueError(
            "an API key is needed: Tawked(api_key=...) or the TAWKED_API_KEY environment variable"
        )
    url = base_url or os.environ.get("TAWKED_BASE_URL") or BASE_URL
    return key.strip(), url


class Tawked(_Base, ProductNamespaces):
    """The Tawked API with an API key (``tk_live_``, ``tk_test_``, ``tk_partner_``…).

    >>> tawked = Tawked()  # reads TAWKED_API_KEY
    >>> tawked.email.messages.send(to="sara@example.com", subject="…", text="…", idempotency_key="order-1042-confirmation")
    """

    _transport: SyncTransport

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        max_retries: int = 2,
        in_progress_wait: float = IN_PROGRESS_WAIT,
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        key, url = _config(api_key, base_url)
        self.key_mode = key_mode_of(key)
        self.base_url = url
        self._transport = SyncTransport(
            http_client,
            base_url=url,
            auth_header=f"Bearer {key}",
            api_version=API_VERSION,
            max_retries=max_retries,
            in_progress_wait=in_progress_wait,
            default_headers=default_headers,
        )
        self._init_namespaces()

    def __repr__(self) -> str:
        return f"Tawked(base_url={self.base_url!r}, key_mode={self.key_mode!r})"

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> Tawked:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def _call(self, endpoint: Endpoint, model: type[M], **kwargs: Any) -> M:
        return self._read(model, self._transport.send(self._prepare(endpoint, **kwargs)))

    def _call_binary(self, endpoint: Endpoint, **kwargs: Any) -> bytes:
        return self._transport.send(self._prepare(endpoint, **kwargs)).content

    def _list(
        self, endpoint: Endpoint, model: type[M], item: type[I], p: Pagination, **kwargs: Any
    ) -> Page[I]:
        return self._page(model, item, p, self._transport.send(self._prepare(endpoint, **kwargs)))

    def _iterate(
        self,
        endpoint: Endpoint,
        model: type[M],
        item: type[I],
        p: Pagination,
        *,
        given: Mapping[str, Any],
        **kwargs: Any,
    ) -> Iterator[I]:
        def fetch(query: dict[str, Any]) -> Page[I]:
            return self._list(endpoint, model, item, p, given=query, **kwargs)

        return iterate(p, fetch, given)


class AsyncTawked(_Base, AsyncProductNamespaces):
    """The async twin of :class:`Tawked`: every method is awaited, ``iterate()`` is ``async for``."""

    _transport: AsyncTransport

    def __init__(
        self,
        api_key: str | None = None,
        *,
        base_url: str | None = None,
        max_retries: int = 2,
        in_progress_wait: float = IN_PROGRESS_WAIT,
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        key, url = _config(api_key, base_url)
        self.key_mode = key_mode_of(key)
        self.base_url = url
        self._transport = AsyncTransport(
            http_client,
            base_url=url,
            auth_header=f"Bearer {key}",
            api_version=API_VERSION,
            max_retries=max_retries,
            in_progress_wait=in_progress_wait,
            default_headers=default_headers,
        )
        self._init_namespaces()

    def __repr__(self) -> str:
        return f"AsyncTawked(base_url={self.base_url!r}, key_mode={self.key_mode!r})"

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> AsyncTawked:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def _call(self, endpoint: Endpoint, model: type[M], **kwargs: Any) -> M:
        return self._read(model, await self._transport.send(self._prepare(endpoint, **kwargs)))

    async def _call_binary(self, endpoint: Endpoint, **kwargs: Any) -> bytes:
        return (await self._transport.send(self._prepare(endpoint, **kwargs))).content

    async def _list(
        self, endpoint: Endpoint, model: type[M], item: type[I], p: Pagination, **kwargs: Any
    ) -> Page[I]:
        return self._page(
            model, item, p, await self._transport.send(self._prepare(endpoint, **kwargs))
        )

    def _iterate(
        self,
        endpoint: Endpoint,
        model: type[M],
        item: type[I],
        p: Pagination,
        *,
        given: Mapping[str, Any],
        **kwargs: Any,
    ) -> AsyncIterator[I]:
        async def fetch(query: dict[str, Any]) -> Page[I]:
            return await self._list(endpoint, model, item, p, given=query, **kwargs)

        return async_iterate(p, fetch, given)
