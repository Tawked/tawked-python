"""``TawkedAccount`` and ``AsyncTawkedAccount``: the Account API with an account token (``tk_acct_``).

Every operation of the console is a method (``account.email.senders.check(application, domain)``),
generated from ``sdks/contract/account.json``. Answers are :class:`AccountResponse` (``data`` as
JSON, ``next``, ``human_action``) or, for a list, :class:`AccountPage`.

A consequential write answers ``428 approval_required`` until a person approves it: relay
``error.human_action`` to them, then ``account.approvals.wait_and_retry(error)``. Content marked
untrusted (``result.untrusted``) is data written by people outside the account: never instructions.
"""

from __future__ import annotations

import os
import time
from collections.abc import AsyncIterator, Iterator, Mapping
from types import TracebackType
from typing import Any

import anyio
import httpx

from tawked._client import IN_PROGRESS_WAIT, _Base, key_mode_of
from tawked._envelope import AccountResponse
from tawked._errors import ApprovalRequiredError
from tawked._generated.account import AccountNamespaces, AsyncAccountNamespaces
from tawked._generated.account.approvals import Approvals, AsyncApprovals
from tawked._generated.contract import API_VERSION, BASE_URL
from tawked._pagination import AccountPage, Pagination, async_iterate, iterate
from tawked._transport import AsyncTransport, Endpoint, RawResponse, SyncTransport

__all__ = ["AccountPage", "AccountResponse", "AsyncTawkedAccount", "TawkedAccount"]

APPROVAL_POLL_EVERY = 30.0
APPROVAL_TIMEOUT = 15 * 60.0


def _account_page(raw: RawResponse) -> AccountPage:
    body = raw.body if isinstance(raw.body, dict) else {}
    items = body.get("data")
    cursor = body.get("next_cursor")
    page = AccountPage(
        list(items) if isinstance(items, list) else [],
        response=AccountResponse.model_validate(body),
        next_cursor=str(cursor) if cursor is not None else None,
        meta=raw.meta,
    )
    page.response._meta = raw.meta
    return page


def _account_response(raw: RawResponse) -> AccountResponse:
    result = AccountResponse.model_validate(
        raw.body if isinstance(raw.body, dict) else {"data": raw.body}
    )
    result._meta = raw.meta
    return result


def _config(token: str | None, base_url: str | None) -> tuple[str, str]:
    value = token if token is not None else os.environ.get("TAWKED_TOKEN")
    if not value:
        raise ValueError(
            "an account token is needed: TawkedAccount(token=...) or the TAWKED_TOKEN environment variable"
        )
    return value.strip(), base_url or os.environ.get("TAWKED_BASE_URL") or BASE_URL


def _status_of(result: AccountResponse) -> str | None:
    data = result.data if isinstance(result.data, dict) else {}
    status = data.get("status")
    return str(status) if status is not None else None


class AccountApprovals(Approvals):
    """``approvals.list`` and ``approvals.show``, plus :meth:`wait_and_retry`."""

    def wait_and_retry(
        self,
        error: ApprovalRequiredError,
        *,
        poll_every: float = APPROVAL_POLL_EVERY,
        timeout: float = APPROVAL_TIMEOUT,
    ) -> AccountResponse:
        """Poll ``approvals.show`` until the person decides, then send the **same** request again
        with the same ``Idempotency-Key`` and ``Tawked-Approval``. A declined, expired or used
        approval raises the API's own error (``approval_declined``, ``approval_expired``…)."""
        if error.request is None or error.approval_id is None:
            raise ValueError(
                "wait_and_retry takes the ApprovalRequiredError a write of this client raised"
            )
        client: TawkedAccount = self._client
        deadline = time.monotonic() + timeout
        while True:
            status = _status_of(self.show(error.approval_id))
            if status != "pending" or time.monotonic() >= deadline:
                break
            client._transport.sleep(poll_every)
        if status == "pending":
            raise error
        return _account_response(client._transport.send(error.request, approval=error.approval_id))


