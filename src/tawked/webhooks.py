"""Verify the webhooks Tawked sends you, with the standard library's ``hmac``.

Two schemes, kept apart by the secret's form:

- ``tawked``: ``tawked-timestamp`` (milliseconds), ``tawked-signature`` = hex HMAC-SHA256 of
  ``"{timestamp}.{body}"`` keyed with the secret's UTF-8 bytes. Any secret that does not start
  with ``whsec_``.
- ``standard_webhooks``: ``webhook-id``, ``webhook-timestamp`` (seconds), ``webhook-signature`` =
  space-separated ``v1,<base64>`` entries of HMAC-SHA256 over ``"{id}.{timestamp}.{body}"`` keyed
  with the base64-decoded bytes after ``whsec_``. Used by Tawked Email webhook endpoints with
  Standard signing on.

``scheme="auto"`` picks the scheme by the secrets you give, never by the headers that arrive: with a
``whsec_`` secret only Standard Webhooks is checked and its answer stands (no fallback); with other
secrets alone, ``tawked-signature``. Pass the **raw body bytes** as they arrived, never re-serialised JSON.
"""

from __future__ import annotations

import base64
import binascii
import hashlib
import hmac
import json
import re
import secrets as _secrets
import time
from collections.abc import Iterable, Mapping, Sequence
from typing import Any, Literal

from tawked._errors import WebhookVerificationError
from tawked._generated.events import UnknownEvent, WebhookEvent, parse_event

__all__ = [
    "STANDARD_PREFIX",
    "TOLERANCE",
    "Scheme",
    "UnknownEvent",
    "WebhookEvent",
    "WebhookVerificationError",
    "assert_valid",
    "construct_event",
    "new_standard_secret",
    "sign",
    "test_headers",
    "verify",
]

STANDARD_PREFIX = "whsec_"
TOLERANCE = 300

Scheme = Literal["auto", "tawked", "standard_webhooks"]

_TEN = re.compile(r"^\d{10}$")
_THIRTEEN = re.compile(r"^\d{13}$")


def _bytes(payload: bytes | bytearray | memoryview | str) -> bytes:
    if isinstance(payload, str):
        return payload.encode("utf-8")
    return bytes(payload)


def _headers(headers: Mapping[str, str] | Iterable[tuple[str, str]]) -> dict[str, str]:
    items = headers.items() if isinstance(headers, Mapping) else headers
    out: dict[str, str] = {}
    for name, value in items:
        key = str(name).lower().replace("_", "-")
        if key.startswith("http-"):  # Django's request.META spelling: HTTP_TAWKED_SIGNATURE
            key = key[5:]
        out[key] = str(value)
    return out


def _secret_list(secrets: str | Sequence[str]) -> list[str]:
    values = [secrets] if isinstance(secrets, str) else list(secrets)
    return [s.strip() for s in values if isinstance(s, str) and s.strip()]


def _standard_key(secret: str) -> bytes:
    try:
        return base64.b64decode(secret[len(STANDARD_PREFIX) :], validate=True)
    except (binascii.Error, ValueError) as error:
        raise ValueError("a whsec_ secret is whsec_ followed by standard base64") from error


def _standard_signature(secret: str, msg_id: str, timestamp: int, body: bytes) -> str:
    message = f"{msg_id}.{timestamp}.".encode() + body
    digest = hmac.new(_standard_key(secret), message, hashlib.sha256).digest()
    return "v1," + base64.b64encode(digest).decode("ascii")


def _tawked_signature(secret: str, timestamp: str, body: bytes) -> str:
    return hmac.new(
        secret.encode("utf-8"), f"{timestamp}.".encode() + body, hashlib.sha256
    ).hexdigest()


def _reason(
    body: bytes,
    headers: dict[str, str],
    secrets: list[str],
    *,
    tolerance: float,
    scheme: str,
    now: float | None,
) -> str | None:
    now_s = time.time() if now is None else now
    standard = [s for s in secrets if s.startswith(STANDARD_PREFIX)]
    tawked = [s for s in secrets if not s.startswith(STANDARD_PREFIX)]
    has_standard = "webhook-signature" in headers
    has_tawked = "tawked-signature" in headers
    if scheme not in ("auto", "tawked", "standard_webhooks"):
        raise ValueError("scheme is auto, tawked or standard_webhooks")

    # under "auto" the secrets choose the scheme, never the headers; a whsec_ secret means Standard only.
    if scheme == "standard_webhooks" or (scheme == "auto" and standard):
        if not has_standard:
            if scheme == "auto" and has_tawked and not tawked:
                return "no_secret_for_scheme"
            return "missing_header"
        if not standard:
            return "no_secret_for_scheme"
        msg_id = headers.get("webhook-id", "")
        ts = headers.get("webhook-timestamp")
        if not msg_id or ts is None:
            return "missing_header"
        if not _TEN.match(ts):
            return "malformed_header"
        if abs(int(now_s) - int(ts)) > tolerance:
            return "timestamp_out_of_tolerance"
        entries = [e for e in headers["webhook-signature"].strip().split() if e.startswith("v1,")]
        for secret in standard:
            expected = _standard_signature(secret, msg_id, int(ts), body)
            for entry in entries:
                if hmac.compare_digest(expected.encode(), entry.encode()):
                    return None
        return "signature_mismatch"

    if scheme == "tawked" or (scheme == "auto" and tawked):
        if not has_tawked:
            if scheme == "auto" and has_standard:
                return "no_secret_for_scheme"
            return "missing_header"
        if not tawked:
            return "no_secret_for_scheme"
        ts = headers.get("tawked-timestamp")
        if ts is None:
            return "missing_header"
        if not _THIRTEEN.match(ts):
            return "malformed_header"
        if abs(int(now_s * 1000) - int(ts)) > tolerance * 1000:
            return "timestamp_out_of_tolerance"
        given = headers["tawked-signature"].strip().lower()
        for secret in tawked:
            if hmac.compare_digest(_tawked_signature(secret, ts, body).encode(), given.encode()):
                return None
        return "signature_mismatch"

    return "no_secret_for_scheme" if (has_standard or has_tawked) else "missing_header"


