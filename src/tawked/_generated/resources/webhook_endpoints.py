"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked import _generated as _g
from tawked._generated import endpoints as _E
from tawked._generated.endpoints import _PAGE_WEBHOOK_DELIVERIES
from tawked._generated.types import (
    WebhookDeliveryGetResponse,
    WebhookDeliveryListParams,
    WebhookDeliveryListResponse,
    WebhookDeliveryReplayResponse,
    WebhookEndpointCreateParams,
    WebhookEndpointCreateResponse,
    WebhookEndpointDeleteResponse,
    WebhookEndpointDelivery,
    WebhookEndpointGetResponse,
    WebhookEndpointListResponse,
    WebhookEndpointUpdateParams,
    WebhookEndpointUpdateResponse,
    WebhookReplayCreateParams,
    WebhookReplayCreateResponse,
    WebhookReplayGetResponse,
    WebhookSecretRotateParams,
    WebhookSecretRotateResponse,
    WebhookTestSendParams,
    WebhookTestSendResponse,
)
from tawked._models import NOT_GIVEN, NotGiven, TawkedModel, TawkedParams
from tawked._pagination import Page
from tawked._transport import options
from tawked.attachments import FileInput

if TYPE_CHECKING:
    from tawked._client import AsyncTawked, Tawked

_ = (
    builtins,
    AsyncIterator,
    Iterator,
    Mapping,
    Sequence,
    datetime,
    Any,
    Literal,
    NOT_GIVEN,
    NotGiven,
    TawkedModel,
    TawkedParams,
    Page,
    FileInput,
    _g,
)
early_access = _g.early_access


class WebhookEndpointsDeliveries:
    """``webhook_endpoints.deliveries``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def list(
        self,
        id: str,
        *,
        status: str | NotGiven = NOT_GIVEN,
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
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[WebhookEndpointDelivery]:
        """List deliveries

        ``GET /v1/webhooks/{id}/deliveries``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.deliveries.list('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', status='delivered', limit=20)
        """
        return self._client._list(
            _E.WEBHOOK_DELIVERIES,
            WebhookDeliveryListResponse,
            WebhookEndpointDelivery,
            _PAGE_WEBHOOK_DELIVERIES,
            path={"id": id},
            given={
                "status": status,
                "event": event,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=WebhookDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        id: str,
        *,
        status: str | NotGiven = NOT_GIVEN,
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
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[WebhookEndpointDelivery]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.WEBHOOK_DELIVERIES,
            WebhookDeliveryListResponse,
            WebhookEndpointDelivery,
            _PAGE_WEBHOOK_DELIVERIES,
            path={"id": id},
            given={
                "status": status,
                "event": event,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=WebhookDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        id: str,
        delivery: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookDeliveryGetResponse:
        """Get a delivery

        ``GET /v1/webhooks/{id}/deliveries/{delivery}``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.deliveries.get('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', '0199f220-5f6a-7b7c-8d8e-9f0a1b2c3d45')
        """
        return self._client._call(
            _E.WEBHOOK_DELIVERY,
            WebhookDeliveryGetResponse,
            path={"id": id, "delivery": delivery},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def replay(
        self,
        id: str,
        delivery: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookDeliveryReplayResponse:
        """Send a delivery again

        ``POST /v1/webhooks/{id}/deliveries/{delivery}/replay``, scope ``webhooks:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``application_key_required``, ``delivery_erased``, ``delivery_pending``, ``endpoint_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.deliveries.replay('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', '0199f220-5f6a-7b7c-8d8e-9f0a1b2c3d45')
        """
        return self._client._call(
            _E.WEBHOOK_DELIVERY_REPLAY,
            WebhookDeliveryReplayResponse,
            path={"id": id, "delivery": delivery},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class WebhookEndpointsReplays:
    """``webhook_endpoints.replays``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def get(
        self,
        id: str,
        replay: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookReplayGetResponse:
        """Get a replay

        ``GET /v1/webhooks/{id}/replays/{replay}``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.replays.get('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', '0199f230-6a7b-7c8d-9e0f-0a1b2c3d4e56')
        """
        return self._client._call(
            _E.WEBHOOK_REPLAY_STATUS,
            WebhookReplayGetResponse,
            path={"id": id, "replay": replay},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class WebhookEndpoints:
    """``webhook_endpoints``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.deliveries = WebhookEndpointsDeliveries(client)
        self.replays = WebhookEndpointsReplays(client)

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointListResponse:
        """List webhook endpoints

        ``GET /v1/webhooks``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.list()
        """
        return self._client._call(
            _E.WEBHOOKS,
            WebhookEndpointListResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        *,
        url: str,
        events: Sequence[Any] | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointCreateResponse:
        """Create a webhook endpoint

        ``POST /v1/webhooks``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``credentials``, ``endpoint_limit_reached``, ``idempotency_secret_not_replayable``, ``insufficient_scope``, ``internal_error``, ``invalid_host``, ``invalid_json``, ``invalid_request``, ``ip_address``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_https``, ``private_host``, ``too_many_requests``, ``unauthorized``, ``webhook_event_unknown``.

        Example::

            tawked.webhook_endpoints.create(url='https://hooks.acme.sa/tawked', events=['email.delivered', 'email.bounced', 'email.complained', 'email.failed'])
        """
        return self._client._call(
            _E.WEBHOOK_CREATE,
            WebhookEndpointCreateResponse,
            path={},
            given={"url": url, "events": events, "receives_test": receives_test},
            params=WebhookEndpointCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointGetResponse:
        """Get a webhook endpoint

        ``GET /v1/webhooks/{id}``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.get('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34')
        """
        return self._client._call(
            _E.WEBHOOK,
            WebhookEndpointGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        id: str,
        *,
        url: str | NotGiven = NOT_GIVEN,
        events: Sequence[Any] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        signing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointUpdateResponse:
        """Update a webhook endpoint

        ``PATCH /v1/webhooks/{id}``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``credentials``, ``insufficient_scope``, ``internal_error``, ``invalid_host``, ``invalid_json``, ``invalid_request``, ``ip_address``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``not_https``, ``private_host``, ``too_many_requests``, ``unauthorized``, ``webhook_event_unknown``.

        Example::

            tawked.webhook_endpoints.update('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', receives_test=True)
        """
        return self._client._call(
            _E.WEBHOOK_UPDATE,
            WebhookEndpointUpdateResponse,
            path={"id": id},
            given={
                "url": url,
                "events": events,
                "enabled": enabled,
                "receives_test": receives_test,
                "signing": signing,
            },
            params=WebhookEndpointUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointDeleteResponse:
        """Delete a webhook endpoint

        ``DELETE /v1/webhooks/{id}``, scope ``webhooks:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.delete('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34')
        """
        return self._client._call(
            _E.WEBHOOK_DELETE,
            WebhookEndpointDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def rotate_secret(
        self,
        id: str,
        *,
        scheme: Literal["standard", "tawked", "both"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookSecretRotateResponse:
        """Rotate a webhook secret

        ``POST /v1/webhooks/{id}/rotate-secret``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``idempotency_secret_not_replayable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.rotate_secret('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', scheme='standard')
        """
        return self._client._call(
            _E.WEBHOOK_ROTATE_SECRET,
            WebhookSecretRotateResponse,
            path={"id": id},
            given={"scheme": scheme},
            params=WebhookSecretRotateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def test(
        self,
        id: str,
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
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookTestSendResponse:
        """Send a test event

        ``POST /v1/webhooks/{id}/test``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``endpoint_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``, ``webhook_event_unknown``.

        Example::

            tawked.webhook_endpoints.test('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', event='email.delivered')
        """
        return self._client._call(
            _E.WEBHOOK_TEST,
            WebhookTestSendResponse,
            path={"id": id},
            given={"event": event},
            params=WebhookTestSendParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def replay(
        self,
        id: str,
        *,
        since: datetime | str,
        until: datetime | str | NotGiven = NOT_GIVEN,
        status: Literal["failed", "all"] | str | NotGiven = NOT_GIVEN,
        events: Sequence[Any] | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookReplayCreateResponse:
        """Replay deliveries

        ``POST /v1/webhooks/{id}/replay``, scope ``webhooks:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``application_key_required``, ``endpoint_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``replay_running``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.replay('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', since='2026-10-22T00:00:00+00:00', until='2026-10-23T00:00:00+00:00', status='failed')
        """
        return self._client._call(
            _E.WEBHOOK_REPLAY,
            WebhookReplayCreateResponse,
            path={"id": id},
            given={"since": since, "until": until, "status": status, "events": events},
            params=WebhookReplayCreateParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncWebhookEndpointsDeliveries:
    """``webhook_endpoints.deliveries``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def list(
        self,
        id: str,
        *,
        status: str | NotGiven = NOT_GIVEN,
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
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[WebhookEndpointDelivery]:
        """List deliveries

        ``GET /v1/webhooks/{id}/deliveries``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.deliveries.list('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', status='delivered', limit=20)
        """
        return await self._client._list(
            _E.WEBHOOK_DELIVERIES,
            WebhookDeliveryListResponse,
            WebhookEndpointDelivery,
            _PAGE_WEBHOOK_DELIVERIES,
            path={"id": id},
            given={
                "status": status,
                "event": event,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=WebhookDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        id: str,
        *,
        status: str | NotGiven = NOT_GIVEN,
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
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[WebhookEndpointDelivery]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.WEBHOOK_DELIVERIES,
            WebhookDeliveryListResponse,
            WebhookEndpointDelivery,
            _PAGE_WEBHOOK_DELIVERIES,
            path={"id": id},
            given={
                "status": status,
                "event": event,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=WebhookDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        id: str,
        delivery: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookDeliveryGetResponse:
        """Get a delivery

        ``GET /v1/webhooks/{id}/deliveries/{delivery}``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.deliveries.get('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', '0199f220-5f6a-7b7c-8d8e-9f0a1b2c3d45')
        """
        return await self._client._call(
            _E.WEBHOOK_DELIVERY,
            WebhookDeliveryGetResponse,
            path={"id": id, "delivery": delivery},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def replay(
        self,
        id: str,
        delivery: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookDeliveryReplayResponse:
        """Send a delivery again

        ``POST /v1/webhooks/{id}/deliveries/{delivery}/replay``, scope ``webhooks:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``application_key_required``, ``delivery_erased``, ``delivery_pending``, ``endpoint_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.deliveries.replay('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', '0199f220-5f6a-7b7c-8d8e-9f0a1b2c3d45')
        """
        return await self._client._call(
            _E.WEBHOOK_DELIVERY_REPLAY,
            WebhookDeliveryReplayResponse,
            path={"id": id, "delivery": delivery},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncWebhookEndpointsReplays:
    """``webhook_endpoints.replays``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def get(
        self,
        id: str,
        replay: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookReplayGetResponse:
        """Get a replay

        ``GET /v1/webhooks/{id}/replays/{replay}``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.replays.get('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', '0199f230-6a7b-7c8d-9e0f-0a1b2c3d4e56')
        """
        return await self._client._call(
            _E.WEBHOOK_REPLAY_STATUS,
            WebhookReplayGetResponse,
            path={"id": id, "replay": replay},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncWebhookEndpoints:
    """``webhook_endpoints``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.deliveries = AsyncWebhookEndpointsDeliveries(client)
        self.replays = AsyncWebhookEndpointsReplays(client)

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointListResponse:
        """List webhook endpoints

        ``GET /v1/webhooks``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.list()
        """
        return await self._client._call(
            _E.WEBHOOKS,
            WebhookEndpointListResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        *,
        url: str,
        events: Sequence[Any] | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointCreateResponse:
        """Create a webhook endpoint

        ``POST /v1/webhooks``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``credentials``, ``endpoint_limit_reached``, ``idempotency_secret_not_replayable``, ``insufficient_scope``, ``internal_error``, ``invalid_host``, ``invalid_json``, ``invalid_request``, ``ip_address``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_https``, ``private_host``, ``too_many_requests``, ``unauthorized``, ``webhook_event_unknown``.

        Example::

            tawked.webhook_endpoints.create(url='https://hooks.acme.sa/tawked', events=['email.delivered', 'email.bounced', 'email.complained', 'email.failed'])
        """
        return await self._client._call(
            _E.WEBHOOK_CREATE,
            WebhookEndpointCreateResponse,
            path={},
            given={"url": url, "events": events, "receives_test": receives_test},
            params=WebhookEndpointCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointGetResponse:
        """Get a webhook endpoint

        ``GET /v1/webhooks/{id}``, scope ``webhooks:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.get('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34')
        """
        return await self._client._call(
            _E.WEBHOOK,
            WebhookEndpointGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        id: str,
        *,
        url: str | NotGiven = NOT_GIVEN,
        events: Sequence[Any] | NotGiven = NOT_GIVEN,
        enabled: bool | NotGiven = NOT_GIVEN,
        receives_test: bool | NotGiven = NOT_GIVEN,
        signing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointUpdateResponse:
        """Update a webhook endpoint

        ``PATCH /v1/webhooks/{id}``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``credentials``, ``insufficient_scope``, ``internal_error``, ``invalid_host``, ``invalid_json``, ``invalid_request``, ``ip_address``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``not_https``, ``private_host``, ``too_many_requests``, ``unauthorized``, ``webhook_event_unknown``.

        Example::

            tawked.webhook_endpoints.update('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', receives_test=True)
        """
        return await self._client._call(
            _E.WEBHOOK_UPDATE,
            WebhookEndpointUpdateResponse,
            path={"id": id},
            given={
                "url": url,
                "events": events,
                "enabled": enabled,
                "receives_test": receives_test,
                "signing": signing,
            },
            params=WebhookEndpointUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookEndpointDeleteResponse:
        """Delete a webhook endpoint

        ``DELETE /v1/webhooks/{id}``, scope ``webhooks:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_key_required``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.delete('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34')
        """
        return await self._client._call(
            _E.WEBHOOK_DELETE,
            WebhookEndpointDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def rotate_secret(
        self,
        id: str,
        *,
        scheme: Literal["standard", "tawked", "both"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookSecretRotateResponse:
        """Rotate a webhook secret

        ``POST /v1/webhooks/{id}/rotate-secret``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``idempotency_secret_not_replayable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.rotate_secret('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', scheme='standard')
        """
        return await self._client._call(
            _E.WEBHOOK_ROTATE_SECRET,
            WebhookSecretRotateResponse,
            path={"id": id},
            given={"scheme": scheme},
            params=WebhookSecretRotateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def test(
        self,
        id: str,
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
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookTestSendResponse:
        """Send a test event

        ``POST /v1/webhooks/{id}/test``, scope ``webhooks:manage``.
        Never retried once sent.

        Errors: ``application_key_required``, ``endpoint_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``, ``webhook_event_unknown``.

        Example::

            tawked.webhook_endpoints.test('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', event='email.delivered')
        """
        return await self._client._call(
            _E.WEBHOOK_TEST,
            WebhookTestSendResponse,
            path={"id": id},
            given={"event": event},
            params=WebhookTestSendParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def replay(
        self,
        id: str,
        *,
        since: datetime | str,
        until: datetime | str | NotGiven = NOT_GIVEN,
        status: Literal["failed", "all"] | str | NotGiven = NOT_GIVEN,
        events: Sequence[Any] | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WebhookReplayCreateResponse:
        """Replay deliveries

        ``POST /v1/webhooks/{id}/replay``, scope ``webhooks:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``application_key_required``, ``endpoint_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``replay_running``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.webhook_endpoints.replay('0199f210-4e5f-7a6b-8c7d-8e9f0a1b2c34', since='2026-10-22T00:00:00+00:00', until='2026-10-23T00:00:00+00:00', status='failed')
        """
        return await self._client._call(
            _E.WEBHOOK_REPLAY,
            WebhookReplayCreateResponse,
            path={"id": id},
            given={"since": since, "until": until, "status": status, "events": events},
            params=WebhookReplayCreateParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )
