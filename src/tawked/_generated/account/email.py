"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountEmailAccessRequestParams,
    AccountEmailInboundAddressesStoreParams,
    AccountEmailInboundAddressesUpdateParams,
    AccountEmailLimitRequestParams,
    AccountEmailMessagesListParams,
    AccountEmailMessagesPreviewParams,
    AccountEmailMessagesShowParams,
    AccountEmailReceivedForwardParams,
    AccountEmailReviewRequestParams,
    AccountEmailSendersCreateParams,
    AccountEmailSendersSendTestParams,
    AccountEmailSendersSetMailFromParams,
    AccountEmailSendersTrackingUpdateParams,
    AccountEmailSendersUpdateParams,
    AccountEmailSettingsUpdateParams,
    AccountEmailSuppressionsCreateParams,
    AccountEmailSuppressionsDeleteParams,
    AccountEmailSuppressionsListParams,
    AccountEmailTestAddressConfirmParams,
    AccountEmailTestAddressSendCodeParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_EMAIL_MESSAGES_LIST,
    _PAGE_A_EMAIL_SENDERS_LIST,
    _PAGE_A_EMAIL_SUPPRESSIONS_LIST,
    _PAGE_A_EMAIL_TEMPLATES_LIST,
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


class AccountEmailAccess:
    """``email.access``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def request(
        self,
        application: str,
        *,
        volume: Literal["under_1k", "1k_10k", "10k_50k", "over_50k"] | str,
        domain: str | NotGiven | None = NOT_GIVEN,
        note: str | NotGiven | None = NOT_GIVEN,
        transactional_only: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Tawked's team for early access to Tawked Email (its volume, an optional domain and note, the transactional-only promise); turns the product on for the application when it was off. Answers the access state, `pending` until the team decides, with `next`: read email.access.show every few hours until it is granted.

        ``POST /v1/applications/{application}/email/access``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_ACCESS_REQUEST,
            path={"application": application},
            given={
                "volume": volume,
                "domain": domain,
                "note": note,
                "transactional_only": transactional_only,
            },
            params=AccountEmailAccessRequestParams,
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
        """Where Tawked Email stands on this application: whether the product is on, the account's early access (`none`, `pending`, `granted`, `declined`, `open`) with its latest request, the stage (`locked`, `setup`, `live`), the sending state, a pause and today's limit. Call it first.

        ``GET /v1/applications/{application}/email``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_ACCESS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailInboundAddresses:
    """``email.inbound.addresses``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def check(
        self,
        application: str,
        address: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the address's MX record now (as the console's Check now button does); answers the address with its state and `next`. Poll it every few minutes after adding the record until `state` is active.

        ``POST /v1/applications/{application}/email/inbound-addresses/{address}/check``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_CHECK,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def destroy(
        self,
        application: str,
        address: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a receiving address: email sent to it is refused from then on; its received emails stay until their 30 days end. Answers ok.

        ``DELETE /v1/applications/{application}/email/inbound-addresses/{address}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_DESTROY,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def index(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's receiving addresses: each one's kind (`hosted`, a Tawked address ready at once; `domain`, on a verified sending domain), its domain (every local part at it reaches the application, e.g. orders@ and support@), its state, its hold, today's count and where it forwards.

        ``GET /v1/applications/{application}/email/inbound-addresses``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_INDEX,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        address: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One receiving address: its state, the MX record to add for an address on your domain (`record`), the other MX hosts found, its hold, spam policy, automatic forward, test message and `next`.

        ``GET /v1/applications/{application}/email/inbound-addresses/{address}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_SHOW,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def store(
        self,
        application: str,
        *,
        kind: Literal["hosted", "domain"] | str,
        domain_id: str | NotGiven | None = NOT_GIVEN,
        label: str | NotGiven | None = NOT_GIVEN,
        slug: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a receiving address: `kind` hosted (a Tawked address, `slug` optional: `<slug>.inbound.tawked.com`, ready at once) or domain (`domain_id` a verified sending domain, `label` optional, default inbound: one MX record to add). Answers the address and `next`.

        ``POST /v1/applications/{application}/email/inbound-addresses``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_STORE,
            path={"application": application},
            given={"kind": kind, "domain_id": domain_id, "label": label, "slug": slug},
            params=AccountEmailInboundAddressesStoreParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def test(
        self,
        application: str,
        address: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a free test email from Tawked to the address, to walk the whole path (the MX record, the receiving, the webhook); it shows in email.received.index within a minute. Answers ok and `next`.

        ``POST /v1/applications/{application}/email/inbound-addresses/{address}/test``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_TEST,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        address: str,
        *,
        forward_from_local: str | NotGiven | None = NOT_GIVEN,
        forward_to: str | NotGiven | None = NOT_GIVEN,
        spam_policy: Literal["keep", "drop"] | str | NotGiven = NOT_GIVEN,
        state: Literal["on", "off"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change one thing of a receiving address: `state` on or off, `spam_policy` keep or drop, or its automatic forward (`forward_to` one of your confirmed addresses or any address on a verified domain of the application, `forward_from_local`; `forward_to` null stops it). Answers the address.

        ``PUT /v1/applications/{application}/email/inbound-addresses/{address}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_UPDATE,
            path={"application": application, "address": address},
            given={
                "forward_from_local": forward_from_local,
                "forward_to": forward_to,
                "spam_policy": spam_policy,
                "state": state,
            },
            params=AccountEmailInboundAddressesUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountEmailInbound:
    """``email.inbound``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.addresses = AccountEmailInboundAddresses(client)


