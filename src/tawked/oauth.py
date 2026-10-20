"""Connected apps: send a merchant to approve your app, then exchange the code for its key.

``authorize_url()`` builds the address of ``GET /oauth/authorize`` with PKCE (S256, a fresh
verifier from :mod:`secrets`) and a random ``state``; keep both in the user's session. When the
browser comes back to your ``redirect_uri`` with ``?code=…&state=…``, check ``state`` first, then
call ``exchange_code()`` from your server: it answers the connection's key, once.

The exchange is never retried after it was sent (the code is single-use and the key is answered
once), and waits up to 120 s. ``invalid_grant`` after a timeout means the connection may have been
made: ask the merchant to approve the app again (a new request replaces it).
"""

from __future__ import annotations

import base64
import hashlib
import os
import re
import secrets
from dataclasses import dataclass
from urllib.parse import quote, urlencode

import httpx

from tawked._errors import APIError, OAuthError, RateLimitError
from tawked._generated.contract import API_VERSION, BASE_URL, OAUTH_ERRORS
from tawked._generated.endpoints import OAUTH_TOKEN
from tawked._generated.types import AppConnection
from tawked._models import parse_model
from tawked._transport import AsyncTransport, RequestOptions, SyncTransport

__all__ = [
    "AuthorizeUrl",
    "authorize_url",
    "code_challenge",
    "exchange_code",
    "exchange_code_async",
]

_VERIFIER = re.compile(r"^[A-Za-z0-9\-._~]{43,128}$")


@dataclass(frozen=True)
class AuthorizeUrl:
    """Where to send the merchant's browser, and what to keep in the session until it returns."""

    url: str
    state: str
    code_verifier: str
    code_challenge: str

    def __repr__(self) -> str:
        return f"AuthorizeUrl(url={self.url!r}, state=…, code_verifier=…)"


def code_challenge(code_verifier: str) -> str:
    """base64url (no padding) of SHA-256 of the verifier (RFC 7636 S256)."""
    digest = hashlib.sha256(code_verifier.encode("ascii")).digest()
    return base64.urlsafe_b64encode(digest).rstrip(b"=").decode("ascii")


def authorize_url(
    *,
    client_id: str,
    redirect_uri: str,
    state: str | None = None,
    code_verifier: str | None = None,
    base_url: str | None = None,
) -> AuthorizeUrl:
    """The authorize address with ``response_type=code``, ``state`` and an S256 challenge (no ``scope``)."""
    verifier = code_verifier or secrets.token_urlsafe(32)
    if not _VERIFIER.match(verifier):
        raise ValueError(
            "code_verifier must be 43 to 128 characters of A-Z a-z 0-9 - . _ ~ (RFC 7636 §4.1)"
        )
    state = state or secrets.token_urlsafe(24)
    challenge = code_challenge(verifier)
    query = urlencode(
        {
            "response_type": "code",
            "client_id": client_id,
            "redirect_uri": redirect_uri,
            "state": state,
            "code_challenge": challenge,
            "code_challenge_method": "S256",
        },
        quote_via=quote,
    )
    root = (base_url or os.environ.get("TAWKED_BASE_URL") or BASE_URL).rstrip("/")
    return AuthorizeUrl(
        url=f"{root}/oauth/authorize?{query}",
        state=state,
        code_verifier=verifier,
        code_challenge=challenge,
    )


def _basic(client_id: str, client_secret: str) -> str:
    raw = f"{quote(client_id, safe='')}:{quote(client_secret, safe='')}".encode()
    return "Basic " + base64.b64encode(raw).decode("ascii")


def _form(code: str, redirect_uri: str, code_verifier: str) -> dict[str, str]:
    return {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": redirect_uri,
        "code_verifier": code_verifier,
    }


def _oauth_error(error: APIError) -> Exception:
    body = error.body if isinstance(error.body, dict) else {}
    if isinstance(error, RateLimitError) or not isinstance(body.get("error"), str):
        return error
    code = str(body["error"])
    if code not in OAUTH_ERRORS and error.status < 500:
        return error
    return OAuthError(
        code, body.get("error_description"), status=error.status, request_id=error.request_id
    )


def exchange_code(
    *,
    client_id: str,
    client_secret: str,
    code: str,
    redirect_uri: str,
    code_verifier: str,
    base_url: str | None = None,
    timeout: float | None = None,
    http_client: httpx.Client | None = None,
) -> AppConnection:
    """``POST /oauth/apps/token``: the connection's key (``access_token``), answered once."""
    transport = SyncTransport(
        http_client,
        base_url=base_url or os.environ.get("TAWKED_BASE_URL") or BASE_URL,
        auth_header=_basic(client_id, client_secret),
        api_version=API_VERSION,
        max_retries=2,
        in_progress_wait=0,
        default_headers=None,
    )
    try:
        prepared = transport.prepare(
            OAUTH_TOKEN,
            OAUTH_TOKEN.path,
            RequestOptions(timeout=timeout),
            form=_form(code, redirect_uri, code_verifier),
        )
        try:
            raw = transport.send(prepared)
        except APIError as error:
            raise _oauth_error(error) from None
        return parse_model(AppConnection, raw.body, raw.meta)
    finally:
        transport.close()


async def exchange_code_async(
    *,
    client_id: str,
    client_secret: str,
    code: str,
    redirect_uri: str,
    code_verifier: str,
    base_url: str | None = None,
    timeout: float | None = None,
    http_client: httpx.AsyncClient | None = None,
) -> AppConnection:
    """The async twin of :func:`exchange_code`."""
    transport = AsyncTransport(
        http_client,
        base_url=base_url or os.environ.get("TAWKED_BASE_URL") or BASE_URL,
        auth_header=_basic(client_id, client_secret),
        api_version=API_VERSION,
        max_retries=2,
        in_progress_wait=0,
        default_headers=None,
    )
    try:
        prepared = transport.prepare(
            OAUTH_TOKEN,
            OAUTH_TOKEN.path,
            RequestOptions(timeout=timeout),
            form=_form(code, redirect_uri, code_verifier),
        )
        try:
            raw = await transport.send(prepared)
        except APIError as error:
            raise _oauth_error(error) from None
        return parse_model(AppConnection, raw.body, raw.meta)
    finally:
        await transport.close()
