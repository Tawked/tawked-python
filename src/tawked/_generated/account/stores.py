"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import AccountStoresSallaEmployeesAddParams
from tawked._generated.endpoints import _PAGE_A_STORES_LIST, _PAGE_A_STORES_SALLA_EMPLOYEES_LIST
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


class AccountStoresSallaChat:
    """``stores.salla.chat``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change what the Tawked Chat team sees and does with the Salla store's orders (the orders tab: customer, orders, status changes); answers the settings as saved.

        ``PUT /v1/stores/salla/{store}/chat``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_CHAT_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaChatButton:
    """``stores.salla.chat_button``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the chat button on the Salla store's own pages, whole (on or off, position, colours, greeting); answers the button as saved. Turning it on needs a number that takes messages.

        ``PUT /v1/stores/salla/{store}/chat-button``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_CHAT_BUTTON_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaConsent:
    """``stores.salla.consent``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Say (`attested: true`) or withdraw that the Salla store's checkout collects its customers' consent to marketing messages; answers the consent as it stands.

        ``PUT /v1/stores/salla/{store}/consent``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_CONSENT_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaEmployees:
    """``stores.salla.employees``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def add(
        self,
        application: str,
        *,
        people: Sequence[Mapping[str, Any]],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add the chosen Salla employees to the application's support team (`as: support`, they answer in Tawked Chat) or as members of the account (`as: member`); answers each person's outcome.

        ``POST /v1/applications/{application}/stores/salla/employees``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_EMPLOYEES_ADD,
            path={"application": application},
            given={"people": people},
            params=AccountStoresSallaEmployeesAddParams,
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
        """List the employees Salla names for the application's store, each with their state in Tawked (none, support, member, …); answers `people`, `error` (denied, unavailable or null) and whether this person may add them.

        ``GET /v1/applications/{application}/stores/salla/employees``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_STORES_SALLA_EMPLOYEES_LIST,
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
            _E.A_STORES_SALLA_EMPLOYEES_LIST,
            _PAGE_A_STORES_SALLA_EMPLOYEES_LIST,
            path={"application": application},
            given={},
            params=None,
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
        """Read the store's employees from Salla again now (after someone was added or changed in Salla); answers the list as stores.salla.employees.list does.

        ``POST /v1/applications/{application}/stores/salla/employees/refresh``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_EMPLOYEES_REFRESH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaKinds:
    """``stores.salla.kinds``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        kind: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change one notification of a Salla store at once: switch it on or off, choose its template (the kit's or the number's own), map the template's placeholders, set its options. Answers the slot as it was before.

        ``PUT /v1/stores/salla/{store}/kinds/{kind}``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_KINDS_UPDATE,
            path={"store": store, "kind": kind},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaKitTemplates:
    """``stores.salla.kit_templates``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Submit to Meta the kit templates the store's enabled notifications still need; answers how many were created and which failed. Meta reviews each one: `next` says how to follow it (stores.salla.templates.refresh, then stores.salla.show).

        ``POST /v1/stores/salla/{store}/templates/kit``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_KIT_TEMPLATES_CREATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaSettings:
    """``stores.salla.settings``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a Salla store's settings: the language its messages go in, English variants, quiet hours, pause. Answers ok.

        ``PUT /v1/stores/salla/{store}/settings``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_SETTINGS_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaSetup:
    """``stores.salla.setup``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def link(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Link a Salla store waiting for its application to one of the account's applications (`application_id`), or to a new one named after the store (null); answers the application's id.

        ``PUT /v1/stores/salla/{store}/setup/link``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_SETUP_LINK,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def number_later(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Leave the WhatsApp number for later in a Salla store's setup (`later`, true when absent), so its notifications list opens before the number; answers ok.

        ``PUT /v1/stores/salla/{store}/setup/number-later``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_SETUP_NUMBER_LATER,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaTemplates:
    """``stores.salla.templates``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def refresh(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the store number's templates from Meta again (after Meta approved or rejected one); answers ok with a `next` (read the store again), or templates_unavailable when Meta did not answer.

        ``POST /v1/stores/salla/{store}/templates/refresh``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_TEMPLATES_REFRESH,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSallaTest:
    """``stores.salla.test``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def send(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test store notification to the account owner's own phone (never a customer), from the store's number; answers ok.

        ``POST /v1/stores/salla/{store}/test``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_TEST_SEND,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresSalla:
    """``stores.salla``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.chat = AccountStoresSallaChat(client)
        self.chat_button = AccountStoresSallaChatButton(client)
        self.consent = AccountStoresSallaConsent(client)
        self.employees = AccountStoresSallaEmployees(client)
        self.kinds = AccountStoresSallaKinds(client)
        self.kit_templates = AccountStoresSallaKitTemplates(client)
        self.settings = AccountStoresSallaSettings(client)
        self.setup = AccountStoresSallaSetup(client)
        self.templates = AccountStoresSallaTemplates(client)
        self.test = AccountStoresSallaTest(client)

    def activate(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn on, at once, the chosen notifications of a Salla store on its first visit (nothing on yet); answers how many are on. The store then messages its customers on each event.

        ``POST /v1/stores/salla/{store}/activate``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_ACTIVATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        store: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one Salla store as the console shows it: its status and application, its setup (link and number), every notification row with its state and template, settings, consent, chat button and chat orders tab.

        ``GET /v1/stores/salla/{store}``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_STORES_SALLA_SHOW,
            path={"store": store},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountStoresZidChatButton:
    """``stores.zid.chat_button``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the chat button on the Zid store's own pages, whole (on or off, position, colours, greeting); answers the button as saved. Turning it on needs a number that takes messages.

        ``PUT /v1/stores/zid/{store}/chat-button``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_CHAT_BUTTON_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidConsent:
    """``stores.zid.consent``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Say (`attested: true`) or withdraw that the Zid store's checkout collects its customers' consent to marketing messages; answers the consent as it stands.

        ``PUT /v1/stores/zid/{store}/consent``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_CONSENT_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidKinds:
    """``stores.zid.kinds``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        kind: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change one notification of a Zid store at once: switch it on or off, choose its template (the kit's or the number's own), map the template's placeholders, set its options. Answers the slot as it was before.

        ``PUT /v1/stores/zid/{store}/kinds/{kind}``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_KINDS_UPDATE,
            path={"store": store, "kind": kind},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidKitTemplates:
    """``stores.zid.kit_templates``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Submit to Meta the kit templates the store's enabled notifications still need; answers how many were created and which failed. Meta reviews each one: `next` says how to follow it (stores.zid.templates.refresh, then stores.zid.show).

        ``POST /v1/stores/zid/{store}/templates/kit``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_KIT_TEMPLATES_CREATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidSettings:
    """``stores.zid.settings``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a Zid store's settings: the language its messages go in, English variants, quiet hours, pause. Answers ok.

        ``PUT /v1/stores/zid/{store}/settings``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_SETTINGS_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidSetup:
    """``stores.zid.setup``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def link(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Link a Zid store waiting for its application to one of the account's applications (`application_id`), or to a new one named after the store (null); answers the application's id.

        ``PUT /v1/stores/zid/{store}/setup/link``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_SETUP_LINK,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def number_later(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Leave the WhatsApp number for later in a Zid store's setup (`later`, true when absent), so its notifications list opens before the number; answers ok.

        ``PUT /v1/stores/zid/{store}/setup/number-later``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_SETUP_NUMBER_LATER,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidTemplates:
    """``stores.zid.templates``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def refresh(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the store number's templates from Meta again (after Meta approved or rejected one); answers ok with a `next` (read the store again), or templates_unavailable when Meta did not answer.

        ``POST /v1/stores/zid/{store}/templates/refresh``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_TEMPLATES_REFRESH,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZidTest:
    """``stores.zid.test``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def send(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test store notification to the account owner's own phone (never a customer), from the store's number; answers ok.

        ``POST /v1/stores/zid/{store}/test``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_TEST_SEND,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountStoresZid:
    """``stores.zid``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.chat_button = AccountStoresZidChatButton(client)
        self.consent = AccountStoresZidConsent(client)
        self.kinds = AccountStoresZidKinds(client)
        self.kit_templates = AccountStoresZidKitTemplates(client)
        self.settings = AccountStoresZidSettings(client)
        self.setup = AccountStoresZidSetup(client)
        self.templates = AccountStoresZidTemplates(client)
        self.test = AccountStoresZidTest(client)

    def activate(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn on, at once, the chosen notifications of a Zid store on its first visit (nothing on yet); answers how many are on. The store then messages its customers on each event.

        ``POST /v1/stores/zid/{store}/activate``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_ACTIVATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        store: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one Zid store as the console shows it: its status and application, its setup (link and number), every notification row with its state and template, settings, consent and chat button.

        ``GET /v1/stores/zid/{store}``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_STORES_ZID_SHOW,
            path={"store": store},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountStores:
    """``stores``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.salla = AccountStoresSalla(client)
        self.zid = AccountStoresZid(client)

    def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the Salla and Zid stores this token reaches: platform, name, status, linked application, whether any notification is on and whether checkout consent is attested. Open one with stores.salla.show or stores.zid.show.

        ``GET /v1/stores``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_STORES_LIST,
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
            _E.A_STORES_LIST,
            _PAGE_A_STORES_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaChat:
    """``stores.salla.chat``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change what the Tawked Chat team sees and does with the Salla store's orders (the orders tab: customer, orders, status changes); answers the settings as saved.

        ``PUT /v1/stores/salla/{store}/chat``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_CHAT_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaChatButton:
    """``stores.salla.chat_button``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the chat button on the Salla store's own pages, whole (on or off, position, colours, greeting); answers the button as saved. Turning it on needs a number that takes messages.

        ``PUT /v1/stores/salla/{store}/chat-button``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_CHAT_BUTTON_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaConsent:
    """``stores.salla.consent``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Say (`attested: true`) or withdraw that the Salla store's checkout collects its customers' consent to marketing messages; answers the consent as it stands.

        ``PUT /v1/stores/salla/{store}/consent``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_CONSENT_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaEmployees:
    """``stores.salla.employees``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def add(
        self,
        application: str,
        *,
        people: Sequence[Mapping[str, Any]],
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add the chosen Salla employees to the application's support team (`as: support`, they answer in Tawked Chat) or as members of the account (`as: member`); answers each person's outcome.

        ``POST /v1/applications/{application}/stores/salla/employees``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_EMPLOYEES_ADD,
            path={"application": application},
            given={"people": people},
            params=AccountStoresSallaEmployeesAddParams,
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
        """List the employees Salla names for the application's store, each with their state in Tawked (none, support, member, …); answers `people`, `error` (denied, unavailable or null) and whether this person may add them.

        ``GET /v1/applications/{application}/stores/salla/employees``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_STORES_SALLA_EMPLOYEES_LIST,
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
            _E.A_STORES_SALLA_EMPLOYEES_LIST,
            _PAGE_A_STORES_SALLA_EMPLOYEES_LIST,
            path={"application": application},
            given={},
            params=None,
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
        """Read the store's employees from Salla again now (after someone was added or changed in Salla); answers the list as stores.salla.employees.list does.

        ``POST /v1/applications/{application}/stores/salla/employees/refresh``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_EMPLOYEES_REFRESH,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaKinds:
    """``stores.salla.kinds``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        kind: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change one notification of a Salla store at once: switch it on or off, choose its template (the kit's or the number's own), map the template's placeholders, set its options. Answers the slot as it was before.

        ``PUT /v1/stores/salla/{store}/kinds/{kind}``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_KINDS_UPDATE,
            path={"store": store, "kind": kind},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaKitTemplates:
    """``stores.salla.kit_templates``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Submit to Meta the kit templates the store's enabled notifications still need; answers how many were created and which failed. Meta reviews each one: `next` says how to follow it (stores.salla.templates.refresh, then stores.salla.show).

        ``POST /v1/stores/salla/{store}/templates/kit``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_KIT_TEMPLATES_CREATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaSettings:
    """``stores.salla.settings``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a Salla store's settings: the language its messages go in, English variants, quiet hours, pause. Answers ok.

        ``PUT /v1/stores/salla/{store}/settings``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_SETTINGS_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaSetup:
    """``stores.salla.setup``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def link(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Link a Salla store waiting for its application to one of the account's applications (`application_id`), or to a new one named after the store (null); answers the application's id.

        ``PUT /v1/stores/salla/{store}/setup/link``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_SETUP_LINK,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def number_later(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Leave the WhatsApp number for later in a Salla store's setup (`later`, true when absent), so its notifications list opens before the number; answers ok.

        ``PUT /v1/stores/salla/{store}/setup/number-later``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_SETUP_NUMBER_LATER,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaTemplates:
    """``stores.salla.templates``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def refresh(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the store number's templates from Meta again (after Meta approved or rejected one); answers ok with a `next` (read the store again), or templates_unavailable when Meta did not answer.

        ``POST /v1/stores/salla/{store}/templates/refresh``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_TEMPLATES_REFRESH,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSallaTest:
    """``stores.salla.test``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def send(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test store notification to the account owner's own phone (never a customer), from the store's number; answers ok.

        ``POST /v1/stores/salla/{store}/test``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_TEST_SEND,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresSalla:
    """``stores.salla``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.chat = AsyncAccountStoresSallaChat(client)
        self.chat_button = AsyncAccountStoresSallaChatButton(client)
        self.consent = AsyncAccountStoresSallaConsent(client)
        self.employees = AsyncAccountStoresSallaEmployees(client)
        self.kinds = AsyncAccountStoresSallaKinds(client)
        self.kit_templates = AsyncAccountStoresSallaKitTemplates(client)
        self.settings = AsyncAccountStoresSallaSettings(client)
        self.setup = AsyncAccountStoresSallaSetup(client)
        self.templates = AsyncAccountStoresSallaTemplates(client)
        self.test = AsyncAccountStoresSallaTest(client)

    async def activate(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn on, at once, the chosen notifications of a Salla store on its first visit (nothing on yet); answers how many are on. The store then messages its customers on each event.

        ``POST /v1/stores/salla/{store}/activate``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_ACTIVATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        store: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one Salla store as the console shows it: its status and application, its setup (link and number), every notification row with its state and template, settings, consent, chat button and chat orders tab.

        ``GET /v1/stores/salla/{store}``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_STORES_SALLA_SHOW,
            path={"store": store},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidChatButton:
    """``stores.zid.chat_button``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save the chat button on the Zid store's own pages, whole (on or off, position, colours, greeting); answers the button as saved. Turning it on needs a number that takes messages.

        ``PUT /v1/stores/zid/{store}/chat-button``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_CHAT_BUTTON_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidConsent:
    """``stores.zid.consent``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Say (`attested: true`) or withdraw that the Zid store's checkout collects its customers' consent to marketing messages; answers the consent as it stands.

        ``PUT /v1/stores/zid/{store}/consent``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_CONSENT_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidKinds:
    """``stores.zid.kinds``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        kind: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change one notification of a Zid store at once: switch it on or off, choose its template (the kit's or the number's own), map the template's placeholders, set its options. Answers the slot as it was before.

        ``PUT /v1/stores/zid/{store}/kinds/{kind}``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_KINDS_UPDATE,
            path={"store": store, "kind": kind},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidKitTemplates:
    """``stores.zid.kit_templates``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Submit to Meta the kit templates the store's enabled notifications still need; answers how many were created and which failed. Meta reviews each one: `next` says how to follow it (stores.zid.templates.refresh, then stores.zid.show).

        ``POST /v1/stores/zid/{store}/templates/kit``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_KIT_TEMPLATES_CREATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidSettings:
    """``stores.zid.settings``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Change a Zid store's settings: the language its messages go in, English variants, quiet hours, pause. Answers ok.

        ``PUT /v1/stores/zid/{store}/settings``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_SETTINGS_UPDATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidSetup:
    """``stores.zid.setup``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def link(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Link a Zid store waiting for its application to one of the account's applications (`application_id`), or to a new one named after the store (null); answers the application's id.

        ``PUT /v1/stores/zid/{store}/setup/link``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_SETUP_LINK,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def number_later(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Leave the WhatsApp number for later in a Zid store's setup (`later`, true when absent), so its notifications list opens before the number; answers ok.

        ``PUT /v1/stores/zid/{store}/setup/number-later``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_SETUP_NUMBER_LATER,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidTemplates:
    """``stores.zid.templates``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def refresh(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the store number's templates from Meta again (after Meta approved or rejected one); answers ok with a `next` (read the store again), or templates_unavailable when Meta did not answer.

        ``POST /v1/stores/zid/{store}/templates/refresh``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_TEMPLATES_REFRESH,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZidTest:
    """``stores.zid.test``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def send(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send a test store notification to the account owner's own phone (never a customer), from the store's number; answers ok.

        ``POST /v1/stores/zid/{store}/test``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_TEST_SEND,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountStoresZid:
    """``stores.zid``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.chat_button = AsyncAccountStoresZidChatButton(client)
        self.consent = AsyncAccountStoresZidConsent(client)
        self.kinds = AsyncAccountStoresZidKinds(client)
        self.kit_templates = AsyncAccountStoresZidKitTemplates(client)
        self.settings = AsyncAccountStoresZidSettings(client)
        self.setup = AsyncAccountStoresZidSetup(client)
        self.templates = AsyncAccountStoresZidTemplates(client)
        self.test = AsyncAccountStoresZidTest(client)

    async def activate(
        self,
        store: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn on, at once, the chosen notifications of a Zid store on its first visit (nothing on yet); answers how many are on. The store then messages its customers on each event.

        ``POST /v1/stores/zid/{store}/activate``, permission ``stores:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_ACTIVATE,
            path={"store": store},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        store: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one Zid store as the console shows it: its status and application, its setup (link and number), every notification row with its state and template, settings, consent and chat button.

        ``GET /v1/stores/zid/{store}``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_STORES_ZID_SHOW,
            path={"store": store},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountStores:
    """``stores``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.salla = AsyncAccountStoresSalla(client)
        self.zid = AsyncAccountStoresZid(client)

    async def list(
        self,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the Salla and Zid stores this token reaches: platform, name, status, linked application, whether any notification is on and whether checkout consent is attested. Open one with stores.salla.show or stores.zid.show.

        ``GET /v1/stores``, permission ``stores:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_STORES_LIST,
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
            _E.A_STORES_LIST,
            _PAGE_A_STORES_LIST,
            path={},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )
