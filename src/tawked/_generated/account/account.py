"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountAccountAlertsListParams,
    AccountAccountDocumentUpdateParams,
    AccountAccountEmailConfirmParams,
    AccountAccountEmailSendParams,
    AccountAccountMeUpdateParams,
    AccountAccountProfileUpdateParams,
)
from tawked._generated.endpoints import _PAGE_A_ACCOUNT_ALERTS_LIST, _PAGE_A_ACCOUNT_TOKENS_LIST
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


class AccountAccountAlerts:
    """``account.alerts``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        group: Literal[
            "review",
            "verify",
            "whatsapp",
            "templates",
            "salla",
            "zid",
            "workflows",
            "chat_agent",
            "email",
            "applications",
            "apps",
            "clients",
            "wallet",
            "account",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["unread", "needs"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The alerts this person may read, newest first (an application approved or rejected, a template rejected, a low balance…), each with its kind, data, whether they read it and whether it waits on them (`needs`).

        ``GET /v1/account/alerts``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_ACCOUNT_ALERTS_LIST,
            path={},
            given={
                "application": application,
                "group": group,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountAccountAlertsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        group: Literal[
            "review",
            "verify",
            "whatsapp",
            "templates",
            "salla",
            "zid",
            "workflows",
            "chat_agent",
            "email",
            "applications",
            "apps",
            "clients",
            "wallet",
            "account",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["unread", "needs"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_ACCOUNT_ALERTS_LIST,
            _PAGE_A_ACCOUNT_ALERTS_LIST,
            path={},
            given={
                "application": application,
                "group": group,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountAccountAlertsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def read(
        self,
        notification: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Mark one alert read for this person (others still see it unread); answers ok.

        ``POST /v1/account/alerts/{notification}/read``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_ALERTS_READ,
            path={"notification": notification},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def read_all(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Mark every alert this person may read as read, for them alone; answers ok with how many were marked.

        ``POST /v1/account/alerts/read-all``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_ALERTS_READ_ALL,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccountDocument:
    """``account.document``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        *,
        business_document_number: str,
        business_document_type: Literal["commercial_registration", "freelance_certificate"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the account's business document alone: `business_document_type` (commercial_registration or freelance_certificate) and its `business_document_number`; the owner's alone. Answers the account as account.show does.

        ``PUT /v1/account/document``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_DOCUMENT_UPDATE,
            path={},
            given={
                "business_document_number": business_document_number,
                "business_document_type": business_document_type,
            },
            params=AccountAccountDocumentUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccountEmail:
    """``account.email``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def confirm(
        self,
        *,
        code: str,
        application: str | NotGiven | None = NOT_GIVEN,
        then: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm the pending business e-mail with the code the person received; with `application`, Verify is then turned on for that application. Answers the account as account.show does, and `verify_turned_on_for`.

        ``POST /v1/account/email/confirm``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_EMAIL_CONFIRM,
            path={},
            given={"code": code, "application": application, "then": then},
            params=AccountAccountEmailConfirmParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def forget(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop the business e-mail waiting for its code (to send a code to another address); answers ok.

        ``DELETE /v1/account/email/pending``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_EMAIL_FORGET,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send(
        self,
        *,
        email: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a six-digit code to the business e-mail (an address on the business's own domain); answers the address now pending and when another code may be asked for. The person reads the code and you call account.email.confirm.

        ``POST /v1/account/email/send``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_EMAIL_SEND,
            path={},
            given={"email": email},
            params=AccountAccountEmailSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccountMe:
    """``account.me``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        *,
        name: str,
        email: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save this person's own name and e-mail (a member; the owner saves theirs with account.profile.update). Answers the account as account.show does.

        ``PATCH /v1/account/me``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_ME_UPDATE,
            path={},
            given={"name": name, "email": email},
            params=AccountAccountMeUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccountProfile:
    """``account.profile``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        *,
        business_document_number: str,
        business_document_type: Literal["commercial_registration", "freelance_certificate"] | str,
        contact_name: str,
        contact_email: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the account's profile (contact name, contact e-mail, business document); the owner's alone. Answers the account as account.show does.

        ``PATCH /v1/account/profile``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_PROFILE_UPDATE,
            path={},
            given={
                "business_document_number": business_document_number,
                "business_document_type": business_document_type,
                "contact_name": contact_name,
                "contact_email": contact_email,
            },
            params=AccountAccountProfileUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccountSessions:
    """``account.sessions``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def revoke(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Sign this person out of every console session on every device, and out of the AI assistants they signed in; this token keeps working. Answers ok.

        ``POST /v1/account/sessions/revoke``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_SESSIONS_REVOKE,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccountTokens:
    """``account.tokens``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def activity(
        self,
        token: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The last calls made with an Account API token, newest first: the operation, method and path, the status and error code, the address, the client (user agent), the assistant when it came through the MCP server, and how long it took. Kept 90 days. Your own tokens, or any of the account's for the owner.

        ``GET /v1/account/tokens/{token}/activity``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_TOKENS_ACTIVITY,
            path={"token": token},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The Account API tokens this person may see (their own; the owner sees every token of the account), newest first: name, prefix, permissions, applications, who made it, last use, expiry and revocation. Never the secret.

        ``GET /v1/account/tokens``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_ACCOUNT_TOKENS_LIST,
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
            _E.A_ACCOUNT_TOKENS_LIST,
            _PAGE_A_ACCOUNT_TOKENS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def revoke(
        self,
        token: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Revoke an Account API token: the next call made with it answers 401. Your own, or any of the account's for the owner. Answers the token, revoked.

        ``DELETE /v1/account/tokens/{token}``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_TOKENS_REVOKE,
            path={"token": token},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAccount:
    """``account``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.alerts = AccountAccountAlerts(client)
        self.document = AccountAccountDocument(client)
        self.email = AccountAccountEmail(client)
        self.me = AccountAccountMe(client)
        self.profile = AccountAccountProfile(client)
        self.sessions = AccountAccountSessions(client)
        self.tokens = AccountAccountTokens(client)

    def show(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The account as Settings shows it to this person: the profile (owner only), their own name, e-mail and phone, their role, and the business e-mail's state (confirmed, or a code pending).

        ``GET /v1/account``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_ACCOUNT_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountAlerts:
    """``account.alerts``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        group: Literal[
            "review",
            "verify",
            "whatsapp",
            "templates",
            "salla",
            "zid",
            "workflows",
            "chat_agent",
            "email",
            "applications",
            "apps",
            "clients",
            "wallet",
            "account",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["unread", "needs"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The alerts this person may read, newest first (an application approved or rejected, a template rejected, a low balance…), each with its kind, data, whether they read it and whether it waits on them (`needs`).

        ``GET /v1/account/alerts``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_ACCOUNT_ALERTS_LIST,
            path={},
            given={
                "application": application,
                "group": group,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountAccountAlertsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        group: Literal[
            "review",
            "verify",
            "whatsapp",
            "templates",
            "salla",
            "zid",
            "workflows",
            "chat_agent",
            "email",
            "applications",
            "apps",
            "clients",
            "wallet",
            "account",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["unread", "needs"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_ACCOUNT_ALERTS_LIST,
            _PAGE_A_ACCOUNT_ALERTS_LIST,
            path={},
            given={
                "application": application,
                "group": group,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountAccountAlertsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def read(
        self,
        notification: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Mark one alert read for this person (others still see it unread); answers ok.

        ``POST /v1/account/alerts/{notification}/read``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_ALERTS_READ,
            path={"notification": notification},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def read_all(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Mark every alert this person may read as read, for them alone; answers ok with how many were marked.

        ``POST /v1/account/alerts/read-all``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_ALERTS_READ_ALL,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountDocument:
    """``account.document``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        *,
        business_document_number: str,
        business_document_type: Literal["commercial_registration", "freelance_certificate"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the account's business document alone: `business_document_type` (commercial_registration or freelance_certificate) and its `business_document_number`; the owner's alone. Answers the account as account.show does.

        ``PUT /v1/account/document``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_DOCUMENT_UPDATE,
            path={},
            given={
                "business_document_number": business_document_number,
                "business_document_type": business_document_type,
            },
            params=AccountAccountDocumentUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountEmail:
    """``account.email``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def confirm(
        self,
        *,
        code: str,
        application: str | NotGiven | None = NOT_GIVEN,
        then: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm the pending business e-mail with the code the person received; with `application`, Verify is then turned on for that application. Answers the account as account.show does, and `verify_turned_on_for`.

        ``POST /v1/account/email/confirm``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_EMAIL_CONFIRM,
            path={},
            given={"code": code, "application": application, "then": then},
            params=AccountAccountEmailConfirmParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def forget(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop the business e-mail waiting for its code (to send a code to another address); answers ok.

        ``DELETE /v1/account/email/pending``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_EMAIL_FORGET,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send(
        self,
        *,
        email: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a six-digit code to the business e-mail (an address on the business's own domain); answers the address now pending and when another code may be asked for. The person reads the code and you call account.email.confirm.

        ``POST /v1/account/email/send``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_EMAIL_SEND,
            path={},
            given={"email": email},
            params=AccountAccountEmailSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountMe:
    """``account.me``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        *,
        name: str,
        email: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save this person's own name and e-mail (a member; the owner saves theirs with account.profile.update). Answers the account as account.show does.

        ``PATCH /v1/account/me``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_ME_UPDATE,
            path={},
            given={"name": name, "email": email},
            params=AccountAccountMeUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountProfile:
    """``account.profile``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        *,
        business_document_number: str,
        business_document_type: Literal["commercial_registration", "freelance_certificate"] | str,
        contact_name: str,
        contact_email: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the account's profile (contact name, contact e-mail, business document); the owner's alone. Answers the account as account.show does.

        ``PATCH /v1/account/profile``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_PROFILE_UPDATE,
            path={},
            given={
                "business_document_number": business_document_number,
                "business_document_type": business_document_type,
                "contact_name": contact_name,
                "contact_email": contact_email,
            },
            params=AccountAccountProfileUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountSessions:
    """``account.sessions``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def revoke(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Sign this person out of every console session on every device, and out of the AI assistants they signed in; this token keeps working. Answers ok.

        ``POST /v1/account/sessions/revoke``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_SESSIONS_REVOKE,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccountTokens:
    """``account.tokens``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def activity(
        self,
        token: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The last calls made with an Account API token, newest first: the operation, method and path, the status and error code, the address, the client (user agent), the assistant when it came through the MCP server, and how long it took. Kept 90 days. Your own tokens, or any of the account's for the owner.

        ``GET /v1/account/tokens/{token}/activity``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_TOKENS_ACTIVITY,
            path={"token": token},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The Account API tokens this person may see (their own; the owner sees every token of the account), newest first: name, prefix, permissions, applications, who made it, last use, expiry and revocation. Never the secret.

        ``GET /v1/account/tokens``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_ACCOUNT_TOKENS_LIST,
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
            _E.A_ACCOUNT_TOKENS_LIST,
            _PAGE_A_ACCOUNT_TOKENS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def revoke(
        self,
        token: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Revoke an Account API token: the next call made with it answers 401. Your own, or any of the account's for the owner. Answers the token, revoked.

        ``DELETE /v1/account/tokens/{token}``, permission ``account:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_TOKENS_REVOKE,
            path={"token": token},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAccount:
    """``account``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.alerts = AsyncAccountAccountAlerts(client)
        self.document = AsyncAccountAccountDocument(client)
        self.email = AsyncAccountAccountEmail(client)
        self.me = AsyncAccountAccountMe(client)
        self.profile = AsyncAccountAccountProfile(client)
        self.sessions = AsyncAccountAccountSessions(client)
        self.tokens = AsyncAccountAccountTokens(client)

    async def show(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The account as Settings shows it to this person: the profile (owner only), their own name, e-mail and phone, their role, and the business e-mail's state (confirmed, or a code pending).

        ``GET /v1/account``, permission ``account:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_ACCOUNT_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )
