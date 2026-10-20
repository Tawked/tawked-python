"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountIntegrationAppsAppsCreateParams,
    AccountIntegrationAppsAppsUpdateParams,
)
from tawked._generated.endpoints import _PAGE_A_INTEGRATION_APPS_APPS_LIST
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


class AccountIntegrationAppsApps:
    """``integration_apps.apps``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        *,
        name_ar: str,
        name_en: str,
        redirect_uris: Sequence[str],
        site_url: str,
        connect_url: str | NotGiven | None = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        logo: FileInput | NotGiven | None = NOT_GIVEN,
        remove_logo: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make an integration app, in testing (open to this account's own applications only); answers it with its client id and its client secret, the secret this once.

        ``POST /v1/integration-apps``, permission ``integration_apps:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_CREATE,
            path={},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "redirect_uris": redirect_uris,
                "site_url": site_url,
                "connect_url": connect_url,
                "description": description,
                "logo": logo,
                "remove_logo": remove_logo,
            },
            params=AccountIntegrationAppsAppsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    def delete(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete an integration app that was never approved, with its test connections (their keys revoked), its requests and its client. Cannot be undone.

        ``DELETE /v1/integration-apps/{app}``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_DELETE,
            path={"app": app},
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
        """List the integration apps this partner account made, newest first: each with its status (testing, in_review, approved, rejected), whether a change waits for Tawked's team, and how many applications it is connected to.

        ``GET /v1/integration-apps``, permission ``integration_apps:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_INTEGRATION_APPS_APPS_LIST,
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
            _E.A_INTEGRATION_APPS_APPS_LIST,
            _PAGE_A_INTEGRATION_APPS_APPS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        app: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one integration app: its status, client id, facts, return addresses, the change that waits for Tawked's team, why it was sent back, what the review still needs (`checklist`) and what may be done now (`can`). Never its secret.

        ``GET /v1/integration-apps/{app}``, permission ``integration_apps:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_SHOW,
            path={"app": app},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def submit(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send an integration app in testing (or sent back) to Tawked's review; answers it in_review. Tawked's team approves it or sends it back with a reason: `next` says how often to read integration_apps.apps.show.

        ``POST /v1/integration-apps/{app}/submit``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_SUBMIT,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        app: str,
        *,
        name_ar: str,
        name_en: str,
        redirect_uris: Sequence[str],
        site_url: str,
        connect_url: str | NotGiven | None = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        logo: FileInput | NotGiven | None = NOT_GIVEN,
        remove_logo: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace an integration app's facts and return addresses; answers the app and `outcome`: saved (at once, while testing or sent back), proposed (approved: the reviewed facts wait for Tawked's team, the approved ones keep working), cancelled (the change that waited was dropped) or unchanged.

        ``PUT /v1/integration-apps/{app}``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_UPDATE,
            path={"app": app},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "redirect_uris": redirect_uris,
                "site_url": site_url,
                "connect_url": connect_url,
                "description": description,
                "logo": logo,
                "remove_logo": remove_logo,
            },
            params=AccountIntegrationAppsAppsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    def withdraw(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take an integration app back from Tawked's review, to testing, so it can be edited; answers the app.

        ``POST /v1/integration-apps/{app}/withdraw``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_WITHDRAW,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationAppsPendingChange:
    """``integration_apps.pending_change``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def cancel(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop the change of an approved integration app that waits for Tawked's team; the approved facts stay. Answers the app.

        ``DELETE /v1/integration-apps/{app}/pending``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_PENDING_CHANGE_CANCEL,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationAppsSecret:
    """``integration_apps.secret``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def renew(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Renew an integration app's client secret: the old one stops at once, so the app's sign-ins fail until it uses the new one. Answers the new secret this once.

        ``POST /v1/integration-apps/{app}/secret``, permission ``integration_apps:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATION_APPS_SECRET_RENEW,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationApps:
    """``integration_apps``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.apps = AccountIntegrationAppsApps(client)
        self.pending_change = AccountIntegrationAppsPendingChange(client)
        self.secret = AccountIntegrationAppsSecret(client)


class AsyncAccountIntegrationAppsApps:
    """``integration_apps.apps``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        *,
        name_ar: str,
        name_en: str,
        redirect_uris: Sequence[str],
        site_url: str,
        connect_url: str | NotGiven | None = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        logo: FileInput | NotGiven | None = NOT_GIVEN,
        remove_logo: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make an integration app, in testing (open to this account's own applications only); answers it with its client id and its client secret, the secret this once.

        ``POST /v1/integration-apps``, permission ``integration_apps:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_CREATE,
            path={},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "redirect_uris": redirect_uris,
                "site_url": site_url,
                "connect_url": connect_url,
                "description": description,
                "logo": logo,
                "remove_logo": remove_logo,
            },
            params=AccountIntegrationAppsAppsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    async def delete(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete an integration app that was never approved, with its test connections (their keys revoked), its requests and its client. Cannot be undone.

        ``DELETE /v1/integration-apps/{app}``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_DELETE,
            path={"app": app},
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
        """List the integration apps this partner account made, newest first: each with its status (testing, in_review, approved, rejected), whether a change waits for Tawked's team, and how many applications it is connected to.

        ``GET /v1/integration-apps``, permission ``integration_apps:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_INTEGRATION_APPS_APPS_LIST,
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
            _E.A_INTEGRATION_APPS_APPS_LIST,
            _PAGE_A_INTEGRATION_APPS_APPS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        app: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one integration app: its status, client id, facts, return addresses, the change that waits for Tawked's team, why it was sent back, what the review still needs (`checklist`) and what may be done now (`can`). Never its secret.

        ``GET /v1/integration-apps/{app}``, permission ``integration_apps:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_SHOW,
            path={"app": app},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def submit(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send an integration app in testing (or sent back) to Tawked's review; answers it in_review. Tawked's team approves it or sends it back with a reason: `next` says how often to read integration_apps.apps.show.

        ``POST /v1/integration-apps/{app}/submit``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_SUBMIT,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        app: str,
        *,
        name_ar: str,
        name_en: str,
        redirect_uris: Sequence[str],
        site_url: str,
        connect_url: str | NotGiven | None = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        logo: FileInput | NotGiven | None = NOT_GIVEN,
        remove_logo: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace an integration app's facts and return addresses; answers the app and `outcome`: saved (at once, while testing or sent back), proposed (approved: the reviewed facts wait for Tawked's team, the approved ones keep working), cancelled (the change that waited was dropped) or unchanged.

        ``PUT /v1/integration-apps/{app}``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_UPDATE,
            path={"app": app},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "redirect_uris": redirect_uris,
                "site_url": site_url,
                "connect_url": connect_url,
                "description": description,
                "logo": logo,
                "remove_logo": remove_logo,
            },
            params=AccountIntegrationAppsAppsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    async def withdraw(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take an integration app back from Tawked's review, to testing, so it can be edited; answers the app.

        ``POST /v1/integration-apps/{app}/withdraw``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_APPS_WITHDRAW,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationAppsPendingChange:
    """``integration_apps.pending_change``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def cancel(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop the change of an approved integration app that waits for Tawked's team; the approved facts stay. Answers the app.

        ``DELETE /v1/integration-apps/{app}/pending``, permission ``integration_apps:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_PENDING_CHANGE_CANCEL,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationAppsSecret:
    """``integration_apps.secret``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def renew(
        self,
        app: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Renew an integration app's client secret: the old one stops at once, so the app's sign-ins fail until it uses the new one. Answers the new secret this once.

        ``POST /v1/integration-apps/{app}/secret``, permission ``integration_apps:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATION_APPS_SECRET_RENEW,
            path={"app": app},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationApps:
    """``integration_apps``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.apps = AsyncAccountIntegrationAppsApps(client)
        self.pending_change = AsyncAccountIntegrationAppsPendingChange(client)
        self.secret = AsyncAccountIntegrationAppsSecret(client)