def verify(
    payload: bytes | str,
    headers: Mapping[str, str] | Iterable[tuple[str, str]],
    secrets: str | Sequence[str],
    *,
    tolerance: float = TOLERANCE,
    scheme: Scheme = "auto",
    now: float | None = None,
) -> bool:
    """``True`` when the webhook is Tawked's. ``secrets`` is one secret or a list (rotation: the old
    and the new one both pass while you switch). ``now`` (Unix seconds) is for tests."""
    return (
        _reason(
            _bytes(payload),
            _headers(headers),
            _secret_list(secrets),
            tolerance=tolerance,
            scheme=scheme,
            now=now,
        )
        is None
    )


def assert_valid(
    payload: bytes | str,
    headers: Mapping[str, str] | Iterable[tuple[str, str]],
    secrets: str | Sequence[str],
    *,
    tolerance: float = TOLERANCE,
    scheme: Scheme = "auto",
    now: float | None = None,
) -> None:
    """Like :func:`verify`, but raises :class:`WebhookVerificationError` with the ``reason``."""
    reason = _reason(
        _bytes(payload),
        _headers(headers),
        _secret_list(secrets),
        tolerance=tolerance,
        scheme=scheme,
        now=now,
    )
    if reason is not None:
        raise WebhookVerificationError(reason, f"the webhook failed verification: {reason}")


def construct_event(
    payload: bytes | str,
    headers: Mapping[str, str] | Iterable[tuple[str, str]],
    secrets: str | Sequence[str],
    *,
    tolerance: float = TOLERANCE,
    scheme: Scheme = "auto",
    now: float | None = None,
) -> WebhookEvent:
    """Verify, then parse the body into its typed event (``UnknownEvent`` for one this version
    does not know yet: never an exception)."""
    assert_valid(payload, headers, secrets, tolerance=tolerance, scheme=scheme, now=now)
    try:
        data = json.loads(_bytes(payload))
    except ValueError as error:
        raise WebhookVerificationError(
            "malformed_body", "the webhook's body is not JSON"
        ) from error
    if not isinstance(data, dict):
        raise WebhookVerificationError("malformed_body", "the webhook's body is not a JSON object")
    return parse_event(data)


def _scheme_of(secret: str, scheme: str | None) -> str:
    found = "standard_webhooks" if secret.startswith(STANDARD_PREFIX) else "tawked"
    if scheme is not None and scheme != found:
        raise ValueError(
            f"a {'whsec_' if found == 'standard_webhooks' else 'non-whsec_'} secret signs only with {found}"
        )
    return found


def sign(
    payload: bytes | str,
    secret: str,
    timestamp: int | str,
    *,
    scheme: Literal["tawked", "standard_webhooks"] | None = None,
    id: str | None = None,
) -> str:
    """The signature header's value for ``payload``: hex for ``tawked`` (timestamp in ms),
    ``v1,<base64>`` for ``standard_webhooks`` (timestamp in seconds, ``id`` required)."""
    body = _bytes(payload)
    if _scheme_of(secret, scheme) == "standard_webhooks":
        if not id:
            raise ValueError("a Standard Webhooks signature needs the webhook-id (id=...)")
        return _standard_signature(secret, id, int(timestamp), body)
    return _tawked_signature(secret, str(timestamp), body)


def test_headers(
    payload: bytes | str,
    secret: str,
    *,
    scheme: Literal["tawked", "standard_webhooks"] | None = None,
    timestamp: int | None = None,
    id: str | None = None,
    event: str | None = None,
) -> dict[str, str]:
    """Headers that make ``payload`` pass :func:`verify` with ``secret``, for your own tests."""
    if _scheme_of(secret, scheme) == "standard_webhooks":
        ts = int(time.time()) if timestamp is None else int(timestamp)
        msg_id = id or "msg_" + _secrets.token_hex(12)
        return {
            "webhook-id": msg_id,
            "webhook-timestamp": str(ts),
            "webhook-signature": _standard_signature(secret, msg_id, ts, _bytes(payload)),
        }
    ts_ms = str(int(time.time() * 1000) if timestamp is None else int(timestamp))
    headers = {
        "tawked-timestamp": ts_ms,
        "tawked-signature": _tawked_signature(secret, ts_ms, _bytes(payload)),
    }
    if event is None:
        try:
            parsed: Any = json.loads(_bytes(payload))
            event = parsed.get("event") if isinstance(parsed, dict) else None
        except ValueError:
            event = None
    if event:
        headers["tawked-event"] = str(event)
    return headers


def new_standard_secret() -> str:
    """A fresh ``whsec_`` secret (32 random bytes), the form Tawked mints."""
    return STANDARD_PREFIX + base64.b64encode(_secrets.token_bytes(32)).decode("ascii")


test_headers.__test__ = False  # type: ignore[attr-defined]  # not a pytest test
