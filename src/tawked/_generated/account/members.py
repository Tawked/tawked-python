"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountMembersMembersCreateParams,
    AccountMembersMembersUpdateParams,
)
from tawked._generated.endpoints import _PAGE_A_MEMBERS_MEMBERS_LIST
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


class AccountMembersMembers:
    """``members.members``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        *,
        name: str,
        phone: str,
        role: Literal["admin", "developer", "viewer"] | str,
        access: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        all_applications: bool | NotGiven = NOT_GIVEN,
        clients_access: Literal["none", "read", "manage"] | str | NotGiven = NOT_GIVEN,
        email: str | NotGiven | None = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a member by `name` and `phone` (a Saudi mobile, 05… or +9665…) with a console `role` and what they manage; answers the member and `sign_in`, the message to send them, written in your person's language or `language` (ar or en). Tawked sends nothing.

        ``POST /v1/account/members``, permission ``members:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_MEMBERS_MEMBERS_CREATE,
            path={},
            given={
                "name": name,
                "phone": phone,
                "role": role,
                "access": access,
                "all_applications": all_applications,
                "clients_access": clients_access,
                "email": email,
                "language": language,
            },
            params=AccountMembersMembersCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        member: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a member from the console: their role and access go (and their saved cards); someone who also answers in Tawked Chat stays on their support teams (chat.team.remove takes them off). Answers ok.

        ``DELETE /v1/account/members/{member}``, permission ``members:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_MEMBERS_MEMBERS_DELETE,
            path={"member": member},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the account's people who manage on tawked.com (the owner first, then each member with their role and what they manage); `application` narrows to who manages that application.

        ``GET /v1/account/members``, permission ``members:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_MEMBERS_MEMBERS_LIST,
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
            _E.A_MEMBERS_MEMBERS_LIST,
            _PAGE_A_MEMBERS_MEMBERS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        member: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One member: role, every application or the chosen ones with their products, Clients access on a partner account, last sign-in, and whether you may change them.

        ``GET /v1/account/members/{member}``, permission ``members:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_MEMBERS_MEMBERS_SHOW,
            path={"member": member},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        member: str,
        *,
        name: str,
        role: Literal["admin", "developer", "viewer"] | str,
        access: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        all_applications: bool | NotGiven = NOT_GIVEN,
        clients_access: Literal["none", "read", "manage"] | str | NotGiven = NOT_GIVEN,
        email: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a member's name, e-mail, role and what they manage (the phone never changes: it is how they sign in); answers the member.

        ``PATCH /v1/account/members/{member}``, permission ``members:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_MEMBERS_MEMBERS_UPDATE,
            path={"member": member},
            given={
                "name": name,
                "role": role,
                "access": access,
                "all_applications": all_applications,
                "clients_access": clients_access,
                "email": email,
            },
            params=AccountMembersMembersUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountMembers:
    """``members``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.members = AccountMembersMembers(client)


class AsyncAccountMembersMembers:
    """``members.members``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        *,
        name: str,
        phone: str,
        role: Literal["admin", "developer", "viewer"] | str,
        access: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        all_applications: bool | NotGiven = NOT_GIVEN,
        clients_access: Literal["none", "read", "manage"] | str | NotGiven = NOT_GIVEN,
        email: str | NotGiven | None = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a member by `name` and `phone` (a Saudi mobile, 05… or +9665…) with a console `role` and what they manage; answers the member and `sign_in`, the message to send them, written in your person's language or `language` (ar or en). Tawked sends nothing.

        ``POST /v1/account/members``, permission ``members:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_MEMBERS_MEMBERS_CREATE,
            path={},
            given={
                "name": name,
                "phone": phone,
                "role": role,
                "access": access,
                "all_applications": all_applications,
                "clients_access": clients_access,
                "email": email,
                "language": language,
            },
            params=AccountMembersMembersCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        member: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a member from the console: their role and access go (and their saved cards); someone who also answers in Tawked Chat stays on their support teams (chat.team.remove takes them off). Answers ok.

        ``DELETE /v1/account/members/{member}``, permission ``members:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_MEMBERS_MEMBERS_DELETE,
            path={"member": member},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the account's people who manage on tawked.com (the owner first, then each member with their role and what they manage); `application` narrows to who manages that application.

        ``GET /v1/account/members``, permission ``members:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_MEMBERS_MEMBERS_LIST,
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
            _E.A_MEMBERS_MEMBERS_LIST,
            _PAGE_A_MEMBERS_MEMBERS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        member: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One member: role, every application or the chosen ones with their products, Clients access on a partner account, last sign-in, and whether you may change them.

        ``GET /v1/account/members/{member}``, permission ``members:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_MEMBERS_MEMBERS_SHOW,
            path={"member": member},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        member: str,
        *,
        name: str,
        role: Literal["admin", "developer", "viewer"] | str,
        access: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        all_applications: bool | NotGiven = NOT_GIVEN,
        clients_access: Literal["none", "read", "manage"] | str | NotGiven = NOT_GIVEN,
        email: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a member's name, e-mail, role and what they manage (the phone never changes: it is how they sign in); answers the member.

        ``PATCH /v1/account/members/{member}``, permission ``members:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_MEMBERS_MEMBERS_UPDATE,
            path={"member": member},
            given={
                "name": name,
                "role": role,
                "access": access,
                "all_applications": all_applications,
                "clients_access": clients_access,
                "email": email,
            },
            params=AccountMembersMembersUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountMembers:
    """``members``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.members = AsyncAccountMembersMembers(client)
