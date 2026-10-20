"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.endpoints import _PAGE_A_OPERATIONS_SEARCH
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


class AccountOperations:
    """``operations``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def search(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """Search the operations by words (`q`) and area (`area`); each with its method, path, summary, whether it is consequential, and `allowed`: whether this token may call it. When `allowed` is false, `needs` names the permission its person would add on the token's page. The best `limit` matches (default 50) in one answer.

        ``GET /v1/operations``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_OPERATIONS_SEARCH,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate_search(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`search`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_OPERATIONS_SEARCH,
            _PAGE_A_OPERATIONS_SEARCH,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        operation: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One operation in full: its path parameters, the JSON Schema of its body (a write) or its query (a read), `allowed` (whether this token may call it) and `next` (how to call it). When `allowed` is false, `needs` names the permission and `human_action` opens the token's page with it ready to allow.

        ``GET /v1/operations/{operation}``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_OPERATIONS_SHOW,
            path={"operation": operation},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountOperations:
    """``operations``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def search(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """Search the operations by words (`q`) and area (`area`); each with its method, path, summary, whether it is consequential, and `allowed`: whether this token may call it. When `allowed` is false, `needs` names the permission its person would add on the token's page. The best `limit` matches (default 50) in one answer.

        ``GET /v1/operations``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_OPERATIONS_SEARCH,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate_search(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`search`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_OPERATIONS_SEARCH,
            _PAGE_A_OPERATIONS_SEARCH,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        operation: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One operation in full: its path parameters, the JSON Schema of its body (a write) or its query (a read), `allowed` (whether this token may call it) and `next` (how to call it). When `allowed` is false, `needs` names the permission and `human_action` opens the token's page with it ready to allow.

        ``GET /v1/operations/{operation}``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_OPERATIONS_SHOW,
            path={"operation": operation},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )
