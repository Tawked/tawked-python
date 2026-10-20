"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountClientsApiKeyCreateParams,
    AccountClientsAppealsCreateParams,
    AccountClientsApplicationsBulkApproveParams,
    AccountClientsApplicationsCreateParams,
    AccountClientsApplicationsListParams,
    AccountClientsApplicationsRejectParams,
    AccountClientsApplicationsUpdateParams,
    AccountClientsDeliveriesListParams,
    AccountClientsReviewsListParams,
    AccountClientsUsageShowParams,
    AccountClientsWebhookUpdateParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_CLIENTS_APPLICATIONS_LIST,
    _PAGE_A_CLIENTS_DELIVERIES_LIST,
    _PAGE_A_CLIENTS_REVIEWS_LIST,
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


class AccountClientsApi:
    """``clients.api``."""

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
        """Read the Partner API's state: whether a partner key works (its prefix, expiry and allowlist; never the key), the sandbox key's prefix, the webhook (URL, events, threshold), its health and the newest deliveries.

        ``GET /v1/clients/api``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CLIENTS_API_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountClientsApiKey:
    """``clients.api_key``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        *,
        expires_in_days: Literal["30", "90", "180", "365"]
        | str
        | int
        | NotGiven
        | None = NOT_GIVEN,
        ip_allowlist: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a new partner key (tk_partner_…) for the Partner API; the key that worked until now stops at once. Answers the key's plaintext this once, with its prefix and the prefix of the key it replaced.

        ``POST /v1/clients/api/key``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_API_KEY_CREATE,
            path={},
            given={"expires_in_days": expires_in_days, "ip_allowlist": ip_allowlist},
            params=AccountClientsApiKeyCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountClientsAppeals:
    """``clients.appeals``."""

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
        """Appeal Tawked's rejection of a client application with a note and an optional document (PDF or image, multipart); it goes back to Tawked's review. Your client is never told.

        ``POST /v1/clients/applications/{application}/appeal``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPEALS_CREATE,
            path={"application": application},
            given={"note": note, "document": document},
            params=AccountClientsAppealsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("document",),
        )


class AccountClientsApplications:
    """``clients.applications``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def approve(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Approve a client application that waits on your decision (state awaiting_partner); it starts sending codes. Answers the application.

        ``POST /v1/clients/applications/{application}/approve``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_APPROVE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def archive(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Archive a client application: it stops sending codes, leaves the lists and takes no write but clients.applications.restore. Answers the application.

        ``POST /v1/clients/applications/{application}/archive``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_ARCHIVE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def bulk_approve(
        self,
        *,
        ids: Sequence[str],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Approve at once every listed client application that waits on your decision and whose names were screened clean; answers how many were approved and skipped.

        ``POST /v1/clients/applications/bulk-approve``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_BULK_APPROVE,
            path={},
            given={"ids": ids},
            params=AccountClientsApplicationsBulkApproveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def check_name(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check the names of a client application before creating it: answers the screening's verdict and who would decide it (you, Tawked, or nobody: approved at once). Nothing is written.

        ``POST /v1/clients/applications/name-check``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_CHECK_NAME,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        *,
        external_id: str,
        name_ar: str,
        name_en: str,
        website_url: str,
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
        | str
        | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Open a Verify application for one of your clients (Verify only, Verify's default settings); answers it with its state: active at once, or awaiting a review by you or by Tawked, by your approval mode and the name's screening; `next` says what follows.

        ``POST /v1/clients/applications``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_CREATE,
            path={},
            given={
                "external_id": external_id,
                "name_ar": name_ar,
                "name_en": name_en,
                "website_url": website_url,
                "industry": industry,
            },
            params=AccountClientsApplicationsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def disable(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn a client application off: no code goes out for it until clients.applications.enable. Answers the application.

        ``POST /v1/clients/applications/{application}/disable``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_DISABLE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def enable(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn a client application you turned off back on; it sends codes again once nothing else holds it (its `state_detail.then`). Answers the application.

        ``POST /v1/clients/applications/{application}/enable``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_ENABLE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        *,
        archived: Literal["1"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        sort: Literal["newest", "codes", "waiting"] | str | NotGiven = NOT_GIVEN,
        state: Literal["needs_you", "active", "review", "rejected", "stopped", "disabled"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the client applications this partner opened for its clients, each with its one state (active, awaiting_partner, awaiting_tawked, rejected, paused, suspended, disabled, archived), its codes and cost of the period.

        ``GET /v1/clients/applications``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CLIENTS_APPLICATIONS_LIST,
            path={},
            given={
                "archived": archived,
                "page": page,
                "period": period,
                "q": q,
                "sort": sort,
                "state": state,
            },
            params=AccountClientsApplicationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        archived: Literal["1"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        sort: Literal["newest", "codes", "waiting"] | str | NotGiven = NOT_GIVEN,
        state: Literal["needs_you", "active", "review", "rejected", "stopped", "disabled"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CLIENTS_APPLICATIONS_LIST,
            _PAGE_A_CLIENTS_APPLICATIONS_LIST,
            path={},
            given={
                "archived": archived,
                "page": page,
                "period": period,
                "q": q,
                "sort": sort,
                "state": state,
            },
            params=AccountClientsApplicationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def reject(
        self,
        application: str,
        *,
        reason: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Reject a client application that waits on your decision, with the reason; it sends no code. Answers the application.

        ``POST /v1/clients/applications/{application}/reject``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_REJECT,
            path={"application": application},
            given={"reason": reason},
            params=AccountClientsApplicationsRejectParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def restore(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Restore an archived client application to where it stood before; answers the application.

        ``POST /v1/clients/applications/{application}/restore``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_RESTORE,
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
        """Read one client application: its state and what it waits on, the code message its users read, its Verify settings, the last 30 days of usage, recent codes, its history, Tawked's rejection and its appeal, and what you may do on it (`can`).

        ``GET /v1/clients/applications/{application}``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_SHOW,
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
        """Lift the pause Tawked's pumping guard put on a client application (state paused); answers the application.

        ``POST /v1/clients/applications/{application}/unpause``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_UNPAUSE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        *,
        name_ar: str,
        name_en: str,
        website_url: str,
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
        | str
        | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a client application's names, website and industry; a change of what its users read sends it back to review. Answers the application with `review: true` when it went back to review.

        ``PATCH /v1/clients/applications/{application}``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_UPDATE,
            path={"application": application},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "website_url": website_url,
                "industry": industry,
            },
            params=AccountClientsApplicationsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountClientsDeliveries:
    """``clients.deliveries``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        *,
        event: Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the webhook's deliveries, newest first: each with its event, status (pending, delivered, failed), attempts, last answer, payload and the client application it was about.

        ``GET /v1/clients/api/deliveries``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CLIENTS_DELIVERIES_LIST,
            path={},
            given={"event": event, "page": page, "q": q, "status": status},
            params=AccountClientsDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        event: Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CLIENTS_DELIVERIES_LIST,
            _PAGE_A_CLIENTS_DELIVERIES_LIST,
            path={},
            given={"event": event, "page": page, "q": q, "status": status},
            params=AccountClientsDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def retry(
        self,
        delivery: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send one failed delivery again, now; answers whether it was queued (a delivery that did not fail is left as it is).

        ``POST /v1/clients/api/deliveries/{delivery}/retry``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_DELIVERIES_RETRY,
            path={"delivery": delivery},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def retry_failed(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send every failed delivery again, one more attempt each; answers how many were queued (0 when none had failed).

        ``POST /v1/clients/api/deliveries/retry-failed``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_DELIVERIES_RETRY_FAILED,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountClientsOverview:
    """``clients.overview``."""

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
        """Read the Clients place at a glance: your approval mode, what waits on you (the oldest five, with the count, and how many wait at Tawked), and the period's figures (active client applications, codes sent, verified rate, cost).

        ``GET /v1/clients``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CLIENTS_OVERVIEW_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountClientsReviews:
    """``clients.reviews``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        queue: Literal["yours", "tawked"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the client applications in review, oldest first: `queue=yours` (default) what waits on your decision, `queue=tawked` what waits at Tawked; each with since when it waits, its screening flags and whether you may approve it in bulk.

        ``GET /v1/clients/reviews``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CLIENTS_REVIEWS_LIST,
            path={},
            given={"page": page, "q": q, "queue": queue},
            params=AccountClientsReviewsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        queue: Literal["yours", "tawked"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CLIENTS_REVIEWS_LIST,
            _PAGE_A_CLIENTS_REVIEWS_LIST,
            path={},
            given={"page": page, "q": q, "queue": queue},
            params=AccountClientsReviewsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountClientsSandboxKey:
    """``clients.sandbox_key``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a new sandbox key (tk_partner_test_…) for trying the Partner API without spending; the sandbox key before it stops at once. Answers its plaintext this once.

        ``POST /v1/clients/api/sandbox-key``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_SANDBOX_KEY_CREATE,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountClientsUsage:
    """``clients.usage``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        *,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the usage you bill your clients from: per client application the codes sent, the codes verified and (for who may see the money) the Verify cost, busiest first, with the totals and your price per code.

        ``GET /v1/clients/usage``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CLIENTS_USAGE_SHOW,
            path={},
            given={"from": from_, "month": month, "page": page, "q": q, "to": to},
            params=AccountClientsUsageShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountClientsVerifySettings:
    """``clients.verify_settings``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change some of a client application's Verify settings (a partial patch: only the fields sent change); answers the application with its settings.

        ``PATCH /v1/clients/applications/{application}/verify-settings``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_VERIFY_SETTINGS_UPDATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountClientsWebhook:
    """``clients.webhook``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def health(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read where the webhook stands (none, idle, delivering, failing), since when it fails, what waits, the last answer and the next automatic attempt, with the deliveries counted by status.

        ``GET /v1/clients/api/webhook``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_HEALTH,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def reveal_secret(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Answer the webhook's current signing secret (`secret`), to verify the deliveries' signatures; each reveal is recorded on the account.

        ``POST /v1/clients/api/webhook/reveal-secret``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_REVEAL_SECRET,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def rotate_secret(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a new signing secret for the webhook; the old one stops signing at once. Answers the secret this once.

        ``POST /v1/clients/api/webhook/rotate-secret``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_ROTATE_SECRET,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        *,
        events: Sequence[str] | NotGiven | None = NOT_GIVEN,
        threshold_sar: float | NotGiven | None = NOT_GIVEN,
        url: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the Partner API's webhook: its URL (empty turns it off), the events it receives and the balance.low threshold; answers the webhook as it stands.

        ``PATCH /v1/clients/api/webhook``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_UPDATE,
            path={},
            given={"events": events, "threshold_sar": threshold_sar, "url": url},
            params=AccountClientsWebhookUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountClients:
    """``clients``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.api = AccountClientsApi(client)
        self.api_key = AccountClientsApiKey(client)
        self.appeals = AccountClientsAppeals(client)
        self.applications = AccountClientsApplications(client)
        self.deliveries = AccountClientsDeliveries(client)
        self.overview = AccountClientsOverview(client)
        self.reviews = AccountClientsReviews(client)
        self.sandbox_key = AccountClientsSandboxKey(client)
        self.usage = AccountClientsUsage(client)
        self.verify_settings = AccountClientsVerifySettings(client)
        self.webhook = AccountClientsWebhook(client)


class AsyncAccountClientsApi:
    """``clients.api``."""

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
        """Read the Partner API's state: whether a partner key works (its prefix, expiry and allowlist; never the key), the sandbox key's prefix, the webhook (URL, events, threshold), its health and the newest deliveries.

        ``GET /v1/clients/api``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_API_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsApiKey:
    """``clients.api_key``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        *,
        expires_in_days: Literal["30", "90", "180", "365"]
        | str
        | int
        | NotGiven
        | None = NOT_GIVEN,
        ip_allowlist: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a new partner key (tk_partner_…) for the Partner API; the key that worked until now stops at once. Answers the key's plaintext this once, with its prefix and the prefix of the key it replaced.

        ``POST /v1/clients/api/key``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_API_KEY_CREATE,
            path={},
            given={"expires_in_days": expires_in_days, "ip_allowlist": ip_allowlist},
            params=AccountClientsApiKeyCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsAppeals:
    """``clients.appeals``."""

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
        """Appeal Tawked's rejection of a client application with a note and an optional document (PDF or image, multipart); it goes back to Tawked's review. Your client is never told.

        ``POST /v1/clients/applications/{application}/appeal``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPEALS_CREATE,
            path={"application": application},
            given={"note": note, "document": document},
            params=AccountClientsAppealsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("document",),
        )


class AsyncAccountClientsApplications:
    """``clients.applications``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def approve(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Approve a client application that waits on your decision (state awaiting_partner); it starts sending codes. Answers the application.

        ``POST /v1/clients/applications/{application}/approve``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_APPROVE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def archive(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Archive a client application: it stops sending codes, leaves the lists and takes no write but clients.applications.restore. Answers the application.

        ``POST /v1/clients/applications/{application}/archive``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_ARCHIVE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def bulk_approve(
        self,
        *,
        ids: Sequence[str],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Approve at once every listed client application that waits on your decision and whose names were screened clean; answers how many were approved and skipped.

        ``POST /v1/clients/applications/bulk-approve``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_BULK_APPROVE,
            path={},
            given={"ids": ids},
            params=AccountClientsApplicationsBulkApproveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def check_name(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check the names of a client application before creating it: answers the screening's verdict and who would decide it (you, Tawked, or nobody: approved at once). Nothing is written.

        ``POST /v1/clients/applications/name-check``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_CHECK_NAME,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        *,
        external_id: str,
        name_ar: str,
        name_en: str,
        website_url: str,
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
        | str
        | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Open a Verify application for one of your clients (Verify only, Verify's default settings); answers it with its state: active at once, or awaiting a review by you or by Tawked, by your approval mode and the name's screening; `next` says what follows.

        ``POST /v1/clients/applications``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_CREATE,
            path={},
            given={
                "external_id": external_id,
                "name_ar": name_ar,
                "name_en": name_en,
                "website_url": website_url,
                "industry": industry,
            },
            params=AccountClientsApplicationsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def disable(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn a client application off: no code goes out for it until clients.applications.enable. Answers the application.

        ``POST /v1/clients/applications/{application}/disable``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_DISABLE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def enable(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn a client application you turned off back on; it sends codes again once nothing else holds it (its `state_detail.then`). Answers the application.

        ``POST /v1/clients/applications/{application}/enable``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_ENABLE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        *,
        archived: Literal["1"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        sort: Literal["newest", "codes", "waiting"] | str | NotGiven = NOT_GIVEN,
        state: Literal["needs_you", "active", "review", "rejected", "stopped", "disabled"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the client applications this partner opened for its clients, each with its one state (active, awaiting_partner, awaiting_tawked, rejected, paused, suspended, disabled, archived), its codes and cost of the period.

        ``GET /v1/clients/applications``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CLIENTS_APPLICATIONS_LIST,
            path={},
            given={
                "archived": archived,
                "page": page,
                "period": period,
                "q": q,
                "sort": sort,
                "state": state,
            },
            params=AccountClientsApplicationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        archived: Literal["1"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        sort: Literal["newest", "codes", "waiting"] | str | NotGiven = NOT_GIVEN,
        state: Literal["needs_you", "active", "review", "rejected", "stopped", "disabled"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CLIENTS_APPLICATIONS_LIST,
            _PAGE_A_CLIENTS_APPLICATIONS_LIST,
            path={},
            given={
                "archived": archived,
                "page": page,
                "period": period,
                "q": q,
                "sort": sort,
                "state": state,
            },
            params=AccountClientsApplicationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def reject(
        self,
        application: str,
        *,
        reason: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Reject a client application that waits on your decision, with the reason; it sends no code. Answers the application.

        ``POST /v1/clients/applications/{application}/reject``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_REJECT,
            path={"application": application},
            given={"reason": reason},
            params=AccountClientsApplicationsRejectParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def restore(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Restore an archived client application to where it stood before; answers the application.

        ``POST /v1/clients/applications/{application}/restore``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_RESTORE,
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
        """Read one client application: its state and what it waits on, the code message its users read, its Verify settings, the last 30 days of usage, recent codes, its history, Tawked's rejection and its appeal, and what you may do on it (`can`).

        ``GET /v1/clients/applications/{application}``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_SHOW,
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
        """Lift the pause Tawked's pumping guard put on a client application (state paused); answers the application.

        ``POST /v1/clients/applications/{application}/unpause``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_UNPAUSE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        *,
        name_ar: str,
        name_en: str,
        website_url: str,
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
        | str
        | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a client application's names, website and industry; a change of what its users read sends it back to review. Answers the application with `review: true` when it went back to review.

        ``PATCH /v1/clients/applications/{application}``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_APPLICATIONS_UPDATE,
            path={"application": application},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "website_url": website_url,
                "industry": industry,
            },
            params=AccountClientsApplicationsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsDeliveries:
    """``clients.deliveries``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        *,
        event: Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the webhook's deliveries, newest first: each with its event, status (pending, delivered, failed), attempts, last answer, payload and the client application it was about.

        ``GET /v1/clients/api/deliveries``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CLIENTS_DELIVERIES_LIST,
            path={},
            given={"event": event, "page": page, "q": q, "status": status},
            params=AccountClientsDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        event: Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CLIENTS_DELIVERIES_LIST,
            _PAGE_A_CLIENTS_DELIVERIES_LIST,
            path={},
            given={"event": event, "page": page, "q": q, "status": status},
            params=AccountClientsDeliveriesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def retry(
        self,
        delivery: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send one failed delivery again, now; answers whether it was queued (a delivery that did not fail is left as it is).

        ``POST /v1/clients/api/deliveries/{delivery}/retry``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_DELIVERIES_RETRY,
            path={"delivery": delivery},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def retry_failed(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send every failed delivery again, one more attempt each; answers how many were queued (0 when none had failed).

        ``POST /v1/clients/api/deliveries/retry-failed``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_DELIVERIES_RETRY_FAILED,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsOverview:
    """``clients.overview``."""

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
        """Read the Clients place at a glance: your approval mode, what waits on you (the oldest five, with the count, and how many wait at Tawked), and the period's figures (active client applications, codes sent, verified rate, cost).

        ``GET /v1/clients``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_OVERVIEW_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsReviews:
    """``clients.reviews``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        queue: Literal["yours", "tawked"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the client applications in review, oldest first: `queue=yours` (default) what waits on your decision, `queue=tawked` what waits at Tawked; each with since when it waits, its screening flags and whether you may approve it in bulk.

        ``GET /v1/clients/reviews``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CLIENTS_REVIEWS_LIST,
            path={},
            given={"page": page, "q": q, "queue": queue},
            params=AccountClientsReviewsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        queue: Literal["yours", "tawked"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CLIENTS_REVIEWS_LIST,
            _PAGE_A_CLIENTS_REVIEWS_LIST,
            path={},
            given={"page": page, "q": q, "queue": queue},
            params=AccountClientsReviewsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsSandboxKey:
    """``clients.sandbox_key``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a new sandbox key (tk_partner_test_…) for trying the Partner API without spending; the sandbox key before it stops at once. Answers its plaintext this once.

        ``POST /v1/clients/api/sandbox-key``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_SANDBOX_KEY_CREATE,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsUsage:
    """``clients.usage``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        *,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the usage you bill your clients from: per client application the codes sent, the codes verified and (for who may see the money) the Verify cost, busiest first, with the totals and your price per code.

        ``GET /v1/clients/usage``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_USAGE_SHOW,
            path={},
            given={"from": from_, "month": month, "page": page, "q": q, "to": to},
            params=AccountClientsUsageShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsVerifySettings:
    """``clients.verify_settings``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change some of a client application's Verify settings (a partial patch: only the fields sent change); answers the application with its settings.

        ``PATCH /v1/clients/applications/{application}/verify-settings``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_VERIFY_SETTINGS_UPDATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountClientsWebhook:
    """``clients.webhook``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def health(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read where the webhook stands (none, idle, delivering, failing), since when it fails, what waits, the last answer and the next automatic attempt, with the deliveries counted by status.

        ``GET /v1/clients/api/webhook``, permission ``clients:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_HEALTH,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def reveal_secret(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Answer the webhook's current signing secret (`secret`), to verify the deliveries' signatures; each reveal is recorded on the account.

        ``POST /v1/clients/api/webhook/reveal-secret``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_REVEAL_SECRET,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def rotate_secret(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a new signing secret for the webhook; the old one stops signing at once. Answers the secret this once.

        ``POST /v1/clients/api/webhook/rotate-secret``, permission ``clients:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_ROTATE_SECRET,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        *,
        events: Sequence[str] | NotGiven | None = NOT_GIVEN,
        threshold_sar: float | NotGiven | None = NOT_GIVEN,
        url: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the Partner API's webhook: its URL (empty turns it off), the events it receives and the balance.low threshold; answers the webhook as it stands.

        ``PATCH /v1/clients/api/webhook``, permission ``clients:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CLIENTS_WEBHOOK_UPDATE,
            path={},
            given={"events": events, "threshold_sar": threshold_sar, "url": url},
            params=AccountClientsWebhookUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountClients:
    """``clients``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.api = AsyncAccountClientsApi(client)
        self.api_key = AsyncAccountClientsApiKey(client)
        self.appeals = AsyncAccountClientsAppeals(client)
        self.applications = AsyncAccountClientsApplications(client)
        self.deliveries = AsyncAccountClientsDeliveries(client)
        self.overview = AsyncAccountClientsOverview(client)
        self.reviews = AsyncAccountClientsReviews(client)
        self.sandbox_key = AsyncAccountClientsSandboxKey(client)
        self.usage = AsyncAccountClientsUsage(client)
        self.verify_settings = AsyncAccountClientsVerifySettings(client)
        self.webhook = AsyncAccountClientsWebhook(client)
