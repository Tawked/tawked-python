"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountChatAttendantLogParams,
    AccountChatAttendantSaveDraftParams,
    AccountChatAttendantSwitchParams,
    AccountChatAttendantUpdateSettingsParams,
    AccountChatMenusCheckParams,
    AccountChatMenusCreateParams,
    AccountChatMenusUpdateParams,
    AccountChatTeamAddParams,
    AccountChatTeamUpdateParams,
)
from tawked._generated.endpoints import _PAGE_A_CHAT_MENUS_LIST, _PAGE_A_CHAT_TEAM_LIST
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


class AccountChatAttendant:
    """``chat.attendant``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def log(
        self,
        application: str,
        *,
        cursor: str | NotGiven | None = NOT_GIVEN,
        limit: int | NotGiven | None = NOT_GIVEN,
        outcome: Literal["answered", "team", "radeef", "human", "ended", "ongoing"]
        | str
        | NotGiven = NOT_GIVEN,
        q: str | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The auto-attendant's log: every conversation it held, newest first, with the customer's name, the choices they tapped and how it ended (`answered`, `team`, `radeef`, `human`, `expired`, `stopped`, or `ongoing`).

        ``GET /v1/applications/{application}/chat/attendant/log``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CHAT_ATTENDANT_LOG,
            path={"application": application},
            given={"cursor": cursor, "limit": limit, "outcome": outcome, "q": q},
            params=AccountChatAttendantLogParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def publish(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Publish the stored draft (the starter when nothing was saved yet) as the next live version of the auto-attendant: once it is on, customers get this menu. Answers the attendant.

        ``POST /v1/applications/{application}/chat/attendant/publish``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CHAT_ATTENDANT_PUBLISH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def save_draft(
        self,
        application: str,
        *,
        definition: Mapping[str, Any],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the auto-attendant's draft (`definition`, the whole menu): it reaches no customer. Answers when it was saved and the problems that keep it from being published.

        ``PUT /v1/applications/{application}/chat/attendant/draft``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_ATTENDANT_SAVE_DRAFT,
            path={"application": application},
            given={"definition": definition},
            params=AccountChatAttendantSaveDraftParams,
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
        """The auto-attendant of this application's number: its state and whether it is on, its settings, the draft with the problems that keep it from being published, the published version, the people a fallback may go to, and the limits.

        ``GET /v1/applications/{application}/chat/attendant``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CHAT_ATTENDANT_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def switch(
        self,
        application: str,
        *,
        enabled: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the auto-attendant on (`enabled: true`: it answers every new conversation on the number with the published menu) or off (its conversations go to the team). Answers the attendant.

        ``PUT /v1/applications/{application}/chat/attendant/state``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CHAT_ATTENDANT_SWITCH,
            path={"application": application},
            given={"enabled": enabled},
            params=AccountChatAttendantSwitchParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update_settings(
        self,
        application: str,
        *,
        fallback_assign: Literal["auto", "member"] | str | NotGiven = NOT_GIVEN,
        fallback_member_id: str | NotGiven | None = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven = NOT_GIVEN,
        mode: Literal["menu_then_radeef", "menu_only"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change the auto-attendant's settings: `mode` (`menu_then_radeef` or `menu_only`), the customers' `language` (`ar` or `en`), and who gets a fallback handoff (`fallback_assign`: `auto` or `member` with `fallback_member_id`, one of `assignees`). Answers the attendant and the settings before.

        ``PUT /v1/applications/{application}/chat/attendant/settings``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_ATTENDANT_UPDATE_SETTINGS,
            path={"application": application},
            given={
                "fallback_assign": fallback_assign,
                "fallback_member_id": fallback_member_id,
                "language": language,
                "mode": mode,
            },
            params=AccountChatAttendantUpdateSettingsParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountChatMenus:
    """``chat.menus``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def check(
        self,
        application: str,
        *,
        url: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check a link before adding it as a menu: whether Tawked Chat can open it inside the conversation (`frame`: `opens`, `window` or `unknown`), and the link's own problem if any (`problem`: `length`, `http`, `host`, or null).

        ``POST /v1/applications/{application}/chat/menus/check``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_MENUS_CHECK,
            path={"application": application},
            given={"url": url},
            params=AccountChatMenusCheckParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        title: str,
        url: str,
        icon: FileInput | NotGiven | None = NOT_GIVEN,
        icon_mode: Literal["site", "upload", "none"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a chat menu: a page of your business (`title`, an https `url`) shown beside this application's conversations in Tawked Chat; `icon_mode` takes the site's icon (`site`, the default), an uploaded `icon` (`upload`) or none. Answers the menu.

        ``POST /v1/applications/{application}/chat/menus``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_MENUS_CREATE,
            path={"application": application},
            given={"title": title, "url": url, "icon": icon, "icon_mode": icon_mode},
            params=AccountChatMenusCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("icon",),
        )

    def delete(
        self,
        application: str,
        menu: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a chat menu from Tawked Chat and from this application; answers ok.

        ``DELETE /v1/applications/{application}/chat/menus/{menu}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CHAT_MENUS_DELETE,
            path={"application": application, "menu": menu},
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
        """List the chat menus that show beside this application's conversations in Tawked Chat (its own, the ones of every conversation, and the Salla store's orders tab), in Tawked Chat's order.

        ``GET /v1/applications/{application}/chat/menus``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CHAT_MENUS_LIST,
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
            _E.A_CHAT_MENUS_LIST,
            _PAGE_A_CHAT_MENUS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        menu: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One chat menu of this application: its title, link, icon and whether it opens inside Tawked Chat.

        ``GET /v1/applications/{application}/chat/menus/{menu}``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CHAT_MENUS_SHOW,
            path={"application": application, "menu": menu},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        menu: str,
        *,
        title: str,
        url: str,
        icon: FileInput | NotGiven | None = NOT_GIVEN,
        icon_mode: Literal["site", "upload", "none"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a chat menu: send its `title` and `url` (both, as they should be), and `icon_mode` only to change the icon. Answers the menu.

        ``PATCH /v1/applications/{application}/chat/menus/{menu}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_MENUS_UPDATE,
            path={"application": application, "menu": menu},
            given={"title": title, "url": url, "icon": icon, "icon_mode": icon_mode},
            params=AccountChatMenusUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("icon",),
        )


class AccountChatTeam:
    """``chat.team``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def add(
        self,
        application: str,
        *,
        role: Literal["administrator", "agent"] | str,
        email: str | NotGiven | None = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven | None = NOT_GIVEN,
        member_id: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a person to this application's support team: someone of the account by `member_id`, or someone new by `name` with a `phone` (a Saudi mobile, 05… or +9665…), an `email`, or both, and a `role` (`agent` or `administrator`). Someone new with an email signs in with it and Tawked e-mails them the invitation (`invitation_sent_to`); with a mobile, answers `sign_in_message` for whoever added them to send, written in your person's language or `language` (ar or en).

        ``POST /v1/applications/{application}/chat/team``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CHAT_TEAM_ADD,
            path={"application": application},
            given={
                "role": role,
                "email": email,
                "language": language,
                "member_id": member_id,
                "name": name,
                "phone": phone,
            },
            params=AccountChatTeamAddParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def candidates(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Who could join this support team without a new seat (the account's people not on it yet, mobiles masked), and the account's seats: the limit, how many are used, how many are left.

        ``GET /v1/applications/{application}/chat/team/candidates``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CHAT_TEAM_CANDIDATES,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def invite(
        self,
        application: str,
        member: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """E-mail the invitation again to a person of this support team who signs in with an email: one a minute and five a day per person, the one sent at the add included. Answers ok.

        ``POST /v1/applications/{application}/chat/team/{member}/invite``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_TEAM_INVITE,
            path={"application": application, "member": member},
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
        """List who answers this application's customers in Tawked Chat: the owner, the supervisors, then the agents of this number, each with their role, mobile (never the owner's) and whether you may change them.

        ``GET /v1/applications/{application}/chat/team``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CHAT_TEAM_LIST,
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
            _E.A_CHAT_TEAM_LIST,
            _PAGE_A_CHAT_TEAM_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def remove(
        self,
        application: str,
        member: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take a person off this application's support team: an agent loses this number's conversations and keeps the others; a supervisor leaves Tawked Chat as a whole. Someone left with no role at all is removed from the account. Answers ok.

        ``DELETE /v1/applications/{application}/chat/team/{member}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CHAT_TEAM_REMOVE,
            path={"application": application, "member": member},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        member: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One person of this support team: their role, mobile, last sign-in, and what they are beyond this number (the other inboxes they answer, their console role).

        ``GET /v1/applications/{application}/chat/team/{member}``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CHAT_TEAM_SHOW,
            path={"application": application, "member": member},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        member: str,
        *,
        name: str,
        role: Literal["administrator", "agent"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a support team person's name and role (`agent` or `administrator`); the mobile never changes (it is how they sign in). Answers the person.

        ``PATCH /v1/applications/{application}/chat/team/{member}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CHAT_TEAM_UPDATE,
            path={"application": application, "member": member},
            given={"name": name, "role": role},
            params=AccountChatTeamUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountChat:
    """``chat``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.attendant = AccountChatAttendant(client)
        self.menus = AccountChatMenus(client)
        self.team = AccountChatTeam(client)

    def open_link(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Where a person opens this application's conversations in Tawked Chat: the web address (they sign in with their own mobile), the phone apps once listed, the inbox's state, and whether this token's person answers this number's conversations.

        ``GET /v1/applications/{application}/chat/link``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CHAT_OPEN_LINK,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountChatAttendant:
    """``chat.attendant``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def log(
        self,
        application: str,
        *,
        cursor: str | NotGiven | None = NOT_GIVEN,
        limit: int | NotGiven | None = NOT_GIVEN,
        outcome: Literal["answered", "team", "radeef", "human", "ended", "ongoing"]
        | str
        | NotGiven = NOT_GIVEN,
        q: str | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The auto-attendant's log: every conversation it held, newest first, with the customer's name, the choices they tapped and how it ended (`answered`, `team`, `radeef`, `human`, `expired`, `stopped`, or `ongoing`).

        ``GET /v1/applications/{application}/chat/attendant/log``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CHAT_ATTENDANT_LOG,
            path={"application": application},
            given={"cursor": cursor, "limit": limit, "outcome": outcome, "q": q},
            params=AccountChatAttendantLogParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def publish(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Publish the stored draft (the starter when nothing was saved yet) as the next live version of the auto-attendant: once it is on, customers get this menu. Answers the attendant.

        ``POST /v1/applications/{application}/chat/attendant/publish``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CHAT_ATTENDANT_PUBLISH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def save_draft(
        self,
        application: str,
        *,
        definition: Mapping[str, Any],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the auto-attendant's draft (`definition`, the whole menu): it reaches no customer. Answers when it was saved and the problems that keep it from being published.

        ``PUT /v1/applications/{application}/chat/attendant/draft``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_ATTENDANT_SAVE_DRAFT,
            path={"application": application},
            given={"definition": definition},
            params=AccountChatAttendantSaveDraftParams,
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
        """The auto-attendant of this application's number: its state and whether it is on, its settings, the draft with the problems that keep it from being published, the published version, the people a fallback may go to, and the limits.

        ``GET /v1/applications/{application}/chat/attendant``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CHAT_ATTENDANT_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def switch(
        self,
        application: str,
        *,
        enabled: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the auto-attendant on (`enabled: true`: it answers every new conversation on the number with the published menu) or off (its conversations go to the team). Answers the attendant.

        ``PUT /v1/applications/{application}/chat/attendant/state``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CHAT_ATTENDANT_SWITCH,
            path={"application": application},
            given={"enabled": enabled},
            params=AccountChatAttendantSwitchParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update_settings(
        self,
        application: str,
        *,
        fallback_assign: Literal["auto", "member"] | str | NotGiven = NOT_GIVEN,
        fallback_member_id: str | NotGiven | None = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven = NOT_GIVEN,
        mode: Literal["menu_then_radeef", "menu_only"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change the auto-attendant's settings: `mode` (`menu_then_radeef` or `menu_only`), the customers' `language` (`ar` or `en`), and who gets a fallback handoff (`fallback_assign`: `auto` or `member` with `fallback_member_id`, one of `assignees`). Answers the attendant and the settings before.

        ``PUT /v1/applications/{application}/chat/attendant/settings``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_ATTENDANT_UPDATE_SETTINGS,
            path={"application": application},
            given={
                "fallback_assign": fallback_assign,
                "fallback_member_id": fallback_member_id,
                "language": language,
                "mode": mode,
            },
            params=AccountChatAttendantUpdateSettingsParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountChatMenus:
    """``chat.menus``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def check(
        self,
        application: str,
        *,
        url: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check a link before adding it as a menu: whether Tawked Chat can open it inside the conversation (`frame`: `opens`, `window` or `unknown`), and the link's own problem if any (`problem`: `length`, `http`, `host`, or null).

        ``POST /v1/applications/{application}/chat/menus/check``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_MENUS_CHECK,
            path={"application": application},
            given={"url": url},
            params=AccountChatMenusCheckParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        title: str,
        url: str,
        icon: FileInput | NotGiven | None = NOT_GIVEN,
        icon_mode: Literal["site", "upload", "none"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a chat menu: a page of your business (`title`, an https `url`) shown beside this application's conversations in Tawked Chat; `icon_mode` takes the site's icon (`site`, the default), an uploaded `icon` (`upload`) or none. Answers the menu.

        ``POST /v1/applications/{application}/chat/menus``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_MENUS_CREATE,
            path={"application": application},
            given={"title": title, "url": url, "icon": icon, "icon_mode": icon_mode},
            params=AccountChatMenusCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("icon",),
        )

    async def delete(
        self,
        application: str,
        menu: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a chat menu from Tawked Chat and from this application; answers ok.

        ``DELETE /v1/applications/{application}/chat/menus/{menu}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CHAT_MENUS_DELETE,
            path={"application": application, "menu": menu},
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
        """List the chat menus that show beside this application's conversations in Tawked Chat (its own, the ones of every conversation, and the Salla store's orders tab), in Tawked Chat's order.

        ``GET /v1/applications/{application}/chat/menus``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CHAT_MENUS_LIST,
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
            _E.A_CHAT_MENUS_LIST,
            _PAGE_A_CHAT_MENUS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        menu: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One chat menu of this application: its title, link, icon and whether it opens inside Tawked Chat.

        ``GET /v1/applications/{application}/chat/menus/{menu}``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CHAT_MENUS_SHOW,
            path={"application": application, "menu": menu},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        menu: str,
        *,
        title: str,
        url: str,
        icon: FileInput | NotGiven | None = NOT_GIVEN,
        icon_mode: Literal["site", "upload", "none"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a chat menu: send its `title` and `url` (both, as they should be), and `icon_mode` only to change the icon. Answers the menu.

        ``PATCH /v1/applications/{application}/chat/menus/{menu}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_MENUS_UPDATE,
            path={"application": application, "menu": menu},
            given={"title": title, "url": url, "icon": icon, "icon_mode": icon_mode},
            params=AccountChatMenusUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("icon",),
        )


class AsyncAccountChatTeam:
    """``chat.team``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def add(
        self,
        application: str,
        *,
        role: Literal["administrator", "agent"] | str,
        email: str | NotGiven | None = NOT_GIVEN,
        language: Literal["ar", "en"] | str | NotGiven | None = NOT_GIVEN,
        member_id: str | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven = NOT_GIVEN,
        phone: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a person to this application's support team: someone of the account by `member_id`, or someone new by `name` with a `phone` (a Saudi mobile, 05… or +9665…), an `email`, or both, and a `role` (`agent` or `administrator`). Someone new with an email signs in with it and Tawked e-mails them the invitation (`invitation_sent_to`); with a mobile, answers `sign_in_message` for whoever added them to send, written in your person's language or `language` (ar or en).

        ``POST /v1/applications/{application}/chat/team``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CHAT_TEAM_ADD,
            path={"application": application},
            given={
                "role": role,
                "email": email,
                "language": language,
                "member_id": member_id,
                "name": name,
                "phone": phone,
            },
            params=AccountChatTeamAddParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def candidates(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Who could join this support team without a new seat (the account's people not on it yet, mobiles masked), and the account's seats: the limit, how many are used, how many are left.

        ``GET /v1/applications/{application}/chat/team/candidates``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CHAT_TEAM_CANDIDATES,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def invite(
        self,
        application: str,
        member: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """E-mail the invitation again to a person of this support team who signs in with an email: one a minute and five a day per person, the one sent at the add included. Answers ok.

        ``POST /v1/applications/{application}/chat/team/{member}/invite``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_TEAM_INVITE,
            path={"application": application, "member": member},
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
        """List who answers this application's customers in Tawked Chat: the owner, the supervisors, then the agents of this number, each with their role, mobile (never the owner's) and whether you may change them.

        ``GET /v1/applications/{application}/chat/team``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CHAT_TEAM_LIST,
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
            _E.A_CHAT_TEAM_LIST,
            _PAGE_A_CHAT_TEAM_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def remove(
        self,
        application: str,
        member: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take a person off this application's support team: an agent loses this number's conversations and keeps the others; a supervisor leaves Tawked Chat as a whole. Someone left with no role at all is removed from the account. Answers ok.

        ``DELETE /v1/applications/{application}/chat/team/{member}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CHAT_TEAM_REMOVE,
            path={"application": application, "member": member},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        member: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One person of this support team: their role, mobile, last sign-in, and what they are beyond this number (the other inboxes they answer, their console role).

        ``GET /v1/applications/{application}/chat/team/{member}``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CHAT_TEAM_SHOW,
            path={"application": application, "member": member},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        member: str,
        *,
        name: str,
        role: Literal["administrator", "agent"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a support team person's name and role (`agent` or `administrator`); the mobile never changes (it is how they sign in). Answers the person.

        ``PATCH /v1/applications/{application}/chat/team/{member}``, permission ``chat:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CHAT_TEAM_UPDATE,
            path={"application": application, "member": member},
            given={"name": name, "role": role},
            params=AccountChatTeamUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountChat:
    """``chat``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.attendant = AsyncAccountChatAttendant(client)
        self.menus = AsyncAccountChatMenus(client)
        self.team = AsyncAccountChatTeam(client)

    async def open_link(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Where a person opens this application's conversations in Tawked Chat: the web address (they sign in with their own mobile), the phone apps once listed, the inbox's state, and whether this token's person answers this number's conversations.

        ``GET /v1/applications/{application}/chat/link``, permission ``chat:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CHAT_OPEN_LINK,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )
