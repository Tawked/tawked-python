"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked import _generated as _g
from tawked._generated import endpoints as _E
from tawked._generated.types import (
    VerifyCancelParams,
    VerifyCancelResponse,
    VerifyCheckParams,
    VerifyCheckResponse,
    VerifyGetParams,
    VerifyGetResponse,
    VerifyResendParams,
    VerifyResendResponse,
    VerifyStartParams,
    VerifyStartResponse,
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


class Verify:
    """``verify``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def start(
        self,
        *,
        to: str,
        phone: str | NotGiven = NOT_GIVEN,
        channel: str | NotGiven = NOT_GIVEN,
        lang: str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        client_ip: str | NotGiven = NOT_GIVEN,
        autofill: Literal["web", "android", "none"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyStartResponse:
        """Start a verification

        ``POST /v1/verify/start``, scope ``verify:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``application_paused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``ip_rate_limited``, ``key_expired``, ``rate_limited``, ``sandbox_quota_exceeded``, ``sandbox_unsupported_channel``, ``sandbox_unverified_destination``, ``send_failed``, ``service_not_found``, ``service_required``, ``spend_cap_reached``, ``too_many_requests``, ``unauthorized``, ``unsupported_channel``.

        Example::

            tawked.verify.start(to='0551234567', channel='sms', lang='ar', reference='order-1042')
        """
        return self._client._call(
            _E.START,
            VerifyStartResponse,
            path={},
            given={
                "to": to,
                "phone": phone,
                "channel": channel,
                "lang": lang,
                "application": application,
                "reference": reference,
                "client_ip": client_ip,
                "autofill": autofill,
            },
            params=VerifyStartParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def check(
        self,
        *,
        id: str,
        code: str,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyCheckResponse:
        """Check a code

        ``POST /v1/verify/check``, scope ``verify:check``.
        Never retried once sent.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.check(id='b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44', code='123456')
        """
        return self._client._call(
            _E.CHECK,
            VerifyCheckResponse,
            path={},
            given={"id": id, "code": code, "application": application},
            params=VerifyCheckParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyGetResponse:
        """Get a verification

        ``GET /v1/verify/{id}``, scope ``verify:check``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.get('b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44')
        """
        return self._client._call(
            _E.STATUS,
            VerifyGetResponse,
            path={"id": id},
            given={"application": application},
            params=VerifyGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def resend(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyResendResponse:
        """Resend a code

        ``POST /v1/verify/{id}/resend``, scope ``verify:send``.
        Never retried once sent.

        Errors: ``account_not_active``, ``application_paused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``ip_not_allowed``, ``ip_rate_limited``, ``key_expired``, ``not_found``, ``not_resendable``, ``rate_limited``, ``resend_limit_reached``, ``send_failed``, ``service_not_found``, ``service_required``, ``spend_cap_reached``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.resend('b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44')
        """
        return self._client._call(
            _E.RESEND,
            VerifyResendResponse,
            path={"id": id},
            given={"application": application},
            params=VerifyResendParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def cancel(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyCancelResponse:
        """Cancel a verification

        ``POST /v1/verify/{id}/cancel``, scope ``verify:send``.
        Never retried once sent.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``ip_not_allowed``, ``key_expired``, ``not_cancelable``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.cancel('b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44')
        """
        return self._client._call(
            _E.CANCEL,
            VerifyCancelResponse,
            path={"id": id},
            given={"application": application},
            params=VerifyCancelParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncVerify:
    """``verify``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def start(
        self,
        *,
        to: str,
        phone: str | NotGiven = NOT_GIVEN,
        channel: str | NotGiven = NOT_GIVEN,
        lang: str | NotGiven = NOT_GIVEN,
        application: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        client_ip: str | NotGiven = NOT_GIVEN,
        autofill: Literal["web", "android", "none"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyStartResponse:
        """Start a verification

        ``POST /v1/verify/start``, scope ``verify:send``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.

        Errors: ``account_not_active``, ``application_paused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_destination``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``ip_rate_limited``, ``key_expired``, ``rate_limited``, ``sandbox_quota_exceeded``, ``sandbox_unsupported_channel``, ``sandbox_unverified_destination``, ``send_failed``, ``service_not_found``, ``service_required``, ``spend_cap_reached``, ``too_many_requests``, ``unauthorized``, ``unsupported_channel``.

        Example::

            tawked.verify.start(to='0551234567', channel='sms', lang='ar', reference='order-1042')
        """
        return await self._client._call(
            _E.START,
            VerifyStartResponse,
            path={},
            given={
                "to": to,
                "phone": phone,
                "channel": channel,
                "lang": lang,
                "application": application,
                "reference": reference,
                "client_ip": client_ip,
                "autofill": autofill,
            },
            params=VerifyStartParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def check(
        self,
        *,
        id: str,
        code: str,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyCheckResponse:
        """Check a code

        ``POST /v1/verify/check``, scope ``verify:check``.
        Never retried once sent.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.check(id='b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44', code='123456')
        """
        return await self._client._call(
            _E.CHECK,
            VerifyCheckResponse,
            path={},
            given={"id": id, "code": code, "application": application},
            params=VerifyCheckParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyGetResponse:
        """Get a verification

        ``GET /v1/verify/{id}``, scope ``verify:check``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.get('b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44')
        """
        return await self._client._call(
            _E.STATUS,
            VerifyGetResponse,
            path={"id": id},
            given={"application": application},
            params=VerifyGetParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def resend(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyResendResponse:
        """Resend a code

        ``POST /v1/verify/{id}/resend``, scope ``verify:send``.
        Never retried once sent.

        Errors: ``account_not_active``, ``application_paused``, ``insufficient_credits``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``ip_not_allowed``, ``ip_rate_limited``, ``key_expired``, ``not_found``, ``not_resendable``, ``rate_limited``, ``resend_limit_reached``, ``send_failed``, ``service_not_found``, ``service_required``, ``spend_cap_reached``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.resend('b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44')
        """
        return await self._client._call(
            _E.RESEND,
            VerifyResendResponse,
            path={"id": id},
            given={"application": application},
            params=VerifyResendParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def cancel(
        self,
        id: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> VerifyCancelResponse:
        """Cancel a verification

        ``POST /v1/verify/{id}/cancel``, scope ``verify:send``.
        Never retried once sent.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``ip_not_allowed``, ``key_expired``, ``not_cancelable``, ``not_found``, ``service_not_found``, ``service_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.verify.cancel('b7e5c2b0-9c1a-4e2f-8f2a-3a6b0e9d1c44')
        """
        return await self._client._call(
            _E.CANCEL,
            VerifyCancelResponse,
            path={"id": id},
            given={"application": application},
            params=VerifyCancelParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )
