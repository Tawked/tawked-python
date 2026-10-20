"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.endpoints import _PAGE_A_APPROVALS_LIST
from tawked._models import NOT_GIVEN, NotGiven, TawkedParams
from tawked._pagination import AccountPage
from tawked._transport import options
from tawked.attachments import FileInput

if TYPE_CHECKING:
    from tawked.account import AsyncTawkedAccount, TawkedAccount

_ = (
    AsyncIterator,
    Iterator,
    Mapping,
    Sequence,
    datetime,
    Any,
    Literal,
    NOT_GIVEN,
    NotGiven,
    TawkedParams,
    AccountPage,
    AccountResponse,
    FileInput,
)


class AccountApprovals:
    """``approvals``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the approvals this token asked its person for, newest first, each with its status (pending, approved, used, declined, expired, stale), operation, request, `target` (the draft it acts on, as the person saw it) and expiry.

        ``GET /v1/approvals``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_APPROVALS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_APPROVALS_LIST,
            _PAGE_A_APPROVALS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        approval: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one approval this token asked for: its status, what it covers (the request, and `target`: the campaign, automation, auto-attendant, template draft or Radeef it acts on, as the person saw it) and `next`, what to do in that status. Once it is `approved`, send exactly the same request again with the header `Tawked-Approval: <id>`; it runs once.

        ``GET /v1/approvals/{approval}``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_APPROVALS_SHOW,
            path={"approval": approval},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountApprovals:
    """``approvals``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the approvals this token asked its person for, newest first, each with its status (pending, approved, used, declined, expired, stale), operation, request, `target` (the draft it acts on, as the person saw it) and expiry.

        ``GET /v1/approvals``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_APPROVALS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_APPROVALS_LIST,
            _PAGE_A_APPROVALS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        approval: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one approval this token asked for: its status, what it covers (the request, and `target`: the campaign, automation, auto-attendant, template draft or Radeef it acts on, as the person saw it) and `next`, what to do in that status. Once it is `approved`, send exactly the same request again with the header `Tawked-Approval: <id>`; it runs once.

        ``GET /v1/approvals/{approval}``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_APPROVALS_SHOW,
            path={"approval": approval},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


Approvals = AccountApprovals
AsyncApprovals = AsyncAccountApprovals
