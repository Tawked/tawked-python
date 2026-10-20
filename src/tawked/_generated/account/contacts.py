"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountContactsContactsListParams,
    AccountContactsContactsRecordOptInParams,
    AccountContactsContactsTagParams,
    AccountContactsImportsConfirmParams,
    AccountContactsImportsCreateParams,
    AccountContactsOptInUpdateParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_CONTACTS_CONTACTS_LIST,
    _PAGE_A_CONTACTS_IMPORTS_LIST,
    _PAGE_A_CONTACTS_TAGS_LIST,
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


class AccountContactsContacts:
    """``contacts.contacts``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def delete(
        self,
        application: str,
        contact: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a contact for the business (its customer's data, PDPL): gone from the list now, its automations' runs stopped, forgotten for good 30 days later. Answers ok with `purge_at`, when it is forgotten.

        ``DELETE /v1/applications/{application}/contacts/{contact}``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CONTACTS_CONTACTS_DELETE,
            path={"application": application, "contact": contact},
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
        source: Literal["keyword", "salla", "import", "manual"] | str | NotGiven = NOT_GIVEN,
        status: Literal["subscribed", "none", "unsubscribed"] | str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's WhatsApp contacts, newest first, phones masked: each with its consent status (subscribed, none, unsubscribed), tags and source. Filters: q (a name, or a whole Saudi mobile), status, tag, source.

        ``GET /v1/applications/{application}/contacts``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CONTACTS_CONTACTS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "source": source, "status": status, "tag": tag},
            params=AccountContactsContactsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        source: Literal["keyword", "salla", "import", "manual"] | str | NotGiven = NOT_GIVEN,
        status: Literal["subscribed", "none", "unsubscribed"] | str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CONTACTS_CONTACTS_LIST,
            _PAGE_A_CONTACTS_CONTACTS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "source": source, "status": status, "tag": tag},
            params=AccountContactsContactsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def record_opt_in(
        self,
        application: str,
        contact: str,
        *,
        method: Literal["in_person", "written", "phone_call", "other"] | str,
        note: str,
        attested: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Record that the customer agreed to receive marketing outside the opt-in link and an import (in person, in writing, on a call): subscribes them, with your note and your name as the evidence.

        ``POST /v1/applications/{application}/contacts/{contact}/consent``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CONTACTS_CONTACTS_RECORD_OPT_IN,
            path={"application": application, "contact": contact},
            given={"method": method, "note": note, "attested": attested},
            params=AccountContactsContactsRecordOptInParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        contact: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One contact: its consent status from the ledger, tags, language, city, source, and its consent history newest first (who recorded each opt-in or stop, and the evidence).

        ``GET /v1/applications/{application}/contacts/{contact}``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CONTACTS_CONTACTS_SHOW,
            path={"application": application, "contact": contact},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def tag(
        self,
        application: str,
        contact: str,
        *,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set a contact's tags to exactly this list (up to 10): missing tags are made, tags left on no contact are removed. Answers the contact and what was added and removed.

        ``PUT /v1/applications/{application}/contacts/{contact}/tags``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CONTACTS_CONTACTS_TAG,
            path={"application": application, "contact": contact},
            given={"tags": tags},
            params=AccountContactsContactsTagParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def unsubscribe(
        self,
        application: str,
        contact: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Stop a contact's marketing messages (the customer asked you directly): recorded at once in the consent ledger; answers the contact, now unsubscribed. Nothing is recorded when they already are.

        ``POST /v1/applications/{application}/contacts/{contact}/unsubscribe``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CONTACTS_CONTACTS_UNSUBSCRIBE,
            path={"application": application, "contact": contact},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountContactsImports:
    """``contacts.imports``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def confirm(
        self,
        application: str,
        import_: str,
        *,
        basis: Literal["checkout", "form", "none"] | str,
        attested: Any | NotGiven = NOT_GIVEN,
        consent_since: datetime | str | NotGiven | None = NOT_GIVEN,
        consent_text: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm a pending import with how these people agreed to marketing; it runs in the background. Answers the import, `queued`, and `next`: poll contacts.imports.show until `status` is done or failed.

        ``POST /v1/applications/{application}/contacts/imports/{import}/confirm``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CONTACTS_IMPORTS_CONFIRM,
            path={"application": application, "import": import_},
            given={
                "basis": basis,
                "attested": attested,
                "consent_since": consent_since,
                "consent_text": consent_text,
            },
            params=AccountContactsImportsConfirmParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        csv: str | NotGiven | None = NOT_GIVEN,
        file: FileInput | NotGiven | None = NOT_GIVEN,
        file_name: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload a CSV of contacts (columns: phone, and optionally name, tags, city): read and counted, nothing imported yet. Answers the import, `pending`, with its preview (rows, valid, duplicates, outside Saudi Arabia, invalid); confirm it next with contacts.imports.confirm.

        ``POST /v1/applications/{application}/contacts/imports``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CONTACTS_IMPORTS_CREATE,
            path={"application": application},
            given={"csv": csv, "file": file, "file_name": file_name},
            params=AccountContactsImportsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("file",),
        )

    def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's contact imports, newest first, each with its status, counts and outcome.

        ``GET /v1/applications/{application}/contacts/imports``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CONTACTS_IMPORTS_LIST,
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
            _E.A_CONTACTS_IMPORTS_LIST,
            _PAGE_A_CONTACTS_IMPORTS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        import_: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One import: its status (pending, queued, running, done, failed), its preview, its progress (`processed` of `total`), once done its result counted by outcome, and `next` until it is done.

        ``GET /v1/applications/{application}/contacts/imports/{import}``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CONTACTS_IMPORTS_SHOW,
            path={"application": application, "import": import_},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountContactsOptIn:
    """``contacts.opt_in``."""

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
        """The opt-in link: the wa.me link with its word, the welcome reply, whether it is on, and its QR code as SVG. Customers who send the word subscribe to marketing.

        ``GET /v1/applications/{application}/contacts/opt-in``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CONTACTS_OPT_IN_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        *,
        keyword: str,
        welcome_reply: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the opt-in link's word and its welcome reply; the first save turns the link on. Answers the link as it now stands.

        ``PUT /v1/applications/{application}/contacts/opt-in``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CONTACTS_OPT_IN_UPDATE,
            path={"application": application},
            given={"keyword": keyword, "welcome_reply": welcome_reply},
            params=AccountContactsOptInUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountContactsTags:
    """``contacts.tags``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's contact tags by name, each with how many live contacts carry it. Use a tag in a campaign's audience (`audience.kind: tags`).

        ``GET /v1/applications/{application}/contacts/tags``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CONTACTS_TAGS_LIST,
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
            _E.A_CONTACTS_TAGS_LIST,
            _PAGE_A_CONTACTS_TAGS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountContacts:
    """``contacts``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.contacts = AccountContactsContacts(client)
        self.imports = AccountContactsImports(client)
        self.opt_in = AccountContactsOptIn(client)
        self.tags = AccountContactsTags(client)


class AsyncAccountContactsContacts:
    """``contacts.contacts``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def delete(
        self,
        application: str,
        contact: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a contact for the business (its customer's data, PDPL): gone from the list now, its automations' runs stopped, forgotten for good 30 days later. Answers ok with `purge_at`, when it is forgotten.

        ``DELETE /v1/applications/{application}/contacts/{contact}``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_CONTACTS_DELETE,
            path={"application": application, "contact": contact},
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
        source: Literal["keyword", "salla", "import", "manual"] | str | NotGiven = NOT_GIVEN,
        status: Literal["subscribed", "none", "unsubscribed"] | str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's WhatsApp contacts, newest first, phones masked: each with its consent status (subscribed, none, unsubscribed), tags and source. Filters: q (a name, or a whole Saudi mobile), status, tag, source.

        ``GET /v1/applications/{application}/contacts``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CONTACTS_CONTACTS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "source": source, "status": status, "tag": tag},
            params=AccountContactsContactsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        source: Literal["keyword", "salla", "import", "manual"] | str | NotGiven = NOT_GIVEN,
        status: Literal["subscribed", "none", "unsubscribed"] | str | NotGiven = NOT_GIVEN,
        tag: str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CONTACTS_CONTACTS_LIST,
            _PAGE_A_CONTACTS_CONTACTS_LIST,
            path={"application": application},
            given={"page": page, "q": q, "source": source, "status": status, "tag": tag},
            params=AccountContactsContactsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def record_opt_in(
        self,
        application: str,
        contact: str,
        *,
        method: Literal["in_person", "written", "phone_call", "other"] | str,
        note: str,
        attested: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Record that the customer agreed to receive marketing outside the opt-in link and an import (in person, in writing, on a call): subscribes them, with your note and your name as the evidence.

        ``POST /v1/applications/{application}/contacts/{contact}/consent``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_CONTACTS_RECORD_OPT_IN,
            path={"application": application, "contact": contact},
            given={"method": method, "note": note, "attested": attested},
            params=AccountContactsContactsRecordOptInParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        contact: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One contact: its consent status from the ledger, tags, language, city, source, and its consent history newest first (who recorded each opt-in or stop, and the evidence).

        ``GET /v1/applications/{application}/contacts/{contact}``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_CONTACTS_SHOW,
            path={"application": application, "contact": contact},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def tag(
        self,
        application: str,
        contact: str,
        *,
        tags: Sequence[str] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set a contact's tags to exactly this list (up to 10): missing tags are made, tags left on no contact are removed. Answers the contact and what was added and removed.

        ``PUT /v1/applications/{application}/contacts/{contact}/tags``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_CONTACTS_TAG,
            path={"application": application, "contact": contact},
            given={"tags": tags},
            params=AccountContactsContactsTagParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def unsubscribe(
        self,
        application: str,
        contact: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Stop a contact's marketing messages (the customer asked you directly): recorded at once in the consent ledger; answers the contact, now unsubscribed. Nothing is recorded when they already are.

        ``POST /v1/applications/{application}/contacts/{contact}/unsubscribe``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_CONTACTS_UNSUBSCRIBE,
            path={"application": application, "contact": contact},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountContactsImports:
    """``contacts.imports``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def confirm(
        self,
        application: str,
        import_: str,
        *,
        basis: Literal["checkout", "form", "none"] | str,
        attested: Any | NotGiven = NOT_GIVEN,
        consent_since: datetime | str | NotGiven | None = NOT_GIVEN,
        consent_text: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm a pending import with how these people agreed to marketing; it runs in the background. Answers the import, `queued`, and `next`: poll contacts.imports.show until `status` is done or failed.

        ``POST /v1/applications/{application}/contacts/imports/{import}/confirm``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_IMPORTS_CONFIRM,
            path={"application": application, "import": import_},
            given={
                "basis": basis,
                "attested": attested,
                "consent_since": consent_since,
                "consent_text": consent_text,
            },
            params=AccountContactsImportsConfirmParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        csv: str | NotGiven | None = NOT_GIVEN,
        file: FileInput | NotGiven | None = NOT_GIVEN,
        file_name: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload a CSV of contacts (columns: phone, and optionally name, tags, city): read and counted, nothing imported yet. Answers the import, `pending`, with its preview (rows, valid, duplicates, outside Saudi Arabia, invalid); confirm it next with contacts.imports.confirm.

        ``POST /v1/applications/{application}/contacts/imports``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_IMPORTS_CREATE,
            path={"application": application},
            given={"csv": csv, "file": file, "file_name": file_name},
            params=AccountContactsImportsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("file",),
        )

    async def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's contact imports, newest first, each with its status, counts and outcome.

        ``GET /v1/applications/{application}/contacts/imports``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CONTACTS_IMPORTS_LIST,
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
            _E.A_CONTACTS_IMPORTS_LIST,
            _PAGE_A_CONTACTS_IMPORTS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        import_: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One import: its status (pending, queued, running, done, failed), its preview, its progress (`processed` of `total`), once done its result counted by outcome, and `next` until it is done.

        ``GET /v1/applications/{application}/contacts/imports/{import}``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_IMPORTS_SHOW,
            path={"application": application, "import": import_},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountContactsOptIn:
    """``contacts.opt_in``."""

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
        """The opt-in link: the wa.me link with its word, the welcome reply, whether it is on, and its QR code as SVG. Customers who send the word subscribe to marketing.

        ``GET /v1/applications/{application}/contacts/opt-in``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_OPT_IN_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        *,
        keyword: str,
        welcome_reply: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set the opt-in link's word and its welcome reply; the first save turns the link on. Answers the link as it now stands.

        ``PUT /v1/applications/{application}/contacts/opt-in``, permission ``contacts:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CONTACTS_OPT_IN_UPDATE,
            path={"application": application},
            given={"keyword": keyword, "welcome_reply": welcome_reply},
            params=AccountContactsOptInUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountContactsTags:
    """``contacts.tags``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's contact tags by name, each with how many live contacts carry it. Use a tag in a campaign's audience (`audience.kind: tags`).

        ``GET /v1/applications/{application}/contacts/tags``, permission ``contacts:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CONTACTS_TAGS_LIST,
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
            _E.A_CONTACTS_TAGS_LIST,
            _PAGE_A_CONTACTS_TAGS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountContacts:
    """``contacts``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.contacts = AsyncAccountContactsContacts(client)
        self.imports = AsyncAccountContactsImports(client)
        self.opt_in = AsyncAccountContactsOptIn(client)
        self.tags = AsyncAccountContactsTags(client)
