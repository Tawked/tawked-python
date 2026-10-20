"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
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


class AccountMe:
    """``me``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Who this token acts for: the person, the account, the token's permissions, the applications it reaches with their products, and `next_steps`: what is left to set up. Call it first.

        ``GET /v1/me``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_ME_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountMe:
    """``me``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Who this token acts for: the person, the account, the token's permissions, the applications it reaches with their products, and `next_steps`: what is left to set up. Call it first.

        ``GET /v1/me``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_ME_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )
