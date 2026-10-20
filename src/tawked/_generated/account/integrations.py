"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountIntegrationsLarmConsentUpdateParams,
    AccountIntegrationsLarmMessagesUpdateParams,
)
from tawked._generated.endpoints import _PAGE_A_INTEGRATIONS_APPS_LIST
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


class AccountIntegrationsApps:
    """``integrations.apps``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def disconnect(
        self,
        application: str,
        connection: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """End a connected app's connection: its key stops at its next call; the templates it made stay the client's and the record is kept. Answers ok.

        ``DELETE /v1/applications/{application}/integrations/apps/{connection}``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_APPS_DISCONNECT,
            path={"application": application, "connection": connection},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the apps connected to the application now: each connection's id, the app (name, host, logo), its state (connected, stopped) and when it was approved and last called.

        ``GET /v1/applications/{application}/integrations/apps``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_INTEGRATIONS_APPS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_INTEGRATIONS_APPS_LIST,
            _PAGE_A_INTEGRATIONS_APPS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        connection: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one connected app's connection: who the app is, its state, what it may do, who approved it and when, and (for who reads Notifications) the messages it sent, the templates it made and its last calls.

        ``GET /v1/applications/{application}/integrations/apps/{connection}``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_APPS_SHOW,
            path={"application": application, "connection": connection},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountIntegrationsLarmConsent:
    """``integrations.larm.consent``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        application: str,
        *,
        attested: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Say (`attested: true`) or withdraw that the Larm store's checkout collects its customers' consent to marketing messages; answers the consent as it stands.

        ``PUT /v1/applications/{application}/integrations/larm/consent``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_LARM_CONSENT_UPDATE,
            path={"application": application},
            given={"attested": attested},
            params=AccountIntegrationsLarmConsentUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationsLarmMessages:
    """``integrations.larm.messages``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        application: str,
        kind: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        statuses: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Switch one of the Larm store's messages on or off (`enabled`), or set which order statuses an order update speaks about (`statuses`: completed, cancelled, refunded, each true or false); answers whether it was on before.

        ``PUT /v1/applications/{application}/integrations/larm/messages/{kind}``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_LARM_MESSAGES_UPDATE,
            path={"application": application, "kind": kind},
            given={"enabled": enabled, "statuses": statuses},
            params=AccountIntegrationsLarmMessagesUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationsLarm:
    """``integrations.larm``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.consent = AccountIntegrationsLarmConsent(client)
        self.messages = AccountIntegrationsLarmMessages(client)

    def disconnect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect the Larm store from the application: Tawked drops its tokens and its webhook subscription, the messages stop, and the record stays. Answers ok. The merchant connects it again by opening Tawked from Larm.

        ``DELETE /v1/applications/{application}/integrations/larm``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_LARM_DISCONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the Larm store linked to the application: the store (name, address, status, the permissions Larm granted, who linked it and when) and its four WhatsApp messages (order confirmed, order status with its three statuses, digital delivery, abandoned cart), each with its switch, its state and the week's count, with the checkout's consent. `store` is null when no Larm store was ever linked.

        ``GET /v1/applications/{application}/integrations/larm``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_LARM_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountIntegrationsSupabase:
    """``integrations.supabase``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def connect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Connect Supabase's Send SMS hook to this application (once; again answers the same connection): answers the hook URL and its secret, and the `human_action` that has the person paste them into Supabase › Auth › Hooks (only they reach their Supabase dashboard).

        ``POST /v1/applications/{application}/integrations/supabase``, permission ``integrations:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_CONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def disconnect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect Supabase: the hook stops sending codes at once and the keys it sent with are revoked; the codes it sent stay in the Verify log. Answers ok.

        ``DELETE /v1/applications/{application}/integrations/supabase``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_DISCONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def secret(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace the hook's secret: a new one made by Tawked (no body), or the one Supabase's hook settings generated (`secret`, `v1,whsec_…`); answers the hook URL and the secret, once.

        ``POST /v1/applications/{application}/integrations/supabase/secret``, permission ``integrations:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_SECRET,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the application's Supabase phone sign-in: how codes go out (live, review: the owner's phone only, blocked), the connection's hook URL, language, last call and outcome, and the last codes it sent.

        ``GET /v1/applications/{application}/integrations/supabase``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def test(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Run the hook as Supabase would for a sign-in on the account owner's own phone: a real code is sent there with the test key; answers the outcome, the hook's status and body, and the request it was given.

        ``POST /v1/applications/{application}/integrations/supabase/test``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_TEST,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the language of the sign-in codes Supabase's hook sends (`lang`: ar or en); answers ok.

        ``PATCH /v1/applications/{application}/integrations/supabase``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_UPDATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationsWoocommerceKeys:
    """``integrations.woocommerce.keys``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make the WooCommerce plugin's key (`mode`: live, or test while the application is in review); answers its plaintext once, and the `human_action` that has the person install the plugin and paste it into its settings. A key of that mode it held before is revoked.

        ``POST /v1/applications/{application}/integrations/woocommerce/keys``, permission ``integrations:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_WOOCOMMERCE_KEYS_CREATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountIntegrationsWoocommerce:
    """``integrations.woocommerce``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.keys = AccountIntegrationsWoocommerceKeys(client)

    def disconnect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect the WooCommerce plugin: every key it holds is revoked and the store stops sending codes and order updates until it gets a new key. Answers how many keys were revoked.

        ``DELETE /v1/applications/{application}/integrations/woocommerce``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_WOOCOMMERCE_DISCONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read where the WooCommerce plugin stands on the application: the plugin's version and download, the live and test keys it holds (prefix, last use), which key may be made now, its last call, what WhatsApp order updates need, its `state` (none, waiting, connected) and `next`.

        ``GET /v1/applications/{application}/integrations/woocommerce``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_WOOCOMMERCE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountIntegrations:
    """``integrations``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.apps = AccountIntegrationsApps(client)
        self.larm = AccountIntegrationsLarm(client)
        self.supabase = AccountIntegrationsSupabase(client)
        self.woocommerce = AccountIntegrationsWoocommerce(client)

    def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read an application's integrations at a glance: its Salla or Zid store, a Larm store linked to it, Supabase phone sign-in (for who reads Verify), the WooCommerce plugin's state (none, waiting, connected) and the connected apps. Open each with its own operation.

        ``GET /v1/applications/{application}/integrations``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_INTEGRATIONS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsApps:
    """``integrations.apps``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def disconnect(
        self,
        application: str,
        connection: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """End a connected app's connection: its key stops at its next call; the templates it made stay the client's and the record is kept. Answers ok.

        ``DELETE /v1/applications/{application}/integrations/apps/{connection}``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_APPS_DISCONNECT,
            path={"application": application, "connection": connection},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the apps connected to the application now: each connection's id, the app (name, host, logo), its state (connected, stopped) and when it was approved and last called.

        ``GET /v1/applications/{application}/integrations/apps``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_INTEGRATIONS_APPS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_INTEGRATIONS_APPS_LIST,
            _PAGE_A_INTEGRATIONS_APPS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        connection: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one connected app's connection: who the app is, its state, what it may do, who approved it and when, and (for who reads Notifications) the messages it sent, the templates it made and its last calls.

        ``GET /v1/applications/{application}/integrations/apps/{connection}``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_APPS_SHOW,
            path={"application": application, "connection": connection},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsLarmConsent:
    """``integrations.larm.consent``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        application: str,
        *,
        attested: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Say (`attested: true`) or withdraw that the Larm store's checkout collects its customers' consent to marketing messages; answers the consent as it stands.

        ``PUT /v1/applications/{application}/integrations/larm/consent``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_LARM_CONSENT_UPDATE,
            path={"application": application},
            given={"attested": attested},
            params=AccountIntegrationsLarmConsentUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsLarmMessages:
    """``integrations.larm.messages``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        application: str,
        kind: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        statuses: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Switch one of the Larm store's messages on or off (`enabled`), or set which order statuses an order update speaks about (`statuses`: completed, cancelled, refunded, each true or false); answers whether it was on before.

        ``PUT /v1/applications/{application}/integrations/larm/messages/{kind}``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_LARM_MESSAGES_UPDATE,
            path={"application": application, "kind": kind},
            given={"enabled": enabled, "statuses": statuses},
            params=AccountIntegrationsLarmMessagesUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsLarm:
    """``integrations.larm``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.consent = AsyncAccountIntegrationsLarmConsent(client)
        self.messages = AsyncAccountIntegrationsLarmMessages(client)

    async def disconnect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect the Larm store from the application: Tawked drops its tokens and its webhook subscription, the messages stop, and the record stays. Answers ok. The merchant connects it again by opening Tawked from Larm.

        ``DELETE /v1/applications/{application}/integrations/larm``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_LARM_DISCONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the Larm store linked to the application: the store (name, address, status, the permissions Larm granted, who linked it and when) and its four WhatsApp messages (order confirmed, order status with its three statuses, digital delivery, abandoned cart), each with its switch, its state and the week's count, with the checkout's consent. `store` is null when no Larm store was ever linked.

        ``GET /v1/applications/{application}/integrations/larm``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_LARM_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsSupabase:
    """``integrations.supabase``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def connect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Connect Supabase's Send SMS hook to this application (once; again answers the same connection): answers the hook URL and its secret, and the `human_action` that has the person paste them into Supabase › Auth › Hooks (only they reach their Supabase dashboard).

        ``POST /v1/applications/{application}/integrations/supabase``, permission ``integrations:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_CONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def disconnect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect Supabase: the hook stops sending codes at once and the keys it sent with are revoked; the codes it sent stay in the Verify log. Answers ok.

        ``DELETE /v1/applications/{application}/integrations/supabase``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_DISCONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def secret(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace the hook's secret: a new one made by Tawked (no body), or the one Supabase's hook settings generated (`secret`, `v1,whsec_…`); answers the hook URL and the secret, once.

        ``POST /v1/applications/{application}/integrations/supabase/secret``, permission ``integrations:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_SECRET,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the application's Supabase phone sign-in: how codes go out (live, review: the owner's phone only, blocked), the connection's hook URL, language, last call and outcome, and the last codes it sent.

        ``GET /v1/applications/{application}/integrations/supabase``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def test(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Run the hook as Supabase would for a sign-in on the account owner's own phone: a real code is sent there with the test key; answers the outcome, the hook's status and body, and the request it was given.

        ``POST /v1/applications/{application}/integrations/supabase/test``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_TEST,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the language of the sign-in codes Supabase's hook sends (`lang`: ar or en); answers ok.

        ``PATCH /v1/applications/{application}/integrations/supabase``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SUPABASE_UPDATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsWoocommerceKeys:
    """``integrations.woocommerce.keys``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make the WooCommerce plugin's key (`mode`: live, or test while the application is in review); answers its plaintext once, and the `human_action` that has the person install the plugin and paste it into its settings. A key of that mode it held before is revoked.

        ``POST /v1/applications/{application}/integrations/woocommerce/keys``, permission ``integrations:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_WOOCOMMERCE_KEYS_CREATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrationsWoocommerce:
    """``integrations.woocommerce``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.keys = AsyncAccountIntegrationsWoocommerceKeys(client)

    async def disconnect(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect the WooCommerce plugin: every key it holds is revoked and the store stops sending codes and order updates until it gets a new key. Answers how many keys were revoked.

        ``DELETE /v1/applications/{application}/integrations/woocommerce``, permission ``integrations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_WOOCOMMERCE_DISCONNECT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read where the WooCommerce plugin stands on the application: the plugin's version and download, the live and test keys it holds (prefix, last use), which key may be made now, its last call, what WhatsApp order updates need, its `state` (none, waiting, connected) and `next`.

        ``GET /v1/applications/{application}/integrations/woocommerce``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_WOOCOMMERCE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountIntegrations:
    """``integrations``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.apps = AsyncAccountIntegrationsApps(client)
        self.larm = AsyncAccountIntegrationsLarm(client)
        self.supabase = AsyncAccountIntegrationsSupabase(client)
        self.woocommerce = AsyncAccountIntegrationsWoocommerce(client)

    async def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read an application's integrations at a glance: its Salla or Zid store, a Larm store linked to it, Supabase phone sign-in (for who reads Verify), the WooCommerce plugin's state (none, waiting, connected) and the connected apps. Open each with its own operation.

        ``GET /v1/applications/{application}/integrations``, permission ``integrations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_INTEGRATIONS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )
