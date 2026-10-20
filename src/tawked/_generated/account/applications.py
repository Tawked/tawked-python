"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountApplicationsAppealsCreateParams,
    AccountApplicationsApplicationsCreateParams,
    AccountApplicationsApplicationsDeleteParams,
    AccountApplicationsApplicationsUpdateParams,
    AccountApplicationsKeysCreateParams,
    AccountApplicationsLogoUploadParams,
    AccountApplicationsProductsAddParams,
    AccountApplicationsWebhookDeliveriesListParams,
    AccountApplicationsWebhooksCreateParams,
    AccountApplicationsWebhooksRotateSecretParams,
    AccountApplicationsWebhooksTestParams,
    AccountApplicationsWebhooksUpdateParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_APPLICATIONS_APPLICATIONS_LIST,
    _PAGE_A_APPLICATIONS_KEYS_LIST,
    _PAGE_A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
    _PAGE_A_APPLICATIONS_WEBHOOKS_LIST,
)
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


class AccountApplicationsAppeals:
    """``applications.appeals``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        note: str,
        document: FileInput | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Appeal Tawked's rejection of the application with a `note` (and optionally a multipart `document`, up to 10 MB): it goes back to review; answers the application and `next`.

        ``POST /v1/applications/{application}/appeal``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPEALS_CREATE,
            path={"application": application},
            given={"note": note, "document": document},
            params=AccountApplicationsAppealsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("document",),
        )


class AccountApplicationsApplications:
    """``applications.applications``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        *,
        industry: Literal[
            "ecommerce",
            "fintech",
            "healthcare",
            "education",
            "logistics",
            "saas",
            "marketplace",
            "other",
        ]
        | str,
        name_ar: str,
        name_en: str,
        products: Sequence[Literal["verify", "notifications", "chat", "email"] | str],
        website_url: str,
        integration: Literal["api", "salla", "both"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create an application (names in Arabic and English, website, industry, products); it enters Tawked's review at once and answers the application with its state and `next` (read applications.applications.show every few hours until the review ends).

        ``POST /v1/applications``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_CREATE,
            path={},
            given={
                "industry": industry,
                "name_ar": name_ar,
                "name_en": name_en,
                "products": products,
                "website_url": website_url,
                "integration": integration,
            },
            params=AccountApplicationsApplicationsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        *,
        confirm_name: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete the application, its name typed to confirm (`confirm_name`, Arabic or English): every key is revoked, its own WhatsApp number disconnected. Cannot be undone.

        ``DELETE /v1/applications/{application}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_DELETE,
            path={"application": application},
            given={"confirm_name": confirm_name},
            params=AccountApplicationsApplicationsDeleteParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the applications this token reaches, newest first: names, logo, products, status and state (working, review, review_flagged, rejected, suspended, paused, disabled, withdrawn), the decision's words, what the person may do.

        ``GET /v1/applications``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_APPLICATIONS_APPLICATIONS_LIST,
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
            _E.A_APPLICATIONS_APPLICATIONS_LIST,
            _PAGE_A_APPLICATIONS_APPLICATIONS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def reapply(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Apply again after withdrawing: the application goes back into Tawked's review queue and the team is told; answers the application and `next` (read applications.applications.show until the review ends).

        ``POST /v1/applications/{application}/reapply``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_REAPPLY,
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
        """One application as its Details page shows it, with its review history: where the review stands, a rejection's reason and appeal, Verify's pause, its WhatsApp number.

        ``GET /v1/applications/{application}``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def unpause(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Lift the pause Verify's pumping guard put on the application (its `paused`), once the spike was looked at; codes go out again. Answers the application.

        ``POST /v1/applications/{application}/unpause``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_UNPAUSE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        *,
        industry: Literal[
            "ecommerce",
            "fintech",
            "healthcare",
            "education",
            "logistics",
            "saas",
            "marketplace",
            "other",
        ]
        | str,
        name_ar: str,
        name_en: str,
        website_url: str,
        integration: Literal["api", "salla", "both"] | str | NotGiven = NOT_GIVEN,
        logo: FileInput | NotGiven | None = NOT_GIVEN,
        remove_logo: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the application's details (both names, website, industry; optionally `remove_logo`): answers the application, whether the change sent it back to Tawked's review, and `next`.

        ``PATCH /v1/applications/{application}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_UPDATE,
            path={"application": application},
            given={
                "industry": industry,
                "name_ar": name_ar,
                "name_en": name_en,
                "website_url": website_url,
                "integration": integration,
                "logo": logo,
                "remove_logo": remove_logo,
            },
            params=AccountApplicationsApplicationsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    def withdraw(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Withdraw the application's review request: it leaves Tawked's queue until applications.applications.reapply; answers the application.

        ``POST /v1/applications/{application}/withdraw``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_WITHDRAW,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountApplicationsKeys:
    """``applications.keys``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        mode: Literal["live", "test"] | str,
        access: Literal["full", "custom"] | str | NotGiven = NOT_GIVEN,
        email_domain_id: str | NotGiven | None = NOT_GIVEN,
        expires_in_days: Literal["30", "90", "180", "365"]
        | str
        | int
        | NotGiven
        | None = NOT_GIVEN,
        inbound: bool | NotGiven | None = NOT_GIVEN,
        ip_allowlist: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        scope: Literal["full", "check"] | str | NotGiven = NOT_GIVEN,
        scopes: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        webhooks: bool | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a Sending API key for the application (`mode` live or test, `name`, `access` full or custom with `scopes` per product, `expires_in_days`, `ip_allowlist`; Email `manage`, `webhooks` true to manage the application's webhook endpoints (the `webhooks:manage` scope), `email_domain_id` for a sending key limited to one domain, `inbound` true to let it read received email (opt-in, live keys only)); answers the key with its `plaintext`, shown this once.

        ``POST /v1/applications/{application}/keys``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_KEYS_CREATE,
            path={"application": application},
            given={
                "mode": mode,
                "access": access,
                "email_domain_id": email_domain_id,
                "expires_in_days": expires_in_days,
                "inbound": inbound,
                "ip_allowlist": ip_allowlist,
                "name": name,
                "scope": scope,
                "scopes": scopes,
                "webhooks": webhooks,
            },
            params=AccountApplicationsKeysCreateParams,
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
        """List the application's Sending API keys, newest first, live and test, revoked ones too: prefix, mode, what each may call, allowlist, last used. Never a secret.

        ``GET /v1/applications/{application}/keys``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_APPLICATIONS_KEYS_LIST,
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
            _E.A_APPLICATIONS_KEYS_LIST,
            _PAGE_A_APPLICATIONS_KEYS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def revoke(
        self,
        application: str,
        key: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Revoke one of the application's keys: every call with it is refused from now on (a connected app's key also ends that connection). Cannot be undone. Answers ok; make a new one with applications.keys.create.

        ``DELETE /v1/applications/{application}/keys/{key}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_KEYS_REVOKE,
            path={"application": application, "key": key},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountApplicationsLogo:
    """``applications.logo``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def remove(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove the application's logo; answers the application.

        ``DELETE /v1/applications/{application}/logo``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_LOGO_REMOVE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def upload(
        self,
        application: str,
        *,
        logo: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload the application's logo (multipart field `logo`, PNG or JPEG); answers the application with its `logo_url`. A logo never sends it back to review.

        ``POST /v1/applications/{application}/logo``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_LOGO_UPLOAD,
            path={"application": application},
            given={"logo": logo},
            params=AccountApplicationsLogoUploadParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )


class AccountApplicationsProducts:
    """``applications.products``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def add(
        self,
        application: str,
        *,
        product: Literal["verify", "notifications", "chat", "email"] | str,
        then: Literal["supabase"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn a product on for the application (`product`: verify, notifications, chat or email); answers the application. Turning one on is intent: each product's own setup follows.

        ``POST /v1/applications/{application}/products``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_PRODUCTS_ADD,
            path={"application": application},
            given={"product": product, "then": then},
            params=AccountApplicationsProductsAddParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountApplicationsWebhookDeliveries:
    """``applications.webhook_deliveries``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        application: str,
        *,
        endpoint: str | NotGiven = NOT_GIVEN,
        event: Literal[
            "verification.verified",
            "verification.failed",
            "verification.expired",
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "email.received",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        log: Literal["all"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The application's webhook delivery log, newest first, narrowed by `status` (pending, delivered, failed), `event` and `endpoint`: each with its attempts, last HTTP code and error, and the payload sent.

        ``GET /v1/applications/{application}/webhook-deliveries``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
            path={"application": application},
            given={
                "endpoint": endpoint,
                "event": event,
                "log": log,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountApplicationsWebhookDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        endpoint: str | NotGiven = NOT_GIVEN,
        event: Literal[
            "verification.verified",
            "verification.failed",
            "verification.expired",
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "email.received",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        log: Literal["all"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
            _PAGE_A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
            path={"application": application},
            given={
                "endpoint": endpoint,
                "event": event,
                "log": log,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountApplicationsWebhookDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def resend(
        self,
        application: str,
        delivery: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a delivered or failed webhook delivery again, as a new delivery to the same endpoint with the same payload and the same event id (your server dedupes on it); answers the new delivery.

        ``POST /v1/applications/{application}/webhook-deliveries/{delivery}/resend``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOK_DELIVERIES_RESEND,
            path={"application": application, "delivery": delivery},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountApplicationsWebhooksReplays:
    """``applications.webhooks.replays``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        application: str,
        endpoint: str,
        replay: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One replay of a webhook endpoint: its `state` (queued, running, done), how many deliveries `matched` and how many were `queued` again, its window.

        ``GET /v1/applications/{application}/webhooks/{endpoint}/replays/{replay}``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_REPLAYS_SHOW,
            path={"application": application, "endpoint": endpoint, "replay": replay},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountApplicationsWebhooks:
    """``applications.webhooks``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.replays = AccountApplicationsWebhooksReplays(client)

    def create(
        self,
        application: str,
        *,
        events: Sequence[
            Literal[
                "verification.verified",
                "verification.failed",
                "verification.expired",
                "message.sent",
                "message.delivered",
                "message.read",
                "message.failed",
                "email.delivered",
                "email.bounced",
                "email.complained",
                "email.failed",
                "email.sent",
                "email.delivery_delayed",
                "email.suppressed",
                "email.scheduled",
                "email.canceled",
                "email.opened",
                "email.clicked",
                "email.received",
                "domain.created",
                "domain.verified",
                "domain.failed",
                "domain.removed",
                "suppression.added",
                "suppression.removed",
            ]
            | str
        ],
        url: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        signing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        standard_webhooks: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a webhook endpoint (`url` https on a public host, `events`, optionally `receives_test`); answers it with its signing `secret` and its Standard Webhooks `standard_secret`, shown this once.

        ``POST /v1/applications/{application}/webhooks``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_CREATE,
            path={"application": application},
            given={
                "events": events,
                "url": url,
                "enabled": enabled,
                "receives_test": receives_test,
                "signing": signing,
                "standard_webhooks": standard_webhooks,
            },
            params=AccountApplicationsWebhooksCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        endpoint: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a webhook endpoint: nothing more is sent to it, and a delivery still waiting stops. Its past deliveries stay in the log (applications.webhook_deliveries.list). Answers ok.

        ``DELETE /v1/applications/{application}/webhooks/{endpoint}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_DELETE,
            path={"application": application, "endpoint": endpoint},
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
        """List the application's webhook endpoints (address, events, on or off, `state` receiving/failing/off, last delivery), with the events it may subscribe to and the most endpoints it may hold.

        ``GET /v1/applications/{application}/webhooks``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_APPLICATIONS_WEBHOOKS_LIST,
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
            _E.A_APPLICATIONS_WEBHOOKS_LIST,
            _PAGE_A_APPLICATIONS_WEBHOOKS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def replay(
        self,
        application: str,
        endpoint: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send an endpoint's deliveries of a window again (`since`, `until` at most 7 days later and within the last 30 days, `status` failed or all, optional `events`), at most 1,000 oldest first, each with its own event id; answers the replay, queued.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/replay``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_REPLAY,
            path={"application": application, "endpoint": endpoint},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def reveal_secret(
        self,
        application: str,
        endpoint: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Answer a webhook endpoint's current signing secret (`secret`); every reveal is recorded.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/reveal-secret``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_REVEAL_SECRET,
            path={"application": application, "endpoint": endpoint},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def rotate_secret(
        self,
        application: str,
        endpoint: str,
        *,
        scheme: Literal["standard", "tawked", "both"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Give a webhook endpoint a new signing secret by `scheme`: `tawked` (the default) a new `tawked-signature` secret, the old one stopping at once, answered as `secret`; `standard` a new Standard Webhooks secret, the old one still signing beside it for 24 hours; or `both`. Answers the new `secrets` once.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/rotate-secret``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_ROTATE_SECRET,
            path={"application": application, "endpoint": endpoint},
            given={"scheme": scheme},
            params=AccountApplicationsWebhooksRotateSecretParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        endpoint: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One webhook endpoint: its address, events, whether it receives, its state and last delivery. Its secret only through applications.webhooks.reveal_secret.

        ``GET /v1/applications/{application}/webhooks/{endpoint}``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_SHOW,
            path={"application": application, "endpoint": endpoint},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def test(
        self,
        application: str,
        endpoint: str,
        *,
        event: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test delivery of one of the endpoint's events (`event`, else its first) to it, marked `"test": true`, with sample data; answers the queued delivery. Read its outcome in applications.webhook_deliveries.list.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/test``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_TEST,
            path={"application": application, "endpoint": endpoint},
            given={"event": event},
            params=AccountApplicationsWebhooksTestParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        endpoint: str,
        *,
        events: Sequence[
            Literal[
                "verification.verified",
                "verification.failed",
                "verification.expired",
                "message.sent",
                "message.delivered",
                "message.read",
                "message.failed",
                "email.delivered",
                "email.bounced",
                "email.complained",
                "email.failed",
                "email.sent",
                "email.delivery_delayed",
                "email.suppressed",
                "email.scheduled",
                "email.canceled",
                "email.opened",
                "email.clicked",
                "email.received",
                "domain.created",
                "domain.verified",
                "domain.failed",
                "domain.removed",
                "suppression.added",
                "suppression.removed",
            ]
            | str
        ],
        url: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        signing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        standard_webhooks: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a webhook endpoint: its `url` and `events` (both sent, as the form does) and, optionally, `enabled` to switch it off or on, `receives_test` and `signing.standard_webhooks`; the secrets stay. Answers the endpoint, with its new `standard_secret` once when Standard signing is turned on for the first time.

        ``PATCH /v1/applications/{application}/webhooks/{endpoint}``, permission ``applications:write``.
        Never retried once sent.
        """
        return self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_UPDATE,
            path={"application": application, "endpoint": endpoint},
            given={
                "events": events,
                "url": url,
                "enabled": enabled,
                "receives_test": receives_test,
                "signing": signing,
                "standard_webhooks": standard_webhooks,
            },
            params=AccountApplicationsWebhooksUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountApplications:
    """``applications``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.appeals = AccountApplicationsAppeals(client)
        self.applications = AccountApplicationsApplications(client)
        self.keys = AccountApplicationsKeys(client)
        self.logo = AccountApplicationsLogo(client)
        self.products = AccountApplicationsProducts(client)
        self.webhook_deliveries = AccountApplicationsWebhookDeliveries(client)
        self.webhooks = AccountApplicationsWebhooks(client)


class AsyncAccountApplicationsAppeals:
    """``applications.appeals``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        note: str,
        document: FileInput | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Appeal Tawked's rejection of the application with a `note` (and optionally a multipart `document`, up to 10 MB): it goes back to review; answers the application and `next`.

        ``POST /v1/applications/{application}/appeal``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPEALS_CREATE,
            path={"application": application},
            given={"note": note, "document": document},
            params=AccountApplicationsAppealsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("document",),
        )


class AsyncAccountApplicationsApplications:
    """``applications.applications``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        *,
        industry: Literal[
            "ecommerce",
            "fintech",
            "healthcare",
            "education",
            "logistics",
            "saas",
            "marketplace",
            "other",
        ]
        | str,
        name_ar: str,
        name_en: str,
        products: Sequence[Literal["verify", "notifications", "chat", "email"] | str],
        website_url: str,
        integration: Literal["api", "salla", "both"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create an application (names in Arabic and English, website, industry, products); it enters Tawked's review at once and answers the application with its state and `next` (read applications.applications.show every few hours until the review ends).

        ``POST /v1/applications``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_CREATE,
            path={},
            given={
                "industry": industry,
                "name_ar": name_ar,
                "name_en": name_en,
                "products": products,
                "website_url": website_url,
                "integration": integration,
            },
            params=AccountApplicationsApplicationsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        *,
        confirm_name: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete the application, its name typed to confirm (`confirm_name`, Arabic or English): every key is revoked, its own WhatsApp number disconnected. Cannot be undone.

        ``DELETE /v1/applications/{application}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_DELETE,
            path={"application": application},
            given={"confirm_name": confirm_name},
            params=AccountApplicationsApplicationsDeleteParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the applications this token reaches, newest first: names, logo, products, status and state (working, review, review_flagged, rejected, suspended, paused, disabled, withdrawn), the decision's words, what the person may do.

        ``GET /v1/applications``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_APPLICATIONS_APPLICATIONS_LIST,
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
            _E.A_APPLICATIONS_APPLICATIONS_LIST,
            _PAGE_A_APPLICATIONS_APPLICATIONS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def reapply(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Apply again after withdrawing: the application goes back into Tawked's review queue and the team is told; answers the application and `next` (read applications.applications.show until the review ends).

        ``POST /v1/applications/{application}/reapply``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_REAPPLY,
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
        """One application as its Details page shows it, with its review history: where the review stands, a rejection's reason and appeal, Verify's pause, its WhatsApp number.

        ``GET /v1/applications/{application}``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def unpause(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Lift the pause Verify's pumping guard put on the application (its `paused`), once the spike was looked at; codes go out again. Answers the application.

        ``POST /v1/applications/{application}/unpause``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_UNPAUSE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        *,
        industry: Literal[
            "ecommerce",
            "fintech",
            "healthcare",
            "education",
            "logistics",
            "saas",
            "marketplace",
            "other",
        ]
        | str,
        name_ar: str,
        name_en: str,
        website_url: str,
        integration: Literal["api", "salla", "both"] | str | NotGiven = NOT_GIVEN,
        logo: FileInput | NotGiven | None = NOT_GIVEN,
        remove_logo: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the application's details (both names, website, industry; optionally `remove_logo`): answers the application, whether the change sent it back to Tawked's review, and `next`.

        ``PATCH /v1/applications/{application}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_UPDATE,
            path={"application": application},
            given={
                "industry": industry,
                "name_ar": name_ar,
                "name_en": name_en,
                "website_url": website_url,
                "integration": integration,
                "logo": logo,
                "remove_logo": remove_logo,
            },
            params=AccountApplicationsApplicationsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    async def withdraw(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Withdraw the application's review request: it leaves Tawked's queue until applications.applications.reapply; answers the application.

        ``POST /v1/applications/{application}/withdraw``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_APPLICATIONS_WITHDRAW,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountApplicationsKeys:
    """``applications.keys``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        mode: Literal["live", "test"] | str,
        access: Literal["full", "custom"] | str | NotGiven = NOT_GIVEN,
        email_domain_id: str | NotGiven | None = NOT_GIVEN,
        expires_in_days: Literal["30", "90", "180", "365"]
        | str
        | int
        | NotGiven
        | None = NOT_GIVEN,
        inbound: bool | NotGiven | None = NOT_GIVEN,
        ip_allowlist: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        scope: Literal["full", "check"] | str | NotGiven = NOT_GIVEN,
        scopes: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        webhooks: bool | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a Sending API key for the application (`mode` live or test, `name`, `access` full or custom with `scopes` per product, `expires_in_days`, `ip_allowlist`; Email `manage`, `webhooks` true to manage the application's webhook endpoints (the `webhooks:manage` scope), `email_domain_id` for a sending key limited to one domain, `inbound` true to let it read received email (opt-in, live keys only)); answers the key with its `plaintext`, shown this once.

        ``POST /v1/applications/{application}/keys``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_KEYS_CREATE,
            path={"application": application},
            given={
                "mode": mode,
                "access": access,
                "email_domain_id": email_domain_id,
                "expires_in_days": expires_in_days,
                "inbound": inbound,
                "ip_allowlist": ip_allowlist,
                "name": name,
                "scope": scope,
                "scopes": scopes,
                "webhooks": webhooks,
            },
            params=AccountApplicationsKeysCreateParams,
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
        """List the application's Sending API keys, newest first, live and test, revoked ones too: prefix, mode, what each may call, allowlist, last used. Never a secret.

        ``GET /v1/applications/{application}/keys``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_APPLICATIONS_KEYS_LIST,
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
            _E.A_APPLICATIONS_KEYS_LIST,
            _PAGE_A_APPLICATIONS_KEYS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def revoke(
        self,
        application: str,
        key: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Revoke one of the application's keys: every call with it is refused from now on (a connected app's key also ends that connection). Cannot be undone. Answers ok; make a new one with applications.keys.create.

        ``DELETE /v1/applications/{application}/keys/{key}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_KEYS_REVOKE,
            path={"application": application, "key": key},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountApplicationsLogo:
    """``applications.logo``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def remove(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove the application's logo; answers the application.

        ``DELETE /v1/applications/{application}/logo``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_LOGO_REMOVE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def upload(
        self,
        application: str,
        *,
        logo: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload the application's logo (multipart field `logo`, PNG or JPEG); answers the application with its `logo_url`. A logo never sends it back to review.

        ``POST /v1/applications/{application}/logo``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_LOGO_UPLOAD,
            path={"application": application},
            given={"logo": logo},
            params=AccountApplicationsLogoUploadParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )


class AsyncAccountApplicationsProducts:
    """``applications.products``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def add(
        self,
        application: str,
        *,
        product: Literal["verify", "notifications", "chat", "email"] | str,
        then: Literal["supabase"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn a product on for the application (`product`: verify, notifications, chat or email); answers the application. Turning one on is intent: each product's own setup follows.

        ``POST /v1/applications/{application}/products``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_PRODUCTS_ADD,
            path={"application": application},
            given={"product": product, "then": then},
            params=AccountApplicationsProductsAddParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountApplicationsWebhookDeliveries:
    """``applications.webhook_deliveries``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        application: str,
        *,
        endpoint: str | NotGiven = NOT_GIVEN,
        event: Literal[
            "verification.verified",
            "verification.failed",
            "verification.expired",
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "email.received",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        log: Literal["all"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The application's webhook delivery log, newest first, narrowed by `status` (pending, delivered, failed), `event` and `endpoint`: each with its attempts, last HTTP code and error, and the payload sent.

        ``GET /v1/applications/{application}/webhook-deliveries``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
            path={"application": application},
            given={
                "endpoint": endpoint,
                "event": event,
                "log": log,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountApplicationsWebhookDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        endpoint: str | NotGiven = NOT_GIVEN,
        event: Literal[
            "verification.verified",
            "verification.failed",
            "verification.expired",
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "email.received",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        log: Literal["all"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
            _PAGE_A_APPLICATIONS_WEBHOOK_DELIVERIES_LIST,
            path={"application": application},
            given={
                "endpoint": endpoint,
                "event": event,
                "log": log,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountApplicationsWebhookDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def resend(
        self,
        application: str,
        delivery: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a delivered or failed webhook delivery again, as a new delivery to the same endpoint with the same payload and the same event id (your server dedupes on it); answers the new delivery.

        ``POST /v1/applications/{application}/webhook-deliveries/{delivery}/resend``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOK_DELIVERIES_RESEND,
            path={"application": application, "delivery": delivery},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountApplicationsWebhooksReplays:
    """``applications.webhooks.replays``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        application: str,
        endpoint: str,
        replay: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One replay of a webhook endpoint: its `state` (queued, running, done), how many deliveries `matched` and how many were `queued` again, its window.

        ``GET /v1/applications/{application}/webhooks/{endpoint}/replays/{replay}``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_REPLAYS_SHOW,
            path={"application": application, "endpoint": endpoint, "replay": replay},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountApplicationsWebhooks:
    """``applications.webhooks``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.replays = AsyncAccountApplicationsWebhooksReplays(client)

    async def create(
        self,
        application: str,
        *,
        events: Sequence[
            Literal[
                "verification.verified",
                "verification.failed",
                "verification.expired",
                "message.sent",
                "message.delivered",
                "message.read",
                "message.failed",
                "email.delivered",
                "email.bounced",
                "email.complained",
                "email.failed",
                "email.sent",
                "email.delivery_delayed",
                "email.suppressed",
                "email.scheduled",
                "email.canceled",
                "email.opened",
                "email.clicked",
                "email.received",
                "domain.created",
                "domain.verified",
                "domain.failed",
                "domain.removed",
                "suppression.added",
                "suppression.removed",
            ]
            | str
        ],
        url: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        signing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        standard_webhooks: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a webhook endpoint (`url` https on a public host, `events`, optionally `receives_test`); answers it with its signing `secret` and its Standard Webhooks `standard_secret`, shown this once.

        ``POST /v1/applications/{application}/webhooks``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_CREATE,
            path={"application": application},
            given={
                "events": events,
                "url": url,
                "enabled": enabled,
                "receives_test": receives_test,
                "signing": signing,
                "standard_webhooks": standard_webhooks,
            },
            params=AccountApplicationsWebhooksCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        endpoint: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a webhook endpoint: nothing more is sent to it, and a delivery still waiting stops. Its past deliveries stay in the log (applications.webhook_deliveries.list). Answers ok.

        ``DELETE /v1/applications/{application}/webhooks/{endpoint}``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_DELETE,
            path={"application": application, "endpoint": endpoint},
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
        """List the application's webhook endpoints (address, events, on or off, `state` receiving/failing/off, last delivery), with the events it may subscribe to and the most endpoints it may hold.

        ``GET /v1/applications/{application}/webhooks``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_APPLICATIONS_WEBHOOKS_LIST,
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
            _E.A_APPLICATIONS_WEBHOOKS_LIST,
            _PAGE_A_APPLICATIONS_WEBHOOKS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def replay(
        self,
        application: str,
        endpoint: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send an endpoint's deliveries of a window again (`since`, `until` at most 7 days later and within the last 30 days, `status` failed or all, optional `events`), at most 1,000 oldest first, each with its own event id; answers the replay, queued.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/replay``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_REPLAY,
            path={"application": application, "endpoint": endpoint},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def reveal_secret(
        self,
        application: str,
        endpoint: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Answer a webhook endpoint's current signing secret (`secret`); every reveal is recorded.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/reveal-secret``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_REVEAL_SECRET,
            path={"application": application, "endpoint": endpoint},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def rotate_secret(
        self,
        application: str,
        endpoint: str,
        *,
        scheme: Literal["standard", "tawked", "both"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Give a webhook endpoint a new signing secret by `scheme`: `tawked` (the default) a new `tawked-signature` secret, the old one stopping at once, answered as `secret`; `standard` a new Standard Webhooks secret, the old one still signing beside it for 24 hours; or `both`. Answers the new `secrets` once.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/rotate-secret``, permission ``applications:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_ROTATE_SECRET,
            path={"application": application, "endpoint": endpoint},
            given={"scheme": scheme},
            params=AccountApplicationsWebhooksRotateSecretParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        endpoint: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One webhook endpoint: its address, events, whether it receives, its state and last delivery. Its secret only through applications.webhooks.reveal_secret.

        ``GET /v1/applications/{application}/webhooks/{endpoint}``, permission ``applications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_SHOW,
            path={"application": application, "endpoint": endpoint},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def test(
        self,
        application: str,
        endpoint: str,
        *,
        event: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test delivery of one of the endpoint's events (`event`, else its first) to it, marked `"test": true`, with sample data; answers the queued delivery. Read its outcome in applications.webhook_deliveries.list.

        ``POST /v1/applications/{application}/webhooks/{endpoint}/test``, permission ``applications:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_TEST,
            path={"application": application, "endpoint": endpoint},
            given={"event": event},
            params=AccountApplicationsWebhooksTestParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        endpoint: str,
        *,
        events: Sequence[
            Literal[
                "verification.verified",
                "verification.failed",
                "verification.expired",
                "message.sent",
                "message.delivered",
                "message.read",
                "message.failed",
                "email.delivered",
                "email.bounced",
                "email.complained",
                "email.failed",
                "email.sent",
                "email.delivery_delayed",
                "email.suppressed",
                "email.scheduled",
                "email.canceled",
                "email.opened",
                "email.clicked",
                "email.received",
                "domain.created",
                "domain.verified",
                "domain.failed",
                "domain.removed",
                "suppression.added",
                "suppression.removed",
            ]
            | str
        ],
        url: str,
        enabled: bool | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        signing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        standard_webhooks: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a webhook endpoint: its `url` and `events` (both sent, as the form does) and, optionally, `enabled` to switch it off or on, `receives_test` and `signing.standard_webhooks`; the secrets stay. Answers the endpoint, with its new `standard_secret` once when Standard signing is turned on for the first time.

        ``PATCH /v1/applications/{application}/webhooks/{endpoint}``, permission ``applications:write``.
        Never retried once sent.
        """
        return await self._client._account_call(
            _E.A_APPLICATIONS_WEBHOOKS_UPDATE,
            path={"application": application, "endpoint": endpoint},
            given={
                "events": events,
                "url": url,
                "enabled": enabled,
                "receives_test": receives_test,
                "signing": signing,
                "standard_webhooks": standard_webhooks,
            },
            params=AccountApplicationsWebhooksUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountApplications:
    """``applications``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.appeals = AsyncAccountApplicationsAppeals(client)
        self.applications = AsyncAccountApplicationsApplications(client)
        self.keys = AsyncAccountApplicationsKeys(client)
        self.logo = AsyncAccountApplicationsLogo(client)
        self.products = AsyncAccountApplicationsProducts(client)
        self.webhook_deliveries = AsyncAccountApplicationsWebhookDeliveries(client)
        self.webhooks = AsyncAccountApplicationsWebhooks(client)
