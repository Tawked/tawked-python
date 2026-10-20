"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountAutomationsAutomationsCreateParams,
    AccountAutomationsAutomationsUpdateParams,
    AccountAutomationsRunsListParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_AUTOMATIONS_AUTOMATIONS_LIST,
    _PAGE_A_AUTOMATIONS_RECIPES_LIST,
    _PAGE_A_AUTOMATIONS_RUNS_LIST,
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


class AccountAutomationsAutomations:
    """``automations.automations``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        recipe: Literal["welcome", "cart", "review", "winback"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create an automation, off: from a ready-made one (`recipe`, its draft prefilled) or empty without one. Answers the automation with its draft; then save the draft (automations.automations.update), try it (automations.automations.send_test) and turn it on (automations.automations.on).

        ``POST /v1/applications/{application}/automations``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_CREATE,
            path={"application": application},
            given={"recipe": recipe},
            params=AccountAutomationsAutomationsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete an automation: its live runs stop now, its history stays. Answers ok.

        ``DELETE /v1/applications/{application}/automations/{workflow}``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_DELETE,
            path={"application": application, "workflow": workflow},
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
        """List the application's WhatsApp automations, newest first: each on or off, what it starts on (its trigger), whether the draft differs from what runs, and its last publish.

        ``GET /v1/applications/{application}/automations``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_AUTOMATIONS_AUTOMATIONS_LIST,
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
            _E.A_AUTOMATIONS_AUTOMATIONS_LIST,
            _PAGE_A_AUTOMATIONS_AUTOMATIONS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def off(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn an automation off: no run starts; a waiting run finishes the wait it is in and stops there unless it is on again by then. Answers the automation.

        ``POST /v1/applications/{application}/automations/{workflow}/off``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_OFF,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def on(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn an automation on: the draft is published first when it differs, then runs start from now for each contact its trigger meets, messaging customers. Answers the automation.

        ``POST /v1/applications/{application}/automations/{workflow}/on``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_ON,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def publish(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Publish the draft as the version new runs start on (runs under way keep theirs). Answers the automation; 422 definition_invalid with each problem when it cannot run.

        ``POST /v1/applications/{application}/automations/{workflow}/publish``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_PUBLISH,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send_test(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Run the draft as it is now on your own Saudi mobile (the token's person), every wait one minute, labelled a test; answers the test run, to read in its log.

        ``POST /v1/applications/{application}/automations/{workflow}/test``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_SEND_TEST,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        workflow: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One automation: its draft and its published definition whole, on or off, its version, what keeps the draft from running (`problems`, each with its step and code), the Salla notice it would repeat, and its last 30 days (live, completed, stopped, failed runs; messages sent).

        ``GET /v1/applications/{application}/automations/{workflow}``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_SHOW,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        workflow: str,
        *,
        definition: Mapping[str, Any],
        name: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save an automation's draft (its trigger, conditions and steps) and its name: nothing is checked beyond the shape, and what runs does not change until it is published. Answers the automation with the draft's problems; once there are none, try it with automations.automations.send_test and publish it with automations.automations.publish (or automations.automations.on).

        ``PUT /v1/applications/{application}/automations/{workflow}``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_UPDATE,
            path={"application": application, "workflow": workflow},
            given={"definition": definition, "name": name},
            params=AccountAutomationsAutomationsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountAutomationsRecipes:
    """``automations.recipes``."""

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
        """List the ready-made automations (welcome, abandoned cart, win-back, review request…) with their trigger, whether this application may use them (the Salla ones need its store) and, when the store's own notice covers the event, that notice (`locked_by`). The whole catalogue in one answer (no paging).

        ``GET /v1/applications/{application}/automations/recipes``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_AUTOMATIONS_RECIPES_LIST,
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
            _E.A_AUTOMATIONS_RECIPES_LIST,
            _PAGE_A_AUTOMATIONS_RECIPES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountAutomationsRuns:
    """``automations.runs``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        application: str,
        workflow: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["running", "waiting", "completed", "stopped", "failed", "tests"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List an automation's runs, newest first, phones masked: each with who it is for, its status (running, waiting, completed, stopped, failed) and why, and where it is. Filter `status` by a status or `tests`.

        ``GET /v1/applications/{application}/automations/{workflow}/runs``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_AUTOMATIONS_RUNS_LIST,
            path={"application": application, "workflow": workflow},
            given={"page": page, "q": q, "status": status},
            params=AccountAutomationsRunsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        workflow: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["running", "waiting", "completed", "stopped", "failed", "tests"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_AUTOMATIONS_RUNS_LIST,
            _PAGE_A_AUTOMATIONS_RUNS_LIST,
            path={"application": application, "workflow": workflow},
            given={"page": page, "q": q, "status": status},
            params=AccountAutomationsRunsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        workflow: str,
        run: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One run's log: its status, what started it (the order, the cart, the campaign), what it waits for and until when (`waiting`: kind wait, reply or held, and `at`), each line the engine wrote with its message's delivery status, and `next` while it runs or waits.

        ``GET /v1/applications/{application}/automations/{workflow}/runs/{run}``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_AUTOMATIONS_RUNS_SHOW,
            path={"application": application, "workflow": workflow, "run": run},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountAutomations:
    """``automations``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.automations = AccountAutomationsAutomations(client)
        self.recipes = AccountAutomationsRecipes(client)
        self.runs = AccountAutomationsRuns(client)


class AsyncAccountAutomationsAutomations:
    """``automations.automations``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        recipe: Literal["welcome", "cart", "review", "winback"] | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Create an automation, off: from a ready-made one (`recipe`, its draft prefilled) or empty without one. Answers the automation with its draft; then save the draft (automations.automations.update), try it (automations.automations.send_test) and turn it on (automations.automations.on).

        ``POST /v1/applications/{application}/automations``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_CREATE,
            path={"application": application},
            given={"recipe": recipe},
            params=AccountAutomationsAutomationsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete an automation: its live runs stop now, its history stays. Answers ok.

        ``DELETE /v1/applications/{application}/automations/{workflow}``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_DELETE,
            path={"application": application, "workflow": workflow},
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
        """List the application's WhatsApp automations, newest first: each on or off, what it starts on (its trigger), whether the draft differs from what runs, and its last publish.

        ``GET /v1/applications/{application}/automations``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_AUTOMATIONS_AUTOMATIONS_LIST,
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
            _E.A_AUTOMATIONS_AUTOMATIONS_LIST,
            _PAGE_A_AUTOMATIONS_AUTOMATIONS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def off(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn an automation off: no run starts; a waiting run finishes the wait it is in and stops there unless it is on again by then. Answers the automation.

        ``POST /v1/applications/{application}/automations/{workflow}/off``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_OFF,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def on(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn an automation on: the draft is published first when it differs, then runs start from now for each contact its trigger meets, messaging customers. Answers the automation.

        ``POST /v1/applications/{application}/automations/{workflow}/on``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_ON,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def publish(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Publish the draft as the version new runs start on (runs under way keep theirs). Answers the automation; 422 definition_invalid with each problem when it cannot run.

        ``POST /v1/applications/{application}/automations/{workflow}/publish``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_PUBLISH,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send_test(
        self,
        application: str,
        workflow: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Run the draft as it is now on your own Saudi mobile (the token's person), every wait one minute, labelled a test; answers the test run, to read in its log.

        ``POST /v1/applications/{application}/automations/{workflow}/test``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_SEND_TEST,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        workflow: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One automation: its draft and its published definition whole, on or off, its version, what keeps the draft from running (`problems`, each with its step and code), the Salla notice it would repeat, and its last 30 days (live, completed, stopped, failed runs; messages sent).

        ``GET /v1/applications/{application}/automations/{workflow}``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_SHOW,
            path={"application": application, "workflow": workflow},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        workflow: str,
        *,
        definition: Mapping[str, Any],
        name: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save an automation's draft (its trigger, conditions and steps) and its name: nothing is checked beyond the shape, and what runs does not change until it is published. Answers the automation with the draft's problems; once there are none, try it with automations.automations.send_test and publish it with automations.automations.publish (or automations.automations.on).

        ``PUT /v1/applications/{application}/automations/{workflow}``, permission ``automations:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_AUTOMATIONS_UPDATE,
            path={"application": application, "workflow": workflow},
            given={"definition": definition, "name": name},
            params=AccountAutomationsAutomationsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountAutomationsRecipes:
    """``automations.recipes``."""

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
        """List the ready-made automations (welcome, abandoned cart, win-back, review request…) with their trigger, whether this application may use them (the Salla ones need its store) and, when the store's own notice covers the event, that notice (`locked_by`). The whole catalogue in one answer (no paging).

        ``GET /v1/applications/{application}/automations/recipes``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_AUTOMATIONS_RECIPES_LIST,
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
            _E.A_AUTOMATIONS_RECIPES_LIST,
            _PAGE_A_AUTOMATIONS_RECIPES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountAutomationsRuns:
    """``automations.runs``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        application: str,
        workflow: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["running", "waiting", "completed", "stopped", "failed", "tests"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List an automation's runs, newest first, phones masked: each with who it is for, its status (running, waiting, completed, stopped, failed) and why, and where it is. Filter `status` by a status or `tests`.

        ``GET /v1/applications/{application}/automations/{workflow}/runs``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_AUTOMATIONS_RUNS_LIST,
            path={"application": application, "workflow": workflow},
            given={"page": page, "q": q, "status": status},
            params=AccountAutomationsRunsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        workflow: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["running", "waiting", "completed", "stopped", "failed", "tests"]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_AUTOMATIONS_RUNS_LIST,
            _PAGE_A_AUTOMATIONS_RUNS_LIST,
            path={"application": application, "workflow": workflow},
            given={"page": page, "q": q, "status": status},
            params=AccountAutomationsRunsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        workflow: str,
        run: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One run's log: its status, what started it (the order, the cart, the campaign), what it waits for and until when (`waiting`: kind wait, reply or held, and `at`), each line the engine wrote with its message's delivery status, and `next` while it runs or waits.

        ``GET /v1/applications/{application}/automations/{workflow}/runs/{run}``, permission ``automations:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_AUTOMATIONS_RUNS_SHOW,
            path={"application": application, "workflow": workflow, "run": run},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountAutomations:
    """``automations``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.automations = AsyncAccountAutomationsAutomations(client)
        self.recipes = AsyncAccountAutomationsRecipes(client)
        self.runs = AsyncAccountAutomationsRuns(client)