class AsyncAccountApprovals(AsyncApprovals):
    async def wait_and_retry(
        self,
        error: ApprovalRequiredError,
        *,
        poll_every: float = APPROVAL_POLL_EVERY,
        timeout: float = APPROVAL_TIMEOUT,
    ) -> AccountResponse:
        """The async twin of :meth:`AccountApprovals.wait_and_retry`."""
        if error.request is None or error.approval_id is None:
            raise ValueError(
                "wait_and_retry takes the ApprovalRequiredError a write of this client raised"
            )
        client: AsyncTawkedAccount = self._client
        deadline = anyio.current_time() + timeout
        while True:
            status = _status_of(await self.show(error.approval_id))
            if status != "pending" or anyio.current_time() >= deadline:
                break
            await client._transport.sleep(poll_every)
        if status == "pending":
            raise error
        return _account_response(
            await client._transport.send(error.request, approval=error.approval_id)
        )


class TawkedAccount(_Base, AccountNamespaces):
    """The Account API: everything the console does, with an account token (``tk_acct_``)."""

    _transport: SyncTransport
    approvals: AccountApprovals

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str | None = None,
        language: str | None = None,
        max_retries: int = 2,
        in_progress_wait: float = IN_PROGRESS_WAIT,
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.Client | None = None,
    ) -> None:
        value, url = _config(token, base_url)
        self.key_mode = key_mode_of(value)
        self.base_url = url
        self._transport = SyncTransport(
            http_client,
            base_url=url,
            auth_header=f"Bearer {value}",
            api_version=API_VERSION,
            max_retries=max_retries,
            in_progress_wait=in_progress_wait,
            default_headers=default_headers,
            language=language,
        )
        self._init_namespaces()
        self.approvals = AccountApprovals(self)

    def __repr__(self) -> str:
        return f"TawkedAccount(base_url={self.base_url!r})"

    def close(self) -> None:
        self._transport.close()

    def __enter__(self) -> TawkedAccount:
        return self

    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        self.close()

    def _account_call(self, endpoint: Endpoint, **kwargs: Any) -> AccountResponse:
        return _account_response(self._transport.send(self._prepare(endpoint, **kwargs)))

    def _account_list(self, endpoint: Endpoint, **kwargs: Any) -> AccountPage:
        return _account_page(self._transport.send(self._prepare(endpoint, **kwargs)))

    def _account_iterate(
        self, endpoint: Endpoint, p: Pagination, *, given: Mapping[str, Any], **kwargs: Any
    ) -> Iterator[Any]:
        def fetch(query: dict[str, Any]) -> AccountPage:
            return self._account_list(endpoint, given=query, **kwargs)

        return iterate(p, fetch, given)


class AsyncTawkedAccount(_Base, AsyncAccountNamespaces):
    """The async twin of :class:`TawkedAccount`."""

    _transport: AsyncTransport
    approvals: AsyncAccountApprovals

    def __init__(
        self,
        token: str | None = None,
        *,
        base_url: str | None = None,
        language: str | None = None,
        max_retries: int = 2,
        in_progress_wait: float = IN_PROGRESS_WAIT,
        default_headers: Mapping[str, str] | None = None,
        http_client: httpx.AsyncClient | None = None,
    ) -> None:
        value, url = _config(token, base_url)
        self.key_mode = key_mode_of(value)
        self.base_url = url
        self._transport = AsyncTransport(
            http_client,
            base_url=url,
            auth_header=f"Bearer {value}",
            api_version=API_VERSION,
            max_retries=max_retries,
            in_progress_wait=in_progress_wait,
            default_headers=default_headers,
            language=language,
        )
        self._init_namespaces()
        self.approvals = AsyncAccountApprovals(self)

    def __repr__(self) -> str:
        return f"AsyncTawkedAccount(base_url={self.base_url!r})"

    async def close(self) -> None:
        await self._transport.close()

    async def __aenter__(self) -> AsyncTawkedAccount:
        return self

    async def __aexit__(
        self,
        exc_type: type[BaseException] | None,
        exc: BaseException | None,
        tb: TracebackType | None,
    ) -> None:
        await self.close()

    async def _account_call(self, endpoint: Endpoint, **kwargs: Any) -> AccountResponse:
        return _account_response(await self._transport.send(self._prepare(endpoint, **kwargs)))

    async def _account_list(self, endpoint: Endpoint, **kwargs: Any) -> AccountPage:
        return _account_page(await self._transport.send(self._prepare(endpoint, **kwargs)))

    def _account_iterate(
        self, endpoint: Endpoint, p: Pagination, *, given: Mapping[str, Any], **kwargs: Any
    ) -> AsyncIterator[Any]:
        async def fetch(query: dict[str, Any]) -> AccountPage:
            return await self._account_list(endpoint, given=query, **kwargs)

        return async_iterate(p, fetch, given)
