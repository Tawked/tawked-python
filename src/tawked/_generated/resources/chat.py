"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked import _generated as _g
from tawked._generated import endpoints as _E
from tawked._generated.types import (
    ChatAttendantDraftSaveParams,
    ChatAttendantDraftSaveResponse,
    ChatAttendantGetResponse,
    ChatAttendantPublishResponse,
    ChatAttendantSettingsUpdateParams,
    ChatAttendantSettingsUpdateResponse,
    ChatAttendantStateSetParams,
    ChatAttendantStateSetResponse,
    ChatMenuCreateParams,
    ChatMenuCreateResponse,
    ChatMenuDeleteResponse,
    ChatMenuGetResponse,
    ChatMenuListResponse,
    ChatMenuUpdateParams,
    ChatMenuUpdateResponse,
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


class ChatMenus:
    """``chat.menus``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuListResponse:
        """List menus

        ``GET /v1/chat/menus``, scope ``chat:menus``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.list()
        """
        return self._client._call(
            _E.CHAT_MENUS,
            ChatMenuListResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        *,
        title: str,
        url: str,
        icon: str | Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuCreateResponse:
        """Add a menu

        ``POST /v1/chat/menus``, scope ``chat:menus``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``menu_limit_reached``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.create(title='الحجوزات', url='https://app.yourplatform.example/tawked/bookings?phone={customer_phone}')
        """
        return self._client._call(
            _E.CHAT_MENU_CREATE,
            ChatMenuCreateResponse,
            path={},
            given={"title": title, "url": url, "icon": icon},
            params=ChatMenuCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuGetResponse:
        """Get a menu

        ``GET /v1/chat/menus/{id}``, scope ``chat:menus``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.get('5b1d2c3e-4f5a-4b6c-8d7e-9f0a1b2c3d4e')
        """
        return self._client._call(
            _E.CHAT_MENU,
            ChatMenuGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        id: str,
        *,
        title: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        icon: str | Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuUpdateResponse:
        """Update a menu

        ``PATCH /v1/chat/menus/{id}``, scope ``chat:menus``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.update('5b1d2c3e-4f5a-4b6c-8d7e-9f0a1b2c3d4e', title='حجوزاتي')
        """
        return self._client._call(
            _E.CHAT_MENU_UPDATE,
            ChatMenuUpdateResponse,
            path={"id": id},
            given={"title": title, "url": url, "icon": icon},
            params=ChatMenuUpdateParams,
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
    ) -> ChatMenuDeleteResponse:
        """Delete a menu

        ``DELETE /v1/chat/menus/{id}``, scope ``chat:menus``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.delete('5b1d2c3e-4f5a-4b6c-8d7e-9f0a1b2c3d4e')
        """
        return self._client._call(
            _E.CHAT_MENU_DELETE,
            ChatMenuDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class ChatAttendant:
    """``chat.attendant``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client

    def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantGetResponse:
        """Get the auto-attendant

        ``GET /v1/chat/attendant``, scope ``chat:attendant``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.get()
        """
        return self._client._call(
            _E.CHAT_ATTENDANT,
            ChatAttendantGetResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def save_draft(
        self,
        *,
        menu: Mapping[str, Any],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantDraftSaveResponse:
        """Save the auto-attendant draft

        ``PUT /v1/chat/attendant/draft``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.save_draft(...)
        """
        return self._client._call(
            _E.CHAT_ATTENDANT_DRAFT,
            ChatAttendantDraftSaveResponse,
            path={},
            given={"menu": menu},
            params=ChatAttendantDraftSaveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def publish(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantPublishResponse:
        """Publish the auto-attendant

        ``POST /v1/chat/attendant/publish``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``attendant_no_draft``, ``attendant_not_ready``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.publish()
        """
        return self._client._call(
            _E.CHAT_ATTENDANT_PUBLISH,
            ChatAttendantPublishResponse,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def set_state(
        self,
        *,
        enabled: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantStateSetResponse:
        """Switch the auto-attendant on or off

        ``PUT /v1/chat/attendant/state``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``attendant_unpublished``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``sending_blocked``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.set_state(enabled=True)
        """
        return self._client._call(
            _E.CHAT_ATTENDANT_STATE,
            ChatAttendantStateSetResponse,
            path={},
            given={"enabled": enabled},
            params=ChatAttendantStateSetParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update_settings(
        self,
        *,
        mode: Literal["menu_only", "menu_then_radeef"] | str | NotGiven = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantSettingsUpdateResponse:
        """Update the auto-attendant settings

        ``PATCH /v1/chat/attendant/settings``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.update_settings(mode='menu_only', language='ar')
        """
        return self._client._call(
            _E.CHAT_ATTENDANT_SETTINGS,
            ChatAttendantSettingsUpdateResponse,
            path={},
            given={"mode": mode, "language": language},
            params=ChatAttendantSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class Chat:
    """``chat``."""

    _client: Tawked

    def __init__(self, client: Tawked) -> None:
        self._client = client
        self.menus = ChatMenus(client)
        self.attendant = ChatAttendant(client)


class AsyncChatMenus:
    """``chat.menus``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuListResponse:
        """List menus

        ``GET /v1/chat/menus``, scope ``chat:menus``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.list()
        """
        return await self._client._call(
            _E.CHAT_MENUS,
            ChatMenuListResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        *,
        title: str,
        url: str,
        icon: str | Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuCreateResponse:
        """Add a menu

        ``POST /v1/chat/menus``, scope ``chat:menus``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``menu_limit_reached``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.create(title='الحجوزات', url='https://app.yourplatform.example/tawked/bookings?phone={customer_phone}')
        """
        return await self._client._call(
            _E.CHAT_MENU_CREATE,
            ChatMenuCreateResponse,
            path={},
            given={"title": title, "url": url, "icon": icon},
            params=ChatMenuCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def get(
        self,
        id: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuGetResponse:
        """Get a menu

        ``GET /v1/chat/menus/{id}``, scope ``chat:menus``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.get('5b1d2c3e-4f5a-4b6c-8d7e-9f0a1b2c3d4e')
        """
        return await self._client._call(
            _E.CHAT_MENU,
            ChatMenuGetResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        id: str,
        *,
        title: str | NotGiven = NOT_GIVEN,
        url: str | NotGiven = NOT_GIVEN,
        icon: str | Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatMenuUpdateResponse:
        """Update a menu

        ``PATCH /v1/chat/menus/{id}``, scope ``chat:menus``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.update('5b1d2c3e-4f5a-4b6c-8d7e-9f0a1b2c3d4e', title='حجوزاتي')
        """
        return await self._client._call(
            _E.CHAT_MENU_UPDATE,
            ChatMenuUpdateResponse,
            path={"id": id},
            given={"title": title, "url": url, "icon": icon},
            params=ChatMenuUpdateParams,
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
    ) -> ChatMenuDeleteResponse:
        """Delete a menu

        ``DELETE /v1/chat/menus/{id}``, scope ``chat:menus``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``not_found``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.menus.delete('5b1d2c3e-4f5a-4b6c-8d7e-9f0a1b2c3d4e')
        """
        return await self._client._call(
            _E.CHAT_MENU_DELETE,
            ChatMenuDeleteResponse,
            path={"id": id},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncChatAttendant:
    """``chat.attendant``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client

    async def get(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantGetResponse:
        """Get the auto-attendant

        ``GET /v1/chat/attendant``, scope ``chat:attendant``.
        Retried on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``insufficient_scope``, ``internal_error``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.get()
        """
        return await self._client._call(
            _E.CHAT_ATTENDANT,
            ChatAttendantGetResponse,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def save_draft(
        self,
        *,
        menu: Mapping[str, Any],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantDraftSaveResponse:
        """Save the auto-attendant draft

        ``PUT /v1/chat/attendant/draft``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.save_draft(...)
        """
        return await self._client._call(
            _E.CHAT_ATTENDANT_DRAFT,
            ChatAttendantDraftSaveResponse,
            path={},
            given={"menu": menu},
            params=ChatAttendantDraftSaveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def publish(
        self,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantPublishResponse:
        """Publish the auto-attendant

        ``POST /v1/chat/attendant/publish``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``attendant_no_draft``, ``attendant_not_ready``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.publish()
        """
        return await self._client._call(
            _E.CHAT_ATTENDANT_PUBLISH,
            ChatAttendantPublishResponse,
            path={},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def set_state(
        self,
        *,
        enabled: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantStateSetResponse:
        """Switch the auto-attendant on or off

        ``PUT /v1/chat/attendant/state``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``attendant_unpublished``, ``chat_not_ready``, ``chat_unavailable``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``sending_blocked``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.set_state(enabled=True)
        """
        return await self._client._call(
            _E.CHAT_ATTENDANT_STATE,
            ChatAttendantStateSetResponse,
            path={},
            given={"enabled": enabled},
            params=ChatAttendantStateSetParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update_settings(
        self,
        *,
        mode: Literal["menu_only", "menu_then_radeef"] | str | NotGiven = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> ChatAttendantSettingsUpdateResponse:
        """Update the auto-attendant settings

        ``PATCH /v1/chat/attendant/settings``, scope ``chat:attendant``.
        Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.

        Errors: ``account_not_active``, ``idempotency_in_progress``, ``idempotency_key_reused``, ``insufficient_scope``, ``internal_error``, ``invalid_json``, ``invalid_request``, ``ip_not_allowed``, ``key_expired``, ``live_key_required``, ``too_many_requests``, ``unauthorized``.

        Example::

            tawked.chat.attendant.update_settings(mode='menu_only', language='ar')
        """
        return await self._client._call(
            _E.CHAT_ATTENDANT_SETTINGS,
            ChatAttendantSettingsUpdateResponse,
            path={},
            given={"mode": mode, "language": language},
            params=ChatAttendantSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncChat:
    """``chat``."""

    _client: AsyncTawked

    def __init__(self, client: AsyncTawked) -> None:
        self._client = client
        self.menus = AsyncChatMenus(client)
        self.attendant = AsyncChatAttendant(client)
