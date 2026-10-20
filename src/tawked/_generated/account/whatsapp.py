"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountWhatsAppMessagesListParams,
    AccountWhatsAppMessagesPreviewParams,
    AccountWhatsAppMessagesSendParams,
    AccountWhatsAppNumberChangePinParams,
    AccountWhatsAppNumberRequestDisplayNameParams,
    AccountWhatsAppNumberRequestOfficialBadgeParams,
    AccountWhatsAppNumberUpdateComponentsParams,
    AccountWhatsAppNumberUpdateProfileParams,
    AccountWhatsAppTemplateDraftsAssistantParams,
    AccountWhatsAppTemplateDraftsCreateParams,
    AccountWhatsAppTemplateDraftsListParams,
    AccountWhatsAppTemplateDraftsSubmitParams,
    AccountWhatsAppTemplateDraftsUpdateParams,
    AccountWhatsAppTemplateLibraryCreateParams,
    AccountWhatsAppTemplateLibraryListParams,
    AccountWhatsAppTemplateSamplesCreateParams,
    AccountWhatsAppTemplatesCheckParams,
    AccountWhatsAppTemplatesCreateParams,
    AccountWhatsAppTemplatesListParams,
    AccountWhatsAppTemplateSuggestionsCreateParams,
    AccountWhatsAppTemplateSuggestionsStartParams,
    AccountWhatsAppTemplatesUpdateParams,
    AccountWhatsAppUsageShowParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_WHATSAPP_MESSAGES_LIST,
    _PAGE_A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
    _PAGE_A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
    _PAGE_A_WHATSAPP_TEMPLATES_LIST,
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


class AccountWhatsAppBilling:
    """``whatsapp.billing``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def check(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Meta again whether the number's WhatsApp Business Account has a payment method; answers `billing_state` (ready, missing or unknown), and while it is missing the `human_action` that adds one at Meta.

        ``POST /v1/applications/{application}/whatsapp/billing/check``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_BILLING_CHECK,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppCharges:
    """``whatsapp.charges``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """What Meta charged on the application's WhatsApp number this month and last, by Meta's category (MARKETING, UTILITY, AUTHENTICATION, SERVICE for the replies past the free ones), with an estimate where Meta keeps the amount from Tawked, and the number's free replies this month.

        ``GET /v1/applications/{application}/whatsapp/charges``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_CHARGES_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppConnection:
    """``whatsapp.connection``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def delete(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect the application's WhatsApp number from Tawked: its Tawked Chat inbox goes, sending stops until a number is connected again (whatsapp.connection.link). Answers ok.

        ``DELETE /v1/applications/{application}/whatsapp/connection``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_CONNECTION_DELETE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def link(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Where the person connects the application's WhatsApp number (the console address that opens Meta's window), and how far it got: connected or not, the stage, the person's signup in flight.

        ``GET /v1/applications/{application}/whatsapp/connection``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_CONNECTION_LINK,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppFirstMessage:
    """``whatsapp.first_message``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create_key(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a live application key for the sending API (named "First message"); answers the key's plaintext once, and its prefix.

        ``POST /v1/applications/{application}/whatsapp/first-message/key``, permission ``whatsapp:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_FIRST_MESSAGE_CREATE_KEY,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send_test(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send the guide's template to the token's person's own phone, as the application (Meta bills it); answers the message with its status. Poll whatsapp.first_message.show for delivery.

        ``POST /v1/applications/{application}/whatsapp/first-message/test``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_FIRST_MESSAGE_SEND_TEST,
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
        """Where the number stands on the way to its first message: the phase (setting up, payment, blocked, ready…), the template a test sends and the request that sends it from your servers, and the last test with its delivery status.

        ``GET /v1/applications/{application}/whatsapp/first-message``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_FIRST_MESSAGE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppGoLive:
    """``whatsapp.go_live``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def check(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Re-read every go-live fact from Meta (payment method, display name, business verification, health, an approved template, a first message, the badge); answers the checklist, each item done, to do, blocked or unknown with where to act.

        ``POST /v1/applications/{application}/whatsapp/go-live/check``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_GO_LIVE_CHECK,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppMessages:
    """``whatsapp.messages``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "sent", "delivered", "read", "failed", "in_flight"]
        | str
        | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the WhatsApp messages the application sent, newest first, each with its masked destination, template, status (accepted, sent, delivered, read, failed with Meta's error) and times; filter by status (or `in_flight`), period (`range`: today, 7d, 30d, 90d; default 30d), template, or a reference or phone (`q`).

        ``GET /v1/applications/{application}/whatsapp/messages``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WHATSAPP_MESSAGES_LIST,
            path={"application": application},
            given={"page": page, "q": q, "range": range, "status": status, "template": template},
            params=AccountWhatsAppMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "sent", "delivered", "read", "failed", "in_flight"]
        | str
        | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_MESSAGES_LIST,
            _PAGE_A_WHATSAPP_MESSAGES_LIST,
            path={"application": application},
            given={"page": page, "q": q, "range": range, "status": status, "template": template},
            params=AccountWhatsAppMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def preview(
        self,
        application: str,
        *,
        template: str,
        to: str,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        lang: str | NotGiven | None = NOT_GIVEN,
        language: str | NotGiven | None = NOT_GIVEN,
        params: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Render a WhatsApp template message exactly as whatsapp.messages.send would send it, sending nothing: the message with its buttons, every check (number, recipient, template APPROVED, values, consent, account, balance), the price (Tawked's fee and Meta's estimate for MARKETING), `problems` that block it and `warnings` to show the person. The body is whatsapp.messages.send's.

        ``POST /v1/applications/{application}/whatsapp/messages/preview``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_MESSAGES_PREVIEW,
            path={"application": application},
            given={
                "template": template,
                "to": to,
                "buttons": buttons,
                "header": header,
                "lang": lang,
                "language": language,
                "params": params,
                "reference": reference,
            },
            params=AccountWhatsAppMessagesPreviewParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send(
        self,
        application: str,
        *,
        template: str,
        to: str,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        lang: str | NotGiven | None = NOT_GIVEN,
        language: str | NotGiven | None = NOT_GIVEN,
        params: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send one APPROVED WhatsApp template to a customer from the application's number; answers the message (status `accepted`, then poll whatsapp.messages.show for sent, delivered, read or failed). Charges Tawked's fee from the wallet.

        ``POST /v1/applications/{application}/whatsapp/messages``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_MESSAGES_SEND,
            path={"application": application},
            given={
                "template": template,
                "to": to,
                "buttons": buttons,
                "header": header,
                "lang": lang,
                "language": language,
                "params": params,
                "reference": reference,
            },
            params=AccountWhatsAppMessagesSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        message: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One WhatsApp message the application sent, by its id: its status and the time of each step, Meta's error when it failed, the text the customer read, the key that sent it, and `next`: poll while it is accepted or sent, what a failure means.

        ``GET /v1/applications/{application}/whatsapp/messages/{message}``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_MESSAGES_SHOW,
            path={"application": application, "message": message},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppNumber:
    """``whatsapp.number``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def change_pin(
        self,
        application: str,
        *,
        pin: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the number's two-step verification PIN on Meta (six digits); answers ok.

        ``POST /v1/applications/{application}/whatsapp/number/pin``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_CHANGE_PIN,
            path={"application": application},
            given={"pin": pin},
            params=AccountWhatsAppNumberChangePinParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def refresh(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the number's facts, health, quality and account again from Meta (the console's "check again"); answers the number as whatsapp.number.show does.

        ``POST /v1/applications/{application}/whatsapp/number/refresh``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_REFRESH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def request_display_name(
        self,
        application: str,
        *,
        name: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Meta to change the number's display name (the name customers see); Meta reviews it against the business. Answers the number and `next`: read whatsapp.number.show once or twice a day for `new_name_status`.

        ``POST /v1/applications/{application}/whatsapp/number/display-name``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_REQUEST_DISPLAY_NAME,
            path={"application": application},
            given={"name": name},
            params=AccountWhatsAppNumberRequestDisplayNameParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def request_official_badge(
        self,
        application: str,
        *,
        country: str,
        language: str,
        links: Sequence[str],
        website: str,
        note: str | NotGiven | None = NOT_GIVEN,
        parent_brand: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Request Meta's verified badge (Official Business Account) for the number: the website, country, language, five to ten links that show the business is notable; answers the number with `oba_status` and `next` (read whatsapp.number.show once a day until Meta decides).

        ``POST /v1/applications/{application}/whatsapp/number/official-business-account``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_REQUEST_OFFICIAL_BADGE,
            path={"application": application},
            given={
                "country": country,
                "language": language,
                "links": links,
                "website": website,
                "note": note,
                "parent_brand": parent_brand,
            },
            params=AccountWhatsAppNumberRequestOfficialBadgeParams,
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
        """The application's WhatsApp number: connected or not, its stage and what to do next, display name and its review, quality, messaging tier and limit, business profile, verified badge, Meta billing state and the go-live checklist.

        ``GET /v1/applications/{application}/whatsapp/number``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update_components(
        self,
        application: str,
        *,
        welcome_message: bool,
        commands: Sequence[Mapping[str, Any]] | NotGiven | None = NOT_GIVEN,
        prompts: Sequence[str] | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set what a customer sees on opening the chat: the welcome message switch, up to four prompts and up to thirty commands (name and hint). Answers the number.

        ``PUT /v1/applications/{application}/whatsapp/number/components``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_UPDATE_COMPONENTS,
            path={"application": application},
            given={"welcome_message": welcome_message, "commands": commands, "prompts": prompts},
            params=AccountWhatsAppNumberUpdateComponentsParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update_profile(
        self,
        application: str,
        *,
        about: str,
        address: str | NotGiven | None = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        email: str | NotGiven | None = NOT_GIVEN,
        picture: FileInput | NotGiven | None = NOT_GIVEN,
        vertical: Literal[
            "ALCOHOL",
            "APPAREL",
            "AUTO",
            "BEAUTY",
            "EDU",
            "ENTERTAIN",
            "EVENT_PLAN",
            "FINANCE",
            "GOVT",
            "GROCERY",
            "HEALTH",
            "HOTEL",
            "NONPROFIT",
            "ONLINE_GAMBLING",
            "OTC_DRUGS",
            "OTHER",
            "PHYSICAL_GAMBLING",
            "PROF_SERVICES",
            "RESTAURANT",
            "RETAIL",
            "TRAVEL",
            "UNDEFINED",
        ]
        | str
        | NotGiven
        | None = NOT_GIVEN,
        websites: Sequence[str] | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change the business profile customers see on WhatsApp (about, address, description, e-mail, up to two websites, category, a JPG or PNG picture); a field left out stays as it is. Answers the number.

        ``PUT /v1/applications/{application}/whatsapp/number/profile``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_NUMBER_UPDATE_PROFILE,
            path={"application": application},
            given={
                "about": about,
                "address": address,
                "description": description,
                "email": email,
                "picture": picture,
                "vertical": vertical,
                "websites": websites,
            },
            params=AccountWhatsAppNumberUpdateProfileParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("picture",),
        )


class AccountWhatsAppTemplateDrafts:
    """``whatsapp.template_drafts``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def assistant(
        self,
        application: str,
        draft: str,
        *,
        draft_: Mapping[str, Any],
        message: str,
        revision: int,
        retry: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One turn of Tawked's template assistant on a draft: send your message (or `retry: true`) with the draft's state and revision; it writes into the draft and answers what it said (`turns`), the draft and its lint.

        ``POST /v1/applications/{application}/whatsapp/template-drafts/{draft}/assistant``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_ASSISTANT,
            path={"application": application, "draft": draft},
            given={"draft": draft_, "message": message, "revision": revision, "retry": retry},
            params=AccountWhatsAppTemplateDraftsAssistantParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        duplicate: str | NotGiven = NOT_GIVEN,
        source: Literal["assistant", "blank"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a template draft: blank (`source: blank`), for the template assistant (`source: assistant`), or a copy of a template on the number by its name (`duplicate`). Answers the draft with its `revision`.

        ``POST /v1/applications/{application}/whatsapp/template-drafts``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_CREATE,
            path={"application": application},
            given={"duplicate": duplicate, "source": source},
            params=AccountWhatsAppTemplateDraftsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        draft: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a template draft (only Tawked's working copy; nothing on Meta changes); answers ok.

        ``DELETE /v1/applications/{application}/whatsapp/template-drafts/{draft}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_DELETE,
            path={"application": application, "draft": draft},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's template drafts (not yet submitted to Meta), newest change first, each with its languages and variants; filter by name (`q`).

        ``GET /v1/applications/{application}/whatsapp/template-drafts``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
            path={"application": application},
            given={"page": page, "q": q},
            params=AccountWhatsAppTemplateDraftsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
            _PAGE_A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
            path={"application": application},
            given={"page": page, "q": q},
            params=AccountWhatsAppTemplateDraftsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        draft: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One template draft in full: its variants, `revision` (send it back on update and submit), and `lint`, the checks it must pass before Meta sees it (an `error` blocks submit).

        ``GET /v1/applications/{application}/whatsapp/template-drafts/{draft}``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_SHOW,
            path={"application": application, "draft": draft},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def submit(
        self,
        application: str,
        draft: str,
        *,
        revision: int,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        category: str | NotGiven | None = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        otp_type: str | NotGiven | None = NOT_GIVEN,
        package_name: str | NotGiven | None = NOT_GIVEN,
        security_recommendation: bool | NotGiven | None = NOT_GIVEN,
        signature_hash: str | NotGiven | None = NOT_GIVEN,
        variants: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the draft (same body as update) and submit it to Meta, one template per language; answers the templates created (each id and status) and the languages Meta refused, with its words. Then poll whatsapp.templates.show per id.

        ``POST /v1/applications/{application}/whatsapp/template-drafts/{draft}/submit``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_SUBMIT,
            path={"application": application, "draft": draft},
            given={
                "revision": revision,
                "autofill_text": autofill_text,
                "category": category,
                "code_expiry_minutes": code_expiry_minutes,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "name": name,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "variants": variants,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplateDraftsSubmitParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        draft: str,
        *,
        revision: int,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        category: str | NotGiven | None = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        otp_type: str | NotGiven | None = NOT_GIVEN,
        package_name: str | NotGiven | None = NOT_GIVEN,
        security_recommendation: bool | NotGiven | None = NOT_GIVEN,
        signature_hash: str | NotGiven | None = NOT_GIVEN,
        variants: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save a draft's whole state (name, category, variants per language with header, body, footer, buttons, examples) under the `revision` last read; answers the draft with its new revision and its `lint`; once no `lint` error is left, send it to Meta with whatsapp.template_drafts.submit.

        ``PUT /v1/applications/{application}/whatsapp/template-drafts/{draft}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_UPDATE,
            path={"application": application, "draft": draft},
            given={
                "revision": revision,
                "autofill_text": autofill_text,
                "category": category,
                "code_expiry_minutes": code_expiry_minutes,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "name": name,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "variants": variants,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplateDraftsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppTemplateLibrary:
    """``whatsapp.template_library``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        language: Literal["ar", "en_US"] | str,
        library_name: str,
        name: str,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        library_id: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a template from Meta's library: the library row's name and language, the new template's name, one input per library button in its order (a link's base, a phone number). Answers the new template's id, status and `next` (poll whatsapp.templates.show while it is PENDING).

        ``POST /v1/applications/{application}/whatsapp/template-library``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_LIBRARY_CREATE,
            path={"application": application},
            given={
                "language": language,
                "library_name": library_name,
                "name": name,
                "buttons": buttons,
                "library_id": library_id,
            },
            params=AccountWhatsAppTemplateLibraryCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        industry: Literal["E_COMMERCE", "FINANCIAL_SERVICES"] | str | NotGiven = NOT_GIVEN,
        language: Literal["ar", "en_US"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        topic: Literal["ACCOUNT_UPDATES", "CUSTOMER_FEEDBACK", "ORDER_MANAGEMENT", "PAYMENTS"]
        | str
        | NotGiven = NOT_GIVEN,
        usecase: Literal[
            "ACCOUNT_CREATION_CONFIRMATION",
            "AUTO_PAY_REMINDER",
            "DELIVERY_CONFIRMATION",
            "DELIVERY_FAILED",
            "DELIVERY_UPDATE",
            "FEEDBACK_SURVEY",
            "FRAUD_ALERT",
            "LOW_BALANCE_WARNING",
            "ORDER_ACTION_NEEDED",
            "ORDER_CONFIRMATION",
            "ORDER_DELAY",
            "ORDER_OR_TRANSACTION_CANCEL",
            "ORDER_PICK_UP",
            "PAYMENT_ACTION_REQUIRED",
            "PAYMENT_CONFIRMATION",
            "PAYMENT_DUE_REMINDER",
            "PAYMENT_OVERDUE",
            "PAYMENT_REJECT_FAIL",
            "PAYMENT_SCHEDULED",
            "RECEIPT_ATTACHMENT",
            "RETURN_CONFIRMATION",
            "SHIPMENT_CONFIRMATION",
            "STATEMENT_ATTACHMENT",
            "STATEMENT_AVAILABLE",
            "TRANSACTION_ALERT",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """Browse Meta's template library (ready-made utility templates Meta usually approves at once), filtered by topic, use case, industry, language or words (`q`); each with the name and buttons whatsapp.template_library.create takes.

        ``GET /v1/applications/{application}/whatsapp/template-library``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
            path={"application": application},
            given={
                "industry": industry,
                "language": language,
                "page": page,
                "q": q,
                "topic": topic,
                "usecase": usecase,
            },
            params=AccountWhatsAppTemplateLibraryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        industry: Literal["E_COMMERCE", "FINANCIAL_SERVICES"] | str | NotGiven = NOT_GIVEN,
        language: Literal["ar", "en_US"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        topic: Literal["ACCOUNT_UPDATES", "CUSTOMER_FEEDBACK", "ORDER_MANAGEMENT", "PAYMENTS"]
        | str
        | NotGiven = NOT_GIVEN,
        usecase: Literal[
            "ACCOUNT_CREATION_CONFIRMATION",
            "AUTO_PAY_REMINDER",
            "DELIVERY_CONFIRMATION",
            "DELIVERY_FAILED",
            "DELIVERY_UPDATE",
            "FEEDBACK_SURVEY",
            "FRAUD_ALERT",
            "LOW_BALANCE_WARNING",
            "ORDER_ACTION_NEEDED",
            "ORDER_CONFIRMATION",
            "ORDER_DELAY",
            "ORDER_OR_TRANSACTION_CANCEL",
            "ORDER_PICK_UP",
            "PAYMENT_ACTION_REQUIRED",
            "PAYMENT_CONFIRMATION",
            "PAYMENT_DUE_REMINDER",
            "PAYMENT_OVERDUE",
            "PAYMENT_REJECT_FAIL",
            "PAYMENT_SCHEDULED",
            "RECEIPT_ATTACHMENT",
            "RETURN_CONFIRMATION",
            "SHIPMENT_CONFIRMATION",
            "STATEMENT_ATTACHMENT",
            "STATEMENT_AVAILABLE",
            "TRANSACTION_ALERT",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
            _PAGE_A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
            path={"application": application},
            given={
                "industry": industry,
                "language": language,
                "page": page,
                "q": q,
                "topic": topic,
                "usecase": usecase,
            },
            params=AccountWhatsAppTemplateLibraryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppTemplateSamples:
    """``whatsapp.template_samples``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        image: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload a sample image for a template's IMAGE header (multipart `image`, a JPG or PNG of at most 5 MB); answers its `path`, sent as `header_sample` to whatsapp.templates.create or a draft's variant.

        ``POST /v1/applications/{application}/whatsapp/template-samples``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SAMPLES_CREATE,
            path={"application": application},
            given={"image": image},
            params=AccountWhatsAppTemplateSamplesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("image",),
        )


class AccountWhatsAppTemplateSuggestions:
    """``whatsapp.template_suggestions``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        analysis: str,
        *,
        keys: Sequence[str],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the picked suggestions of a finished run (`keys`) into drafts and submit them to Meta; answers each one's outcome (submitted, partial or failed, with the templates created). Then poll whatsapp.templates.show per created id.

        ``POST /v1/applications/{application}/whatsapp/template-suggestions/{analysis}/create``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_CREATE,
            path={"application": application, "analysis": analysis},
            given={"keys": keys},
            params=AccountWhatsAppTemplateSuggestionsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def draft(
        self,
        application: str,
        analysis: str,
        key: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make one suggestion of a finished run a template draft (or answer the draft it already has), to edit before submitting; answers the draft.

        ``POST /v1/applications/{application}/whatsapp/template-suggestions/{analysis}/suggestions/{key}/draft``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_DRAFT,
            path={"application": application, "analysis": analysis, "key": key},
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
        """The application's latest run of template suggestions from the business: its status (queued, reading, writing, done, failed), the business profile, and each suggested template with its key, variants and outcome; plus the runs left today.

        ``GET /v1/applications/{application}/whatsapp/template-suggestions``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def start(
        self,
        application: str,
        *,
        description: str | NotGiven | None = NOT_GIVEN,
        website_url: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a run of template suggestions from the business's website (`website_url`) and a short description; answers the run (status queued). Poll whatsapp.template_suggestions.show until it is done.

        ``POST /v1/applications/{application}/whatsapp/template-suggestions``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_START,
            path={"application": application},
            given={"description": description, "website_url": website_url},
            params=AccountWhatsAppTemplateSuggestionsStartParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppTemplates:
    """``whatsapp.templates``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def check(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        name: str,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        header_format: Literal["TEXT", "IMAGE", "DOCUMENT"] | str | NotGiven | None = NOT_GIVEN,
        header_sample: str | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        otp_type: Literal["COPY_CODE", "ONE_TAP", "ZERO_TAP"] | str | NotGiven = NOT_GIVEN,
        package_name: str | NotGiven = NOT_GIVEN,
        security_recommendation: bool | NotGiven = NOT_GIVEN,
        signature_hash: str | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check a proposed template with whatsapp.templates.create's own rules before creating it, saving nothing: answers `ready` (no error blocks it) and every problem once (`level` error or warning, `field`, `code`, and `problem`: what is wrong in words). The body is exactly whatsapp.templates.create's (any category, an IMAGE header with its `header_sample`, AUTHENTICATION with its fields); then call whatsapp.templates.create with it.

        ``POST /v1/applications/{application}/whatsapp/templates/check``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_CHECK,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "name": name,
                "autofill_text": autofill_text,
                "body": body,
                "buttons": buttons,
                "code_expiry_minutes": code_expiry_minutes,
                "examples": examples,
                "footer": footer,
                "header": header,
                "header_format": header_format,
                "header_sample": header_sample,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplatesCheckParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        name: str,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        header_format: Literal["TEXT", "IMAGE", "DOCUMENT"] | str | NotGiven | None = NOT_GIVEN,
        header_sample: str | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        otp_type: Literal["COPY_CODE", "ONE_TAP", "ZERO_TAP"] | str | NotGiven = NOT_GIVEN,
        package_name: str | NotGiven = NOT_GIVEN,
        security_recommendation: bool | NotGiven = NOT_GIVEN,
        signature_hash: str | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a WhatsApp template and submit it to Meta for review; answers its id and status (PENDING until Meta decides). Then poll whatsapp.templates.show with the id until the status is APPROVED or REJECTED.

        ``POST /v1/applications/{application}/whatsapp/templates``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_CREATE,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "name": name,
                "autofill_text": autofill_text,
                "body": body,
                "buttons": buttons,
                "code_expiry_minutes": code_expiry_minutes,
                "examples": examples,
                "footer": footer,
                "header": header,
                "header_format": header_format,
                "header_sample": header_sample,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplatesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete one language of a template on Meta; answers ok with its id, name and language. It stops for every application on the same WhatsApp Business Account: read whatsapp.templates.show's `used_by` first.

        ``DELETE /v1/applications/{application}/whatsapp/templates/{template}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_DELETE,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "APPROVED",
            "PENDING",
            "REJECTED",
            "PAUSED",
            "DISABLED",
            "IN_APPEAL",
            "PENDING_DELETION",
            "LIMIT_EXCEEDED",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the WhatsApp templates on the application's number as Meta holds them, each with its id, status (APPROVED, PENDING, REJECTED…), quality, rejection reason and whether it can be sent; filter by status, category, language or a name (`q`).

        ``GET /v1/applications/{application}/whatsapp/templates``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WHATSAPP_TEMPLATES_LIST,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountWhatsAppTemplatesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "APPROVED",
            "PENDING",
            "REJECTED",
            "PAUSED",
            "DISABLED",
            "IN_APPEAL",
            "PENDING_DELETION",
            "LIMIT_EXCEEDED",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_TEMPLATES_LIST,
            _PAGE_A_WHATSAPP_TEMPLATES_LIST,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountWhatsAppTemplatesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def refresh(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop Tawked's cached copy of the number's templates; answers ok. The next whatsapp.templates.list or whatsapp.templates.show reads them from Meta afresh.

        ``POST /v1/applications/{application}/whatsapp/templates/refresh``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_REFRESH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        template: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One WhatsApp template by its Meta id: Meta's status (poll this after a create until APPROVED or REJECTED), quality, rejection reason, whether it can be sent and edited, its parts, what sends it today (campaigns, automations), and `next`: what to do in its status.

        ``GET /v1/applications/{application}/whatsapp/templates/{template}``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_SHOW,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def starter_kit(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Submit Tawked's starter kit (order and shipping updates in Arabic and English) to Meta, skipping names the number already holds; answers how many were created and which failed with Meta's words. Then poll whatsapp.templates.list until Meta approves them.

        ``POST /v1/applications/{application}/whatsapp/templates/starter-kit``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_STARTER_KIT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def unpause(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Resume a template Meta paused for low quality; answers ok, or Meta's refusal when its pause has not ended.

        ``POST /v1/applications/{application}/whatsapp/templates/{template}/unpause``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_UNPAUSE,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        template: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        name: str,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        header_format: Literal["TEXT", "IMAGE", "DOCUMENT"] | str | NotGiven | None = NOT_GIVEN,
        header_sample: str | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        otp_type: Literal["COPY_CODE", "ONE_TAP", "ZERO_TAP"] | str | NotGiven = NOT_GIVEN,
        package_name: str | NotGiven = NOT_GIVEN,
        security_recommendation: bool | NotGiven = NOT_GIVEN,
        signature_hash: str | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Edit a template's content on Meta (its name and language stay); Meta reviews it again. Answers the template's id and status; poll whatsapp.templates.show for Meta's decision.

        ``PATCH /v1/applications/{application}/whatsapp/templates/{template}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_UPDATE,
            path={"application": application, "template": template},
            given={
                "category": category,
                "language": language,
                "name": name,
                "autofill_text": autofill_text,
                "body": body,
                "buttons": buttons,
                "code_expiry_minutes": code_expiry_minutes,
                "examples": examples,
                "footer": footer,
                "header": header,
                "header_format": header_format,
                "header_sample": header_sample,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplatesUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWhatsAppUsage:
    """``whatsapp.usage``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        application: str,
        *,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's WhatsApp template messages for a `period` (today, 7d, month, 30d; Riyadh time) against the same span before: sent, delivered, read, failed, in flight, the delivered and read rates, and Tawked's fees charged (`charged_halalas`, for who sees the money; Meta bills its own charges separately).

        ``GET /v1/applications/{application}/whatsapp/usage``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WHATSAPP_USAGE_SHOW,
            path={"application": application},
            given={"period": period},
            params=AccountWhatsAppUsageShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWhatsApp:
    """``whatsapp``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.billing = AccountWhatsAppBilling(client)
        self.charges = AccountWhatsAppCharges(client)
        self.connection = AccountWhatsAppConnection(client)
        self.first_message = AccountWhatsAppFirstMessage(client)
        self.go_live = AccountWhatsAppGoLive(client)
        self.messages = AccountWhatsAppMessages(client)
        self.number = AccountWhatsAppNumber(client)
        self.template_drafts = AccountWhatsAppTemplateDrafts(client)
        self.template_library = AccountWhatsAppTemplateLibrary(client)
        self.template_samples = AccountWhatsAppTemplateSamples(client)
        self.template_suggestions = AccountWhatsAppTemplateSuggestions(client)
        self.templates = AccountWhatsAppTemplates(client)
        self.usage = AccountWhatsAppUsage(client)


class AsyncAccountWhatsAppBilling:
    """``whatsapp.billing``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def check(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Meta again whether the number's WhatsApp Business Account has a payment method; answers `billing_state` (ready, missing or unknown), and while it is missing the `human_action` that adds one at Meta.

        ``POST /v1/applications/{application}/whatsapp/billing/check``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_BILLING_CHECK,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppCharges:
    """``whatsapp.charges``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """What Meta charged on the application's WhatsApp number this month and last, by Meta's category (MARKETING, UTILITY, AUTHENTICATION, SERVICE for the replies past the free ones), with an estimate where Meta keeps the amount from Tawked, and the number's free replies this month.

        ``GET /v1/applications/{application}/whatsapp/charges``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_CHARGES_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppConnection:
    """``whatsapp.connection``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def delete(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Disconnect the application's WhatsApp number from Tawked: its Tawked Chat inbox goes, sending stops until a number is connected again (whatsapp.connection.link). Answers ok.

        ``DELETE /v1/applications/{application}/whatsapp/connection``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_CONNECTION_DELETE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def link(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Where the person connects the application's WhatsApp number (the console address that opens Meta's window), and how far it got: connected or not, the stage, the person's signup in flight.

        ``GET /v1/applications/{application}/whatsapp/connection``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_CONNECTION_LINK,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppFirstMessage:
    """``whatsapp.first_message``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create_key(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make a live application key for the sending API (named "First message"); answers the key's plaintext once, and its prefix.

        ``POST /v1/applications/{application}/whatsapp/first-message/key``, permission ``whatsapp:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_FIRST_MESSAGE_CREATE_KEY,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send_test(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send the guide's template to the token's person's own phone, as the application (Meta bills it); answers the message with its status. Poll whatsapp.first_message.show for delivery.

        ``POST /v1/applications/{application}/whatsapp/first-message/test``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_FIRST_MESSAGE_SEND_TEST,
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
        """Where the number stands on the way to its first message: the phase (setting up, payment, blocked, ready…), the template a test sends and the request that sends it from your servers, and the last test with its delivery status.

        ``GET /v1/applications/{application}/whatsapp/first-message``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_FIRST_MESSAGE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppGoLive:
    """``whatsapp.go_live``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def check(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Re-read every go-live fact from Meta (payment method, display name, business verification, health, an approved template, a first message, the badge); answers the checklist, each item done, to do, blocked or unknown with where to act.

        ``POST /v1/applications/{application}/whatsapp/go-live/check``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_GO_LIVE_CHECK,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppMessages:
    """``whatsapp.messages``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "sent", "delivered", "read", "failed", "in_flight"]
        | str
        | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the WhatsApp messages the application sent, newest first, each with its masked destination, template, status (accepted, sent, delivered, read, failed with Meta's error) and times; filter by status (or `in_flight`), period (`range`: today, 7d, 30d, 90d; default 30d), template, or a reference or phone (`q`).

        ``GET /v1/applications/{application}/whatsapp/messages``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WHATSAPP_MESSAGES_LIST,
            path={"application": application},
            given={"page": page, "q": q, "range": range, "status": status, "template": template},
            params=AccountWhatsAppMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        range: Literal["today", "7d", "30d", "90d"] | str | NotGiven = NOT_GIVEN,
        status: Literal["accepted", "sent", "delivered", "read", "failed", "in_flight"]
        | str
        | NotGiven = NOT_GIVEN,
        template: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_MESSAGES_LIST,
            _PAGE_A_WHATSAPP_MESSAGES_LIST,
            path={"application": application},
            given={"page": page, "q": q, "range": range, "status": status, "template": template},
            params=AccountWhatsAppMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def preview(
        self,
        application: str,
        *,
        template: str,
        to: str,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        lang: str | NotGiven | None = NOT_GIVEN,
        language: str | NotGiven | None = NOT_GIVEN,
        params: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Render a WhatsApp template message exactly as whatsapp.messages.send would send it, sending nothing: the message with its buttons, every check (number, recipient, template APPROVED, values, consent, account, balance), the price (Tawked's fee and Meta's estimate for MARKETING), `problems` that block it and `warnings` to show the person. The body is whatsapp.messages.send's.

        ``POST /v1/applications/{application}/whatsapp/messages/preview``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_MESSAGES_PREVIEW,
            path={"application": application},
            given={
                "template": template,
                "to": to,
                "buttons": buttons,
                "header": header,
                "lang": lang,
                "language": language,
                "params": params,
                "reference": reference,
            },
            params=AccountWhatsAppMessagesPreviewParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send(
        self,
        application: str,
        *,
        template: str,
        to: str,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        lang: str | NotGiven | None = NOT_GIVEN,
        language: str | NotGiven | None = NOT_GIVEN,
        params: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        reference: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send one APPROVED WhatsApp template to a customer from the application's number; answers the message (status `accepted`, then poll whatsapp.messages.show for sent, delivered, read or failed). Charges Tawked's fee from the wallet.

        ``POST /v1/applications/{application}/whatsapp/messages``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_MESSAGES_SEND,
            path={"application": application},
            given={
                "template": template,
                "to": to,
                "buttons": buttons,
                "header": header,
                "lang": lang,
                "language": language,
                "params": params,
                "reference": reference,
            },
            params=AccountWhatsAppMessagesSendParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        message: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One WhatsApp message the application sent, by its id: its status and the time of each step, Meta's error when it failed, the text the customer read, the key that sent it, and `next`: poll while it is accepted or sent, what a failure means.

        ``GET /v1/applications/{application}/whatsapp/messages/{message}``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_MESSAGES_SHOW,
            path={"application": application, "message": message},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppNumber:
    """``whatsapp.number``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def change_pin(
        self,
        application: str,
        *,
        pin: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the number's two-step verification PIN on Meta (six digits); answers ok.

        ``POST /v1/applications/{application}/whatsapp/number/pin``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_CHANGE_PIN,
            path={"application": application},
            given={"pin": pin},
            params=AccountWhatsAppNumberChangePinParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def refresh(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the number's facts, health, quality and account again from Meta (the console's "check again"); answers the number as whatsapp.number.show does.

        ``POST /v1/applications/{application}/whatsapp/number/refresh``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_REFRESH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def request_display_name(
        self,
        application: str,
        *,
        name: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Meta to change the number's display name (the name customers see); Meta reviews it against the business. Answers the number and `next`: read whatsapp.number.show once or twice a day for `new_name_status`.

        ``POST /v1/applications/{application}/whatsapp/number/display-name``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_REQUEST_DISPLAY_NAME,
            path={"application": application},
            given={"name": name},
            params=AccountWhatsAppNumberRequestDisplayNameParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def request_official_badge(
        self,
        application: str,
        *,
        country: str,
        language: str,
        links: Sequence[str],
        website: str,
        note: str | NotGiven | None = NOT_GIVEN,
        parent_brand: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Request Meta's verified badge (Official Business Account) for the number: the website, country, language, five to ten links that show the business is notable; answers the number with `oba_status` and `next` (read whatsapp.number.show once a day until Meta decides).

        ``POST /v1/applications/{application}/whatsapp/number/official-business-account``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_REQUEST_OFFICIAL_BADGE,
            path={"application": application},
            given={
                "country": country,
                "language": language,
                "links": links,
                "website": website,
                "note": note,
                "parent_brand": parent_brand,
            },
            params=AccountWhatsAppNumberRequestOfficialBadgeParams,
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
        """The application's WhatsApp number: connected or not, its stage and what to do next, display name and its review, quality, messaging tier and limit, business profile, verified badge, Meta billing state and the go-live checklist.

        ``GET /v1/applications/{application}/whatsapp/number``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update_components(
        self,
        application: str,
        *,
        welcome_message: bool,
        commands: Sequence[Mapping[str, Any]] | NotGiven | None = NOT_GIVEN,
        prompts: Sequence[str] | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set what a customer sees on opening the chat: the welcome message switch, up to four prompts and up to thirty commands (name and hint). Answers the number.

        ``PUT /v1/applications/{application}/whatsapp/number/components``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_UPDATE_COMPONENTS,
            path={"application": application},
            given={"welcome_message": welcome_message, "commands": commands, "prompts": prompts},
            params=AccountWhatsAppNumberUpdateComponentsParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update_profile(
        self,
        application: str,
        *,
        about: str,
        address: str | NotGiven | None = NOT_GIVEN,
        description: str | NotGiven | None = NOT_GIVEN,
        email: str | NotGiven | None = NOT_GIVEN,
        picture: FileInput | NotGiven | None = NOT_GIVEN,
        vertical: Literal[
            "ALCOHOL",
            "APPAREL",
            "AUTO",
            "BEAUTY",
            "EDU",
            "ENTERTAIN",
            "EVENT_PLAN",
            "FINANCE",
            "GOVT",
            "GROCERY",
            "HEALTH",
            "HOTEL",
            "NONPROFIT",
            "ONLINE_GAMBLING",
            "OTC_DRUGS",
            "OTHER",
            "PHYSICAL_GAMBLING",
            "PROF_SERVICES",
            "RESTAURANT",
            "RETAIL",
            "TRAVEL",
            "UNDEFINED",
        ]
        | str
        | NotGiven
        | None = NOT_GIVEN,
        websites: Sequence[str] | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change the business profile customers see on WhatsApp (about, address, description, e-mail, up to two websites, category, a JPG or PNG picture); a field left out stays as it is. Answers the number.

        ``PUT /v1/applications/{application}/whatsapp/number/profile``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_NUMBER_UPDATE_PROFILE,
            path={"application": application},
            given={
                "about": about,
                "address": address,
                "description": description,
                "email": email,
                "picture": picture,
                "vertical": vertical,
                "websites": websites,
            },
            params=AccountWhatsAppNumberUpdateProfileParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("picture",),
        )


class AsyncAccountWhatsAppTemplateDrafts:
    """``whatsapp.template_drafts``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def assistant(
        self,
        application: str,
        draft: str,
        *,
        draft_: Mapping[str, Any],
        message: str,
        revision: int,
        retry: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One turn of Tawked's template assistant on a draft: send your message (or `retry: true`) with the draft's state and revision; it writes into the draft and answers what it said (`turns`), the draft and its lint.

        ``POST /v1/applications/{application}/whatsapp/template-drafts/{draft}/assistant``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_ASSISTANT,
            path={"application": application, "draft": draft},
            given={"draft": draft_, "message": message, "revision": revision, "retry": retry},
            params=AccountWhatsAppTemplateDraftsAssistantParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        duplicate: str | NotGiven = NOT_GIVEN,
        source: Literal["assistant", "blank"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a template draft: blank (`source: blank`), for the template assistant (`source: assistant`), or a copy of a template on the number by its name (`duplicate`). Answers the draft with its `revision`.

        ``POST /v1/applications/{application}/whatsapp/template-drafts``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_CREATE,
            path={"application": application},
            given={"duplicate": duplicate, "source": source},
            params=AccountWhatsAppTemplateDraftsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        draft: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a template draft (only Tawked's working copy; nothing on Meta changes); answers ok.

        ``DELETE /v1/applications/{application}/whatsapp/template-drafts/{draft}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_DELETE,
            path={"application": application, "draft": draft},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's template drafts (not yet submitted to Meta), newest change first, each with its languages and variants; filter by name (`q`).

        ``GET /v1/applications/{application}/whatsapp/template-drafts``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
            path={"application": application},
            given={"page": page, "q": q},
            params=AccountWhatsAppTemplateDraftsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
            _PAGE_A_WHATSAPP_TEMPLATE_DRAFTS_LIST,
            path={"application": application},
            given={"page": page, "q": q},
            params=AccountWhatsAppTemplateDraftsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        draft: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One template draft in full: its variants, `revision` (send it back on update and submit), and `lint`, the checks it must pass before Meta sees it (an `error` blocks submit).

        ``GET /v1/applications/{application}/whatsapp/template-drafts/{draft}``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_SHOW,
            path={"application": application, "draft": draft},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def submit(
        self,
        application: str,
        draft: str,
        *,
        revision: int,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        category: str | NotGiven | None = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        otp_type: str | NotGiven | None = NOT_GIVEN,
        package_name: str | NotGiven | None = NOT_GIVEN,
        security_recommendation: bool | NotGiven | None = NOT_GIVEN,
        signature_hash: str | NotGiven | None = NOT_GIVEN,
        variants: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the draft (same body as update) and submit it to Meta, one template per language; answers the templates created (each id and status) and the languages Meta refused, with its words. Then poll whatsapp.templates.show per id.

        ``POST /v1/applications/{application}/whatsapp/template-drafts/{draft}/submit``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_SUBMIT,
            path={"application": application, "draft": draft},
            given={
                "revision": revision,
                "autofill_text": autofill_text,
                "category": category,
                "code_expiry_minutes": code_expiry_minutes,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "name": name,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "variants": variants,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplateDraftsSubmitParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        draft: str,
        *,
        revision: int,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        category: str | NotGiven | None = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        otp_type: str | NotGiven | None = NOT_GIVEN,
        package_name: str | NotGiven | None = NOT_GIVEN,
        security_recommendation: bool | NotGiven | None = NOT_GIVEN,
        signature_hash: str | NotGiven | None = NOT_GIVEN,
        variants: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save a draft's whole state (name, category, variants per language with header, body, footer, buttons, examples) under the `revision` last read; answers the draft with its new revision and its `lint`; once no `lint` error is left, send it to Meta with whatsapp.template_drafts.submit.

        ``PUT /v1/applications/{application}/whatsapp/template-drafts/{draft}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_DRAFTS_UPDATE,
            path={"application": application, "draft": draft},
            given={
                "revision": revision,
                "autofill_text": autofill_text,
                "category": category,
                "code_expiry_minutes": code_expiry_minutes,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "name": name,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "variants": variants,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplateDraftsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppTemplateLibrary:
    """``whatsapp.template_library``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        language: Literal["ar", "en_US"] | str,
        library_name: str,
        name: str,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        library_id: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a template from Meta's library: the library row's name and language, the new template's name, one input per library button in its order (a link's base, a phone number). Answers the new template's id, status and `next` (poll whatsapp.templates.show while it is PENDING).

        ``POST /v1/applications/{application}/whatsapp/template-library``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_LIBRARY_CREATE,
            path={"application": application},
            given={
                "language": language,
                "library_name": library_name,
                "name": name,
                "buttons": buttons,
                "library_id": library_id,
            },
            params=AccountWhatsAppTemplateLibraryCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        industry: Literal["E_COMMERCE", "FINANCIAL_SERVICES"] | str | NotGiven = NOT_GIVEN,
        language: Literal["ar", "en_US"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        topic: Literal["ACCOUNT_UPDATES", "CUSTOMER_FEEDBACK", "ORDER_MANAGEMENT", "PAYMENTS"]
        | str
        | NotGiven = NOT_GIVEN,
        usecase: Literal[
            "ACCOUNT_CREATION_CONFIRMATION",
            "AUTO_PAY_REMINDER",
            "DELIVERY_CONFIRMATION",
            "DELIVERY_FAILED",
            "DELIVERY_UPDATE",
            "FEEDBACK_SURVEY",
            "FRAUD_ALERT",
            "LOW_BALANCE_WARNING",
            "ORDER_ACTION_NEEDED",
            "ORDER_CONFIRMATION",
            "ORDER_DELAY",
            "ORDER_OR_TRANSACTION_CANCEL",
            "ORDER_PICK_UP",
            "PAYMENT_ACTION_REQUIRED",
            "PAYMENT_CONFIRMATION",
            "PAYMENT_DUE_REMINDER",
            "PAYMENT_OVERDUE",
            "PAYMENT_REJECT_FAIL",
            "PAYMENT_SCHEDULED",
            "RECEIPT_ATTACHMENT",
            "RETURN_CONFIRMATION",
            "SHIPMENT_CONFIRMATION",
            "STATEMENT_ATTACHMENT",
            "STATEMENT_AVAILABLE",
            "TRANSACTION_ALERT",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """Browse Meta's template library (ready-made utility templates Meta usually approves at once), filtered by topic, use case, industry, language or words (`q`); each with the name and buttons whatsapp.template_library.create takes.

        ``GET /v1/applications/{application}/whatsapp/template-library``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
            path={"application": application},
            given={
                "industry": industry,
                "language": language,
                "page": page,
                "q": q,
                "topic": topic,
                "usecase": usecase,
            },
            params=AccountWhatsAppTemplateLibraryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        industry: Literal["E_COMMERCE", "FINANCIAL_SERVICES"] | str | NotGiven = NOT_GIVEN,
        language: Literal["ar", "en_US"] | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        topic: Literal["ACCOUNT_UPDATES", "CUSTOMER_FEEDBACK", "ORDER_MANAGEMENT", "PAYMENTS"]
        | str
        | NotGiven = NOT_GIVEN,
        usecase: Literal[
            "ACCOUNT_CREATION_CONFIRMATION",
            "AUTO_PAY_REMINDER",
            "DELIVERY_CONFIRMATION",
            "DELIVERY_FAILED",
            "DELIVERY_UPDATE",
            "FEEDBACK_SURVEY",
            "FRAUD_ALERT",
            "LOW_BALANCE_WARNING",
            "ORDER_ACTION_NEEDED",
            "ORDER_CONFIRMATION",
            "ORDER_DELAY",
            "ORDER_OR_TRANSACTION_CANCEL",
            "ORDER_PICK_UP",
            "PAYMENT_ACTION_REQUIRED",
            "PAYMENT_CONFIRMATION",
            "PAYMENT_DUE_REMINDER",
            "PAYMENT_OVERDUE",
            "PAYMENT_REJECT_FAIL",
            "PAYMENT_SCHEDULED",
            "RECEIPT_ATTACHMENT",
            "RETURN_CONFIRMATION",
            "SHIPMENT_CONFIRMATION",
            "STATEMENT_ATTACHMENT",
            "STATEMENT_AVAILABLE",
            "TRANSACTION_ALERT",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
            _PAGE_A_WHATSAPP_TEMPLATE_LIBRARY_LIST,
            path={"application": application},
            given={
                "industry": industry,
                "language": language,
                "page": page,
                "q": q,
                "topic": topic,
                "usecase": usecase,
            },
            params=AccountWhatsAppTemplateLibraryListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppTemplateSamples:
    """``whatsapp.template_samples``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        image: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload a sample image for a template's IMAGE header (multipart `image`, a JPG or PNG of at most 5 MB); answers its `path`, sent as `header_sample` to whatsapp.templates.create or a draft's variant.

        ``POST /v1/applications/{application}/whatsapp/template-samples``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SAMPLES_CREATE,
            path={"application": application},
            given={"image": image},
            params=AccountWhatsAppTemplateSamplesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("image",),
        )


class AsyncAccountWhatsAppTemplateSuggestions:
    """``whatsapp.template_suggestions``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        analysis: str,
        *,
        keys: Sequence[str],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the picked suggestions of a finished run (`keys`) into drafts and submit them to Meta; answers each one's outcome (submitted, partial or failed, with the templates created). Then poll whatsapp.templates.show per created id.

        ``POST /v1/applications/{application}/whatsapp/template-suggestions/{analysis}/create``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_CREATE,
            path={"application": application, "analysis": analysis},
            given={"keys": keys},
            params=AccountWhatsAppTemplateSuggestionsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def draft(
        self,
        application: str,
        analysis: str,
        key: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make one suggestion of a finished run a template draft (or answer the draft it already has), to edit before submitting; answers the draft.

        ``POST /v1/applications/{application}/whatsapp/template-suggestions/{analysis}/suggestions/{key}/draft``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_DRAFT,
            path={"application": application, "analysis": analysis, "key": key},
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
        """The application's latest run of template suggestions from the business: its status (queued, reading, writing, done, failed), the business profile, and each suggested template with its key, variants and outcome; plus the runs left today.

        ``GET /v1/applications/{application}/whatsapp/template-suggestions``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def start(
        self,
        application: str,
        *,
        description: str | NotGiven | None = NOT_GIVEN,
        website_url: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a run of template suggestions from the business's website (`website_url`) and a short description; answers the run (status queued). Poll whatsapp.template_suggestions.show until it is done.

        ``POST /v1/applications/{application}/whatsapp/template-suggestions``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATE_SUGGESTIONS_START,
            path={"application": application},
            given={"description": description, "website_url": website_url},
            params=AccountWhatsAppTemplateSuggestionsStartParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppTemplates:
    """``whatsapp.templates``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def check(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        name: str,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        header_format: Literal["TEXT", "IMAGE", "DOCUMENT"] | str | NotGiven | None = NOT_GIVEN,
        header_sample: str | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        otp_type: Literal["COPY_CODE", "ONE_TAP", "ZERO_TAP"] | str | NotGiven = NOT_GIVEN,
        package_name: str | NotGiven = NOT_GIVEN,
        security_recommendation: bool | NotGiven = NOT_GIVEN,
        signature_hash: str | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check a proposed template with whatsapp.templates.create's own rules before creating it, saving nothing: answers `ready` (no error blocks it) and every problem once (`level` error or warning, `field`, `code`, and `problem`: what is wrong in words). The body is exactly whatsapp.templates.create's (any category, an IMAGE header with its `header_sample`, AUTHENTICATION with its fields); then call whatsapp.templates.create with it.

        ``POST /v1/applications/{application}/whatsapp/templates/check``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_CHECK,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "name": name,
                "autofill_text": autofill_text,
                "body": body,
                "buttons": buttons,
                "code_expiry_minutes": code_expiry_minutes,
                "examples": examples,
                "footer": footer,
                "header": header,
                "header_format": header_format,
                "header_sample": header_sample,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplatesCheckParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        name: str,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        header_format: Literal["TEXT", "IMAGE", "DOCUMENT"] | str | NotGiven | None = NOT_GIVEN,
        header_sample: str | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        otp_type: Literal["COPY_CODE", "ONE_TAP", "ZERO_TAP"] | str | NotGiven = NOT_GIVEN,
        package_name: str | NotGiven = NOT_GIVEN,
        security_recommendation: bool | NotGiven = NOT_GIVEN,
        signature_hash: str | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a WhatsApp template and submit it to Meta for review; answers its id and status (PENDING until Meta decides). Then poll whatsapp.templates.show with the id until the status is APPROVED or REJECTED.

        ``POST /v1/applications/{application}/whatsapp/templates``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_CREATE,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "name": name,
                "autofill_text": autofill_text,
                "body": body,
                "buttons": buttons,
                "code_expiry_minutes": code_expiry_minutes,
                "examples": examples,
                "footer": footer,
                "header": header,
                "header_format": header_format,
                "header_sample": header_sample,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplatesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete one language of a template on Meta; answers ok with its id, name and language. It stops for every application on the same WhatsApp Business Account: read whatsapp.templates.show's `used_by` first.

        ``DELETE /v1/applications/{application}/whatsapp/templates/{template}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_DELETE,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "APPROVED",
            "PENDING",
            "REJECTED",
            "PAUSED",
            "DISABLED",
            "IN_APPEAL",
            "PENDING_DELETION",
            "LIMIT_EXCEEDED",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the WhatsApp templates on the application's number as Meta holds them, each with its id, status (APPROVED, PENDING, REJECTED…), quality, rejection reason and whether it can be sent; filter by status, category, language or a name (`q`).

        ``GET /v1/applications/{application}/whatsapp/templates``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WHATSAPP_TEMPLATES_LIST,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountWhatsAppTemplatesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str | NotGiven = NOT_GIVEN,
        language: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "APPROVED",
            "PENDING",
            "REJECTED",
            "PAUSED",
            "DISABLED",
            "IN_APPEAL",
            "PENDING_DELETION",
            "LIMIT_EXCEEDED",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WHATSAPP_TEMPLATES_LIST,
            _PAGE_A_WHATSAPP_TEMPLATES_LIST,
            path={"application": application},
            given={
                "category": category,
                "language": language,
                "page": page,
                "q": q,
                "status": status,
            },
            params=AccountWhatsAppTemplatesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def refresh(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop Tawked's cached copy of the number's templates; answers ok. The next whatsapp.templates.list or whatsapp.templates.show reads them from Meta afresh.

        ``POST /v1/applications/{application}/whatsapp/templates/refresh``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_REFRESH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        template: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One WhatsApp template by its Meta id: Meta's status (poll this after a create until APPROVED or REJECTED), quality, rejection reason, whether it can be sent and edited, its parts, what sends it today (campaigns, automations), and `next`: what to do in its status.

        ``GET /v1/applications/{application}/whatsapp/templates/{template}``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_SHOW,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def starter_kit(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Submit Tawked's starter kit (order and shipping updates in Arabic and English) to Meta, skipping names the number already holds; answers how many were created and which failed with Meta's words. Then poll whatsapp.templates.list until Meta approves them.

        ``POST /v1/applications/{application}/whatsapp/templates/starter-kit``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_STARTER_KIT,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def unpause(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Resume a template Meta paused for low quality; answers ok, or Meta's refusal when its pause has not ended.

        ``POST /v1/applications/{application}/whatsapp/templates/{template}/unpause``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_UNPAUSE,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        template: str,
        *,
        category: Literal["UTILITY", "MARKETING", "AUTHENTICATION"] | str,
        language: Literal["ar", "en", "en_US", "en_GB", "ur", "hi", "bn", "tl", "id", "fr"] | str,
        name: str,
        autofill_text: str | NotGiven | None = NOT_GIVEN,
        body: str | NotGiven = NOT_GIVEN,
        buttons: Sequence[Mapping[str, Any]] | NotGiven = NOT_GIVEN,
        code_expiry_minutes: int | NotGiven = NOT_GIVEN,
        examples: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        footer: str | NotGiven | None = NOT_GIVEN,
        header: str | NotGiven | None = NOT_GIVEN,
        header_format: Literal["TEXT", "IMAGE", "DOCUMENT"] | str | NotGiven | None = NOT_GIVEN,
        header_sample: str | NotGiven | None = NOT_GIVEN,
        message_send_ttl_seconds: int | NotGiven | None = NOT_GIVEN,
        otp_type: Literal["COPY_CODE", "ONE_TAP", "ZERO_TAP"] | str | NotGiven = NOT_GIVEN,
        package_name: str | NotGiven = NOT_GIVEN,
        security_recommendation: bool | NotGiven = NOT_GIVEN,
        signature_hash: str | NotGiven = NOT_GIVEN,
        zero_tap_terms_accepted: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Edit a template's content on Meta (its name and language stay); Meta reviews it again. Answers the template's id and status; poll whatsapp.templates.show for Meta's decision.

        ``PATCH /v1/applications/{application}/whatsapp/templates/{template}``, permission ``whatsapp:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_TEMPLATES_UPDATE,
            path={"application": application, "template": template},
            given={
                "category": category,
                "language": language,
                "name": name,
                "autofill_text": autofill_text,
                "body": body,
                "buttons": buttons,
                "code_expiry_minutes": code_expiry_minutes,
                "examples": examples,
                "footer": footer,
                "header": header,
                "header_format": header_format,
                "header_sample": header_sample,
                "message_send_ttl_seconds": message_send_ttl_seconds,
                "otp_type": otp_type,
                "package_name": package_name,
                "security_recommendation": security_recommendation,
                "signature_hash": signature_hash,
                "zero_tap_terms_accepted": zero_tap_terms_accepted,
            },
            params=AccountWhatsAppTemplatesUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsAppUsage:
    """``whatsapp.usage``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        application: str,
        *,
        period: Literal["today", "7d", "month", "30d"] | str | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's WhatsApp template messages for a `period` (today, 7d, month, 30d; Riyadh time) against the same span before: sent, delivered, read, failed, in flight, the delivered and read rates, and Tawked's fees charged (`charged_halalas`, for who sees the money; Meta bills its own charges separately).

        ``GET /v1/applications/{application}/whatsapp/usage``, permission ``whatsapp:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WHATSAPP_USAGE_SHOW,
            path={"application": application},
            given={"period": period},
            params=AccountWhatsAppUsageShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWhatsApp:
    """``whatsapp``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.billing = AsyncAccountWhatsAppBilling(client)
        self.charges = AsyncAccountWhatsAppCharges(client)
        self.connection = AsyncAccountWhatsAppConnection(client)
        self.first_message = AsyncAccountWhatsAppFirstMessage(client)
        self.go_live = AsyncAccountWhatsAppGoLive(client)
        self.messages = AsyncAccountWhatsAppMessages(client)
        self.number = AsyncAccountWhatsAppNumber(client)
        self.template_drafts = AsyncAccountWhatsAppTemplateDrafts(client)
        self.template_library = AsyncAccountWhatsAppTemplateLibrary(client)
        self.template_samples = AsyncAccountWhatsAppTemplateSamples(client)
        self.template_suggestions = AsyncAccountWhatsAppTemplateSuggestions(client)
        self.templates = AsyncAccountWhatsAppTemplates(client)
        self.usage = AsyncAccountWhatsAppUsage(client)
