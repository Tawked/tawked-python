"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked import _generated as _g
from tawked._generated import endpoints as _E
from tawked._generated.endpoints import (
    _PAGE_PARTNER_DELIVERIES,
    _PAGE_PARTNER_EVENTS,
    _PAGE_PARTNER_LIST,
    _PAGE_PARTNER_VERIFICATIONS,
)
from tawked._generated.types import (
    ApplicationRow,
    PartnerApplicationArchiveResponse,
    PartnerApplicationBatchResponse,
    PartnerApplicationCreateParams,
    PartnerApplicationCreateResponse,
    PartnerApplicationGetResponse,
    PartnerApplicationHistoryResponse,
    PartnerApplicationListParams,
    PartnerApplicationListResponse,
    PartnerApplicationRestoreResponse,
    PartnerApplicationResumeResponse,
    PartnerApplicationSuspendResponse,
    PartnerApplicationUnpauseResponse,
    PartnerApplicationUpdateParams,
    PartnerApplicationUpdateResponse,
    PartnerDeliveryListParams,
    PartnerDeliveryListResponse,
    PartnerDeliveryRetryResponse,
    PartnerEventListItem,
    PartnerEventListParams,
    PartnerEventListResponse,
    PartnerLogoRemoveResponse,
    PartnerLogoUploadParams,
    PartnerLogoUploadResponse,
    PartnerProfileResponse,
    PartnerScreeningParams,
    PartnerScreeningResponse,
    PartnerUsageParams,
    PartnerUsageResponse,
    PartnerVerificationListItem,
    PartnerVerificationListParams,
    PartnerVerificationListResponse,
    PartnerVerifySettingsUpdateParams,
    PartnerVerifySettingsUpdateResponse,
    PartnerWebhookGetResponse,
    PartnerWebhookUpdateParams,
    PartnerWebhookUpdateResponse,
    WebhookDelivery,
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


class PartnerProfile:
    """``partner.profile``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerProfileResponse:
        """Get the profile

        ``GET /v1/partner/profile``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.profile.get()
        """
        return self._client._call(
            _E.PARTNER_PROFILE,
            PartnerProfileResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class PartnerScreening:
    """``partner.screening``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def check(
        self,
        *,
        name_ar: str,
        name_en: str,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerScreeningResponse:
        """Preview the screening

        ``POST /v1/partner/screening``.
        Never retried once sent.

        Errors: ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.screening.check(name_ar='متجر الورد', name_en='Flower Shop')
        """
        return self._client._call(
            _E.PARTNER_SCREENING,
            PartnerScreeningResponse,
            path={},
            given={"name_ar": name_ar, "name_en": name_en},
            params=PartnerScreeningParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class PartnerApplications:
    """``partner.applications``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def create(
        self,
        *,
        external_id: str,
        name_ar: str,
        name_en: str,
        website: str,
        industry: str | NotGiven = NOT_GIVEN,
        merchant: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        verify: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationCreateResponse:
        """Provision an application

        ``POST /v1/partner/applications``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.create(external_id='store_88', name_ar='متجر الورد', name_en='Flower Shop', website='https://flowers.example', industry='retail', idempotency_key='provision-store_88')
        """
        return self._client._call(
            _E.PARTNER_PROVISION,
            PartnerApplicationCreateResponse,
            path={},
            given={
                "external_id": external_id,
                "name_ar": name_ar,
                "name_en": name_en,
                "website": website,
                "industry": industry,
                "merchant": merchant,
                "verify": verify,
                "metadata": metadata,
            },
            params=PartnerApplicationCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def batch(
        self,
        applications: Sequence[Mapping[str, Any] | TawkedParams],
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationBatchResponse:
        """Provision in bulk

        ``POST /v1/partner/applications/batch``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.batch([{'external_id': 'store_88', 'name_ar': 'متجر الورد', 'name_en': 'Flower Shop', 'website': 'https://flowers.example', 'industry': 'retail'}, {'external_id': 'store_89', 'name_ar': 'متجر الهدايا', 'name_en': 'Gift Shop', 'website': 'https://gifts.example', 'industry': 'retail'}])
        """
        if len(applications) > 100:
            raise ValueError("applications holds at most 100 items")
        return self._client._call(
            _E.PARTNER_BATCH,
            PartnerApplicationBatchResponse,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            list_param=("applications", applications),
        )

    def list(
        self,
        *,
        status: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[ApplicationRow]:
        """List applications

        ``GET /v1/partner/applications``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.list(status='active', limit=50, offset=0)
        """
        return self._client._list(
            _E.PARTNER_LIST,
            PartnerApplicationListResponse,
            ApplicationRow,
            _PAGE_PARTNER_LIST,
            path={},
            given={
                "status": status,
                "disabled": disabled,
                "archived": archived,
                "metadata": metadata,
                "limit": limit,
                "offset": offset,
            },
            params=PartnerApplicationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        status: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[ApplicationRow]:
        """Every item of :meth:`list`, page after page (offset); the same filters."""
        return self._client._iterate(
            _E.PARTNER_LIST,
            PartnerApplicationListResponse,
            ApplicationRow,
            _PAGE_PARTNER_LIST,
            path={},
            given={
                "status": status,
                "disabled": disabled,
                "archived": archived,
                "metadata": metadata,
                "limit": limit,
                "offset": offset,
            },
            params=PartnerApplicationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        external_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationGetResponse:
        """Get an application

        ``GET /v1/partner/applications/{external_id}``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.get('store_88')
        """
        return self._client._call(
            _E.PARTNER_SHOW,
            PartnerApplicationGetResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def history(
        self,
        external_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationHistoryResponse:
        """Get the history

        ``GET /v1/partner/applications/{external_id}/history``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.history('store_88')
        """
        return self._client._call(
            _E.PARTNER_HISTORY,
            PartnerApplicationHistoryResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        external_id: str,
        *,
        name_ar: str,
        name_en: str,
        website: str,
        industry: str | NotGiven = NOT_GIVEN,
        merchant: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        verify: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationUpdateResponse:
        """Update the brand

        ``PATCH /v1/partner/applications/{external_id}``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.update('store_88', name_ar='متجر الورد', name_en='Flower Shop', website='https://flowers.example')
        """
        return self._client._call(
            _E.PARTNER_UPDATE,
            PartnerApplicationUpdateResponse,
            path={"external_id": external_id},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "website": website,
                "industry": industry,
                "merchant": merchant,
                "verify": verify,
                "metadata": metadata,
            },
            params=PartnerApplicationUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def upload_logo(
        self,
        external_id: str,
        *,
        logo: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerLogoUploadResponse:
        """Upload the logo

        ``POST /v1/partner/applications/{external_id}/logo``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``storage_unavailable``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.upload_logo('store_88', logo=open('logo.png', 'rb'))
        """
        return self._client._call(
            _E.PARTNER_LOGO_UPLOAD,
            PartnerLogoUploadResponse,
            path={"external_id": external_id},
            given={"logo": logo},
            params=PartnerLogoUploadParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    def remove_logo(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerLogoRemoveResponse:
        """Remove the logo

        ``DELETE /v1/partner/applications/{external_id}/logo``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.remove_logo('store_88')
        """
        return self._client._call(
            _E.PARTNER_LOGO_REMOVE,
            PartnerLogoRemoveResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update_verify_settings(
        self,
        external_id: str,
        *,
        code_length: int | NotGiven = NOT_GIVEN,
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        max_attempts: int | NotGiven = NOT_GIVEN,
        max_per_hour: int | NotGiven = NOT_GIVEN,
        autofill_domain_enabled: bool | NotGiven = NOT_GIVEN,
        android_app_hash: str | NotGiven | None = NOT_GIVEN,
        daily_spend_cap_halalas: int | NotGiven | None = NOT_GIVEN,
        max_per_ip_per_hour: int | NotGiven = NOT_GIVEN,
        max_new_destinations_per_hour: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerVerifySettingsUpdateResponse:
        """Update the verify settings

        ``PATCH /v1/partner/applications/{external_id}/verify-settings``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.update_verify_settings('store_88', code_length=6, ttl_seconds=300)
        """
        return self._client._call(
            _E.PARTNER_VERIFY_SETTINGS,
            PartnerVerifySettingsUpdateResponse,
            path={"external_id": external_id},
            given={
                "code_length": code_length,
                "ttl_seconds": ttl_seconds,
                "max_attempts": max_attempts,
                "max_per_hour": max_per_hour,
                "autofill_domain_enabled": autofill_domain_enabled,
                "android_app_hash": android_app_hash,
                "daily_spend_cap_halalas": daily_spend_cap_halalas,
                "max_per_ip_per_hour": max_per_ip_per_hour,
                "max_new_destinations_per_hour": max_new_destinations_per_hour,
            },
            params=PartnerVerifySettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def suspend(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationSuspendResponse:
        """Suspend an application

        ``POST /v1/partner/applications/{external_id}/suspend``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.suspend('store_88')
        """
        return self._client._call(
            _E.PARTNER_SUSPEND,
            PartnerApplicationSuspendResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def resume(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationResumeResponse:
        """Resume an application

        ``POST /v1/partner/applications/{external_id}/resume``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.resume('store_88')
        """
        return self._client._call(
            _E.PARTNER_RESUME,
            PartnerApplicationResumeResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def unpause(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationUnpauseResponse:
        """Unpause an application

        ``POST /v1/partner/applications/{external_id}/unpause``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.unpause('store_88')
        """
        return self._client._call(
            _E.PARTNER_UNPAUSE,
            PartnerApplicationUnpauseResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def archive(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationArchiveResponse:
        """Archive an application

        ``POST /v1/partner/applications/{external_id}/archive``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``number_connected``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.archive('store_88')
        """
        return self._client._call(
            _E.PARTNER_ARCHIVE,
            PartnerApplicationArchiveResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def restore(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationRestoreResponse:
        """Restore an application

        ``POST /v1/partner/applications/{external_id}/restore``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.restore('store_88')
        """
        return self._client._call(
            _E.PARTNER_RESTORE,
            PartnerApplicationRestoreResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class PartnerUsage:
    """``partner.usage``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def get(
        self,
        *,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerUsageResponse:
        """Get usage

        ``GET /v1/partner/usage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.usage.get(from_='2026-10-01', to='2026-10-20')
        """
        return self._client._call(
            _E.PARTNER_USAGE,
            PartnerUsageResponse,
            path={},
            given={"from": from_, "to": to},
            params=PartnerUsageParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class PartnerVerifications:
    """``partner.verifications``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "verified", "failed", "expired", "canceled"]
        | str
        | NotGiven = NOT_GIVEN,
        mode: Literal["live", "test", "partner", "partner_test"] | str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[PartnerVerificationListItem]:
        """List verifications

        ``GET /v1/partner/verifications``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.verifications.list(status='verified', limit=50)
        """
        return self._client._list(
            _E.PARTNER_VERIFICATIONS,
            PartnerVerificationListResponse,
            PartnerVerificationListItem,
            _PAGE_PARTNER_VERIFICATIONS,
            path={},
            given={
                "application": application,
                "status": status,
                "mode": mode,
                "reference": reference,
                "from": from_,
                "to": to,
                "cursor": cursor,
                "limit": limit,
            },
            params=PartnerVerificationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "verified", "failed", "expired", "canceled"]
        | str
        | NotGiven = NOT_GIVEN,
        mode: Literal["live", "test", "partner", "partner_test"] | str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[PartnerVerificationListItem]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.PARTNER_VERIFICATIONS,
            PartnerVerificationListResponse,
            PartnerVerificationListItem,
            _PAGE_PARTNER_VERIFICATIONS,
            path={},
            given={
                "application": application,
                "status": status,
                "mode": mode,
                "reference": reference,
                "from": from_,
                "to": to,
                "cursor": cursor,
                "limit": limit,
            },
            params=PartnerVerificationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class PartnerEvents:
    """``partner.events``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def list(
        self,
        *,
        since: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
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
        application: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[PartnerEventListItem]:
        """Get the event feed

        ``GET /v1/partner/events``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.events.list(event='service.approved', limit=50)
        """
        return self._client._list(
            _E.PARTNER_EVENTS,
            PartnerEventListResponse,
            PartnerEventListItem,
            _PAGE_PARTNER_EVENTS,
            path={},
            given={
                "since": since,
                "cursor": cursor,
                "event": event,
                "application": application,
                "limit": limit,
            },
            params=PartnerEventListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        since: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
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
        application: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[PartnerEventListItem]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.PARTNER_EVENTS,
            PartnerEventListResponse,
            PartnerEventListItem,
            _PAGE_PARTNER_EVENTS,
            path={},
            given={
                "since": since,
                "cursor": cursor,
                "event": event,
                "application": application,
                "limit": limit,
            },
            params=PartnerEventListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class PartnerWebhookDeliveries:
    """``partner.webhook.deliveries``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def list(
        self,
        *,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[WebhookDelivery]:
        """List deliveries

        ``GET /v1/partner/webhook/deliveries``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.deliveries.list(status='failed', limit=50)
        """
        return self._client._list(
            _E.PARTNER_DELIVERIES,
            PartnerDeliveryListResponse,
            WebhookDelivery,
            _PAGE_PARTNER_DELIVERIES,
            path={},
            given={"status": status, "event": event, "cursor": cursor, "limit": limit},
            params=PartnerDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[WebhookDelivery]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.PARTNER_DELIVERIES,
            PartnerDeliveryListResponse,
            WebhookDelivery,
            _PAGE_PARTNER_DELIVERIES,
            path={},
            given={"status": status, "event": event, "cursor": cursor, "limit": limit},
            params=PartnerDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def retry(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerDeliveryRetryResponse:
        """Retry a delivery

        ``POST /v1/partner/webhook/deliveries/{id}/retry``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``not_retryable``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.deliveries.retry('7e3c5d9b-0a4f-4c1e-9b8d-2f6a1c3e5d7b')
        """
        return self._client._call(
            _E.PARTNER_DELIVERY_RETRY,
            PartnerDeliveryRetryResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class PartnerWebhook:
    """``partner.webhook``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.deliveries = PartnerWebhookDeliveries(client)

    def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerWebhookGetResponse:
        """Get the webhook

        ``GET /v1/partner/webhook``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.get()
        """
        return self._client._call(
            _E.PARTNER_WEBHOOK,
            PartnerWebhookGetResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        *,
        events: Sequence[Any] | NotGiven | None = NOT_GIVEN,
        low_balance_threshold_halalas: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerWebhookUpdateResponse:
        """Update the webhook

        ``PUT /v1/partner/webhook``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.update(events=['service.approved', 'service.rejected', 'balance.low'], low_balance_threshold_halalas=10000)
        """
        return self._client._call(
            _E.PARTNER_WEBHOOK_UPDATE,
            PartnerWebhookUpdateResponse,
            path={},
            given={
                "events": events,
                "low_balance_threshold_halalas": low_balance_threshold_halalas,
            },
            params=PartnerWebhookUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class Partner:
    """``partner``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.profile = PartnerProfile(client)
        self.screening = PartnerScreening(client)
        self.applications = PartnerApplications(client)
        self.usage = PartnerUsage(client)
        self.verifications = PartnerVerifications(client)
        self.events = PartnerEvents(client)
        self.webhook = PartnerWebhook(client)


class AsyncPartnerProfile:
    """``partner.profile``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerProfileResponse:
        """Get the profile

        ``GET /v1/partner/profile``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.profile.get()
        """
        return await self._client._call(
            _E.PARTNER_PROFILE,
            PartnerProfileResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncPartnerScreening:
    """``partner.screening``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def check(
        self,
        *,
        name_ar: str,
        name_en: str,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerScreeningResponse:
        """Preview the screening

        ``POST /v1/partner/screening``.
        Never retried once sent.

        Errors: ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.screening.check(name_ar='متجر الورد', name_en='Flower Shop')
        """
        return await self._client._call(
            _E.PARTNER_SCREENING,
            PartnerScreeningResponse,
            path={},
            given={"name_ar": name_ar, "name_en": name_en},
            params=PartnerScreeningParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncPartnerApplications:
    """``partner.applications``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def create(
        self,
        *,
        external_id: str,
        name_ar: str,
        name_en: str,
        website: str,
        industry: str | NotGiven = NOT_GIVEN,
        merchant: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        verify: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationCreateResponse:
        """Provision an application

        ``POST /v1/partner/applications``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.create(external_id='store_88', name_ar='متجر الورد', name_en='Flower Shop', website='https://flowers.example', industry='retail', idempotency_key='provision-store_88')
        """
        return await self._client._call(
            _E.PARTNER_PROVISION,
            PartnerApplicationCreateResponse,
            path={},
            given={
                "external_id": external_id,
                "name_ar": name_ar,
                "name_en": name_en,
                "website": website,
                "industry": industry,
                "merchant": merchant,
                "verify": verify,
                "metadata": metadata,
            },
            params=PartnerApplicationCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def batch(
        self,
        applications: Sequence[Mapping[str, Any] | TawkedParams],
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationBatchResponse:
        """Provision in bulk

        ``POST /v1/partner/applications/batch``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.batch([{'external_id': 'store_88', 'name_ar': 'متجر الورد', 'name_en': 'Flower Shop', 'website': 'https://flowers.example', 'industry': 'retail'}, {'external_id': 'store_89', 'name_ar': 'متجر الهدايا', 'name_en': 'Gift Shop', 'website': 'https://gifts.example', 'industry': 'retail'}])
        """
        if len(applications) > 100:
            raise ValueError("applications holds at most 100 items")
        return await self._client._call(
            _E.PARTNER_BATCH,
            PartnerApplicationBatchResponse,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            list_param=("applications", applications),
        )

    async def list(
        self,
        *,
        status: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[ApplicationRow]:
        """List applications

        ``GET /v1/partner/applications``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.list(status='active', limit=50, offset=0)
        """
        return await self._client._list(
            _E.PARTNER_LIST,
            PartnerApplicationListResponse,
            ApplicationRow,
            _PAGE_PARTNER_LIST,
            path={},
            given={
                "status": status,
                "disabled": disabled,
                "archived": archived,
                "metadata": metadata,
                "limit": limit,
                "offset": offset,
            },
            params=PartnerApplicationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        status: str | NotGiven = NOT_GIVEN,
        disabled: bool | NotGiven = NOT_GIVEN,
        archived: bool | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        offset: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[ApplicationRow]:
        """Every item of :meth:`list`, page after page (offset); the same filters."""
        return self._client._iterate(
            _E.PARTNER_LIST,
            PartnerApplicationListResponse,
            ApplicationRow,
            _PAGE_PARTNER_LIST,
            path={},
            given={
                "status": status,
                "disabled": disabled,
                "archived": archived,
                "metadata": metadata,
                "limit": limit,
                "offset": offset,
            },
            params=PartnerApplicationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        external_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationGetResponse:
        """Get an application

        ``GET /v1/partner/applications/{external_id}``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.get('store_88')
        """
        return await self._client._call(
            _E.PARTNER_SHOW,
            PartnerApplicationGetResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def history(
        self,
        external_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationHistoryResponse:
        """Get the history

        ``GET /v1/partner/applications/{external_id}/history``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.history('store_88')
        """
        return await self._client._call(
            _E.PARTNER_HISTORY,
            PartnerApplicationHistoryResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        external_id: str,
        *,
        name_ar: str,
        name_en: str,
        website: str,
        industry: str | NotGiven = NOT_GIVEN,
        merchant: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        verify: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        metadata: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationUpdateResponse:
        """Update the brand

        ``PATCH /v1/partner/applications/{external_id}``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.update('store_88', name_ar='متجر الورد', name_en='Flower Shop', website='https://flowers.example')
        """
        return await self._client._call(
            _E.PARTNER_UPDATE,
            PartnerApplicationUpdateResponse,
            path={"external_id": external_id},
            given={
                "name_ar": name_ar,
                "name_en": name_en,
                "website": website,
                "industry": industry,
                "merchant": merchant,
                "verify": verify,
                "metadata": metadata,
            },
            params=PartnerApplicationUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def upload_logo(
        self,
        external_id: str,
        *,
        logo: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerLogoUploadResponse:
        """Upload the logo

        ``POST /v1/partner/applications/{external_id}/logo``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``storage_unavailable``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.upload_logo('store_88', logo=open('logo.png', 'rb'))
        """
        return await self._client._call(
            _E.PARTNER_LOGO_UPLOAD,
            PartnerLogoUploadResponse,
            path={"external_id": external_id},
            given={"logo": logo},
            params=PartnerLogoUploadParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("logo",),
        )

    async def remove_logo(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerLogoRemoveResponse:
        """Remove the logo

        ``DELETE /v1/partner/applications/{external_id}/logo``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.remove_logo('store_88')
        """
        return await self._client._call(
            _E.PARTNER_LOGO_REMOVE,
            PartnerLogoRemoveResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update_verify_settings(
        self,
        external_id: str,
        *,
        code_length: int | NotGiven = NOT_GIVEN,
        ttl_seconds: int | NotGiven = NOT_GIVEN,
        max_attempts: int | NotGiven = NOT_GIVEN,
        max_per_hour: int | NotGiven = NOT_GIVEN,
        autofill_domain_enabled: bool | NotGiven = NOT_GIVEN,
        android_app_hash: str | NotGiven | None = NOT_GIVEN,
        daily_spend_cap_halalas: int | NotGiven | None = NOT_GIVEN,
        max_per_ip_per_hour: int | NotGiven = NOT_GIVEN,
        max_new_destinations_per_hour: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerVerifySettingsUpdateResponse:
        """Update the verify settings

        ``PATCH /v1/partner/applications/{external_id}/verify-settings``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.update_verify_settings('store_88', code_length=6, ttl_seconds=300)
        """
        return await self._client._call(
            _E.PARTNER_VERIFY_SETTINGS,
            PartnerVerifySettingsUpdateResponse,
            path={"external_id": external_id},
            given={
                "code_length": code_length,
                "ttl_seconds": ttl_seconds,
                "max_attempts": max_attempts,
                "max_per_hour": max_per_hour,
                "autofill_domain_enabled": autofill_domain_enabled,
                "android_app_hash": android_app_hash,
                "daily_spend_cap_halalas": daily_spend_cap_halalas,
                "max_per_ip_per_hour": max_per_ip_per_hour,
                "max_new_destinations_per_hour": max_new_destinations_per_hour,
            },
            params=PartnerVerifySettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def suspend(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationSuspendResponse:
        """Suspend an application

        ``POST /v1/partner/applications/{external_id}/suspend``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.suspend('store_88')
        """
        return await self._client._call(
            _E.PARTNER_SUSPEND,
            PartnerApplicationSuspendResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def resume(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationResumeResponse:
        """Resume an application

        ``POST /v1/partner/applications/{external_id}/resume``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.resume('store_88')
        """
        return await self._client._call(
            _E.PARTNER_RESUME,
            PartnerApplicationResumeResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def unpause(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationUnpauseResponse:
        """Unpause an application

        ``POST /v1/partner/applications/{external_id}/unpause``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``application_archived``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.unpause('store_88')
        """
        return await self._client._call(
            _E.PARTNER_UNPAUSE,
            PartnerApplicationUnpauseResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def archive(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationArchiveResponse:
        """Archive an application

        ``POST /v1/partner/applications/{external_id}/archive``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``number_connected``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.archive('store_88')
        """
        return await self._client._call(
            _E.PARTNER_ARCHIVE,
            PartnerApplicationArchiveResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def restore(
        self,
        external_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerApplicationRestoreResponse:
        """Restore an application

        ``POST /v1/partner/applications/{external_id}/restore``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.applications.restore('store_88')
        """
        return await self._client._call(
            _E.PARTNER_RESTORE,
            PartnerApplicationRestoreResponse,
            path={"external_id": external_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncPartnerUsage:
    """``partner.usage``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def get(
        self,
        *,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerUsageResponse:
        """Get usage

        ``GET /v1/partner/usage``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.usage.get(from_='2026-10-01', to='2026-10-20')
        """
        return await self._client._call(
            _E.PARTNER_USAGE,
            PartnerUsageResponse,
            path={},
            given={"from": from_, "to": to},
            params=PartnerUsageParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncPartnerVerifications:
    """``partner.verifications``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "verified", "failed", "expired", "canceled"]
        | str
        | NotGiven = NOT_GIVEN,
        mode: Literal["live", "test", "partner", "partner_test"] | str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[PartnerVerificationListItem]:
        """List verifications

        ``GET /v1/partner/verifications``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.verifications.list(status='verified', limit=50)
        """
        return await self._client._list(
            _E.PARTNER_VERIFICATIONS,
            PartnerVerificationListResponse,
            PartnerVerificationListItem,
            _PAGE_PARTNER_VERIFICATIONS,
            path={},
            given={
                "application": application,
                "status": status,
                "mode": mode,
                "reference": reference,
                "from": from_,
                "to": to,
                "cursor": cursor,
                "limit": limit,
            },
            params=PartnerVerificationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        status: Literal["pending", "verified", "failed", "expired", "canceled"]
        | str
        | NotGiven = NOT_GIVEN,
        mode: Literal["live", "test", "partner", "partner_test"] | str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        from_: datetime | str | NotGiven = NOT_GIVEN,
        to: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[PartnerVerificationListItem]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.PARTNER_VERIFICATIONS,
            PartnerVerificationListResponse,
            PartnerVerificationListItem,
            _PAGE_PARTNER_VERIFICATIONS,
            path={},
            given={
                "application": application,
                "status": status,
                "mode": mode,
                "reference": reference,
                "from": from_,
                "to": to,
                "cursor": cursor,
                "limit": limit,
            },
            params=PartnerVerificationListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncPartnerEvents:
    """``partner.events``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def list(
        self,
        *,
        since: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
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
        application: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[PartnerEventListItem]:
        """Get the event feed

        ``GET /v1/partner/events``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.events.list(event='service.approved', limit=50)
        """
        return await self._client._list(
            _E.PARTNER_EVENTS,
            PartnerEventListResponse,
            PartnerEventListItem,
            _PAGE_PARTNER_EVENTS,
            path={},
            given={
                "since": since,
                "cursor": cursor,
                "event": event,
                "application": application,
                "limit": limit,
            },
            params=PartnerEventListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        since: datetime | str | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
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
        application: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[PartnerEventListItem]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.PARTNER_EVENTS,
            PartnerEventListResponse,
            PartnerEventListItem,
            _PAGE_PARTNER_EVENTS,
            path={},
            given={
                "since": since,
                "cursor": cursor,
                "event": event,
                "application": application,
                "limit": limit,
            },
            params=PartnerEventListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncPartnerWebhookDeliveries:
    """``partner.webhook.deliveries``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def list(
        self,
        *,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[WebhookDelivery]:
        """List deliveries

        ``GET /v1/partner/webhook/deliveries``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.deliveries.list(status='failed', limit=50)
        """
        return await self._client._list(
            _E.PARTNER_DELIVERIES,
            PartnerDeliveryListResponse,
            WebhookDelivery,
            _PAGE_PARTNER_DELIVERIES,
            path={},
            given={"status": status, "event": event, "cursor": cursor, "limit": limit},
            params=PartnerDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        status: Literal["pending", "delivered", "failed"] | str | NotGiven = NOT_GIVEN,
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
        cursor: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[WebhookDelivery]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.PARTNER_DELIVERIES,
            PartnerDeliveryListResponse,
            WebhookDelivery,
            _PAGE_PARTNER_DELIVERIES,
            path={},
            given={"status": status, "event": event, "cursor": cursor, "limit": limit},
            params=PartnerDeliveryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def retry(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerDeliveryRetryResponse:
        """Retry a delivery

        ``POST /v1/partner/webhook/deliveries/{id}/retry``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``not_retryable``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.deliveries.retry('7e3c5d9b-0a4f-4c1e-9b8d-2f6a1c3e5d7b')
        """
        return await self._client._call(
            _E.PARTNER_DELIVERY_RETRY,
            PartnerDeliveryRetryResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncPartnerWebhook:
    """``partner.webhook``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.deliveries = AsyncPartnerWebhookDeliveries(client)

    async def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerWebhookGetResponse:
        """Get the webhook

        ``GET /v1/partner/webhook``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.get()
        """
        return await self._client._call(
            _E.PARTNER_WEBHOOK,
            PartnerWebhookGetResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        *,
        events: Sequence[Any] | NotGiven | None = NOT_GIVEN,
        low_balance_threshold_halalas: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> PartnerWebhookUpdateResponse:
        """Update the webhook

        ``PUT /v1/partner/webhook``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``idempotency_in_progress``, ``idempotency_key_reused``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``partner_suspended``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.partner.webhook.update(events=['service.approved', 'service.rejected', 'balance.low'], low_balance_threshold_halalas=10000)
        """
        return await self._client._call(
            _E.PARTNER_WEBHOOK_UPDATE,
            PartnerWebhookUpdateResponse,
            path={},
            given={
                "events": events,
                "low_balance_threshold_halalas": low_balance_threshold_halalas,
            },
            params=PartnerWebhookUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncPartner:
    """``partner``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.profile = AsyncPartnerProfile(client)
        self.screening = AsyncPartnerScreening(client)
        self.applications = AsyncPartnerApplications(client)
        self.usage = AsyncPartnerUsage(client)
        self.verifications = AsyncPartnerVerifications(client)
        self.events = AsyncPartnerEvents(client)
        self.webhook = AsyncPartnerWebhook(client)