class AccountEmailKeys:
    """``email.keys``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make an application key for Tawked Email: `access` `send` (default: `email:send`, send e-mail and read what it sent) or `manage` (`email:manage`: also the domains, the suppression list and the templates on `/v1`), optionally limited to one domain (`domain_id`, sending keys only), `mode` `live` (default) or `test` (sends only to the simulator addresses, nothing delivered, nothing charged); answers the key once, with its id and prefix.

        ``POST /v1/applications/{application}/email/keys``, permission ``email:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_KEYS_CREATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountEmailLimit:
    """``email.limit``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def cancel(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take back the pending request for a higher daily limit; answers the limit page.

        ``DELETE /v1/applications/{application}/email/limit``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_LIMIT_CANCEL,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def request(
        self,
        application: str,
        *,
        requested_limit: int,
        note: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Tawked's team for a higher daily e-mail limit (`requested_limit`, one of the offered choices up to the maximum; a note); answers the limit page with the request `pending` and `next`: read email.limit.show every few hours until the team answers.

        ``POST /v1/applications/{application}/email/limit``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_LIMIT_REQUEST,
            path={"application": application},
            given={"requested_limit": requested_limit, "note": note},
            params=AccountEmailLimitRequestParams,
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
        """The account's daily e-mail limit: today's use against it (each recipient counts), the requests a second (`per_second`; `per_minute` is the same rate a minute), when it resets, whether it refused a send today; this month's free e-mails (`free_allowance`) and the price after them (`price`); the higher limits one may ask for; the latest request with the team's answer; and why a request is not open now (`blocked`, `available_from`).

        ``GET /v1/applications/{application}/email/limit``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_LIMIT_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailMessages:
    """``email.messages``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def cancel(
        self,
        application: str,
        message: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel a scheduled e-mail before its time: it is never sent and what it cost returns to the balance (the month's free e-mails too); answers the message, its `state` then `canceled`.

        ``POST /v1/applications/{application}/email/messages/{message}/cancel``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_MESSAGES_CANCEL,
            path={"application": application, "message": message},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The application's e-mail, newest first: each message's first recipient and how many more (`recipients`, `more`), subject, reference, state (`delivered`, `sent` for on its way, `scheduled`, `canceled`, `bounced`, `failed`), whether it was complained about, whether it was a test, its domain.

        ``GET /v1/applications/{application}/email/messages``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_EMAIL_MESSAGES_LIST,
            path={"application": application},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_EMAIL_MESSAGES_LIST,
            _PAGE_A_EMAIL_MESSAGES_LIST,
            path={"application": application},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def preview(
        self,
        application: str,
        message: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The copy kept of one e-mail: its `subject`, `html` and `text` as sent (a template's rendered output), and `kept_until`. Only when the application keeps previews (email.settings.update) and kept this message.

        ``GET /v1/applications/{application}/email/messages/{message}/preview``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_MESSAGES_PREVIEW,
            path={"application": application, "message": message},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesPreviewParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        message: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One e-mail: its row, the from and reply-to, each recipient with its type and own state (`recipients_list`), its tags, the custom headers' names, the time it waits for (`scheduled_at`), its attachments' names and sizes, each event in order (accepted, sent, delayed, delivered, bounced, complained, failed, canceled), the bounce (type, subtype, the receiving server's words) or the failure code, whether the address is now suppressed, the key that sent it, and the price for who sees the money.

        ``GET /v1/applications/{application}/email/messages/{message}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_MESSAGES_SHOW,
            path={"application": application, "message": message},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailMetrics:
    """``email.metrics``."""

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
        """The application's e-mail figures over Riyadh days: sent, delivered, delayed, bounced (permanent and transient), complained, failed, suppressed, opens and clicks, as totals, rates and one row per day, week (from Sunday) or month; answers `totals`, `rates` and `data`.

        ``GET /v1/applications/{application}/email/metrics``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_METRICS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailReceived:
    """``email.received``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def destroy(
        self,
        application: str,
        received: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a received email: it leaves the log and the API at once, and its stored copy is erased within a day (or at the end of its 30 days when the same email also reached another account); answers ok.

        ``DELETE /v1/applications/{application}/email/received/{received}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_RECEIVED_DESTROY,
            path={"application": application, "received": received},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def forward(
        self,
        application: str,
        received: str,
        *,
        to: Sequence[str],
        from_: str | NotGiven | None = NOT_GIVEN,
        from_name: str | NotGiven | None = NOT_GIVEN,
        note: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Forward a received email with its attachments to 1 to 10 addresses (`to`), from one of the application's verified domains (`from`, else the default), with an optional `note` above it; it is a sent email, charged as one. Answers the new message; poll email.messages.show for its delivery.

        ``POST /v1/applications/{application}/email/received/{received}/forward``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_RECEIVED_FORWARD,
            path={"application": application, "received": received},
            given={"to": to, "from": from_, "from_name": from_name, "note": note},
            params=AccountEmailReceivedForwardParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def index(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The emails the application received on its receiving addresses, newest first: each one's address, envelope recipients (`to`), sender, subject, whether it is spam, its attachments' count, size, `status` (`received` while it is read, `ready`, `failed`) and the sent email it answers (`thread`).

        ``GET /v1/applications/{application}/email/received``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_RECEIVED_INDEX,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        received: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One received email: its row, the envelope sender, the To, Cc and Reply-To, Message-ID and what it replies to (`reply_headers` ready to pass as `headers` when answering), the sender checks (`authentication`), the forward, the bill, when it expires; and its `body` (the text, the HTML, the headers, the attachments with one-hour download links, the raw copy's link) when the person reads received email.

        ``GET /v1/applications/{application}/email/received/{received}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_RECEIVED_SHOW,
            path={"application": application, "received": received},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailReview:
    """``email.review``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def cancel(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take back the pending review request; answers the review page.

        ``DELETE /v1/applications/{application}/email/review``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_REVIEW_CANCEL,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def request(
        self,
        application: str,
        *,
        note: str,
        fixes: Sequence[
            Literal["removed_bounced", "stopped_old_list", "confirm_signup", "other"] | str
        ]
        | NotGiven
        | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Tawked's team to review an automatic pause and resume sending: what was fixed (`fixes`) and a note; answers the review page with the request `pending` and `next`: read email.review.show every few hours until the team answers.

        ``POST /v1/applications/{application}/email/review``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_REVIEW_REQUEST,
            path={"application": application},
            given={"note": note, "fixes": fixes},
            params=AccountEmailReviewRequestParams,
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
        """Why the account's sending is paused (who paused it, when, the last 24 hours' bounce and complaint rates against the lines), the fixes a review request may name, and the latest request with the team's answer.

        ``GET /v1/applications/{application}/email/review``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_REVIEW_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailSendersTracking:
    """``email.senders.tracking``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        application: str,
        domain: str,
        *,
        clicks: bool | NotGiven = NOT_GIVEN,
        label: str | NotGiven | None = NOT_GIVEN,
        opens: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Switch open and click tracking on or off for a verified sender domain (`opens`, `clicks`) and choose its tracking subdomain's label (`label`, `links` by default: links.<domain>); answers `tracking` (state `awaiting_dns`, `awaiting_tls`, `active` or `failing`, and the problem) and the one CNAME `record` to add.

        ``PUT /v1/applications/{application}/email/senders/{domain}/tracking``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_TRACKING_UPDATE,
            path={"application": application, "domain": domain},
            given={"clicks": clicks, "label": label, "opens": opens},
            params=AccountEmailSendersTrackingUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountEmailSenders:
    """``email.senders``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.tracking = AccountEmailSendersTracking(client)

    def cancel_dkim_rotation(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel a DKIM rotation that has not switched (waiting for its new record, or failed): signing stays on the current key, and the new record may be deleted. Answers the domain.

        ``DELETE /v1/applications/{application}/email/senders/{domain}/dkim-rotation``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_CANCEL_DKIM_ROTATION,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def check(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check the domain's DNS records now (as the console's Check now button does); answers the domain with its state, each record's state and `next`, and reads the return path's records (custom MAIL FROM, SPF) and the DMARC record again into `authentication`. Poll it every one to two minutes after adding the records until `state` is verified; it is the one way to read DMARC anew.

        ``POST /v1/applications/{application}/email/senders/{domain}/check``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_CHECK,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def connect(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """A link the person opens to add the domain's DNS record at their DNS host automatically (Domain Connect, e.g. Cloudflare): they sign in at the host and approve, then return to the domain's page in the console. Answers `url`, the `human_action` to relay and `next`: once the person says it is done, poll `email.senders.check`.

        ``POST /v1/applications/{application}/email/senders/{domain}/connect``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_CONNECT,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        domain: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a sending domain (e.g. shop.example.com) to the application; answers the domain with the DNS records to add at its DNS host and `next`. Add them (with the host's own tools or API), then poll `email.senders.check` every one to two minutes until `state` is `verified`.

        ``POST /v1/applications/{application}/email/senders``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_CREATE,
            path={"application": application},
            given={"domain": domain},
            params=AccountEmailSendersCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a sender domain from the application: its sends stop at once (its messages stay in the log); answers ok.

        ``DELETE /v1/applications/{application}/email/senders/{domain}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_DELETE,
            path={"application": application, "domain": domain},
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
        """The application's sender domains, newest first, each with its state (`pending`, `verified`, `failed`), the DNS records to add and their state, the DNS host when known, the default from address and the messages of the last 30 days.

        ``GET /v1/applications/{application}/email/senders``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_EMAIL_SENDERS_LIST,
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
            _E.A_EMAIL_SENDERS_LIST,
            _PAGE_A_EMAIL_SENDERS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def retry_dkim_rotation(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Try a failed DKIM rotation again once its new record is in place at the DNS host: answers the domain with the rotation publishing again.

        ``POST /v1/applications/{application}/email/senders/{domain}/dkim-rotation/retry``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_RETRY_DKIM_ROTATION,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def rotate_dkim(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start rotating a verified domain's DKIM key: answers the domain with `authentication.dkim.rotation.new_record`, a second TXT record to add beside the current one. Tawked switches signing to it by itself once it reads it, then the old record is deleted at the DNS host (`old_record`).

        ``POST /v1/applications/{application}/email/senders/{domain}/dkim-rotation``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_ROTATE_DKIM,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send_test(
        self,
        application: str,
        domain: str,
        *,
        to: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a free test e-mail from a verified domain to one of the person's own confirmed addresses (`to`, one of `email.test_address.show`'s `recipients`); answers the message; poll `email.messages.show` for its delivery.

        ``POST /v1/applications/{application}/email/senders/{domain}/test``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_SEND_TEST,
            path={"application": application, "domain": domain},
            given={"to": to},
            params=AccountEmailSendersSendTestParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def set_mail_from(
        self,
        application: str,
        domain: str,
        *,
        label: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Name the domain's return path (custom MAIL FROM, `label` before the domain: `send` makes send.example.com) or turn it on again with its label; answers the domain with `authentication.mail_from` and its two records (an MX and an SPF TXT) to add at the DNS host. Optional: it makes SPF align with the domain and never affects verification or sending.

        ``PUT /v1/applications/{application}/email/senders/{domain}/mail-from``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_SET_MAIL_FROM,
            path={"application": application, "domain": domain},
            given={"label": label},
            params=AccountEmailSendersSetMailFromParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        domain: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One sender domain: its state, the DNS records to add at its host (name, value, the host's Name field, each record's state), how long a pending domain still waits, the default from address and its messages of the last 30 days, day by day; and its `authentication`: the DKIM key and its rotation (`dkim.rotation.state`), the return path (custom MAIL FROM, SPF alignment) with its records, the DMARC record and policy as last read, and the Feedback-IDs.

        ``GET /v1/applications/{application}/email/senders/{domain}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_SHOW,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def unset_mail_from(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the domain's return path off: its mail goes out with the default return path again (SPF no longer aligns with the domain); the label is kept for email.senders.set_mail_from. Answers the domain.

        ``DELETE /v1/applications/{application}/email/senders/{domain}/mail-from``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_UNSET_MAIL_FROM,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        domain: str,
        *,
        from_local: str,
        from_name: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set a verified domain's defaults: the name a message is from (`from_name`, may be empty) and the part before the @ (`from_local`, e.g. no-reply) used when a send names no `from`; answers the domain.

        ``PUT /v1/applications/{application}/email/senders/{domain}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SENDERS_UPDATE,
            path={"application": application, "domain": domain},
            given={"from_local": from_local, "from_name": from_name},
            params=AccountEmailSendersUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountEmailSettings:
    """``email.settings``."""

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
        """The application's Email settings: `keep_previews`, whether a copy (subject, HTML, text) of each message sent from now on is kept for its 30 days, and when and by whom it last changed.

        ``GET /v1/applications/{application}/email/settings``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_SETTINGS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        *,
        keep_previews: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn on or off keeping a copy of each message (`keep_previews`); answers the settings. On, every message sent from then on keeps its subject, HTML and text for its 30 days, read with email.messages.preview; off, every copy is deleted at once.

        ``PUT /v1/applications/{application}/email/settings``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SETTINGS_UPDATE,
            path={"application": application},
            given={"keep_previews": keep_previews},
            params=AccountEmailSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountEmailSuppressions:
    """``email.suppressions``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        addresses: Sequence[str],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Put up to 1,000 addresses on the account's suppressed list, for this application: no application of the account sends e-mail to them; answers how many were added, already there, and which were not valid.

        ``POST /v1/applications/{application}/email/suppressions``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_SUPPRESSIONS_CREATE,
            path={"application": application},
            given={"addresses": addresses},
            params=AccountEmailSuppressionsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        suppression: str,
        *,
        note: str | NotGiven | None = NOT_GIVEN,
        reason: Literal["recipient_asked", "reported_by_mistake", "other"]
        | str
        | NotGiven
        | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Lift an address off the suppressed list: e-mail can reach it again; a complaint needs a reason; answers ok.

        ``DELETE /v1/applications/{application}/email/suppressions/{suppression}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_SUPPRESSIONS_DELETE,
            path={"application": application, "suppression": suppression},
            given={"note": note, "reason": reason},
            params=AccountEmailSuppressionsDeleteParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal["bounce", "complaint", "manual"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The addresses the account no longer sends e-mail to, newest first: why (`bounce`, `complaint`, `manual`), where from (`source`), since when, whether and how it may be lifted, and the message that caused it.

        ``GET /v1/applications/{application}/email/suppressions``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_EMAIL_SUPPRESSIONS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "reason": reason},
            params=AccountEmailSuppressionsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal["bounce", "complaint", "manual"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_EMAIL_SUPPRESSIONS_LIST,
            _PAGE_A_EMAIL_SUPPRESSIONS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "reason": reason},
            params=AccountEmailSuppressionsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailTemplates:
    """``email.templates``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a hosted e-mail template (a draft; `publish: true` publishes it at once); answers the template with its problems; send by it with `template: {id or alias, variables}` on a message once published.

        ``POST /v1/applications/{application}/email/templates``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_CREATE,
            path={"application": application},
            given={},
            params=None,
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
        """Delete a hosted e-mail template: sends by its id or alias are refused from now on (422 template_not_found) and its alias is free again; answers ok.

        ``DELETE /v1/applications/{application}/email/templates/{template}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_DELETE,
            path={"application": application, "template": template},
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
        """The application's hosted e-mail templates, last changed first: each one's id, alias, name, state and its published and draft versions without their bodies; read one with email.templates.show.

        ``GET /v1/applications/{application}/email/templates``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_EMAIL_TEMPLATES_LIST,
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
            _E.A_EMAIL_TEMPLATES_LIST,
            _PAGE_A_EMAIL_TEMPLATES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def publish(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Publish a template's draft as its next numbered version: sends by the template use it from now on; answers the template.

        ``POST /v1/applications/{application}/email/templates/{template}/publish``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_PUBLISH,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def restore(
        self,
        application: str,
        template: str,
        number: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Copy a published version of a template into its draft (the published version keeps sending until the draft is published); answers the template.

        ``POST /v1/applications/{application}/email/templates/{template}/versions/{number}/restore``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_RESTORE,
            path={"application": application, "template": template, "number": number},
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
        """One hosted e-mail template by its id or alias, with its published version and its draft in full and each one's problems.

        ``GET /v1/applications/{application}/email/templates/{template}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_SHOW,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def test(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a template's draft (or its published version when no draft waits) as a free test to one of the person's own confirmed addresses; answers the message; poll email.messages.show for its delivery.

        ``POST /v1/applications/{application}/email/templates/{template}/test``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_TEST,
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a template's name or alias, or its draft (made from the published version when none waits); the published version keeps sending until the draft is published; answers the template.

        ``PATCH /v1/applications/{application}/email/templates/{template}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_UPDATE,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def versions(
        self,
        application: str,
        template: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """A template's published versions, newest first: number, state (`published` or `superseded`), subject, when published; restore one into the draft with email.templates.restore.

        ``GET /v1/applications/{application}/email/templates/{template}/versions``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEMPLATES_VERSIONS,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmailTestAddress:
    """``email.test_address``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def confirm(
        self,
        application: str,
        *,
        code: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm the waiting address with the six-digit code the person received (`code`); it becomes the person's own confirmed e-mail and a test recipient. Answers the recipients.

        ``POST /v1/applications/{application}/email/test-address/confirm``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_CONFIRM,
            path={"application": application},
            given={"code": code},
            params=AccountEmailTestAddressConfirmParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def forget(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop the address waiting for its code (to type another); answers ok.

        ``DELETE /v1/applications/{application}/email/test-address/pending``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_FORGET,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send_code(
        self,
        application: str,
        *,
        email: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a six-digit code to an address the person owns (`email`), so it can receive test e-mails once confirmed; answers the address waiting for its code and when a new code may be asked for.

        ``POST /v1/applications/{application}/email/test-address/send``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_SEND_CODE,
            path={"application": application},
            given={"email": email},
            params=AccountEmailTestAddressSendCodeParams,
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
        """The addresses a test e-mail may go to for this person (`recipients`: the account's notification e-mail, the person's confirmed e-mail, the account's confirmed business e-mail), and the address waiting for its code, if any.

        ``GET /v1/applications/{application}/email/test-address``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountEmail:
    """``email``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.access = AccountEmailAccess(client)
        self.inbound = AccountEmailInbound(client)
        self.keys = AccountEmailKeys(client)
        self.limit = AccountEmailLimit(client)
        self.messages = AccountEmailMessages(client)
        self.metrics = AccountEmailMetrics(client)
        self.received = AccountEmailReceived(client)
        self.review = AccountEmailReview(client)
        self.senders = AccountEmailSenders(client)
        self.settings = AccountEmailSettings(client)
        self.suppressions = AccountEmailSuppressions(client)
        self.templates = AccountEmailTemplates(client)
        self.test_address = AccountEmailTestAddress(client)


class AsyncAccountEmailAccess:
    """``email.access``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def request(
        self,
        application: str,
        *,
        volume: Literal["under_1k", "1k_10k", "10k_50k", "over_50k"] | str,
        domain: str | NotGiven | None = NOT_GIVEN,
        note: str | NotGiven | None = NOT_GIVEN,
        transactional_only: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Tawked's team for early access to Tawked Email (its volume, an optional domain and note, the transactional-only promise); turns the product on for the application when it was off. Answers the access state, `pending` until the team decides, with `next`: read email.access.show every few hours until it is granted.

        ``POST /v1/applications/{application}/email/access``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_ACCESS_REQUEST,
            path={"application": application},
            given={
                "volume": volume,
                "domain": domain,
                "note": note,
                "transactional_only": transactional_only,
            },
            params=AccountEmailAccessRequestParams,
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
        """Where Tawked Email stands on this application: whether the product is on, the account's early access (`none`, `pending`, `granted`, `declined`, `open`) with its latest request, the stage (`locked`, `setup`, `live`), the sending state, a pause and today's limit. Call it first.

        ``GET /v1/applications/{application}/email``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_ACCESS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailInboundAddresses:
    """``email.inbound.addresses``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def check(
        self,
        application: str,
        address: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the address's MX record now (as the console's Check now button does); answers the address with its state and `next`. Poll it every few minutes after adding the record until `state` is active.

        ``POST /v1/applications/{application}/email/inbound-addresses/{address}/check``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_CHECK,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def destroy(
        self,
        application: str,
        address: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a receiving address: email sent to it is refused from then on; its received emails stay until their 30 days end. Answers ok.

        ``DELETE /v1/applications/{application}/email/inbound-addresses/{address}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_DESTROY,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def index(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The application's receiving addresses: each one's kind (`hosted`, a Tawked address ready at once; `domain`, on a verified sending domain), its domain (every local part at it reaches the application, e.g. orders@ and support@), its state, its hold, today's count and where it forwards.

        ``GET /v1/applications/{application}/email/inbound-addresses``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_INDEX,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        address: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One receiving address: its state, the MX record to add for an address on your domain (`record`), the other MX hosts found, its hold, spam policy, automatic forward, test message and `next`.

        ``GET /v1/applications/{application}/email/inbound-addresses/{address}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_SHOW,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def store(
        self,
        application: str,
        *,
        kind: Literal["hosted", "domain"] | str,
        domain_id: str | NotGiven | None = NOT_GIVEN,
        label: str | NotGiven | None = NOT_GIVEN,
        slug: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a receiving address: `kind` hosted (a Tawked address, `slug` optional: `<slug>.inbound.tawked.com`, ready at once) or domain (`domain_id` a verified sending domain, `label` optional, default inbound: one MX record to add). Answers the address and `next`.

        ``POST /v1/applications/{application}/email/inbound-addresses``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_STORE,
            path={"application": application},
            given={"kind": kind, "domain_id": domain_id, "label": label, "slug": slug},
            params=AccountEmailInboundAddressesStoreParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def test(
        self,
        application: str,
        address: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a free test email from Tawked to the address, to walk the whole path (the MX record, the receiving, the webhook); it shows in email.received.index within a minute. Answers ok and `next`.

        ``POST /v1/applications/{application}/email/inbound-addresses/{address}/test``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_TEST,
            path={"application": application, "address": address},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        address: str,
        *,
        forward_from_local: str | NotGiven | None = NOT_GIVEN,
        forward_to: str | NotGiven | None = NOT_GIVEN,
        spam_policy: Literal["keep", "drop"] | str | NotGiven = NOT_GIVEN,
        state: Literal["on", "off"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change one thing of a receiving address: `state` on or off, `spam_policy` keep or drop, or its automatic forward (`forward_to` one of your confirmed addresses or any address on a verified domain of the application, `forward_from_local`; `forward_to` null stops it). Answers the address.

        ``PUT /v1/applications/{application}/email/inbound-addresses/{address}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_INBOUND_ADDRESSES_UPDATE,
            path={"application": application, "address": address},
            given={
                "forward_from_local": forward_from_local,
                "forward_to": forward_to,
                "spam_policy": spam_policy,
                "state": state,
            },
            params=AccountEmailInboundAddressesUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailInbound:
    """``email.inbound``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.addresses = AsyncAccountEmailInboundAddresses(client)


class AsyncAccountEmailKeys:
    """``email.keys``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Make an application key for Tawked Email: `access` `send` (default: `email:send`, send e-mail and read what it sent) or `manage` (`email:manage`: also the domains, the suppression list and the templates on `/v1`), optionally limited to one domain (`domain_id`, sending keys only), `mode` `live` (default) or `test` (sends only to the simulator addresses, nothing delivered, nothing charged); answers the key once, with its id and prefix.

        ``POST /v1/applications/{application}/email/keys``, permission ``email:write``.
        Never retried once sent.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_KEYS_CREATE,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailLimit:
    """``email.limit``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def cancel(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take back the pending request for a higher daily limit; answers the limit page.

        ``DELETE /v1/applications/{application}/email/limit``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_LIMIT_CANCEL,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def request(
        self,
        application: str,
        *,
        requested_limit: int,
        note: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Tawked's team for a higher daily e-mail limit (`requested_limit`, one of the offered choices up to the maximum; a note); answers the limit page with the request `pending` and `next`: read email.limit.show every few hours until the team answers.

        ``POST /v1/applications/{application}/email/limit``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_LIMIT_REQUEST,
            path={"application": application},
            given={"requested_limit": requested_limit, "note": note},
            params=AccountEmailLimitRequestParams,
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
        """The account's daily e-mail limit: today's use against it (each recipient counts), the requests a second (`per_second`; `per_minute` is the same rate a minute), when it resets, whether it refused a send today; this month's free e-mails (`free_allowance`) and the price after them (`price`); the higher limits one may ask for; the latest request with the team's answer; and why a request is not open now (`blocked`, `available_from`).

        ``GET /v1/applications/{application}/email/limit``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_LIMIT_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailMessages:
    """``email.messages``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def cancel(
        self,
        application: str,
        message: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel a scheduled e-mail before its time: it is never sent and what it cost returns to the balance (the month's free e-mails too); answers the message, its `state` then `canceled`.

        ``POST /v1/applications/{application}/email/messages/{message}/cancel``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_MESSAGES_CANCEL,
            path={"application": application, "message": message},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The application's e-mail, newest first: each message's first recipient and how many more (`recipients`, `more`), subject, reference, state (`delivered`, `sent` for on its way, `scheduled`, `canceled`, `bounced`, `failed`), whether it was complained about, whether it was a test, its domain.

        ``GET /v1/applications/{application}/email/messages``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_EMAIL_MESSAGES_LIST,
            path={"application": application},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_EMAIL_MESSAGES_LIST,
            _PAGE_A_EMAIL_MESSAGES_LIST,
            path={"application": application},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def preview(
        self,
        application: str,
        message: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The copy kept of one e-mail: its `subject`, `html` and `text` as sent (a template's rendered output), and `kept_until`. Only when the application keeps previews (email.settings.update) and kept this message.

        ``GET /v1/applications/{application}/email/messages/{message}/preview``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_MESSAGES_PREVIEW,
            path={"application": application, "message": message},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesPreviewParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        message: str,
        *,
        domain: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal[
            "delivered", "sent", "scheduled", "undelivered", "complained", "bounced", "failed"
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One e-mail: its row, the from and reply-to, each recipient with its type and own state (`recipients_list`), its tags, the custom headers' names, the time it waits for (`scheduled_at`), its attachments' names and sizes, each event in order (accepted, sent, delayed, delivered, bounced, complained, failed, canceled), the bounce (type, subtype, the receiving server's words) or the failure code, whether the address is now suppressed, the key that sent it, and the price for who sees the money.

        ``GET /v1/applications/{application}/email/messages/{message}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_MESSAGES_SHOW,
            path={"application": application, "message": message},
            given={"domain": domain, "page": page, "q": q, "status": status},
            params=AccountEmailMessagesShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailMetrics:
    """``email.metrics``."""

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
        """The application's e-mail figures over Riyadh days: sent, delivered, delayed, bounced (permanent and transient), complained, failed, suppressed, opens and clicks, as totals, rates and one row per day, week (from Sunday) or month; answers `totals`, `rates` and `data`.

        ``GET /v1/applications/{application}/email/metrics``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_METRICS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailReceived:
    """``email.received``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def destroy(
        self,
        application: str,
        received: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a received email: it leaves the log and the API at once, and its stored copy is erased within a day (or at the end of its 30 days when the same email also reached another account); answers ok.

        ``DELETE /v1/applications/{application}/email/received/{received}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_RECEIVED_DESTROY,
            path={"application": application, "received": received},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def forward(
        self,
        application: str,
        received: str,
        *,
        to: Sequence[str],
        from_: str | NotGiven | None = NOT_GIVEN,
        from_name: str | NotGiven | None = NOT_GIVEN,
        note: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Forward a received email with its attachments to 1 to 10 addresses (`to`), from one of the application's verified domains (`from`, else the default), with an optional `note` above it; it is a sent email, charged as one. Answers the new message; poll email.messages.show for its delivery.

        ``POST /v1/applications/{application}/email/received/{received}/forward``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_RECEIVED_FORWARD,
            path={"application": application, "received": received},
            given={"to": to, "from": from_, "from_name": from_name, "note": note},
            params=AccountEmailReceivedForwardParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def index(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The emails the application received on its receiving addresses, newest first: each one's address, envelope recipients (`to`), sender, subject, whether it is spam, its attachments' count, size, `status` (`received` while it is read, `ready`, `failed`) and the sent email it answers (`thread`).

        ``GET /v1/applications/{application}/email/received``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_RECEIVED_INDEX,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        received: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One received email: its row, the envelope sender, the To, Cc and Reply-To, Message-ID and what it replies to (`reply_headers` ready to pass as `headers` when answering), the sender checks (`authentication`), the forward, the bill, when it expires; and its `body` (the text, the HTML, the headers, the attachments with one-hour download links, the raw copy's link) when the person reads received email.

        ``GET /v1/applications/{application}/email/received/{received}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_RECEIVED_SHOW,
            path={"application": application, "received": received},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailReview:
    """``email.review``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def cancel(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Take back the pending review request; answers the review page.

        ``DELETE /v1/applications/{application}/email/review``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_REVIEW_CANCEL,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def request(
        self,
        application: str,
        *,
        note: str,
        fixes: Sequence[
            Literal["removed_bounced", "stopped_old_list", "confirm_signup", "other"] | str
        ]
        | NotGiven
        | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask Tawked's team to review an automatic pause and resume sending: what was fixed (`fixes`) and a note; answers the review page with the request `pending` and `next`: read email.review.show every few hours until the team answers.

        ``POST /v1/applications/{application}/email/review``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_REVIEW_REQUEST,
            path={"application": application},
            given={"note": note, "fixes": fixes},
            params=AccountEmailReviewRequestParams,
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
        """Why the account's sending is paused (who paused it, when, the last 24 hours' bounce and complaint rates against the lines), the fixes a review request may name, and the latest request with the team's answer.

        ``GET /v1/applications/{application}/email/review``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_REVIEW_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailSendersTracking:
    """``email.senders.tracking``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        application: str,
        domain: str,
        *,
        clicks: bool | NotGiven = NOT_GIVEN,
        label: str | NotGiven | None = NOT_GIVEN,
        opens: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Switch open and click tracking on or off for a verified sender domain (`opens`, `clicks`) and choose its tracking subdomain's label (`label`, `links` by default: links.<domain>); answers `tracking` (state `awaiting_dns`, `awaiting_tls`, `active` or `failing`, and the problem) and the one CNAME `record` to add.

        ``PUT /v1/applications/{application}/email/senders/{domain}/tracking``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_TRACKING_UPDATE,
            path={"application": application, "domain": domain},
            given={"clicks": clicks, "label": label, "opens": opens},
            params=AccountEmailSendersTrackingUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailSenders:
    """``email.senders``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.tracking = AsyncAccountEmailSendersTracking(client)

    async def cancel_dkim_rotation(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel a DKIM rotation that has not switched (waiting for its new record, or failed): signing stays on the current key, and the new record may be deleted. Answers the domain.

        ``DELETE /v1/applications/{application}/email/senders/{domain}/dkim-rotation``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_CANCEL_DKIM_ROTATION,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def check(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Check the domain's DNS records now (as the console's Check now button does); answers the domain with its state, each record's state and `next`, and reads the return path's records (custom MAIL FROM, SPF) and the DMARC record again into `authentication`. Poll it every one to two minutes after adding the records until `state` is verified; it is the one way to read DMARC anew.

        ``POST /v1/applications/{application}/email/senders/{domain}/check``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_CHECK,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def connect(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """A link the person opens to add the domain's DNS record at their DNS host automatically (Domain Connect, e.g. Cloudflare): they sign in at the host and approve, then return to the domain's page in the console. Answers `url`, the `human_action` to relay and `next`: once the person says it is done, poll `email.senders.check`.

        ``POST /v1/applications/{application}/email/senders/{domain}/connect``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_CONNECT,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        domain: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a sending domain (e.g. shop.example.com) to the application; answers the domain with the DNS records to add at its DNS host and `next`. Add them (with the host's own tools or API), then poll `email.senders.check` every one to two minutes until `state` is `verified`.

        ``POST /v1/applications/{application}/email/senders``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_CREATE,
            path={"application": application},
            given={"domain": domain},
            params=AccountEmailSendersCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a sender domain from the application: its sends stop at once (its messages stay in the log); answers ok.

        ``DELETE /v1/applications/{application}/email/senders/{domain}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_DELETE,
            path={"application": application, "domain": domain},
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
        """The application's sender domains, newest first, each with its state (`pending`, `verified`, `failed`), the DNS records to add and their state, the DNS host when known, the default from address and the messages of the last 30 days.

        ``GET /v1/applications/{application}/email/senders``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_EMAIL_SENDERS_LIST,
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
            _E.A_EMAIL_SENDERS_LIST,
            _PAGE_A_EMAIL_SENDERS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def retry_dkim_rotation(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Try a failed DKIM rotation again once its new record is in place at the DNS host: answers the domain with the rotation publishing again.

        ``POST /v1/applications/{application}/email/senders/{domain}/dkim-rotation/retry``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_RETRY_DKIM_ROTATION,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def rotate_dkim(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start rotating a verified domain's DKIM key: answers the domain with `authentication.dkim.rotation.new_record`, a second TXT record to add beside the current one. Tawked switches signing to it by itself once it reads it, then the old record is deleted at the DNS host (`old_record`).

        ``POST /v1/applications/{application}/email/senders/{domain}/dkim-rotation``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_ROTATE_DKIM,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send_test(
        self,
        application: str,
        domain: str,
        *,
        to: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a free test e-mail from a verified domain to one of the person's own confirmed addresses (`to`, one of `email.test_address.show`'s `recipients`); answers the message; poll `email.messages.show` for its delivery.

        ``POST /v1/applications/{application}/email/senders/{domain}/test``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_SEND_TEST,
            path={"application": application, "domain": domain},
            given={"to": to},
            params=AccountEmailSendersSendTestParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def set_mail_from(
        self,
        application: str,
        domain: str,
        *,
        label: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Name the domain's return path (custom MAIL FROM, `label` before the domain: `send` makes send.example.com) or turn it on again with its label; answers the domain with `authentication.mail_from` and its two records (an MX and an SPF TXT) to add at the DNS host. Optional: it makes SPF align with the domain and never affects verification or sending.

        ``PUT /v1/applications/{application}/email/senders/{domain}/mail-from``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_SET_MAIL_FROM,
            path={"application": application, "domain": domain},
            given={"label": label},
            params=AccountEmailSendersSetMailFromParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        domain: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One sender domain: its state, the DNS records to add at its host (name, value, the host's Name field, each record's state), how long a pending domain still waits, the default from address and its messages of the last 30 days, day by day; and its `authentication`: the DKIM key and its rotation (`dkim.rotation.state`), the return path (custom MAIL FROM, SPF alignment) with its records, the DMARC record and policy as last read, and the Feedback-IDs.

        ``GET /v1/applications/{application}/email/senders/{domain}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_SHOW,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def unset_mail_from(
        self,
        application: str,
        domain: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the domain's return path off: its mail goes out with the default return path again (SPF no longer aligns with the domain); the label is kept for email.senders.set_mail_from. Answers the domain.

        ``DELETE /v1/applications/{application}/email/senders/{domain}/mail-from``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_UNSET_MAIL_FROM,
            path={"application": application, "domain": domain},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        domain: str,
        *,
        from_local: str,
        from_name: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set a verified domain's defaults: the name a message is from (`from_name`, may be empty) and the part before the @ (`from_local`, e.g. no-reply) used when a send names no `from`; answers the domain.

        ``PUT /v1/applications/{application}/email/senders/{domain}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SENDERS_UPDATE,
            path={"application": application, "domain": domain},
            given={"from_local": from_local, "from_name": from_name},
            params=AccountEmailSendersUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailSettings:
    """``email.settings``."""

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
        """The application's Email settings: `keep_previews`, whether a copy (subject, HTML, text) of each message sent from now on is kept for its 30 days, and when and by whom it last changed.

        ``GET /v1/applications/{application}/email/settings``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SETTINGS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        *,
        keep_previews: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn on or off keeping a copy of each message (`keep_previews`); answers the settings. On, every message sent from then on keeps its subject, HTML and text for its 30 days, read with email.messages.preview; off, every copy is deleted at once.

        ``PUT /v1/applications/{application}/email/settings``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SETTINGS_UPDATE,
            path={"application": application},
            given={"keep_previews": keep_previews},
            params=AccountEmailSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailSuppressions:
    """``email.suppressions``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        addresses: Sequence[str],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Put up to 1,000 addresses on the account's suppressed list, for this application: no application of the account sends e-mail to them; answers how many were added, already there, and which were not valid.

        ``POST /v1/applications/{application}/email/suppressions``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SUPPRESSIONS_CREATE,
            path={"application": application},
            given={"addresses": addresses},
            params=AccountEmailSuppressionsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        suppression: str,
        *,
        note: str | NotGiven | None = NOT_GIVEN,
        reason: Literal["recipient_asked", "reported_by_mistake", "other"]
        | str
        | NotGiven
        | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Lift an address off the suppressed list: e-mail can reach it again; a complaint needs a reason; answers ok.

        ``DELETE /v1/applications/{application}/email/suppressions/{suppression}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_SUPPRESSIONS_DELETE,
            path={"application": application, "suppression": suppression},
            given={"note": note, "reason": reason},
            params=AccountEmailSuppressionsDeleteParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal["bounce", "complaint", "manual"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The addresses the account no longer sends e-mail to, newest first: why (`bounce`, `complaint`, `manual`), where from (`source`), since when, whether and how it may be lifted, and the message that caused it.

        ``GET /v1/applications/{application}/email/suppressions``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_EMAIL_SUPPRESSIONS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "reason": reason},
            params=AccountEmailSuppressionsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal["bounce", "complaint", "manual"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_EMAIL_SUPPRESSIONS_LIST,
            _PAGE_A_EMAIL_SUPPRESSIONS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "reason": reason},
            params=AccountEmailSuppressionsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailTemplates:
    """``email.templates``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create a hosted e-mail template (a draft; `publish: true` publishes it at once); answers the template with its problems; send by it with `template: {id or alias, variables}` on a message once published.

        ``POST /v1/applications/{application}/email/templates``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_CREATE,
            path={"application": application},
            given={},
            params=None,
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
        """Delete a hosted e-mail template: sends by its id or alias are refused from now on (422 template_not_found) and its alias is free again; answers ok.

        ``DELETE /v1/applications/{application}/email/templates/{template}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_DELETE,
            path={"application": application, "template": template},
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
        """The application's hosted e-mail templates, last changed first: each one's id, alias, name, state and its published and draft versions without their bodies; read one with email.templates.show.

        ``GET /v1/applications/{application}/email/templates``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_EMAIL_TEMPLATES_LIST,
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
            _E.A_EMAIL_TEMPLATES_LIST,
            _PAGE_A_EMAIL_TEMPLATES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def publish(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Publish a template's draft as its next numbered version: sends by the template use it from now on; answers the template.

        ``POST /v1/applications/{application}/email/templates/{template}/publish``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_PUBLISH,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def restore(
        self,
        application: str,
        template: str,
        number: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Copy a published version of a template into its draft (the published version keeps sending until the draft is published); answers the template.

        ``POST /v1/applications/{application}/email/templates/{template}/versions/{number}/restore``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_RESTORE,
            path={"application": application, "template": template, "number": number},
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
        """One hosted e-mail template by its id or alias, with its published version and its draft in full and each one's problems.

        ``GET /v1/applications/{application}/email/templates/{template}``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_SHOW,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def test(
        self,
        application: str,
        template: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a template's draft (or its published version when no draft waits) as a free test to one of the person's own confirmed addresses; answers the message; poll email.messages.show for its delivery.

        ``POST /v1/applications/{application}/email/templates/{template}/test``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_TEST,
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
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a template's name or alias, or its draft (made from the published version when none waits); the published version keeps sending until the draft is published; answers the template.

        ``PATCH /v1/applications/{application}/email/templates/{template}``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_UPDATE,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def versions(
        self,
        application: str,
        template: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """A template's published versions, newest first: number, state (`published` or `superseded`), subject, when published; restore one into the draft with email.templates.restore.

        ``GET /v1/applications/{application}/email/templates/{template}/versions``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEMPLATES_VERSIONS,
            path={"application": application, "template": template},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmailTestAddress:
    """``email.test_address``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def confirm(
        self,
        application: str,
        *,
        code: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm the waiting address with the six-digit code the person received (`code`); it becomes the person's own confirmed e-mail and a test recipient. Answers the recipients.

        ``POST /v1/applications/{application}/email/test-address/confirm``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_CONFIRM,
            path={"application": application},
            given={"code": code},
            params=AccountEmailTestAddressConfirmParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def forget(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Drop the address waiting for its code (to type another); answers ok.

        ``DELETE /v1/applications/{application}/email/test-address/pending``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_FORGET,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send_code(
        self,
        application: str,
        *,
        email: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a six-digit code to an address the person owns (`email`), so it can receive test e-mails once confirmed; answers the address waiting for its code and when a new code may be asked for.

        ``POST /v1/applications/{application}/email/test-address/send``, permission ``email:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_SEND_CODE,
            path={"application": application},
            given={"email": email},
            params=AccountEmailTestAddressSendCodeParams,
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
        """The addresses a test e-mail may go to for this person (`recipients`: the account's notification e-mail, the person's confirmed e-mail, the account's confirmed business e-mail), and the address waiting for its code, if any.

        ``GET /v1/applications/{application}/email/test-address``, permission ``email:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_EMAIL_TEST_ADDRESS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountEmail:
    """``email``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.access = AsyncAccountEmailAccess(client)
        self.inbound = AsyncAccountEmailInbound(client)
        self.keys = AsyncAccountEmailKeys(client)
        self.limit = AsyncAccountEmailLimit(client)
        self.messages = AsyncAccountEmailMessages(client)
        self.metrics = AsyncAccountEmailMetrics(client)
        self.received = AsyncAccountEmailReceived(client)
        self.review = AsyncAccountEmailReview(client)
        self.senders = AsyncAccountEmailSenders(client)
        self.settings = AsyncAccountEmailSettings(client)
        self.suppressions = AsyncAccountEmailSuppressions(client)
        self.templates = AsyncAccountEmailTemplates(client)
        self.test_address = AsyncAccountEmailTestAddress(client)
