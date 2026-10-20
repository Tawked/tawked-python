"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountVerifySettingsUpdateParams,
    AccountVerifyTestCheckParams,
    AccountVerifyUsageShowParams,
    AccountVerifyVerificationsListParams,
)
from tawked._generated.endpoints import _PAGE_A_VERIFY_VERIFICATIONS_LIST
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


class AccountVerifySettings:
    """``verify.settings``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's Verify settings (code length, how long a code lives, attempts, rate limits, autofill, the spike guard; the daily spend cap for who sees the money) with each one's bounds, and the pumping guard's pause.

        ``GET /v1/applications/{application}/verify/settings``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_VERIFY_SETTINGS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        *,
        android_app_hash: str | NotGiven | None = NOT_GIVEN,
        autofill_domain: Any | NotGiven = NOT_GIVEN,
        autofill_domain_enabled: bool | NotGiven | None = NOT_GIVEN,
        code_length: int | NotGiven = NOT_GIVEN,
        daily_spend_cap_halalas: int | NotGiven | None = NOT_GIVEN,
        max_attempts: int | NotGiven = NOT_GIVEN,
        max_new_destinations_per_hour: int | NotGiven | None = NOT_GIVEN,
        max_per_hour: int | NotGiven = NOT_GIVEN,
        max_per_ip_per_hour: int | NotGiven | None = NOT_GIVEN,
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change some of the application's Verify settings (only the fields sent; null clears one that may be empty), in the names verify.settings.show answers; answers the settings.

        ``PATCH /v1/applications/{application}/verify/settings``, permission ``verify:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_VERIFY_SETTINGS_UPDATE,
            path={"application": application},
            given={
                "android_app_hash": android_app_hash,
                "autofill_domain": autofill_domain,
                "autofill_domain_enabled": autofill_domain_enabled,
                "code_length": code_length,
                "daily_spend_cap_halalas": daily_spend_cap_halalas,
                "max_attempts": max_attempts,
                "max_new_destinations_per_hour": max_new_destinations_per_hour,
                "max_per_hour": max_per_hour,
                "max_per_ip_per_hour": max_per_ip_per_hour,
                "ttl_seconds": ttl_seconds,
            },
            params=AccountVerifySettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountVerifyTest:
    """``verify.test``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def check(
        self,
        application: str,
        *,
        code: str,
        id: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check the code the owner's phone received for a test verification (`id` from verify.test.send, `code`), as the public API would (POST /v1/verify/check); answers the API's `response` (its `status`: verified or not).

        ``POST /v1/applications/{application}/verify/test/check``, permission ``verify:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_VERIFY_TEST_CHECK,
            path={"application": application},
            given={"code": code, "id": id},
            params=AccountVerifyTestCheckParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test code to the account owner's own phone through the application's test key, as the public API would (POST /v1/verify/start); answers the API's `response`, the key used (its `plaintext` only when this call created it) and `seconds_left`. Then call verify.test.check.

        ``POST /v1/applications/{application}/verify/test/send``, permission ``verify:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_VERIFY_TEST_SEND,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountVerifyUsage:
    """``verify.usage``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        application: str,
        *,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's Verify usage for a `period` (today, 7d, month, 30d; Riyadh time) against the same span before: codes sent, delivered, verified, expired, failed, not delivered (refunded), the verified rate, and what the wallet was charged (`charged_halalas`, for who sees the money).

        ``GET /v1/applications/{application}/verify/usage``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_VERIFY_USAGE_SHOW,
            path={"application": application},
            given={"period": period},
            params=AccountVerifyUsageShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountVerifyVerifications:
    """``verify.verifications``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        application: str,
        *,
        mode: Literal["live", "test"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "sent", "verified", "failed", "expired", "canceled", "waiting"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The application's verification log, newest first, narrowed by `status` (waiting, verified, failed, expired, canceled), `mode` (live, test), `range` (today, 7d, 30d, 90d) and `q`: each code's masked number, status, attempts, key, times; its price for who sees the money.

        ``GET /v1/applications/{application}/verify/verifications``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_VERIFY_VERIFICATIONS_LIST,
            path={"application": application},
            given={"mode": mode, "page": page, "q": q, "range": range, "status": status},
            params=AccountVerifyVerificationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        mode: Literal["live", "test"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "sent", "verified", "failed", "expired", "canceled", "waiting"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_VERIFY_VERIFICATIONS_LIST,
            _PAGE_A_VERIFY_VERIFICATIONS_LIST,
            path={"application": application},
            given={"mode": mode, "page": page, "q": q, "range": range, "status": status},
            params=AccountVerifyVerificationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        verification: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One verification of the application by its id (from verify.test.send or verify.verifications.list): its status, masked number, attempts, key and times; its price for who sees the money.

        ``GET /v1/applications/{application}/verify/verifications/{verification}``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_VERIFY_VERIFICATIONS_SHOW,
            path={"application": application, "verification": verification},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountVerify:
    """``verify``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.settings = AccountVerifySettings(client)
        self.test = AccountVerifyTest(client)
        self.usage = AccountVerifyUsage(client)
        self.verifications = AccountVerifyVerifications(client)


class AsyncAccountVerifySettings:
    """``verify.settings``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's Verify settings (code length, how long a code lives, attempts, rate limits, autofill, the spike guard; the daily spend cap for who sees the money) with each one's bounds, and the pumping guard's pause.

        ``GET /v1/applications/{application}/verify/settings``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_VERIFY_SETTINGS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        *,
        android_app_hash: str | NotGiven | None = NOT_GIVEN,
        autofill_domain: Any | NotGiven = NOT_GIVEN,
        autofill_domain_enabled: bool | NotGiven | None = NOT_GIVEN,
        code_length: int | NotGiven = NOT_GIVEN,
        daily_spend_cap_halalas: int | NotGiven | None = NOT_GIVEN,
        max_attempts: int | NotGiven = NOT_GIVEN,
        max_new_destinations_per_hour: int | NotGiven | None = NOT_GIVEN,
        max_per_hour: int | NotGiven = NOT_GIVEN,
        max_per_ip_per_hour: int | NotGiven | None = NOT_GIVEN,
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change some of the application's Verify settings (only the fields sent; null clears one that may be empty), in the names verify.settings.show answers; answers the settings.

        ``PATCH /v1/applications/{application}/verify/settings``, permission ``verify:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_VERIFY_SETTINGS_UPDATE,
            path={"application": application},
            given={
                "android_app_hash": android_app_hash,
                "autofill_domain": autofill_domain,
                "autofill_domain_enabled": autofill_domain_enabled,
                "code_length": code_length,
                "daily_spend_cap_halalas": daily_spend_cap_halalas,
                "max_attempts": max_attempts,
                "max_new_destinations_per_hour": max_new_destinations_per_hour,
                "max_per_hour": max_per_hour,
                "max_per_ip_per_hour": max_per_ip_per_hour,
                "ttl_seconds": ttl_seconds,
            },
            params=AccountVerifySettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountVerifyTest:
    """``verify.test``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def check(
        self,
        application: str,
        *,
        code: str,
        id: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check the code the owner's phone received for a test verification (`id` from verify.test.send, `code`), as the public API would (POST /v1/verify/check); answers the API's `response` (its `status`: verified or not).

        ``POST /v1/applications/{application}/verify/test/check``, permission ``verify:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_VERIFY_TEST_CHECK,
            path={"application": application},
            given={"code": code, "id": id},
            params=AccountVerifyTestCheckParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test code to the account owner's own phone through the application's test key, as the public API would (POST /v1/verify/start); answers the API's `response`, the key used (its `plaintext` only when this call created it) and `seconds_left`. Then call verify.test.check.

        ``POST /v1/applications/{application}/verify/test/send``, permission ``verify:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_VERIFY_TEST_SEND,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountVerifyUsage:
    """``verify.usage``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        application: str,
        *,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's Verify usage for a `period` (today, 7d, month, 30d; Riyadh time) against the same span before: codes sent, delivered, verified, expired, failed, not delivered (refunded), the verified rate, and what the wallet was charged (`charged_halalas`, for who sees the money).

        ``GET /v1/applications/{application}/verify/usage``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_VERIFY_USAGE_SHOW,
            path={"application": application},
            given={"period": period},
            params=AccountVerifyUsageShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountVerifyVerifications:
    """``verify.verifications``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        application: str,
        *,
        mode: Literal["live", "test"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "sent", "verified", "failed", "expired", "canceled", "waiting"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The application's verification log, newest first, narrowed by `status` (waiting, verified, failed, expired, canceled), `mode` (live, test), `range` (today, 7d, 30d, 90d) and `q`: each code's masked number, status, attempts, key, times; its price for who sees the money.

        ``GET /v1/applications/{application}/verify/verifications``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_VERIFY_VERIFICATIONS_LIST,
            path={"application": application},
            given={"mode": mode, "page": page, "q": q, "range": range, "status": status},
            params=AccountVerifyVerificationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        mode: Literal["live", "test"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "sent", "verified", "failed", "expired", "canceled", "waiting"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_VERIFY_VERIFICATIONS_LIST,
            _PAGE_A_VERIFY_VERIFICATIONS_LIST,
            path={"application": application},
            given={"mode": mode, "page": page, "q": q, "range": range, "status": status},
            params=AccountVerifyVerificationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        verification: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One verification of the application by its id (from verify.test.send or verify.verifications.list): its status, masked number, attempts, key and times; its price for who sees the money.

        ``GET /v1/applications/{application}/verify/verifications/{verification}``, permission ``verify:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_VERIFY_VERIFICATIONS_SHOW,
            path={"application": application, "verification": verification},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountVerify:
    """``verify``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.settings = AsyncAccountVerifySettings(client)
        self.test = AsyncAccountVerifyTest(client)
        self.usage = AsyncAccountVerifyUsage(client)
        self.verifications = AsyncAccountVerifyVerifications(client)
