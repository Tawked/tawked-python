"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountWalletAutoTopupUpdateParams,
    AccountWalletBillingUpdateParams,
    AccountWalletInvoicesListParams,
    AccountWalletProformasCreateParams,
    AccountWalletSettingsUpdateParams,
    AccountWalletStatementListParams,
    AccountWalletStatementsShowParams,
    AccountWalletTopupsLinkParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_WALLET_INVOICES_LIST,
    _PAGE_A_WALLET_PAYMENT_METHODS_LIST,
    _PAGE_A_WALLET_STATEMENT_LIST,
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


class AccountWalletAutoTopup:
    """``wallet.auto_topup``."""

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
        """The auto top-up as set (on or off, the threshold and the amount in halalas, the card, failures and why it turned itself off), or null while Tawked does not offer it or it was never set.

        ``GET /v1/account/wallet/auto-top-up``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_AUTO_TOPUP_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        *,
        amount_halalas: int,
        enabled: bool,
        threshold_halalas: int,
        payment_method_id: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the auto top-up on or off and set its threshold, amount and saved card (`enabled`, `threshold_halalas`, `amount_halalas`, `payment_method_id`); answers the setting.

        ``PUT /v1/account/wallet/auto-top-up``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WALLET_AUTO_TOPUP_UPDATE,
            path={},
            given={
                "amount_halalas": amount_halalas,
                "enabled": enabled,
                "threshold_halalas": threshold_halalas,
                "payment_method_id": payment_method_id,
            },
            params=AccountWalletAutoTopupUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWalletBalance:
    """``wallet.balance``."""

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
        """The account's prepaid balance as Wallet › Balance shows it, in halalas: the balance and its state (`ok`, `low`, `out`), about how many codes it buys, this month's spend and its projection, how long it lasts, the low-balance alert, the auto top-up and the card on file (masked), the month by product, and the last top-up.

        ``GET /v1/account/wallet``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_BALANCE_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWalletBilling:
    """``wallet.billing``."""

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
        """The account's billing details (legal name, VAT number, the national address, the billing e-mail), whether they are complete, and whether a top-up must ask for them first.

        ``GET /v1/account/wallet/billing``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_BILLING_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        *,
        city: str,
        email: str,
        legal_name: str,
        building_number: str | NotGiven | None = NOT_GIVEN,
        district: str | NotGiven | None = NOT_GIVEN,
        other_id: str | NotGiven | None = NOT_GIVEN,
        other_id_type: Literal["cr", "freelance", "other"] | str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven | None = NOT_GIVEN,
        street: str | NotGiven | None = NOT_GIVEN,
        vat_number: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the account's billing details, the ones every invoice is addressed to (legal name, city, e-mail, and while Tawked is VAT-registered the national address); answers the billing details.

        ``PUT /v1/account/wallet/billing``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WALLET_BILLING_UPDATE,
            path={},
            given={
                "city": city,
                "email": email,
                "legal_name": legal_name,
                "building_number": building_number,
                "district": district,
                "other_id": other_id,
                "other_id_type": other_id_type,
                "postal_code": postal_code,
                "street": street,
                "vat_number": vat_number,
            },
            params=AccountWalletBillingUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWalletInvoices:
    """``wallet.invoices``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        *,
        document_kind: Literal["invoice", "credit_note", "proforma"] | str | NotGiven = NOT_GIVEN,
        document_month: datetime | str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The account's billing documents, newest first: invoices, credit notes and proformas, each with its number, kind, status, totals and VAT in halalas, and its PDF's address.

        ``GET /v1/account/wallet/invoices``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WALLET_INVOICES_LIST,
            path={},
            given={
                "document_kind": document_kind,
                "document_month": document_month,
                "number": number,
                "page": page,
                "q": q,
            },
            params=AccountWalletInvoicesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        document_kind: Literal["invoice", "credit_note", "proforma"] | str | NotGiven = NOT_GIVEN,
        document_month: datetime | str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WALLET_INVOICES_LIST,
            _PAGE_A_WALLET_INVOICES_LIST,
            path={},
            given={
                "document_kind": document_kind,
                "document_month": document_month,
                "number": number,
                "page": page,
                "q": q,
            },
            params=AccountWalletInvoicesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        document: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One billing document: its number, kind, status, totals, VAT and discount in halalas, who it is addressed to, what a credit note corrects, what a settled proforma led to, and its PDF's address.

        ``GET /v1/account/wallet/invoices/{document}``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_INVOICES_SHOW,
            path={"document": document},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWalletPaymentMethods:
    """``wallet.payment_methods``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def delete(
        self,
        method: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a saved card, at the card processor and here; an auto top-up that charged it turns off. Answers ok.

        ``DELETE /v1/account/wallet/payment-methods/{method}``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WALLET_PAYMENT_METHODS_DELETE,
            path={"method": method},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The cards saved for the auto top-up, newest first, masked as the console shows them: brand, last four digits, expiry, whether expired. Empty while Tawked does not offer auto top-up. Every card in one answer (no paging).

        ``GET /v1/account/wallet/payment-methods``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WALLET_PAYMENT_METHODS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WALLET_PAYMENT_METHODS_LIST,
            _PAGE_A_WALLET_PAYMENT_METHODS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWalletProformas:
    """``wallet.proformas``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def cancel(
        self,
        document: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel an open proforma (the transfer will not be expected); answers the proforma, now cancelled.

        ``DELETE /v1/account/wallet/proformas/{document}``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WALLET_PROFORMAS_CANCEL,
            path={"document": document},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        *,
        amount_halalas: int,
        billing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask for a proforma to top up by bank transfer (`amount_halalas`, the credit wanted); answers the proforma with its number, total and PDF. The balance moves only once Tawked's team settles the transfer.

        ``POST /v1/account/wallet/proformas``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_WALLET_PROFORMAS_CREATE,
            path={},
            given={"amount_halalas": amount_halalas, "billing": billing},
            params=AccountWalletProformasCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWalletSettings:
    """``wallet.settings``."""

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
        """The wallet's settings: the low-balance alert (threshold in halalas, the e-mail, the WhatsApp number it goes to, masked) and, while Tawked offers it, the auto top-up (its setting, today's charges against the daily cap, the saved cards masked, the bounds).

        ``GET /v1/account/wallet/settings``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_SETTINGS_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        *,
        alert_enabled: bool,
        alert_email: str | NotGiven | None = NOT_GIVEN,
        alert_threshold_halalas: int | NotGiven = NOT_GIVEN,
        auto_topup: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the wallet's settings in one go, as Balance's save bar does: the low-balance alert (`alert_enabled`, `alert_threshold_halalas`, `alert_email`) and optionally the auto top-up (`auto_topup`: enabled, threshold, amount, card); answers the settings.

        ``PUT /v1/account/wallet/settings``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_WALLET_SETTINGS_UPDATE,
            path={},
            given={
                "alert_enabled": alert_enabled,
                "alert_email": alert_email,
                "alert_threshold_halalas": alert_threshold_halalas,
                "auto_topup": auto_topup,
            },
            params=AccountWalletSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountWalletStatement:
    """``wallet.statement``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        day: datetime | str | NotGiven = NOT_GIVEN,
        kind: Literal[
            "topup",
            "otp_charge",
            "refund",
            "adjustment",
            "signup_bonus",
            "message_charge",
            "whatsapp_message_charge",
            "topup_refund",
            "chat_agent_charge",
            "chat_agent_refund",
            "email_charge",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        product: Literal["verify", "notifications", "chat", "email"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        side: Literal["own", "clients"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The wallet's ledger lines, newest first: each one's kind (topup, otp_charge, whatsapp_message_charge, email_charge, chat_agent_charge, refund, adjustment, signup_bonus…), product, application, template, a reference the client knows, the signed amount and the balance after, in halalas.

        ``GET /v1/account/wallet/statement``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_WALLET_STATEMENT_LIST,
            path={},
            given={
                "application": application,
                "day": day,
                "kind": kind,
                "month": month,
                "page": page,
                "product": product,
                "q": q,
                "reference": reference,
                "side": side,
            },
            params=AccountWalletStatementListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        day: datetime | str | NotGiven = NOT_GIVEN,
        kind: Literal[
            "topup",
            "otp_charge",
            "refund",
            "adjustment",
            "signup_bonus",
            "message_charge",
            "whatsapp_message_charge",
            "topup_refund",
            "chat_agent_charge",
            "chat_agent_refund",
            "email_charge",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        product: Literal["verify", "notifications", "chat", "email"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        side: Literal["own", "clients"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WALLET_STATEMENT_LIST,
            _PAGE_A_WALLET_STATEMENT_LIST,
            path={},
            given={
                "application": application,
                "day": day,
                "kind": kind,
                "month": month,
                "page": page,
                "product": product,
                "q": q,
                "reference": reference,
                "side": side,
            },
            params=AccountWalletStatementListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWalletStatements:
    """``wallet.statements``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def show(
        self,
        period: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        day: datetime | str | NotGiven = NOT_GIVEN,
        kind: Literal[
            "topup",
            "otp_charge",
            "refund",
            "adjustment",
            "signup_bonus",
            "message_charge",
            "whatsapp_message_charge",
            "topup_refund",
            "chat_agent_charge",
            "chat_agent_refund",
            "email_charge",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        product: Literal["verify", "notifications", "chat", "email"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        side: Literal["own", "clients"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One month's statement (YYYY-MM, Riyadh): the opening and closing balance, the top-ups, the usage by product, the refunds and adjustments, the month day by day, and the address of its PDF.

        ``GET /v1/account/wallet/statements/{period}``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_STATEMENTS_SHOW,
            path={"period": period},
            given={
                "application": application,
                "day": day,
                "kind": kind,
                "month": month,
                "page": page,
                "product": product,
                "q": q,
                "reference": reference,
                "side": side,
            },
            params=AccountWalletStatementsShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWalletTopups:
    """``wallet.topups``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def link(
        self,
        *,
        amount_halalas: int | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The console's Top up address for the person to pay by card (optionally with `amount_halalas` filled in), and the amounts it offers: the packages, the range, the bounds. Relay `human_action` (what to say, the link in the person's language); read `wallet.balance.show` after they paid.

        ``GET /v1/account/wallet/top-up-link``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_WALLET_TOPUPS_LINK,
            path={},
            given={"amount_halalas": amount_halalas},
            params=AccountWalletTopupsLinkParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountWallet:
    """``wallet``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.auto_topup = AccountWalletAutoTopup(client)
        self.balance = AccountWalletBalance(client)
        self.billing = AccountWalletBilling(client)
        self.invoices = AccountWalletInvoices(client)
        self.payment_methods = AccountWalletPaymentMethods(client)
        self.proformas = AccountWalletProformas(client)
        self.settings = AccountWalletSettings(client)
        self.statement = AccountWalletStatement(client)
        self.statements = AccountWalletStatements(client)
        self.topups = AccountWalletTopups(client)


class AsyncAccountWalletAutoTopup:
    """``wallet.auto_topup``."""

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
        """The auto top-up as set (on or off, the threshold and the amount in halalas, the card, failures and why it turned itself off), or null while Tawked does not offer it or it was never set.

        ``GET /v1/account/wallet/auto-top-up``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_AUTO_TOPUP_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        *,
        amount_halalas: int,
        enabled: bool,
        threshold_halalas: int,
        payment_method_id: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn the auto top-up on or off and set its threshold, amount and saved card (`enabled`, `threshold_halalas`, `amount_halalas`, `payment_method_id`); answers the setting.

        ``PUT /v1/account/wallet/auto-top-up``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WALLET_AUTO_TOPUP_UPDATE,
            path={},
            given={
                "amount_halalas": amount_halalas,
                "enabled": enabled,
                "threshold_halalas": threshold_halalas,
                "payment_method_id": payment_method_id,
            },
            params=AccountWalletAutoTopupUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletBalance:
    """``wallet.balance``."""

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
        """The account's prepaid balance as Wallet › Balance shows it, in halalas: the balance and its state (`ok`, `low`, `out`), about how many codes it buys, this month's spend and its projection, how long it lasts, the low-balance alert, the auto top-up and the card on file (masked), the month by product, and the last top-up.

        ``GET /v1/account/wallet``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_BALANCE_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletBilling:
    """``wallet.billing``."""

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
        """The account's billing details (legal name, VAT number, the national address, the billing e-mail), whether they are complete, and whether a top-up must ask for them first.

        ``GET /v1/account/wallet/billing``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_BILLING_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        *,
        city: str,
        email: str,
        legal_name: str,
        building_number: str | NotGiven | None = NOT_GIVEN,
        district: str | NotGiven | None = NOT_GIVEN,
        other_id: str | NotGiven | None = NOT_GIVEN,
        other_id_type: Literal["cr", "freelance", "other"] | str | NotGiven = NOT_GIVEN,
        postal_code: str | NotGiven | None = NOT_GIVEN,
        street: str | NotGiven | None = NOT_GIVEN,
        vat_number: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the account's billing details, the ones every invoice is addressed to (legal name, city, e-mail, and while Tawked is VAT-registered the national address); answers the billing details.

        ``PUT /v1/account/wallet/billing``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WALLET_BILLING_UPDATE,
            path={},
            given={
                "city": city,
                "email": email,
                "legal_name": legal_name,
                "building_number": building_number,
                "district": district,
                "other_id": other_id,
                "other_id_type": other_id_type,
                "postal_code": postal_code,
                "street": street,
                "vat_number": vat_number,
            },
            params=AccountWalletBillingUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletInvoices:
    """``wallet.invoices``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        *,
        document_kind: Literal["invoice", "credit_note", "proforma"] | str | NotGiven = NOT_GIVEN,
        document_month: datetime | str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The account's billing documents, newest first: invoices, credit notes and proformas, each with its number, kind, status, totals and VAT in halalas, and its PDF's address.

        ``GET /v1/account/wallet/invoices``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WALLET_INVOICES_LIST,
            path={},
            given={
                "document_kind": document_kind,
                "document_month": document_month,
                "number": number,
                "page": page,
                "q": q,
            },
            params=AccountWalletInvoicesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        document_kind: Literal["invoice", "credit_note", "proforma"] | str | NotGiven = NOT_GIVEN,
        document_month: datetime | str | NotGiven = NOT_GIVEN,
        number: str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WALLET_INVOICES_LIST,
            _PAGE_A_WALLET_INVOICES_LIST,
            path={},
            given={
                "document_kind": document_kind,
                "document_month": document_month,
                "number": number,
                "page": page,
                "q": q,
            },
            params=AccountWalletInvoicesListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        document: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One billing document: its number, kind, status, totals, VAT and discount in halalas, who it is addressed to, what a credit note corrects, what a settled proforma led to, and its PDF's address.

        ``GET /v1/account/wallet/invoices/{document}``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_INVOICES_SHOW,
            path={"document": document},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletPaymentMethods:
    """``wallet.payment_methods``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def delete(
        self,
        method: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a saved card, at the card processor and here; an auto top-up that charged it turns off. Answers ok.

        ``DELETE /v1/account/wallet/payment-methods/{method}``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WALLET_PAYMENT_METHODS_DELETE,
            path={"method": method},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The cards saved for the auto top-up, newest first, masked as the console shows them: brand, last four digits, expiry, whether expired. Empty while Tawked does not offer auto top-up. Every card in one answer (no paging).

        ``GET /v1/account/wallet/payment-methods``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WALLET_PAYMENT_METHODS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WALLET_PAYMENT_METHODS_LIST,
            _PAGE_A_WALLET_PAYMENT_METHODS_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletProformas:
    """``wallet.proformas``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def cancel(
        self,
        document: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel an open proforma (the transfer will not be expected); answers the proforma, now cancelled.

        ``DELETE /v1/account/wallet/proformas/{document}``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WALLET_PROFORMAS_CANCEL,
            path={"document": document},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        *,
        amount_halalas: int,
        billing: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Ask for a proforma to top up by bank transfer (`amount_halalas`, the credit wanted); answers the proforma with its number, total and PDF. The balance moves only once Tawked's team settles the transfer.

        ``POST /v1/account/wallet/proformas``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_WALLET_PROFORMAS_CREATE,
            path={},
            given={"amount_halalas": amount_halalas, "billing": billing},
            params=AccountWalletProformasCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletSettings:
    """``wallet.settings``."""

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
        """The wallet's settings: the low-balance alert (threshold in halalas, the e-mail, the WhatsApp number it goes to, masked) and, while Tawked offers it, the auto top-up (its setting, today's charges against the daily cap, the saved cards masked, the bounds).

        ``GET /v1/account/wallet/settings``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_SETTINGS_SHOW,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        *,
        alert_enabled: bool,
        alert_email: str | NotGiven | None = NOT_GIVEN,
        alert_threshold_halalas: int | NotGiven = NOT_GIVEN,
        auto_topup: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the wallet's settings in one go, as Balance's save bar does: the low-balance alert (`alert_enabled`, `alert_threshold_halalas`, `alert_email`) and optionally the auto top-up (`auto_topup`: enabled, threshold, amount, card); answers the settings.

        ``PUT /v1/account/wallet/settings``, permission ``wallet:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_WALLET_SETTINGS_UPDATE,
            path={},
            given={
                "alert_enabled": alert_enabled,
                "alert_email": alert_email,
                "alert_threshold_halalas": alert_threshold_halalas,
                "auto_topup": auto_topup,
            },
            params=AccountWalletSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletStatement:
    """``wallet.statement``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        day: datetime | str | NotGiven = NOT_GIVEN,
        kind: Literal[
            "topup",
            "otp_charge",
            "refund",
            "adjustment",
            "signup_bonus",
            "message_charge",
            "whatsapp_message_charge",
            "topup_refund",
            "chat_agent_charge",
            "chat_agent_refund",
            "email_charge",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        product: Literal["verify", "notifications", "chat", "email"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        side: Literal["own", "clients"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """The wallet's ledger lines, newest first: each one's kind (topup, otp_charge, whatsapp_message_charge, email_charge, chat_agent_charge, refund, adjustment, signup_bonus…), product, application, template, a reference the client knows, the signed amount and the balance after, in halalas.

        ``GET /v1/account/wallet/statement``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_WALLET_STATEMENT_LIST,
            path={},
            given={
                "application": application,
                "day": day,
                "kind": kind,
                "month": month,
                "page": page,
                "product": product,
                "q": q,
                "reference": reference,
                "side": side,
            },
            params=AccountWalletStatementListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        *,
        application: str | NotGiven = NOT_GIVEN,
        day: datetime | str | NotGiven = NOT_GIVEN,
        kind: Literal[
            "topup",
            "otp_charge",
            "refund",
            "adjustment",
            "signup_bonus",
            "message_charge",
            "whatsapp_message_charge",
            "topup_refund",
            "chat_agent_charge",
            "chat_agent_refund",
            "email_charge",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        product: Literal["verify", "notifications", "chat", "email"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        side: Literal["own", "clients"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_WALLET_STATEMENT_LIST,
            _PAGE_A_WALLET_STATEMENT_LIST,
            path={},
            given={
                "application": application,
                "day": day,
                "kind": kind,
                "month": month,
                "page": page,
                "product": product,
                "q": q,
                "reference": reference,
                "side": side,
            },
            params=AccountWalletStatementListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletStatements:
    """``wallet.statements``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def show(
        self,
        period: str,
        *,
        application: str | NotGiven = NOT_GIVEN,
        day: datetime | str | NotGiven = NOT_GIVEN,
        kind: Literal[
            "topup",
            "otp_charge",
            "refund",
            "adjustment",
            "signup_bonus",
            "message_charge",
            "whatsapp_message_charge",
            "topup_refund",
            "chat_agent_charge",
            "chat_agent_refund",
            "email_charge",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        month: datetime | str | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        product: Literal["verify", "notifications", "chat", "email"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reference: str | NotGiven = NOT_GIVEN,
        side: Literal["own", "clients"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One month's statement (YYYY-MM, Riyadh): the opening and closing balance, the top-ups, the usage by product, the refunds and adjustments, the month day by day, and the address of its PDF.

        ``GET /v1/account/wallet/statements/{period}``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_STATEMENTS_SHOW,
            path={"period": period},
            given={
                "application": application,
                "day": day,
                "kind": kind,
                "month": month,
                "page": page,
                "product": product,
                "q": q,
                "reference": reference,
                "side": side,
            },
            params=AccountWalletStatementsShowParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWalletTopups:
    """``wallet.topups``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def link(
        self,
        *,
        amount_halalas: int | NotGiven | None = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The console's Top up address for the person to pay by card (optionally with `amount_halalas` filled in), and the amounts it offers: the packages, the range, the bounds. Relay `human_action` (what to say, the link in the person's language); read `wallet.balance.show` after they paid.

        ``GET /v1/account/wallet/top-up-link``, permission ``wallet:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_WALLET_TOPUPS_LINK,
            path={},
            given={"amount_halalas": amount_halalas},
            params=AccountWalletTopupsLinkParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountWallet:
    """``wallet``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.auto_topup = AsyncAccountWalletAutoTopup(client)
        self.balance = AsyncAccountWalletBalance(client)
        self.billing = AsyncAccountWalletBilling(client)
        self.invoices = AsyncAccountWalletInvoices(client)
        self.payment_methods = AsyncAccountWalletPaymentMethods(client)
        self.proformas = AsyncAccountWalletProformas(client)
        self.settings = AsyncAccountWalletSettings(client)
        self.statement = AsyncAccountWalletStatement(client)
        self.statements = AsyncAccountWalletStatements(client)
        self.topups = AsyncAccountWalletTopups(client)
