"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked import _generated as _g
from tawked._generated import endpoints as _E
from tawked._generated.endpoints import (
    _PAGE_EMAIL_DOMAINS,
    _PAGE_EMAIL_LIST,
    _PAGE_EMAIL_RECEIVED_LIST,
    _PAGE_EMAIL_SUPPRESSIONS,
    _PAGE_EMAIL_TEMPLATES,
)
from tawked._generated.types import (
    EmailBatchSendParams,
    EmailBatchSendResponse,
    EmailDomain,
    EmailDomainCreateParams,
    EmailDomainCreateResponse,
    EmailDomainDeleteResponse,
    EmailDomainGetResponse,
    EmailDomainListParams,
    EmailDomainListResponse,
    EmailDomainUpdateParams,
    EmailDomainUpdateResponse,
    EmailDomainVerifyResponse,
    EmailInboundAddressListResponse,
    EmailKeyCheckParams,
    EmailKeyCheckResponse,
    EmailMessageCancelParams,
    EmailMessageCancelResponse,
    EmailMessageContentResponse,
    EmailMessageExtended,
    EmailMessageGetParams,
    EmailMessageGetResponse,
    EmailMessageListParams,
    EmailMessageListResponse,
    EmailMessageRescheduleParams,
    EmailMessageRescheduleResponse,
    EmailMetricsGetParams,
    EmailMetricsGetResponse,
    EmailReceivedDeleteResponse,
    EmailReceivedForwardParams,
    EmailReceivedForwardResponse,
    EmailReceivedGetResponse,
    EmailReceivedListItem,
    EmailReceivedListParams,
    EmailReceivedListResponse,
    EmailReceivedTestResponse,
    EmailSendParams,
    EmailSendResponse,
    EmailSuppression,
    EmailSuppressionAddParams,
    EmailSuppressionAddResponse,
    EmailSuppressionGetResponse,
    EmailSuppressionImportCreateParams,
    EmailSuppressionImportCreateResponse,
    EmailSuppressionImportGetResponse,
    EmailSuppressionListParams,
    EmailSuppressionListResponse,
    EmailSuppressionRemoveParams,
    EmailSuppressionRemoveResponse,
    EmailTemplate,
    EmailTemplateCreateParams,
    EmailTemplateCreateResponse,
    EmailTemplateDeleteResponse,
    EmailTemplateGetResponse,
    EmailTemplateListParams,
    EmailTemplateListResponse,
    EmailTemplatePublishResponse,
    EmailTemplateUpdateParams,
    EmailTemplateUpdateResponse,
    EmailTemplateVersionGetResponse,
    EmailTemplateVersionListResponse,
    EmailTemplateVersionRestoreResponse,
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


class EmailMessages:
    """``email.messages``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def send(
        self,
        *,
        subject: str,
        from_: str | Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        to: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        cc: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        bcc: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        reply_to: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        html: str | NotGiven | None = NOT_GIVEN,
        text: str | NotGiven | None = NOT_GIVEN,
        template: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven | None = NOT_GIVEN,
        headers: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        tags: Sequence[Mapping[str, Any]] | NotGiven | None = NOT_GIVEN,
        scheduled_at: datetime | str | NotGiven | None = NOT_GIVEN,
        attachments: Sequence[Mapping[str, Any]] | NotGiven | None = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSendResponse:
        """Send an email

        ``POST /v1/email/messages``, scope ``email:send``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``attachment_invalid``, ``attachment_type_blocked``, ``attachments_too_large``, ``content_blocked``, ``daily_cap_reached``, ``email_early_access``, ``email_paused``, ``email_platform_busy``, ``header_not_allowed``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_domain_mismatch``, ``key_expired``, ``live_key_required``, ``message_too_large``, ``no_verified_domain``, ``rate_limited``, ``recipient_suppressed``, ``request_too_large``, ``sender_not_verified``, ``service_not_found``, ``service_required``, ``service_unavailable``, ``template_not_found``, ``template_not_published``, ``template_variable_invalid``, ``template_variable_missing``, ``template_variable_unknown``, ``template_variables_invalid``, ``test_mode_limit_reached``, ``test_mode_recipient``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.send(from_={'name': 'متجر أكمي', 'address': 'orders@acme.sa'}, to=['sara@example.com'], subject='طلبك رقم 1042 قيد التجهيز', html='<p>استلمنا طلبك رقم 1042، وسنرسل رابط التتبع حين يُشحن.</p>', text='استلمنا طلبك رقم 1042، وسنرسل رابط التتبع حين يُشحن.', reference='order-1042', tags=[{'name': 'category', 'value': 'order'}], idempotency_key='order-1042-confirmation')
        """
        return self._client._call(
            _E.EMAIL_SEND,
            EmailSendResponse,
            path={},
            given={
                "from": from_,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "reply_to": reply_to,
                "subject": subject,
                "html": html,
                "text": text,
                "template": template,
                "reference": reference,
                "headers": headers,
                "tags": tags,
                "scheduled_at": scheduled_at,
                "attachments": attachments,
                "application": application,
            },
            params=EmailSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def send_batch(
        self,
        emails: Sequence[Mapping[str, Any] | TawkedParams],
        *,
        application: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailBatchSendResponse:
        """Send a batch of emails

        ``POST /v1/email/messages/batch``, scope ``email:send``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``batch_invalid``, ``content_blocked``, ``daily_cap_reached``, ``email_early_access``, ``email_paused``, ``email_platform_busy``, ``header_not_allowed``, ``idempotency_key_reused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_domain_mismatch``, ``key_expired``, ``live_key_required``, ``message_too_large``, ``no_verified_domain``, ``rate_limited``, ``request_too_large``, ``sender_not_verified``, ``service_not_found``, ``service_required``, ``service_unavailable``, ``template_not_found``, ``template_not_published``, ``template_variable_invalid``, ``template_variable_missing``, ``template_variable_unknown``, ``template_variables_invalid``, ``test_mode_limit_reached``, ``test_mode_recipient``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.send_batch(...)
        """
        if len(emails) > 100:
            raise ValueError("emails holds at most 100 items")
        return self._client._call(
            _E.EMAIL_BATCH,
            EmailBatchSendResponse,
            path={},
            given={"application": application},
            params=EmailBatchSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            list_param=("emails", emails),
        )

    @early_access
    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailMessageExtended]:
        """List emails

        ``GET /v1/email/messages``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.list(limit=20, status='delivered')
        """
        return self._client._list(
            _E.EMAIL_LIST,
            EmailMessageListResponse,
            EmailMessageExtended,
            _PAGE_EMAIL_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "status": status,
                "to": to,
                "reference": reference,
                "tag": tag,
                "created_after": created_after,
                "created_before": created_before,
                "application": application,
            },
            params=EmailMessageListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[EmailMessageExtended]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_LIST,
            EmailMessageListResponse,
            EmailMessageExtended,
            _PAGE_EMAIL_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "status": status,
                "to": to,
                "reference": reference,
                "tag": tag,
                "created_after": created_after,
                "created_before": created_before,
                "application": application,
            },
            params=EmailMessageListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def get(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageGetResponse:
        """Get an email

        ``GET /v1/email/messages/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.get('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return self._client._call(
            _E.EMAIL_MESSAGE,
            EmailMessageGetResponse,
            path={"id": id},
            given={"application": application},
            params=EmailMessageGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def update(
        self,
        id: str,
        *,
        scheduled_at: datetime | str,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageRescheduleResponse:
        """Reschedule an email

        ``PATCH /v1/email/messages/{id}``, scope ``email:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``daily_cap_reached``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``message_not_scheduled``, ``not_found``, ``rate_limited``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.update('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d', scheduled_at='2026-10-23T09:00:00+03:00')
        """
        return self._client._call(
            _E.EMAIL_UPDATE,
            EmailMessageRescheduleResponse,
            path={"id": id},
            given={"scheduled_at": scheduled_at, "application": application},
            params=EmailMessageRescheduleParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def cancel(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageCancelResponse:
        """Cancel a scheduled email

        ``POST /v1/email/messages/{id}/cancel``, scope ``email:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``message_not_scheduled``, ``not_found``, ``rate_limited``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.cancel('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return self._client._call(
            _E.EMAIL_CANCEL,
            EmailMessageCancelResponse,
            path={"id": id},
            given={"application": application},
            params=EmailMessageCancelParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def content(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageContentResponse:
        """Get an email's content

        ``GET /v1/email/messages/{id}/content``, scope ``email:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``content_not_kept``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.content('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return self._client._call(
            _E.EMAIL_MESSAGE_CONTENT,
            EmailMessageContentResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class EmailDomains:
    """``email.domains``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def list(
        self,
        *,
        state: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailDomain]:
        """List domains

        ``GET /v1/email/domains``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.list(state='verified', limit=20)
        """
        return self._client._list(
            _E.EMAIL_DOMAINS,
            EmailDomainListResponse,
            EmailDomain,
            _PAGE_EMAIL_DOMAINS,
            path={},
            given={"state": state, "limit": limit, "cursor": cursor},
            params=EmailDomainListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        state: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[EmailDomain]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_DOMAINS,
            EmailDomainListResponse,
            EmailDomain,
            _PAGE_EMAIL_DOMAINS,
            path={},
            given={"state": state, "limit": limit, "cursor": cursor},
            params=EmailDomainListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def create(
        self,
        *,
        name: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainCreateResponse:
        """Add a domain

        ``POST /v1/email/domains``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``domain_invalid``, ``domain_limit``, ``domain_public``, ``domain_taken``, ``domain_tawked``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``rate_limited``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.create(name='acme.sa', idempotency_key='domain-acme.sa')
        """
        return self._client._call(
            _E.EMAIL_DOMAIN_CREATE,
            EmailDomainCreateResponse,
            path={},
            given={"name": name},
            params=EmailDomainCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainGetResponse:
        """Get a domain

        ``GET /v1/email/domains/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.get('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return self._client._call(
            _E.EMAIL_DOMAIN,
            EmailDomainGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def update(
        self,
        id: str,
        *,
        from_name: str | NotGiven = NOT_GIVEN,
        from_local: str | NotGiven = NOT_GIVEN,
        tracking: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainUpdateResponse:
        """Update a domain

        ``PATCH /v1/email/domains/{id}``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``domain_not_verified``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``tracking_subdomain_invalid``, ``tracking_subdomain_taken``, ``tracking_unavailable``, ``unauthorized``.

        Example::

            tawked.email.domains.update('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d', from_name='متجر أكمي', from_local='orders')
        """
        return self._client._call(
            _E.EMAIL_DOMAIN_UPDATE,
            EmailDomainUpdateResponse,
            path={"id": id},
            given={"from_name": from_name, "from_local": from_local, "tracking": tracking},
            params=EmailDomainUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def verify(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainVerifyResponse:
        """Check a domain now

        ``POST /v1/email/domains/{id}/verify``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``rate_limited``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.verify('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return self._client._call(
            _E.EMAIL_DOMAIN_VERIFY,
            EmailDomainVerifyResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def delete(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainDeleteResponse:
        """Remove a domain

        ``DELETE /v1/email/domains/{id}``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.delete('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return self._client._call(
            _E.EMAIL_DOMAIN_DELETE,
            EmailDomainDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class EmailSuppressionsImports:
    """``email.suppressions.imports``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def create(
        self,
        *,
        file: FileInput,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionImportCreateResponse:
        """Import suppressed addresses

        ``POST /v1/email/suppressions/imports``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``suppression_import_daily``, ``suppression_import_invalid_file``, ``suppression_import_running``, ``suppression_import_too_large``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.imports.create(file=open('unsubscribed.csv', 'rb'))
        """
        return self._client._call(
            _E.EMAIL_SUPPRESSIONS_IMPORT,
            EmailSuppressionImportCreateResponse,
            path={},
            given={"file": file},
            params=EmailSuppressionImportCreateParams,
            opts=options(None, timeout, max_retries, extra_headers),
            files=("file",),
        )

    @early_access
    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionImportGetResponse:
        """Get an import

        ``GET /v1/email/suppressions/imports/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.imports.get('0199f1e0-2c3d-7e4f-9a5b-6c7d8e9f0a12')
        """
        return self._client._call(
            _E.EMAIL_SUPPRESSIONS_IMPORT_STATUS,
            EmailSuppressionImportGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class EmailSuppressions:
    """``email.suppressions``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.imports = EmailSuppressionsImports(client)

    @early_access
    def list(
        self,
        *,
        reason: str | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        address: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailSuppression]:
        """List suppressed addresses

        ``GET /v1/email/suppressions``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.list(reason='bounce', limit=20)
        """
        return self._client._list(
            _E.EMAIL_SUPPRESSIONS,
            EmailSuppressionListResponse,
            EmailSuppression,
            _PAGE_EMAIL_SUPPRESSIONS,
            path={},
            given={
                "reason": reason,
                "source": source,
                "address": address,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=EmailSuppressionListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        reason: str | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        address: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[EmailSuppression]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_SUPPRESSIONS,
            EmailSuppressionListResponse,
            EmailSuppression,
            _PAGE_EMAIL_SUPPRESSIONS,
            path={},
            given={
                "reason": reason,
                "source": source,
                "address": address,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=EmailSuppressionListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def add(
        self,
        *,
        addresses: Sequence[str] | NotGiven = NOT_GIVEN,
        address: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionAddResponse:
        """Suppress addresses

        ``POST /v1/email/suppressions``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``suppression_invalid_addresses``, ``suppression_too_many``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.add(addresses=['sara@example.com', 'omar@example.com'], idempotency_key='suppress-2026-10-23')
        """
        return self._client._call(
            _E.EMAIL_SUPPRESSIONS_ADD,
            EmailSuppressionAddResponse,
            path={},
            given={"addresses": addresses, "address": address},
            params=EmailSuppressionAddParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def get(
        self,
        address: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionGetResponse:
        """Look up an address

        ``GET /v1/email/suppressions/{address}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.get('sara@example.com')
        """
        return self._client._call(
            _E.EMAIL_SUPPRESSION,
            EmailSuppressionGetResponse,
            path={"address": address},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def remove(
        self,
        address: str,
        *,
        reason: Literal["recipient_asked", "reported_by_mistake", "other"]
        | str
        | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionRemoveResponse:
        """Lift an address

        ``DELETE /v1/email/suppressions/{address}``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``suppression_lift_reason_required``, ``suppression_team_only``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.remove('sara@example.com', reason='recipient_asked')
        """
        return self._client._call(
            _E.EMAIL_SUPPRESSION_DELETE,
            EmailSuppressionRemoveResponse,
            path={"address": address},
            given={"reason": reason, "note": note},
            params=EmailSuppressionRemoveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class EmailMetrics:
    """``email.metrics``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def get(
        self,
        *,
        from_: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        granularity: Literal["day", "week", "month"] | str | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        timezone: Literal["Asia/Riyadh"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMetricsGetResponse:
        """Get email metrics

        ``GET /v1/email/metrics``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.metrics.get(from_='2026-10-01', to='2026-10-20', granularity='day')
        """
        return self._client._call(
            _E.EMAIL_METRICS,
            EmailMetricsGetResponse,
            path={},
            given={
                "from": from_,
                "to": to,
                "granularity": granularity,
                "domain": domain,
                "timezone": timezone,
            },
            params=EmailMetricsGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class EmailTemplatesVersions:
    """``email.templates.versions``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def list(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateVersionListResponse:
        """List a template's versions

        ``GET /v1/email/templates/{id}/versions``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.versions.list('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_VERSIONS,
            EmailTemplateVersionListResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def get(
        self,
        id: str,
        number: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateVersionGetResponse:
        """Get a template version

        ``GET /v1/email/templates/{id}/versions/{number}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.versions.get('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12', 2)
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_VERSION,
            EmailTemplateVersionGetResponse,
            path={"id": id, "number": number},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def restore(
        self,
        id: str,
        number: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateVersionRestoreResponse:
        """Restore a template version

        ``POST /v1/email/templates/{id}/versions/{number}/restore``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.versions.restore('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12', 2)
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_RESTORE,
            EmailTemplateVersionRestoreResponse,
            path={"id": id, "number": number},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class EmailTemplates:
    """``email.templates``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.versions = EmailTemplatesVersions(client)

    @early_access
    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailTemplate]:
        """List templates

        ``GET /v1/email/templates``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.list(limit=20)
        """
        return self._client._list(
            _E.EMAIL_TEMPLATES,
            EmailTemplateListResponse,
            EmailTemplate,
            _PAGE_EMAIL_TEMPLATES,
            path={},
            given={"limit": limit, "cursor": cursor},
            params=EmailTemplateListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[EmailTemplate]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_TEMPLATES,
            EmailTemplateListResponse,
            EmailTemplate,
            _PAGE_EMAIL_TEMPLATES,
            path={},
            given={"limit": limit, "cursor": cursor},
            params=EmailTemplateListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def create(
        self,
        *,
        name: str,
        subject: str,
        alias: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        from_: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reply_to: Sequence[str] | NotGiven = NOT_GIVEN,
        variables: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateCreateResponse:
        """Create a template

        ``POST /v1/email/templates``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``template_alias_invalid``, ``template_alias_taken``, ``template_invalid``, ``template_limit``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.create(name='تم شحن الطلب', alias='order-shipped', subject='طلبك {{ ORDER }} في الطريق', html='<p>مرحبًا {{ NAME }}، طلبك {{ ORDER }} في الطريق.</p>', variables=[{'key': 'ORDER'}, {'key': 'NAME', 'fallback': 'عميلنا'}], publish=True, idempotency_key='template-order-shipped')
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_CREATE,
            EmailTemplateCreateResponse,
            path={},
            given={
                "name": name,
                "alias": alias,
                "subject": subject,
                "html": html,
                "text": text,
                "from": from_,
                "reply_to": reply_to,
                "variables": variables,
                "publish": publish,
            },
            params=EmailTemplateCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateGetResponse:
        """Get a template

        ``GET /v1/email/templates/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.get('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE,
            EmailTemplateGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        alias: str | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        from_: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reply_to: Sequence[str] | NotGiven = NOT_GIVEN,
        variables: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateUpdateResponse:
        """Update a template

        ``PATCH /v1/email/templates/{id}``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``template_alias_invalid``, ``template_alias_taken``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.update('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12', subject='طلبك {{ ORDER }} شُحن')
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_UPDATE,
            EmailTemplateUpdateResponse,
            path={"id": id},
            given={
                "name": name,
                "alias": alias,
                "subject": subject,
                "html": html,
                "text": text,
                "from": from_,
                "reply_to": reply_to,
                "variables": variables,
                "publish": publish,
            },
            params=EmailTemplateUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def delete(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateDeleteResponse:
        """Delete a template

        ``DELETE /v1/email/templates/{id}``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.delete('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_DELETE,
            EmailTemplateDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def publish(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplatePublishResponse:
        """Publish a template

        ``POST /v1/email/templates/{id}/publish``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``template_invalid``, ``template_no_draft``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.publish('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return self._client._call(
            _E.EMAIL_TEMPLATE_PUBLISH,
            EmailTemplatePublishResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class EmailInboundAttachments:
    """``email.inbound.attachments``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def get(
        self,
        id: str,
        attachment: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> bytes:
        """Download a received attachment

        ``GET /v1/email/received/{id}/attachments/{attachment}``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``received_content_gone``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.attachments.get('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60', '0199f241-8c9d-7e0f-9a1b-2c3d4e5f6071')
        """
        return self._client._call_binary(
            _E.EMAIL_RECEIVED_ATTACHMENT,
            path={"id": id, "attachment": attachment},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class EmailInboundAddresses:
    """``email.inbound.addresses``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    @early_access
    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailInboundAddressListResponse:
        """List receiving addresses

        ``GET /v1/email/inbound-addresses``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.addresses.list()
        """
        return self._client._call(
            _E.EMAIL_INBOUND_ADDRESSES,
            EmailInboundAddressListResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class EmailInbound:
    """``email.inbound``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.attachments = EmailInboundAttachments(client)
        self.addresses = EmailInboundAddresses(client)

    @early_access
    def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        address_id: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        spam: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        has_attachments: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        received_after: datetime | str | NotGiven = NOT_GIVEN,
        received_before: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailReceivedListItem]:
        """List received emails

        ``GET /v1/email/received``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.list(limit=20, spam='false')
        """
        return self._client._list(
            _E.EMAIL_RECEIVED_LIST,
            EmailReceivedListResponse,
            EmailReceivedListItem,
            _PAGE_EMAIL_RECEIVED_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "address_id": address_id,
                "to": to,
                "from": from_,
                "spam": spam,
                "has_attachments": has_attachments,
                "received_after": received_after,
                "received_before": received_before,
            },
            params=EmailReceivedListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        address_id: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        spam: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        has_attachments: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        received_after: datetime | str | NotGiven = NOT_GIVEN,
        received_before: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[EmailReceivedListItem]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_RECEIVED_LIST,
            EmailReceivedListResponse,
            EmailReceivedListItem,
            _PAGE_EMAIL_RECEIVED_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "address_id": address_id,
                "to": to,
                "from": from_,
                "spam": spam,
                "has_attachments": has_attachments,
                "received_after": received_after,
                "received_before": received_before,
            },
            params=EmailReceivedListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedGetResponse:
        """Get a received email

        ``GET /v1/email/received/{id}``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.get('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60')
        """
        return self._client._call(
            _E.EMAIL_RECEIVED,
            EmailReceivedGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def raw(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> bytes:
        """Download a received email's raw message

        ``GET /v1/email/received/{id}/raw``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``received_content_gone``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.raw('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60')
        """
        return self._client._call_binary(
            _E.EMAIL_RECEIVED_RAW,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedDeleteResponse:
        """Delete a received email

        ``DELETE /v1/email/received/{id}``, scope ``email:inbound``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.delete('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60')
        """
        return self._client._call(
            _E.EMAIL_RECEIVED_DELETE,
            EmailReceivedDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def forward(
        self,
        id: str,
        *,
        to: str | Sequence[str],
        from_: str | Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        note: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedForwardResponse:
        """Forward a received email

        ``POST /v1/email/received/{id}/forward``, scope ``email:inbound``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``content_blocked``, ``daily_cap_reached``, ``email_early_access``, ``email_paused``, ``email_platform_busy``, ``forward_risky_attachment``, ``forward_too_large``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``message_too_large``, ``no_verified_domain``, ``not_found``, ``rate_limited``, ``received_content_gone``, ``received_not_ready``, ``sender_not_verified``, ``service_unavailable``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.forward('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60', to=['support@acme.sa'], note='من صندوق الطلبات', idempotency_key='forward-order-1042')
        """
        return self._client._call(
            _E.EMAIL_RECEIVED_FORWARD,
            EmailReceivedForwardResponse,
            path={"id": id},
            given={"to": to, "from": from_, "note": note},
            params=EmailReceivedForwardParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    def test(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedTestResponse:
        """Simulate a received email

        ``POST /v1/email/received/test``, scope ``email:send``.
        Never retried once sent.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``email_early_access``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``test_key_required``, ``test_mode_limit_reached``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.test()
        """
        return self._client._call(
            _E.EMAIL_RECEIVED_TEST,
            EmailReceivedTestResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class Email:
    """``email``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.messages = EmailMessages(client)
        self.domains = EmailDomains(client)
        self.suppressions = EmailSuppressions(client)
        self.metrics = EmailMetrics(client)
        self.templates = EmailTemplates(client)
        self.inbound = EmailInbound(client)

    @early_access
    def check_key(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailKeyCheckResponse:
        """Check an email key

        ``GET /v1/email/key``, scope ``email:send``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``email_early_access``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.check_key()
        """
        return self._client._call(
            _E.EMAIL_KEY,
            EmailKeyCheckResponse,
            path={},
            given={"application": application},
            params=EmailKeyCheckParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmailMessages:
    """``email.messages``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def send(
        self,
        *,
        subject: str,
        from_: str | Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        to: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        cc: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        bcc: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        reply_to: str | Sequence[str] | NotGiven | None = NOT_GIVEN,
        html: str | NotGiven | None = NOT_GIVEN,
        text: str | NotGiven | None = NOT_GIVEN,
        template: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven | None = NOT_GIVEN,
        headers: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        tags: Sequence[Mapping[str, Any]] | NotGiven | None = NOT_GIVEN,
        scheduled_at: datetime | str | NotGiven | None = NOT_GIVEN,
        attachments: Sequence[Mapping[str, Any]] | NotGiven | None = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSendResponse:
        """Send an email

        ``POST /v1/email/messages``, scope ``email:send``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``attachment_invalid``, ``attachment_type_blocked``, ``attachments_too_large``, ``content_blocked``, ``daily_cap_reached``, ``email_early_access``, ``email_paused``, ``email_platform_busy``, ``header_not_allowed``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_domain_mismatch``, ``key_expired``, ``live_key_required``, ``message_too_large``, ``no_verified_domain``, ``rate_limited``, ``recipient_suppressed``, ``request_too_large``, ``sender_not_verified``, ``service_not_found``, ``service_required``, ``service_unavailable``, ``template_not_found``, ``template_not_published``, ``template_variable_invalid``, ``template_variable_missing``, ``template_variable_unknown``, ``template_variables_invalid``, ``test_mode_limit_reached``, ``test_mode_recipient``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.send(from_={'name': 'متجر أكمي', 'address': 'orders@acme.sa'}, to=['sara@example.com'], subject='طلبك رقم 1042 قيد التجهيز', html='<p>استلمنا طلبك رقم 1042، وسنرسل رابط التتبع حين يُشحن.</p>', text='استلمنا طلبك رقم 1042، وسنرسل رابط التتبع حين يُشحن.', reference='order-1042', tags=[{'name': 'category', 'value': 'order'}], idempotency_key='order-1042-confirmation')
        """
        return await self._client._call(
            _E.EMAIL_SEND,
            EmailSendResponse,
            path={},
            given={
                "from": from_,
                "to": to,
                "cc": cc,
                "bcc": bcc,
                "reply_to": reply_to,
                "subject": subject,
                "html": html,
                "text": text,
                "template": template,
                "reference": reference,
                "headers": headers,
                "tags": tags,
                "scheduled_at": scheduled_at,
                "attachments": attachments,
                "application": application,
            },
            params=EmailSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def send_batch(
        self,
        emails: Sequence[Mapping[str, Any] | TawkedParams],
        *,
        application: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailBatchSendResponse:
        """Send a batch of emails

        ``POST /v1/email/messages/batch``, scope ``email:send``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``batch_invalid``, ``content_blocked``, ``daily_cap_reached``, ``email_early_access``, ``email_paused``, ``email_platform_busy``, ``header_not_allowed``, ``idempotency_key_reused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_domain_mismatch``, ``key_expired``, ``live_key_required``, ``message_too_large``, ``no_verified_domain``, ``rate_limited``, ``request_too_large``, ``sender_not_verified``, ``service_not_found``, ``service_required``, ``service_unavailable``, ``template_not_found``, ``template_not_published``, ``template_variable_invalid``, ``template_variable_missing``, ``template_variable_unknown``, ``template_variables_invalid``, ``test_mode_limit_reached``, ``test_mode_recipient``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.send_batch(...)
        """
        if len(emails) > 100:
            raise ValueError("emails holds at most 100 items")
        return await self._client._call(
            _E.EMAIL_BATCH,
            EmailBatchSendResponse,
            path={},
            given={"application": application},
            params=EmailBatchSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            list_param=("emails", emails),
        )

    @early_access
    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailMessageExtended]:
        """List emails

        ``GET /v1/email/messages``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.list(limit=20, status='delivered')
        """
        return await self._client._list(
            _E.EMAIL_LIST,
            EmailMessageListResponse,
            EmailMessageExtended,
            _PAGE_EMAIL_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "status": status,
                "to": to,
                "reference": reference,
                "tag": tag,
                "created_after": created_after,
                "created_before": created_before,
                "application": application,
            },
            params=EmailMessageListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        status: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[EmailMessageExtended]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_LIST,
            EmailMessageListResponse,
            EmailMessageExtended,
            _PAGE_EMAIL_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "status": status,
                "to": to,
                "reference": reference,
                "tag": tag,
                "created_after": created_after,
                "created_before": created_before,
                "application": application,
            },
            params=EmailMessageListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def get(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageGetResponse:
        """Get an email

        ``GET /v1/email/messages/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.get('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return await self._client._call(
            _E.EMAIL_MESSAGE,
            EmailMessageGetResponse,
            path={"id": id},
            given={"application": application},
            params=EmailMessageGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def update(
        self,
        id: str,
        *,
        scheduled_at: datetime | str,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageRescheduleResponse:
        """Reschedule an email

        ``PATCH /v1/email/messages/{id}``, scope ``email:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``daily_cap_reached``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``message_not_scheduled``, ``not_found``, ``rate_limited``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.update('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d', scheduled_at='2026-10-23T09:00:00+03:00')
        """
        return await self._client._call(
            _E.EMAIL_UPDATE,
            EmailMessageRescheduleResponse,
            path={"id": id},
            given={"scheduled_at": scheduled_at, "application": application},
            params=EmailMessageRescheduleParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def cancel(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageCancelResponse:
        """Cancel a scheduled email

        ``POST /v1/email/messages/{id}/cancel``, scope ``email:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``message_not_scheduled``, ``not_found``, ``rate_limited``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.cancel('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return await self._client._call(
            _E.EMAIL_CANCEL,
            EmailMessageCancelResponse,
            path={"id": id},
            given={"application": application},
            params=EmailMessageCancelParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def content(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMessageContentResponse:
        """Get an email's content

        ``GET /v1/email/messages/{id}/content``, scope ``email:manage``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``content_not_kept``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.messages.content('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return await self._client._call(
            _E.EMAIL_MESSAGE_CONTENT,
            EmailMessageContentResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmailDomains:
    """``email.domains``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def list(
        self,
        *,
        state: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailDomain]:
        """List domains

        ``GET /v1/email/domains``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.list(state='verified', limit=20)
        """
        return await self._client._list(
            _E.EMAIL_DOMAINS,
            EmailDomainListResponse,
            EmailDomain,
            _PAGE_EMAIL_DOMAINS,
            path={},
            given={"state": state, "limit": limit, "cursor": cursor},
            params=EmailDomainListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        state: str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[EmailDomain]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_DOMAINS,
            EmailDomainListResponse,
            EmailDomain,
            _PAGE_EMAIL_DOMAINS,
            path={},
            given={"state": state, "limit": limit, "cursor": cursor},
            params=EmailDomainListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def create(
        self,
        *,
        name: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainCreateResponse:
        """Add a domain

        ``POST /v1/email/domains``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``domain_invalid``, ``domain_limit``, ``domain_public``, ``domain_taken``, ``domain_tawked``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``rate_limited``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.create(name='acme.sa', idempotency_key='domain-acme.sa')
        """
        return await self._client._call(
            _E.EMAIL_DOMAIN_CREATE,
            EmailDomainCreateResponse,
            path={},
            given={"name": name},
            params=EmailDomainCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainGetResponse:
        """Get a domain

        ``GET /v1/email/domains/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.get('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return await self._client._call(
            _E.EMAIL_DOMAIN,
            EmailDomainGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def update(
        self,
        id: str,
        *,
        from_name: str | NotGiven = NOT_GIVEN,
        from_local: str | NotGiven = NOT_GIVEN,
        tracking: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainUpdateResponse:
        """Update a domain

        ``PATCH /v1/email/domains/{id}``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``domain_not_verified``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``tracking_subdomain_invalid``, ``tracking_subdomain_taken``, ``tracking_unavailable``, ``unauthorized``.

        Example::

            tawked.email.domains.update('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d', from_name='متجر أكمي', from_local='orders')
        """
        return await self._client._call(
            _E.EMAIL_DOMAIN_UPDATE,
            EmailDomainUpdateResponse,
            path={"id": id},
            given={"from_name": from_name, "from_local": from_local, "tracking": tracking},
            params=EmailDomainUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def verify(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainVerifyResponse:
        """Check a domain now

        ``POST /v1/email/domains/{id}/verify``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``rate_limited``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.verify('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return await self._client._call(
            _E.EMAIL_DOMAIN_VERIFY,
            EmailDomainVerifyResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def delete(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailDomainDeleteResponse:
        """Remove a domain

        ``DELETE /v1/email/domains/{id}``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``email_unavailable``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.domains.delete('0199f1c2-7a41-7c3e-9d2b-5e8f1a2b3c4d')
        """
        return await self._client._call(
            _E.EMAIL_DOMAIN_DELETE,
            EmailDomainDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncEmailSuppressionsImports:
    """``email.suppressions.imports``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def create(
        self,
        *,
        file: FileInput,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionImportCreateResponse:
        """Import suppressed addresses

        ``POST /v1/email/suppressions/imports``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``suppression_import_daily``, ``suppression_import_invalid_file``, ``suppression_import_running``, ``suppression_import_too_large``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.imports.create(file=open('unsubscribed.csv', 'rb'))
        """
        return await self._client._call(
            _E.EMAIL_SUPPRESSIONS_IMPORT,
            EmailSuppressionImportCreateResponse,
            path={},
            given={"file": file},
            params=EmailSuppressionImportCreateParams,
            opts=options(None, timeout, max_retries, extra_headers),
            files=("file",),
        )

    @early_access
    async def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionImportGetResponse:
        """Get an import

        ``GET /v1/email/suppressions/imports/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.imports.get('0199f1e0-2c3d-7e4f-9a5b-6c7d8e9f0a12')
        """
        return await self._client._call(
            _E.EMAIL_SUPPRESSIONS_IMPORT_STATUS,
            EmailSuppressionImportGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmailSuppressions:
    """``email.suppressions``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.imports = AsyncEmailSuppressionsImports(client)

    @early_access
    async def list(
        self,
        *,
        reason: str | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        address: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailSuppression]:
        """List suppressed addresses

        ``GET /v1/email/suppressions``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.list(reason='bounce', limit=20)
        """
        return await self._client._list(
            _E.EMAIL_SUPPRESSIONS,
            EmailSuppressionListResponse,
            EmailSuppression,
            _PAGE_EMAIL_SUPPRESSIONS,
            path={},
            given={
                "reason": reason,
                "source": source,
                "address": address,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=EmailSuppressionListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        reason: str | NotGiven = NOT_GIVEN,
        source: str | NotGiven = NOT_GIVEN,
        address: str | NotGiven = NOT_GIVEN,
        created_after: datetime | str | NotGiven = NOT_GIVEN,
        created_before: datetime | str | NotGiven = NOT_GIVEN,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[EmailSuppression]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_SUPPRESSIONS,
            EmailSuppressionListResponse,
            EmailSuppression,
            _PAGE_EMAIL_SUPPRESSIONS,
            path={},
            given={
                "reason": reason,
                "source": source,
                "address": address,
                "created_after": created_after,
                "created_before": created_before,
                "limit": limit,
                "cursor": cursor,
            },
            params=EmailSuppressionListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def add(
        self,
        *,
        addresses: Sequence[str] | NotGiven = NOT_GIVEN,
        address: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionAddResponse:
        """Suppress addresses

        ``POST /v1/email/suppressions``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``suppression_invalid_addresses``, ``suppression_too_many``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.add(addresses=['sara@example.com', 'omar@example.com'], idempotency_key='suppress-2026-10-23')
        """
        return await self._client._call(
            _E.EMAIL_SUPPRESSIONS_ADD,
            EmailSuppressionAddResponse,
            path={},
            given={"addresses": addresses, "address": address},
            params=EmailSuppressionAddParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def get(
        self,
        address: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionGetResponse:
        """Look up an address

        ``GET /v1/email/suppressions/{address}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.get('sara@example.com')
        """
        return await self._client._call(
            _E.EMAIL_SUPPRESSION,
            EmailSuppressionGetResponse,
            path={"address": address},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def remove(
        self,
        address: str,
        *,
        reason: Literal["recipient_asked", "reported_by_mistake", "other"]
        | str
        | NotGiven = NOT_GIVEN,
        note: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailSuppressionRemoveResponse:
        """Lift an address

        ``DELETE /v1/email/suppressions/{address}``, scope ``email:manage``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``suppression_lift_reason_required``, ``suppression_team_only``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.suppressions.remove('sara@example.com', reason='recipient_asked')
        """
        return await self._client._call(
            _E.EMAIL_SUPPRESSION_DELETE,
            EmailSuppressionRemoveResponse,
            path={"address": address},
            given={"reason": reason, "note": note},
            params=EmailSuppressionRemoveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncEmailMetrics:
    """``email.metrics``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def get(
        self,
        *,
        from_: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        granularity: Literal["day", "week", "month"] | str | NotGiven = NOT_GIVEN,
        domain: str | NotGiven = NOT_GIVEN,
        timezone: Literal["Asia/Riyadh"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailMetricsGetResponse:
        """Get email metrics

        ``GET /v1/email/metrics``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.metrics.get(from_='2026-10-01', to='2026-10-20', granularity='day')
        """
        return await self._client._call(
            _E.EMAIL_METRICS,
            EmailMetricsGetResponse,
            path={},
            given={
                "from": from_,
                "to": to,
                "granularity": granularity,
                "domain": domain,
                "timezone": timezone,
            },
            params=EmailMetricsGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmailTemplatesVersions:
    """``email.templates.versions``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def list(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateVersionListResponse:
        """List a template's versions

        ``GET /v1/email/templates/{id}/versions``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.versions.list('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_VERSIONS,
            EmailTemplateVersionListResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def get(
        self,
        id: str,
        number: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateVersionGetResponse:
        """Get a template version

        ``GET /v1/email/templates/{id}/versions/{number}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.versions.get('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12', 2)
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_VERSION,
            EmailTemplateVersionGetResponse,
            path={"id": id, "number": number},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def restore(
        self,
        id: str,
        number: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateVersionRestoreResponse:
        """Restore a template version

        ``POST /v1/email/templates/{id}/versions/{number}/restore``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.versions.restore('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12', 2)
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_RESTORE,
            EmailTemplateVersionRestoreResponse,
            path={"id": id, "number": number},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncEmailTemplates:
    """``email.templates``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.versions = AsyncEmailTemplatesVersions(client)

    @early_access
    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailTemplate]:
        """List templates

        ``GET /v1/email/templates``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.list(limit=20)
        """
        return await self._client._list(
            _E.EMAIL_TEMPLATES,
            EmailTemplateListResponse,
            EmailTemplate,
            _PAGE_EMAIL_TEMPLATES,
            path={},
            given={"limit": limit, "cursor": cursor},
            params=EmailTemplateListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[EmailTemplate]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_TEMPLATES,
            EmailTemplateListResponse,
            EmailTemplate,
            _PAGE_EMAIL_TEMPLATES,
            path={},
            given={"limit": limit, "cursor": cursor},
            params=EmailTemplateListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def create(
        self,
        *,
        name: str,
        subject: str,
        alias: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        from_: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reply_to: Sequence[str] | NotGiven = NOT_GIVEN,
        variables: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateCreateResponse:
        """Create a template

        ``POST /v1/email/templates``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``template_alias_invalid``, ``template_alias_taken``, ``template_invalid``, ``template_limit``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.create(name='تم شحن الطلب', alias='order-shipped', subject='طلبك {{ ORDER }} في الطريق', html='<p>مرحبًا {{ NAME }}، طلبك {{ ORDER }} في الطريق.</p>', variables=[{'key': 'ORDER'}, {'key': 'NAME', 'fallback': 'عميلنا'}], publish=True, idempotency_key='template-order-shipped')
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_CREATE,
            EmailTemplateCreateResponse,
            path={},
            given={
                "name": name,
                "alias": alias,
                "subject": subject,
                "html": html,
                "text": text,
                "from": from_,
                "reply_to": reply_to,
                "variables": variables,
                "publish": publish,
            },
            params=EmailTemplateCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateGetResponse:
        """Get a template

        ``GET /v1/email/templates/{id}``, scope ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.get('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE,
            EmailTemplateGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def update(
        self,
        id: str,
        *,
        name: str | NotGiven = NOT_GIVEN,
        alias: str | NotGiven = NOT_GIVEN,
        subject: str | NotGiven = NOT_GIVEN,
        html: str | NotGiven = NOT_GIVEN,
        text: str | NotGiven = NOT_GIVEN,
        from_: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reply_to: Sequence[str] | NotGiven = NOT_GIVEN,
        variables: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        publish: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateUpdateResponse:
        """Update a template

        ``PATCH /v1/email/templates/{id}``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``template_alias_invalid``, ``template_alias_taken``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.update('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12', subject='طلبك {{ ORDER }} شُحن')
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_UPDATE,
            EmailTemplateUpdateResponse,
            path={"id": id},
            given={
                "name": name,
                "alias": alias,
                "subject": subject,
                "html": html,
                "text": text,
                "from": from_,
                "reply_to": reply_to,
                "variables": variables,
                "publish": publish,
            },
            params=EmailTemplateUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def delete(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplateDeleteResponse:
        """Delete a template

        ``DELETE /v1/email/templates/{id}``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.delete('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_DELETE,
            EmailTemplateDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def publish(
        self,
        id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailTemplatePublishResponse:
        """Publish a template

        ``POST /v1/email/templates/{id}/publish``, scope ``email:manage``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``application_key_required``, ``email_access_pending``, ``email_access_required``, ``email_product_off``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``template_invalid``, ``template_no_draft``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.templates.publish('0199f1f0-2d3e-7f4a-8b5c-6d7e8f9a0b12')
        """
        return await self._client._call(
            _E.EMAIL_TEMPLATE_PUBLISH,
            EmailTemplatePublishResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncEmailInboundAttachments:
    """``email.inbound.attachments``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def get(
        self,
        id: str,
        attachment: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> bytes:
        """Download a received attachment

        ``GET /v1/email/received/{id}/attachments/{attachment}``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``received_content_gone``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.attachments.get('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60', '0199f241-8c9d-7e0f-9a1b-2c3d4e5f6071')
        """
        return await self._client._call_binary(
            _E.EMAIL_RECEIVED_ATTACHMENT,
            path={"id": id, "attachment": attachment},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmailInboundAddresses:
    """``email.inbound.addresses``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    @early_access
    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailInboundAddressListResponse:
        """List receiving addresses

        ``GET /v1/email/inbound-addresses``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.addresses.list()
        """
        return await self._client._call(
            _E.EMAIL_INBOUND_ADDRESSES,
            EmailInboundAddressListResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmailInbound:
    """``email.inbound``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.attachments = AsyncEmailInboundAttachments(client)
        self.addresses = AsyncEmailInboundAddresses(client)

    @early_access
    async def list(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        address_id: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        spam: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        has_attachments: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        received_after: datetime | str | NotGiven = NOT_GIVEN,
        received_before: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Page[EmailReceivedListItem]:
        """List received emails

        ``GET /v1/email/received``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.list(limit=20, spam='false')
        """
        return await self._client._list(
            _E.EMAIL_RECEIVED_LIST,
            EmailReceivedListResponse,
            EmailReceivedListItem,
            _PAGE_EMAIL_RECEIVED_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "address_id": address_id,
                "to": to,
                "from": from_,
                "spam": spam,
                "has_attachments": has_attachments,
                "received_after": received_after,
                "received_before": received_before,
            },
            params=EmailReceivedListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    def iterate(
        self,
        *,
        limit: int | NotGiven = NOT_GIVEN,
        cursor: str | NotGiven = NOT_GIVEN,
        address_id: str | NotGiven = NOT_GIVEN,
        to: str | NotGiven = NOT_GIVEN,
        from_: str | NotGiven = NOT_GIVEN,
        spam: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        has_attachments: Literal["true", "false"] | str | NotGiven = NOT_GIVEN,
        received_after: datetime | str | NotGiven = NOT_GIVEN,
        received_before: datetime | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[EmailReceivedListItem]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._iterate(
            _E.EMAIL_RECEIVED_LIST,
            EmailReceivedListResponse,
            EmailReceivedListItem,
            _PAGE_EMAIL_RECEIVED_LIST,
            path={},
            given={
                "limit": limit,
                "cursor": cursor,
                "address_id": address_id,
                "to": to,
                "from": from_,
                "spam": spam,
                "has_attachments": has_attachments,
                "received_after": received_after,
                "received_before": received_before,
            },
            params=EmailReceivedListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedGetResponse:
        """Get a received email

        ``GET /v1/email/received/{id}``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.get('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60')
        """
        return await self._client._call(
            _E.EMAIL_RECEIVED,
            EmailReceivedGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def raw(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> bytes:
        """Download a received email's raw message

        ``GET /v1/email/received/{id}/raw``, scope ``email:inbound``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``received_content_gone``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.raw('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60')
        """
        return await self._client._call_binary(
            _E.EMAIL_RECEIVED_RAW,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def delete(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedDeleteResponse:
        """Delete a received email

        ``DELETE /v1/email/received/{id}``, scope ``email:inbound``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.delete('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60')
        """
        return await self._client._call(
            _E.EMAIL_RECEIVED_DELETE,
            EmailReceivedDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    @early_access
    async def forward(
        self,
        id: str,
        *,
        to: str | Sequence[str],
        from_: str | Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        note: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedForwardResponse:
        """Forward a received email

        ``POST /v1/email/received/{id}/forward``, scope ``email:inbound``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``content_blocked``, ``daily_cap_reached``, ``email_early_access``, ``email_paused``, ``email_platform_busy``, ``forward_risky_attachment``, ``forward_too_large``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``message_too_large``, ``no_verified_domain``, ``not_found``, ``rate_limited``, ``received_content_gone``, ``received_not_ready``, ``sender_not_verified``, ``service_unavailable``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.forward('0199f240-7b8c-7d9e-8f0a-1b2c3d4e5f60', to=['support@acme.sa'], note='من صندوق الطلبات', idempotency_key='forward-order-1042')
        """
        return await self._client._call(
            _E.EMAIL_RECEIVED_FORWARD,
            EmailReceivedForwardResponse,
            path={"id": id},
            given={"to": to, "from": from_, "note": note},
            params=EmailReceivedForwardParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    @early_access
    async def test(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailReceivedTestResponse:
        """Simulate a received email

        ``POST /v1/email/received/test``, scope ``email:send``.
        Never retried once sent.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``email_early_access``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``test_key_required``, ``test_mode_limit_reached``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.inbound.test()
        """
        return await self._client._call(
            _E.EMAIL_RECEIVED_TEST,
            EmailReceivedTestResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncEmail:
    """``email``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.messages = AsyncEmailMessages(client)
        self.domains = AsyncEmailDomains(client)
        self.suppressions = AsyncEmailSuppressions(client)
        self.metrics = AsyncEmailMetrics(client)
        self.templates = AsyncEmailTemplates(client)
        self.inbound = AsyncEmailInbound(client)

    @early_access
    async def check_key(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> EmailKeyCheckResponse:
        """Check an email key

        ``GET /v1/email/key``, scope ``email:send``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        Early access: the account must be granted Tawked Email first.

        Errors: ``account_not_active``, ``email_early_access``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.email.check_key()
        """
        return await self._client._call(
            _E.EMAIL_KEY,
            EmailKeyCheckResponse,
            path={},
            given={"application": application},
            params=EmailKeyCheckParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )
