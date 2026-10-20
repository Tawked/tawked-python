"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked import _generated as _g
from tawked._generated import endpoints as _E
from tawked._generated.types import (
    WhatsAppMessageGetParams,
    WhatsAppMessageGetResponse,
    WhatsAppSendParams,
    WhatsAppSendResponse,
    WhatsAppTemplateCreateParams,
    WhatsAppTemplateCreateResponse,
    WhatsAppTemplateDeleteResponse,
    WhatsAppTemplateGetResponse,
    WhatsAppTemplateListParams,
    WhatsAppTemplateListResponse,
    WhatsAppTemplateUpdateParams,
    WhatsAppTemplateUpdateResponse,
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


class WhatsAppMessages:
    """``whatsapp.messages``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def send(
        self,
        *,
        to: str,
        template: str,
        lang: str | NotGiven | None = NOT_GIVEN,
        params: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        header: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppSendResponse:
        """Send a template message

        ``POST /v1/whatsapp/messages``, scope ``notifications:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``consent_opted_out``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_params``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``number_disconnected``, ``send_failed``, ``service_not_found``, ``service_required``, ``template_category_not_allowed``, ``template_not_approved``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``unknown_template``, ``unsupported_template``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.messages.send(to='0551234567', template='order_received_v1', lang='ar', params={'1': '1042', '2': '250'}, header={'text': '1042'}, buttons=[{'index': 0, 'parameter': '1042'}], reference='order-1042', idempotency_key='order-1042-received')
        """
        return self._client._call(
            _E.WHATSAPP_SEND,
            WhatsAppSendResponse,
            path={},
            given={
                "to": to,
                "template": template,
                "lang": lang,
                "params": params,
                "header": header,
                "buttons": buttons,
                "reference": reference,
                "application": application,
            },
            params=WhatsAppSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppMessageGetResponse:
        """Get a message

        ``GET /v1/whatsapp/messages/{id}``, scope ``notifications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.whatsapp.messages.get('0f4c9c0e-6d2b-4b8a-9c3e-7a1d2e3f4a5b')
        """
        return self._client._call(
            _E.WHATSAPP_MESSAGE,
            WhatsAppMessageGetResponse,
            path={"id": id},
            given={"application": application},
            params=WhatsAppMessageGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class WhatsAppTemplates:
    """``whatsapp.templates``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateListResponse:
        """List templates

        ``GET /v1/whatsapp/templates``, scope ``notifications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``service_not_found``, ``service_required``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.list()
        """
        return self._client._call(
            _E.WHATSAPP_TEMPLATES,
            WhatsAppTemplateListResponse,
            path={},
            given={"application": application},
            params=WhatsAppTemplateListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        template_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateGetResponse:
        """Get a template

        ``GET /v1/whatsapp/templates/{template_id}``, scope ``notifications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``not_found``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.get('7000')
        """
        return self._client._call(
            _E.WHATSAPP_TEMPLATE,
            WhatsAppTemplateGetResponse,
            path={"template_id": template_id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        *,
        name: str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        category: Literal["UTILITY", "MARKETING"] | str,
        body: str,
        header: str | NotGiven | None = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateCreateResponse:
        """Create a template

        ``POST /v1/whatsapp/templates``, scope ``notifications:templates``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``template_category_not_allowed``, ``template_refused``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.create(name='order_shipped_v1', language='ar', category='UTILITY', body='شُحن طلبك رقم {{1}}، ويصلك خلال {{2}} أيام.', examples={'body:1': '1042', 'body:2': '3'})
        """
        return self._client._call(
            _E.WHATSAPP_TEMPLATE_CREATE,
            WhatsAppTemplateCreateResponse,
            path={},
            given={
                "name": name,
                "language": language,
                "category": category,
                "header": header,
                "body": body,
                "footer": footer,
                "buttons": buttons,
                "examples": examples,
            },
            params=WhatsAppTemplateCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        template_id: str,
        *,
        category: Literal["UTILITY", "MARKETING"] | str,
        body: str,
        header: str | NotGiven | None = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateUpdateResponse:
        """Update a template

        ``PATCH /v1/whatsapp/templates/{template_id}``, scope ``notifications:templates``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``not_found``, ``template_category_not_allowed``, ``template_in_use``, ``template_not_editable``, ``template_not_managed``, ``template_refused``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.update('7000', category='UTILITY', body='استلمنا طلبك رقم {{1}} بقيمة {{2}} ريال.', examples={'body:1': '1042', 'body:2': '250'})
        """
        return self._client._call(
            _E.WHATSAPP_TEMPLATE_UPDATE,
            WhatsAppTemplateUpdateResponse,
            path={"template_id": template_id},
            given={
                "category": category,
                "header": header,
                "body": body,
                "footer": footer,
                "buttons": buttons,
                "examples": examples,
            },
            params=WhatsAppTemplateUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        template_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateDeleteResponse:
        """Delete a template

        ``DELETE /v1/whatsapp/templates/{template_id}``, scope ``notifications:templates``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``not_found``, ``template_in_use``, ``template_not_editable``, ``template_not_managed``, ``template_refused``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.delete('7000')
        """
        return self._client._call(
            _E.WHATSAPP_TEMPLATE_DELETE,
            WhatsAppTemplateDeleteResponse,
            path={"template_id": template_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class WhatsApp:
    """``whatsapp``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.messages = WhatsAppMessages(client)
        self.templates = WhatsAppTemplates(client)


class AsyncWhatsAppMessages:
    """``whatsapp.messages``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def send(
        self,
        *,
        to: str,
        template: str,
        lang: str | NotGiven | None = NOT_GIVEN,
        params: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        header: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppSendResponse:
        """Send a template message

        ``POST /v1/whatsapp/messages``, scope ``notifications:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``consent_opted_out``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_params``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``number_disconnected``, ``send_failed``, ``service_not_found``, ``service_required``, ``template_category_not_allowed``, ``template_not_approved``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``unknown_template``, ``unsupported_template``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.messages.send(to='0551234567', template='order_received_v1', lang='ar', params={'1': '1042', '2': '250'}, header={'text': '1042'}, buttons=[{'index': 0, 'parameter': '1042'}], reference='order-1042', idempotency_key='order-1042-received')
        """
        return await self._client._call(
            _E.WHATSAPP_SEND,
            WhatsAppSendResponse,
            path={},
            given={
                "to": to,
                "template": template,
                "lang": lang,
                "params": params,
                "header": header,
                "buttons": buttons,
                "reference": reference,
                "application": application,
            },
            params=WhatsAppSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppMessageGetResponse:
        """Get a message

        ``GET /v1/whatsapp/messages/{id}``, scope ``notifications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.whatsapp.messages.get('0f4c9c0e-6d2b-4b8a-9c3e-7a1d2e3f4a5b')
        """
        return await self._client._call(
            _E.WHATSAPP_MESSAGE,
            WhatsAppMessageGetResponse,
            path={"id": id},
            given={"application": application},
            params=WhatsAppMessageGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncWhatsAppTemplates:
    """``whatsapp.templates``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateListResponse:
        """List templates

        ``GET /v1/whatsapp/templates``, scope ``notifications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``service_not_found``, ``service_required``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.list()
        """
        return await self._client._call(
            _E.WHATSAPP_TEMPLATES,
            WhatsAppTemplateListResponse,
            path={},
            given={"application": application},
            params=WhatsAppTemplateListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        template_id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateGetResponse:
        """Get a template

        ``GET /v1/whatsapp/templates/{template_id}``, scope ``notifications:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``not_found``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.get('7000')
        """
        return await self._client._call(
            _E.WHATSAPP_TEMPLATE,
            WhatsAppTemplateGetResponse,
            path={"template_id": template_id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        *,
        name: str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        category: Literal["UTILITY", "MARKETING"] | str,
        body: str,
        header: str | NotGiven | None = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateCreateResponse:
        """Create a template

        ``POST /v1/whatsapp/templates``, scope ``notifications:templates``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``template_category_not_allowed``, ``template_refused``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.create(name='order_shipped_v1', language='ar', category='UTILITY', body='شُحن طلبك رقم {{1}}، ويصلك خلال {{2}} أيام.', examples={'body:1': '1042', 'body:2': '3'})
        """
        return await self._client._call(
            _E.WHATSAPP_TEMPLATE_CREATE,
            WhatsAppTemplateCreateResponse,
            path={},
            given={
                "name": name,
                "language": language,
                "category": category,
                "header": header,
                "body": body,
                "footer": footer,
                "buttons": buttons,
                "examples": examples,
            },
            params=WhatsAppTemplateCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        template_id: str,
        *,
        category: Literal["UTILITY", "MARKETING"] | str,
        body: str,
        header: str | NotGiven | None = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateUpdateResponse:
        """Update a template

        ``PATCH /v1/whatsapp/templates/{template_id}``, scope ``notifications:templates``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``not_found``, ``template_category_not_allowed``, ``template_in_use``, ``template_not_editable``, ``template_not_managed``, ``template_refused``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.update('7000', category='UTILITY', body='استلمنا طلبك رقم {{1}} بقيمة {{2}} ريال.', examples={'body:1': '1042', 'body:2': '250'})
        """
        return await self._client._call(
            _E.WHATSAPP_TEMPLATE_UPDATE,
            WhatsAppTemplateUpdateResponse,
            path={"template_id": template_id},
            given={
                "category": category,
                "header": header,
                "body": body,
                "footer": footer,
                "buttons": buttons,
                "examples": examples,
            },
            params=WhatsAppTemplateUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        template_id: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> WhatsAppTemplateDeleteResponse:
        """Delete a template

        ``DELETE /v1/whatsapp/templates/{template_id}``, scope ``notifications:templates``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``no_whatsapp_number``, ``not_found``, ``template_in_use``, ``template_not_editable``, ``template_not_managed``, ``template_refused``, ``templates_unavailable``, ``too_many_requests``, ``unauthorized``, ``whatsapp_not_enabled``.

        Example::

            tawked.whatsapp.templates.delete('7000')
        """
        return await self._client._call(
            _E.WHATSAPP_TEMPLATE_DELETE,
            WhatsAppTemplateDeleteResponse,
            path={"template_id": template_id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncWhatsApp:
    """``whatsapp``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.messages = AsyncWhatsAppMessages(client)
        self.templates = AsyncWhatsAppTemplates(client)
