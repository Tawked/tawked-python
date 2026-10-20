"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountRadeefConversationsCorrectParams,
    AccountRadeefConversationsListParams,
    AccountRadeefFaqsCreateParams,
    AccountRadeefFaqsUpdateParams,
    AccountRadeefFilesApproveParams,
    AccountRadeefFilesCreateParams,
    AccountRadeefNotesCreateParams,
    AccountRadeefNotesGuessParams,
    AccountRadeefNoticesChooseParams,
    AccountRadeefOwnerChangesApplyParams,
    AccountRadeefOwnerChangesDismissParams,
    AccountRadeefOwnerChangesUndoParams,
    AccountRadeefOwnerExamParams,
    AccountRadeefOwnerRehearseParams,
    AccountRadeefOwnerResetParams,
    AccountRadeefOwnerSendParams,
    AccountRadeefPagesCreateParams,
    AccountRadeefPlaygroundPreviewParams,
    AccountRadeefPlaygroundSendParams,
    AccountRadeefReviewApplyParams,
    AccountRadeefScansCreateParams,
    AccountRadeefSettingsUpdateParams,
    AccountRadeefSettingsWhenParams,
    AccountRadeefSetupCharacterParams,
    AccountRadeefSetupLiveParams,
    AccountRadeefSetupReadParams,
    AccountRadeefSourcesSetEnabledParams,
    AccountRadeefStateUpdateParams,
    AccountRadeefTopicsUpdateParams,
    AccountRadeefUnansweredAnswerParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_RADEEF_CONVERSATIONS_LIST,
    _PAGE_A_RADEEF_NOTICES_LIST,
    _PAGE_A_RADEEF_PRODUCTS_LIST,
    _PAGE_A_RADEEF_SOURCES_LIST,
    _PAGE_A_RADEEF_TOPICS_LIST,
    _PAGE_A_RADEEF_UNANSWERED_LIST,
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


class AccountRadeefAgent:
    """``radeef.agent``."""

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
        """Read Radeef (the AI agent answering this application's WhatsApp customers): its state (setup, live, draft, off, paused_budget, paused_balance, locked, unavailable) and why, mode, name, hours mode, what it knows and this month's spend.

        ``GET /v1/applications/{application}/radeef``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_AGENT_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefConversations:
    """``radeef.conversations``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def correct(
        self,
        application: str,
        conversation: str,
        turn: str,
        *,
        answer: str,
        question: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Correct a reply Radeef sent a customer: the `question` in general terms (never the customer's words) and the right `answer` become an FAQ every customer gets from now on; answers the FAQ.

        ``POST /v1/applications/{application}/radeef/conversations/{conversation}/turns/{turn}/correct``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_CONVERSATIONS_CORRECT,
            path={"application": application, "conversation": conversation, "turn": turn},
            given={"answer": answer, "question": question},
            params=AccountRadeefConversationsCorrectParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        outcome: Literal["resolved", "handed_off", "abandoned", "ongoing"]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "30d", "month"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal[
            "keyword",
            "customer_asked",
            "refund",
            "complaint",
            "payment",
            "sensitive",
            "missing_knowledge",
            "guard",
            "order_not_verified",
            "repeated",
            "attachment",
            "reply_cap",
            "hours",
            "budget",
            "balance",
            "busy",
            "delivery",
            "error",
            "returned",
            "stopped",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List Radeef's conversations with customers, newest first, ten a page: who, what they asked first, the outcome (resolved, handed_off, abandoned, ongoing) and the handoff's reason; filter by `outcome`, `reason`, `period` (today, 7d, 30d, month) and `q`.

        ``GET /v1/applications/{application}/radeef/conversations``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_RADEEF_CONVERSATIONS_LIST,
            path={"application": application},
            given={"outcome": outcome, "page": page, "period": period, "q": q, "reason": reason},
            params=AccountRadeefConversationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        outcome: Literal["resolved", "handed_off", "abandoned", "ongoing"]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "30d", "month"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal[
            "keyword",
            "customer_asked",
            "refund",
            "complaint",
            "payment",
            "sensitive",
            "missing_knowledge",
            "guard",
            "order_not_verified",
            "repeated",
            "attachment",
            "reply_cap",
            "hours",
            "budget",
            "balance",
            "busy",
            "delivery",
            "error",
            "returned",
            "stopped",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_RADEEF_CONVERSATIONS_LIST,
            _PAGE_A_RADEEF_CONVERSATIONS_LIST,
            path={"application": application},
            given={"outcome": outcome, "page": page, "period": period, "q": q, "reason": reason},
            params=AccountRadeefConversationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        conversation: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one of Radeef's conversations: the customer, the outcome, and the transcript (the customer's messages, Radeef's replies with how each was made and the sources it used, its notes to the team, the handoff, the close).

        ``GET /v1/applications/{application}/radeef/conversations/{conversation}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_CONVERSATIONS_SHOW,
            path={"application": application, "conversation": conversation},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefFaqs:
    """``radeef.faqs``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        answer: str,
        question: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add an FAQ Radeef answers from (`question`, `answer`); answers the source. Check it with radeef.playground.send.

        ``POST /v1/applications/{application}/radeef/knowledge/faqs``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_FAQS_CREATE,
            path={"application": application},
            given={"answer": answer, "question": question},
            params=AccountRadeefFaqsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete an FAQ (or a correction) from what Radeef knows; answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/faqs/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_FAQS_DELETE,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        source: str,
        *,
        answer: str,
        question: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Correct an FAQ (or a correction) Radeef answers from: its `question` and `answer`; answers the source.

        ``PATCH /v1/applications/{application}/radeef/knowledge/faqs/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_FAQS_UPDATE,
            path={"application": application, "source": source},
            given={"answer": answer, "question": question},
            params=AccountRadeefFaqsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefFiles:
    """``radeef.files``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def approve(
        self,
        application: str,
        source: str,
        *,
        content: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save a file's text (`content`, corrected or as extracted) and approve it, so Radeef reads it from now on; answers the source.

        ``PATCH /v1/applications/{application}/radeef/knowledge/files/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_FILES_APPROVE,
            path={"application": application, "source": source},
            given={"content": content},
            params=AccountRadeefFilesApproveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        file: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload a file for Radeef (multipart `file`: PDF, DOCX, TXT or MD, up to 5 MB); its text is extracted in the background, then waits for approval: answers the file, `state` reading, then review (radeef.files.show, radeef.files.approve).

        ``POST /v1/applications/{application}/radeef/knowledge/files``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_FILES_CREATE,
            path={"application": application},
            given={"file": file},
            params=AccountRadeefFilesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("file",),
        )

    def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a file, its text and what Radeef read from it; answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/files/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_FILES_DELETE,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        source: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read a file of Radeef's with its review: its state, the extracted text to correct and approve, whether its Arabic reads reversed.

        ``GET /v1/applications/{application}/radeef/knowledge/files/{source}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_FILES_SHOW,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefHours:
    """``radeef.hours``."""

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
        """Read the team's week as Radeef reads it from the Tawked Chat inbox (or the suggestion when it holds none), its timezone, and Radeef's hours mode and Ramadan schedule.

        ``GET /v1/applications/{application}/radeef/hours``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_HOURS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefInsights:
    """``radeef.insights``."""

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
        """Read what Radeef did in a `period` (today, 7d, 30d, month): conversations resolved and handed off against the period before, by the hour they started, and why it handed over, most common first.

        ``GET /v1/applications/{application}/radeef/insights``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_INSIGHTS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefKnowledge:
    """``radeef.knowledge``."""

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
        """Read what Radeef knows in counts (pages, confirmed facts, FAQs, files, corrections, products), each topic's state, the sources used most in 30 days, and what it noticed (pages to confirm, disagreements, new pages).

        ``GET /v1/applications/{application}/radeef/knowledge``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_KNOWLEDGE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefNotes:
    """``radeef.notes``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        as_: Literal["topic", "faq"] | str,
        answer: str | NotGiven | None = NOT_GIVEN,
        question: str | NotGiven | None = NOT_GIVEN,
        text: str | NotGiven | None = NOT_GIVEN,
        topic: Literal["shipping", "returns", "payment", "warranty", "contact", "about"]
        | str
        | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Teach Radeef something new: a line added to a topic (`as: topic`, `topic`, `text`) or a question and its answer (`as: faq`, `question`, `answer`, optional `topic`); answers what was saved.

        ``POST /v1/applications/{application}/radeef/knowledge/notes``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_NOTES_CREATE,
            path={"application": application},
            given={"as": as_, "answer": answer, "question": question, "text": text, "topic": topic},
            params=AccountRadeefNotesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def guess(
        self,
        application: str,
        *,
        text: str | NotGiven | None = NOT_GIVEN,
        url: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Before teaching Radeef a line (`text`), read which topic it belongs to; or check a link (`url`) is on the business's own site and can be read. Saves nothing.

        ``POST /v1/applications/{application}/radeef/knowledge/notes/guess``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_NOTES_GUESS,
            path={"application": application},
            given={"text": text, "url": url},
            params=AccountRadeefNotesGuessParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefNotices:
    """``radeef.notices``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def choose(
        self,
        application: str,
        *,
        key: str,
        side: Literal["a", "b"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Settle a disagreement Radeef noticed: the figure of side `a` or `b` of the notice `key` becomes what it knows for sure; answers the chosen figure and the notices left.

        ``POST /v1/applications/{application}/radeef/knowledge/notices/choose``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_NOTICES_CHOOSE,
            path={"application": application},
            given={"key": key, "side": side},
            params=AccountRadeefNoticesChooseParams,
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
        """List what Radeef noticed in its knowledge and waits on the owner: pages to confirm, missing or unconfirmed policies customers asked about, two places disagreeing on a figure (settle with radeef.notices.choose), new pages.

        ``GET /v1/applications/{application}/radeef/knowledge/notices``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_RADEEF_NOTICES_LIST,
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
            _E.A_RADEEF_NOTICES_LIST,
            _PAGE_A_RADEEF_NOTICES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefOwner:
    """``radeef.owner``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def exam(
        self,
        application: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Examine Radeef: ten questions from its own knowledge and hard cases, each answered and judged; queued: answers the thread's message to poll with radeef.owner.message. Missed questions can be answered with radeef.unanswered.answer.

        ``POST /v1/applications/{application}/radeef/owner/exam``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_EXAM,
            path={"application": application},
            given={"count": count},
            params=AccountRadeefOwnerExamParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def message(
        self,
        application: str,
        message: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one message of the person's owner thread again: a rehearsal or an exam fills its message while it runs, so poll it until it is done.

        ``GET /v1/applications/{application}/radeef/owner/messages/{message}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_MESSAGE,
            path={"application": application, "message": message},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def rehearse(
        self,
        application: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Rehearse Radeef on up to three (`count`) real questions customers asked, answered as a customer would be answered; queued: answers the thread's message to poll with radeef.owner.message.

        ``POST /v1/applications/{application}/radeef/owner/rehearse``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_REHEARSE,
            path={"application": application},
            given={"count": count},
            params=AccountRadeefOwnerRehearseParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def reset(
        self,
        application: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a new owner thread with Radeef (the open one is closed); answers the fresh brief.

        ``POST /v1/applications/{application}/radeef/owner/reset``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_RESET,
            path={"application": application},
            given={"count": count},
            params=AccountRadeefOwnerResetParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send(
        self,
        application: str,
        *,
        text: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Talk with Radeef as its owner (`text`: ask what it knows, how it would answer, or tell it something to learn); answers its reply and any change cards it proposes (apply them with radeef.owner_changes.apply).

        ``POST /v1/applications/{application}/radeef/owner/messages``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_SEND,
            path={"application": application},
            given={"text": text},
            params=AccountRadeefOwnerSendParams,
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
        """Read owner mode: the brief of what Radeef knows and lacks, the person's open thread with Radeef, the change cards waiting to be applied, and the messages left.

        ``GET /v1/applications/{application}/radeef/owner``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefOwnerChanges:
    """``radeef.owner_changes``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def apply(
        self,
        application: str,
        change: str,
        *,
        edits: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Apply a change card Radeef proposed in owner mode (optionally with `edits` to its question, answer, topic, text, to or word); answers the card, applied.

        ``POST /v1/applications/{application}/radeef/owner/changes/{change}/apply``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_CHANGES_APPLY,
            path={"application": application, "change": change},
            given={"edits": edits},
            params=AccountRadeefOwnerChangesApplyParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def dismiss(
        self,
        application: str,
        change: str,
        *,
        edits: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Dismiss a change card Radeef proposed in owner mode; answers the card.

        ``POST /v1/applications/{application}/radeef/owner/changes/{change}/dismiss``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_CHANGES_DISMISS,
            path={"application": application, "change": change},
            given={"edits": edits},
            params=AccountRadeefOwnerChangesDismissParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def undo(
        self,
        application: str,
        change: str,
        *,
        edits: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Undo an applied change card: the value before is written back, while what it wrote still stands; answers the card.

        ``POST /v1/applications/{application}/radeef/owner/changes/{change}/undo``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_OWNER_CHANGES_UNDO,
            path={"application": application, "change": change},
            given={"edits": edits},
            params=AccountRadeefOwnerChangesUndoParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefPages:
    """``radeef.pages``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        url: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a page of the business's website for Radeef to read (`url`, https); it is read in the background: answers the source, `state` reading until then (radeef.sources.show).

        ``POST /v1/applications/{application}/radeef/knowledge/pages``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PAGES_CREATE,
            path={"application": application},
            given={"url": url},
            params=AccountRadeefPagesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a website page and what Radeef read from it; answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/pages/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_PAGES_DELETE,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def sync(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read a website page of Radeef's again now, in the background; answers the source.

        ``POST /v1/applications/{application}/radeef/knowledge/pages/{source}/sync``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PAGES_SYNC,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefPlayground:
    """``radeef.playground``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def preview(
        self,
        application: str,
        *,
        text: str,
        topic: Literal["shipping", "returns", "payment", "warranty", "contact", "about", "other"]
        | str,
        question: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Try a topic's text before saving it: Radeef answers `question` (else the question customers ask most on that `topic`) from `text` as typed; answers the reply and the question. Nothing is saved or sent.

        ``POST /v1/applications/{application}/radeef/playground/preview``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_PREVIEW,
            path={"application": application},
            given={"text": text, "topic": topic, "question": question},
            params=AccountRadeefPlaygroundPreviewParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def reset(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a new test conversation in the playground (the person's open one is closed); answers ok.

        ``POST /v1/applications/{application}/radeef/playground/reset``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_RESET,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send(
        self,
        application: str,
        *,
        text: str,
        phone: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Write to Radeef as a customer (`text`; `phone` a real customer's number to try order questions) and get how it would answer: the reply parts or the handoff to the team with its reason, the sources and tools it used, the `turn_id`. Nothing is sent to anyone, nothing is charged.

        ``POST /v1/applications/{application}/radeef/playground/messages``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_SEND,
            path={"application": application},
            given={"text": text, "phone": phone},
            params=AccountRadeefPlaygroundSendParams,
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
        """Read the playground: the day's messages left, whether Radeef knows anything yet, whether a real customer's phone may be used for order questions, suggested questions (from its knowledge, and hard cases), and the person's open test conversation.

        ``GET /v1/applications/{application}/radeef/playground``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefProducts:
    """``radeef.products``."""

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
        """List the store's products Radeef knows (Salla or Zid), ten a page, searched by name or code with `q`.

        ``GET /v1/applications/{application}/radeef/knowledge/products``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_RADEEF_PRODUCTS_LIST,
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
            _E.A_RADEEF_PRODUCTS_LIST,
            _PAGE_A_RADEEF_PRODUCTS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefProposals:
    """``radeef.proposals``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def reject(
        self,
        application: str,
        proposal: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set aside one proposal of a reading (it stays among the set-aside ones, to restore); answers its id and status.

        ``POST /v1/applications/{application}/radeef/knowledge/review/{proposal}/reject``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PROPOSALS_REJECT,
            path={"application": application, "proposal": proposal},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def restore(
        self,
        application: str,
        proposal: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Bring a set-aside proposal back to the review; answers its id and status.

        ``POST /v1/applications/{application}/radeef/knowledge/review/{proposal}/restore``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_PROPOSALS_RESTORE,
            path={"application": application, "proposal": proposal},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefReview:
    """``radeef.review``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def apply(
        self,
        application: str,
        *,
        add_pages: Sequence[str] | NotGiven = NOT_GIVEN,
        edits: Sequence[Any] | NotGiven = NOT_GIVEN,
        follow: Sequence[str] | NotGiven = NOT_GIVEN,
        kept: Sequence[str] | NotGiven = NOT_GIVEN,
        merge: Sequence[Literal["append", "replace"] | str] | NotGiven = NOT_GIVEN,
        rejected: Sequence[str] | NotGiven = NOT_GIVEN,
        scan: str | NotGiven | None = NOT_GIVEN,
        vanished: Sequence[Literal["keep", "delete"] | str] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Apply the owner's choices on what a reading found: `kept` (proposal ids that become knowledge), `rejected`, `edits`, `merge` (append or replace a topic's text), `follow` (pages to keep reading), `add_pages`, `vanished` (keep or delete); answers the result and the review left.

        ``POST /v1/applications/{application}/radeef/knowledge/review``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_REVIEW_APPLY,
            path={"application": application},
            given={
                "add_pages": add_pages,
                "edits": edits,
                "follow": follow,
                "kept": kept,
                "merge": merge,
                "rejected": rejected,
                "scan": scan,
                "vanished": vanished,
            },
            params=AccountRadeefReviewApplyParams,
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
        """Read what readings of the site found and wait for the owner: the proposals by topic with their facts and quotes, how sure each is, the text Radeef holds there, the set-aside ones, and a re-read's new and vanished pages.

        ``GET /v1/applications/{application}/radeef/knowledge/review``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_REVIEW_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefScans:
    """``radeef.scans``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def create(
        self,
        application: str,
        *,
        url: str,
        mine: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start reading the business's website for Radeef (`url`, `mine: true` for a site that is not the store's or the reviewed one); answers the reading. Poll radeef.scans.show, then radeef.review.show.

        ``POST /v1/applications/{application}/radeef/knowledge/scans``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SCANS_CREATE,
            path={"application": application},
            given={"url": url, "mine": mine},
            params=AccountRadeefScansCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def resume(
        self,
        application: str,
        scan: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Resume a stopped or failed reading of the site from where it stopped; answers the reading.

        ``POST /v1/applications/{application}/radeef/knowledge/scans/{scan}/resume``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SCANS_RESUME,
            path={"application": application, "scan": scan},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        scan: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read a reading of the site: its status (running until done, stopped or failed), its counts, each page with its state, and what it proposed.

        ``GET /v1/applications/{application}/radeef/knowledge/scans/{scan}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_SCANS_SHOW,
            path={"application": application, "scan": scan},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def stop(
        self,
        application: str,
        scan: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Stop a reading of the site that is running; what it read so far stays for review. Answers the reading.

        ``POST /v1/applications/{application}/radeef/knowledge/scans/{scan}/stop``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SCANS_STOP,
            path={"application": application, "scan": scan},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def summary(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read what a reading of the site would start from (the address and where it came from), the latest reading, and the readings left today.

        ``GET /v1/applications/{application}/radeef/knowledge/scans``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_SCANS_SUMMARY,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefSettings:
    """``radeef.settings``."""

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
        """Read Radeef's settings: every section (persona, pace, handoff, hours, limits, store) in the shape radeef.settings.update takes, the mode, the character and the price per conversation.

        ``GET /v1/applications/{application}/radeef/settings``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETTINGS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        section: str,
        *,
        assign_mode: Literal["auto", "member", "none"] | str,
        csat: bool,
        emoji: Literal["none", "few"] | str,
        etiquette: bool,
        idle_minutes: int,
        intro: Literal["warm", "brief"] | str,
        mode: Literal["always", "outside", "inside"] | str,
        orders: bool,
        persona_name: str,
        products: bool,
        read_receipts: bool,
        register: Literal["saudi", "msa", "mirror"] | str,
        reply_cap: int,
        reply_length: Literal["short", "standard"] | str,
        speed: Literal["fast", "natural", "relaxed"] | str,
        split: bool,
        strict: bool,
        topics: Mapping[str, Any],
        typing: bool,
        assign_member_id: str | NotGiven | None = NOT_GIVEN,
        custom_enabled: bool | NotGiven = NOT_GIVEN,
        custom_topics: Sequence[str] | NotGiven = NOT_GIVEN,
        keywords: Sequence[str] | NotGiven = NOT_GIVEN,
        keywords_enabled: bool | NotGiven = NOT_GIVEN,
        messages: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        monthly_cap_halalas: int | NotGiven | None = NOT_GIVEN,
        order_status: bool | NotGiven = NOT_GIVEN,
        persona_name_en: str | NotGiven | None = NOT_GIVEN,
        ramadan: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        return_after_hours: Literal["12", "24", "48"] | str | int | NotGiven | None = NOT_GIVEN,
        week: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save one section of Radeef's settings (`persona`, `pace`, `handoff`, `hours`, `limits` or `store`), the whole section as radeef.settings.show answers it; answers the settings.

        ``PUT /v1/applications/{application}/radeef/settings/{section}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETTINGS_UPDATE,
            path={"application": application, "section": section},
            given={
                "assign_mode": assign_mode,
                "csat": csat,
                "emoji": emoji,
                "etiquette": etiquette,
                "idle_minutes": idle_minutes,
                "intro": intro,
                "mode": mode,
                "orders": orders,
                "persona_name": persona_name,
                "products": products,
                "read_receipts": read_receipts,
                "register": register,
                "reply_cap": reply_cap,
                "reply_length": reply_length,
                "speed": speed,
                "split": split,
                "strict": strict,
                "topics": topics,
                "typing": typing,
                "assign_member_id": assign_member_id,
                "custom_enabled": custom_enabled,
                "custom_topics": custom_topics,
                "keywords": keywords,
                "keywords_enabled": keywords_enabled,
                "messages": messages,
                "monthly_cap_halalas": monthly_cap_halalas,
                "order_status": order_status,
                "persona_name_en": persona_name_en,
                "ramadan": ramadan,
                "return_after_hours": return_after_hours,
                "week": week,
            },
            params=AccountRadeefSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def when(
        self,
        application: str,
        *,
        hours_mode: Literal["always", "outside", "inside"] | str,
        mode: Literal["live", "draft"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set when Radeef answers: `hours_mode` (always, outside the team's hours, inside them) with `mode` (live answers customers, draft suggests to the team); answers Radeef.

        ``PUT /v1/applications/{application}/radeef/settings/when``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETTINGS_WHEN,
            path={"application": application},
            given={"hours_mode": hours_mode, "mode": mode},
            params=AccountRadeefSettingsWhenParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefSetup:
    """``radeef.setup``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def character(
        self,
        application: str,
        *,
        character: Literal["close", "formal", "brief", "mirror"] | str,
        persona_name: str,
        persona_name_en: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Choose Radeef's character from the deck (`character`) and its name (`persona_name`, optional `persona_name_en`); answers Radeef.

        ``PUT /v1/applications/{application}/radeef/setup/character``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETUP_CHARACTER,
            path={"application": application},
            given={
                "character": character,
                "persona_name": persona_name,
                "persona_name_en": persona_name_en,
            },
            params=AccountRadeefSetupCharacterParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def confirm_fact(
        self,
        application: str,
        topic: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm a fact of the setup's brief as right: the topic's text (shipping, returns, payment, warranty, contact, about) stands as Radeef holds it; answers the setup.

        ``POST /v1/applications/{application}/radeef/setup/facts/{topic}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETUP_CONFIRM_FACT,
            path={"application": application, "topic": topic},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def live(
        self,
        application: str,
        *,
        choice: Literal["always", "outside", "suggest"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn Radeef on to answer customers: `choice` always (every hour), outside (only outside the team's hours) or suggest (draft replies for the team only); answers Radeef with its state.

        ``POST /v1/applications/{application}/radeef/setup/live``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETUP_LIVE,
            path={"application": application},
            given={"choice": choice},
            params=AccountRadeefSetupLiveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def read(
        self,
        application: str,
        *,
        url: str,
        mine: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start reading the business's website for Radeef (`url`, `mine: true` when it is not the store's or the reviewed site); answers the reading, which runs for a few minutes: poll radeef.scans.show, then review what it found with radeef.review.show.

        ``POST /v1/applications/{application}/radeef/setup/read``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETUP_READ,
            path={"application": application},
            given={"url": url, "mine": mine},
            params=AccountRadeefSetupReadParams,
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
        """Read Radeef's setup: the current move (read, character, meet), the site address to read and the latest reading, the character deck and the chosen one, the brief of what it learned, and how it may go live.

        ``GET /v1/applications/{application}/radeef/setup``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_SETUP_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefSources:
    """``radeef.sources``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def confirm(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm a read website page's text as facts Radeef may state (prices, policies), not just describe; answers the source.

        ``POST /v1/applications/{application}/radeef/knowledge/sources/{source}/confirm``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SOURCES_CONFIRM,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a source from what Radeef knows (any kind); a read page's address is never read again. Answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/sources/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_SOURCES_DELETE,
            path={"application": application, "source": source},
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
        """List what Radeef knows from, ten a page: FAQs, corrections, website pages and files, each with its kind, title, tier, topic, state (confirmed, reference, needs_confirm, reading, review, unreadable, gone, off) and uses; filter by `type`, `tier`, `topic`, `state`, `q`.

        ``GET /v1/applications/{application}/radeef/knowledge/sources``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_RADEEF_SOURCES_LIST,
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
            _E.A_RADEEF_SOURCES_LIST,
            _PAGE_A_RADEEF_SOURCES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def set_enabled(
        self,
        application: str,
        source: str,
        *,
        enabled: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Stop Radeef using a source (`enabled: false`) or use it again (`enabled: true`), without deleting it; answers the source.

        ``PUT /v1/applications/{application}/radeef/knowledge/sources/{source}/enabled``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_SOURCES_SET_ENABLED,
            path={"application": application, "source": source},
            given={"enabled": enabled},
            params=AccountRadeefSourcesSetEnabledParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        source: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one source of Radeef's knowledge (an FAQ, a correction, a page or a file): its state, what Radeef takes from it, its text or question and answer, passages, versions, the customer questions it answered and any disagreement.

        ``GET /v1/applications/{application}/radeef/knowledge/sources/{source}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_SOURCES_SHOW,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeefState:
    """``radeef.state``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def update(
        self,
        application: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        mode: Literal["live", "draft"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn Radeef on (`enabled: true`, optionally with `mode` live or draft) or off, or switch only its `mode`; answers Radeef with its new state.

        ``PUT /v1/applications/{application}/radeef/state``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_RADEEF_STATE_UPDATE,
            path={"application": application},
            given={"enabled": enabled, "mode": mode},
            params=AccountRadeefStateUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefStore:
    """``radeef.store``."""

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
        """Read the store Radeef answers from (Salla or Zid): whether it is connected, its products and when they were last read, and which store tools (orders, order status, products) are on.

        ``GET /v1/applications/{application}/radeef/store``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_STORE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def sync(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the store's product catalogue again for Radeef now (Salla or Zid), queued; answers ok. Follow it with radeef.store.show.

        ``POST /v1/applications/{application}/radeef/store/sync``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_STORE_SYNC,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefTopics:
    """``radeef.topics``."""

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
        """List the topics Radeef knows the business by (shipping, returns, payment, warranty, contact, about), each with its text, its state (known, incomplete, unknown), what is missing and what customers asked about it. The six topics in one answer (no paging).

        ``GET /v1/applications/{application}/radeef/knowledge/topics``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_RADEEF_TOPICS_LIST,
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
            _E.A_RADEEF_TOPICS_LIST,
            _PAGE_A_RADEEF_TOPICS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        topic: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one topic of Radeef's knowledge: its text and state, what is missing, where each line came from, what customers asked about it in 30 days, its FAQs and a change a re-read proposes.

        ``GET /v1/applications/{application}/radeef/knowledge/topics/{topic}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_RADEEF_TOPICS_SHOW,
            path={"application": application, "topic": topic},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        topic: str,
        *,
        text: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace a topic's text (`text`, null or empty clears it): what Radeef says about shipping, returns, payment, warranty, contact, or the business (about); answers the topic.

        ``PUT /v1/applications/{application}/radeef/knowledge/topics/{topic}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_TOPICS_UPDATE,
            path={"application": application, "topic": topic},
            given={"text": text},
            params=AccountRadeefTopicsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountRadeefUnanswered:
    """``radeef.unanswered``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def answer(
        self,
        application: str,
        turn: str,
        *,
        answer: str,
        question: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Answer a question Radeef could not (its `turn_id`, from radeef.unanswered.list, a playground reply or an exam): the `answer` (and optionally the `question` reworded) becomes an FAQ, and every customer who asked it is marked answered; answers the FAQ and how many questions it closed.

        ``POST /v1/applications/{application}/radeef/unanswered/{turn}/answer``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_RADEEF_UNANSWERED_ANSWER,
            path={"application": application, "turn": turn},
            given={"answer": answer, "question": question},
            params=AccountRadeefUnansweredAnswerParams,
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
        """List the questions Radeef could not answer and handed to the team, grouped, the most asked first: the question, how many asked it, its other wordings, its topic, and the `turn_id` to answer it with radeef.unanswered.answer.

        ``GET /v1/applications/{application}/radeef/unanswered``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_RADEEF_UNANSWERED_LIST,
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
            _E.A_RADEEF_UNANSWERED_LIST,
            _PAGE_A_RADEEF_UNANSWERED_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountRadeef:
    """``radeef``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.agent = AccountRadeefAgent(client)
        self.conversations = AccountRadeefConversations(client)
        self.faqs = AccountRadeefFaqs(client)
        self.files = AccountRadeefFiles(client)
        self.hours = AccountRadeefHours(client)
        self.insights = AccountRadeefInsights(client)
        self.knowledge = AccountRadeefKnowledge(client)
        self.notes = AccountRadeefNotes(client)
        self.notices = AccountRadeefNotices(client)
        self.owner = AccountRadeefOwner(client)
        self.owner_changes = AccountRadeefOwnerChanges(client)
        self.pages = AccountRadeefPages(client)
        self.playground = AccountRadeefPlayground(client)
        self.products = AccountRadeefProducts(client)
        self.proposals = AccountRadeefProposals(client)
        self.review = AccountRadeefReview(client)
        self.scans = AccountRadeefScans(client)
        self.settings = AccountRadeefSettings(client)
        self.setup = AccountRadeefSetup(client)
        self.sources = AccountRadeefSources(client)
        self.state = AccountRadeefState(client)
        self.store = AccountRadeefStore(client)
        self.topics = AccountRadeefTopics(client)
        self.unanswered = AccountRadeefUnanswered(client)


class AsyncAccountRadeefAgent:
    """``radeef.agent``."""

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
        """Read Radeef (the AI agent answering this application's WhatsApp customers): its state (setup, live, draft, off, paused_budget, paused_balance, locked, unavailable) and why, mode, name, hours mode, what it knows and this month's spend.

        ``GET /v1/applications/{application}/radeef``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_AGENT_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefConversations:
    """``radeef.conversations``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def correct(
        self,
        application: str,
        conversation: str,
        turn: str,
        *,
        answer: str,
        question: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Correct a reply Radeef sent a customer: the `question` in general terms (never the customer's words) and the right `answer` become an FAQ every customer gets from now on; answers the FAQ.

        ``POST /v1/applications/{application}/radeef/conversations/{conversation}/turns/{turn}/correct``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_CONVERSATIONS_CORRECT,
            path={"application": application, "conversation": conversation, "turn": turn},
            given={"answer": answer, "question": question},
            params=AccountRadeefConversationsCorrectParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        outcome: Literal["resolved", "handed_off", "abandoned", "ongoing"]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "30d", "month"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal[
            "keyword",
            "customer_asked",
            "refund",
            "complaint",
            "payment",
            "sensitive",
            "missing_knowledge",
            "guard",
            "order_not_verified",
            "repeated",
            "attachment",
            "reply_cap",
            "hours",
            "budget",
            "balance",
            "busy",
            "delivery",
            "error",
            "returned",
            "stopped",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List Radeef's conversations with customers, newest first, ten a page: who, what they asked first, the outcome (resolved, handed_off, abandoned, ongoing) and the handoff's reason; filter by `outcome`, `reason`, `period` (today, 7d, 30d, month) and `q`.

        ``GET /v1/applications/{application}/radeef/conversations``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_RADEEF_CONVERSATIONS_LIST,
            path={"application": application},
            given={"outcome": outcome, "page": page, "period": period, "q": q, "reason": reason},
            params=AccountRadeefConversationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        *,
        outcome: Literal["resolved", "handed_off", "abandoned", "ongoing"]
        | str
        | NotGiven = NOT_GIVEN,
        page: int | NotGiven = NOT_GIVEN,
        period: Literal["today", "7d", "30d", "month"] | str | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        reason: Literal[
            "keyword",
            "customer_asked",
            "refund",
            "complaint",
            "payment",
            "sensitive",
            "missing_knowledge",
            "guard",
            "order_not_verified",
            "repeated",
            "attachment",
            "reply_cap",
            "hours",
            "budget",
            "balance",
            "busy",
            "delivery",
            "error",
            "returned",
            "stopped",
        ]
        | str
        | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_RADEEF_CONVERSATIONS_LIST,
            _PAGE_A_RADEEF_CONVERSATIONS_LIST,
            path={"application": application},
            given={"outcome": outcome, "page": page, "period": period, "q": q, "reason": reason},
            params=AccountRadeefConversationsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        conversation: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one of Radeef's conversations: the customer, the outcome, and the transcript (the customer's messages, Radeef's replies with how each was made and the sources it used, its notes to the team, the handoff, the close).

        ``GET /v1/applications/{application}/radeef/conversations/{conversation}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_CONVERSATIONS_SHOW,
            path={"application": application, "conversation": conversation},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefFaqs:
    """``radeef.faqs``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        answer: str,
        question: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add an FAQ Radeef answers from (`question`, `answer`); answers the source. Check it with radeef.playground.send.

        ``POST /v1/applications/{application}/radeef/knowledge/faqs``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FAQS_CREATE,
            path={"application": application},
            given={"answer": answer, "question": question},
            params=AccountRadeefFaqsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete an FAQ (or a correction) from what Radeef knows; answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/faqs/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FAQS_DELETE,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        source: str,
        *,
        answer: str,
        question: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Correct an FAQ (or a correction) Radeef answers from: its `question` and `answer`; answers the source.

        ``PATCH /v1/applications/{application}/radeef/knowledge/faqs/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FAQS_UPDATE,
            path={"application": application, "source": source},
            given={"answer": answer, "question": question},
            params=AccountRadeefFaqsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefFiles:
    """``radeef.files``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def approve(
        self,
        application: str,
        source: str,
        *,
        content: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save a file's text (`content`, corrected or as extracted) and approve it, so Radeef reads it from now on; answers the source.

        ``PATCH /v1/applications/{application}/radeef/knowledge/files/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FILES_APPROVE,
            path={"application": application, "source": source},
            given={"content": content},
            params=AccountRadeefFilesApproveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        file: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload a file for Radeef (multipart `file`: PDF, DOCX, TXT or MD, up to 5 MB); its text is extracted in the background, then waits for approval: answers the file, `state` reading, then review (radeef.files.show, radeef.files.approve).

        ``POST /v1/applications/{application}/radeef/knowledge/files``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FILES_CREATE,
            path={"application": application},
            given={"file": file},
            params=AccountRadeefFilesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("file",),
        )

    async def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a file, its text and what Radeef read from it; answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/files/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FILES_DELETE,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        source: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read a file of Radeef's with its review: its state, the extracted text to correct and approve, whether its Arabic reads reversed.

        ``GET /v1/applications/{application}/radeef/knowledge/files/{source}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_FILES_SHOW,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefHours:
    """``radeef.hours``."""

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
        """Read the team's week as Radeef reads it from the Tawked Chat inbox (or the suggestion when it holds none), its timezone, and Radeef's hours mode and Ramadan schedule.

        ``GET /v1/applications/{application}/radeef/hours``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_HOURS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefInsights:
    """``radeef.insights``."""

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
        """Read what Radeef did in a `period` (today, 7d, 30d, month): conversations resolved and handed off against the period before, by the hour they started, and why it handed over, most common first.

        ``GET /v1/applications/{application}/radeef/insights``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_INSIGHTS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefKnowledge:
    """``radeef.knowledge``."""

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
        """Read what Radeef knows in counts (pages, confirmed facts, FAQs, files, corrections, products), each topic's state, the sources used most in 30 days, and what it noticed (pages to confirm, disagreements, new pages).

        ``GET /v1/applications/{application}/radeef/knowledge``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_KNOWLEDGE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefNotes:
    """``radeef.notes``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        as_: Literal["topic", "faq"] | str,
        answer: str | NotGiven | None = NOT_GIVEN,
        question: str | NotGiven | None = NOT_GIVEN,
        text: str | NotGiven | None = NOT_GIVEN,
        topic: Literal["shipping", "returns", "payment", "warranty", "contact", "about"]
        | str
        | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Teach Radeef something new: a line added to a topic (`as: topic`, `topic`, `text`) or a question and its answer (`as: faq`, `question`, `answer`, optional `topic`); answers what was saved.

        ``POST /v1/applications/{application}/radeef/knowledge/notes``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_NOTES_CREATE,
            path={"application": application},
            given={"as": as_, "answer": answer, "question": question, "text": text, "topic": topic},
            params=AccountRadeefNotesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def guess(
        self,
        application: str,
        *,
        text: str | NotGiven | None = NOT_GIVEN,
        url: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Before teaching Radeef a line (`text`), read which topic it belongs to; or check a link (`url`) is on the business's own site and can be read. Saves nothing.

        ``POST /v1/applications/{application}/radeef/knowledge/notes/guess``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_NOTES_GUESS,
            path={"application": application},
            given={"text": text, "url": url},
            params=AccountRadeefNotesGuessParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefNotices:
    """``radeef.notices``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def choose(
        self,
        application: str,
        *,
        key: str,
        side: Literal["a", "b"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Settle a disagreement Radeef noticed: the figure of side `a` or `b` of the notice `key` becomes what it knows for sure; answers the chosen figure and the notices left.

        ``POST /v1/applications/{application}/radeef/knowledge/notices/choose``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_NOTICES_CHOOSE,
            path={"application": application},
            given={"key": key, "side": side},
            params=AccountRadeefNoticesChooseParams,
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
        """List what Radeef noticed in its knowledge and waits on the owner: pages to confirm, missing or unconfirmed policies customers asked about, two places disagreeing on a figure (settle with radeef.notices.choose), new pages.

        ``GET /v1/applications/{application}/radeef/knowledge/notices``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_RADEEF_NOTICES_LIST,
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
            _E.A_RADEEF_NOTICES_LIST,
            _PAGE_A_RADEEF_NOTICES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefOwner:
    """``radeef.owner``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def exam(
        self,
        application: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Examine Radeef: ten questions from its own knowledge and hard cases, each answered and judged; queued: answers the thread's message to poll with radeef.owner.message. Missed questions can be answered with radeef.unanswered.answer.

        ``POST /v1/applications/{application}/radeef/owner/exam``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_EXAM,
            path={"application": application},
            given={"count": count},
            params=AccountRadeefOwnerExamParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def message(
        self,
        application: str,
        message: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one message of the person's owner thread again: a rehearsal or an exam fills its message while it runs, so poll it until it is done.

        ``GET /v1/applications/{application}/radeef/owner/messages/{message}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_MESSAGE,
            path={"application": application, "message": message},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def rehearse(
        self,
        application: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Rehearse Radeef on up to three (`count`) real questions customers asked, answered as a customer would be answered; queued: answers the thread's message to poll with radeef.owner.message.

        ``POST /v1/applications/{application}/radeef/owner/rehearse``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_REHEARSE,
            path={"application": application},
            given={"count": count},
            params=AccountRadeefOwnerRehearseParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def reset(
        self,
        application: str,
        *,
        count: int | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a new owner thread with Radeef (the open one is closed); answers the fresh brief.

        ``POST /v1/applications/{application}/radeef/owner/reset``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_RESET,
            path={"application": application},
            given={"count": count},
            params=AccountRadeefOwnerResetParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send(
        self,
        application: str,
        *,
        text: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Talk with Radeef as its owner (`text`: ask what it knows, how it would answer, or tell it something to learn); answers its reply and any change cards it proposes (apply them with radeef.owner_changes.apply).

        ``POST /v1/applications/{application}/radeef/owner/messages``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_SEND,
            path={"application": application},
            given={"text": text},
            params=AccountRadeefOwnerSendParams,
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
        """Read owner mode: the brief of what Radeef knows and lacks, the person's open thread with Radeef, the change cards waiting to be applied, and the messages left.

        ``GET /v1/applications/{application}/radeef/owner``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefOwnerChanges:
    """``radeef.owner_changes``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def apply(
        self,
        application: str,
        change: str,
        *,
        edits: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Apply a change card Radeef proposed in owner mode (optionally with `edits` to its question, answer, topic, text, to or word); answers the card, applied.

        ``POST /v1/applications/{application}/radeef/owner/changes/{change}/apply``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_CHANGES_APPLY,
            path={"application": application, "change": change},
            given={"edits": edits},
            params=AccountRadeefOwnerChangesApplyParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def dismiss(
        self,
        application: str,
        change: str,
        *,
        edits: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Dismiss a change card Radeef proposed in owner mode; answers the card.

        ``POST /v1/applications/{application}/radeef/owner/changes/{change}/dismiss``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_CHANGES_DISMISS,
            path={"application": application, "change": change},
            given={"edits": edits},
            params=AccountRadeefOwnerChangesDismissParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def undo(
        self,
        application: str,
        change: str,
        *,
        edits: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Undo an applied change card: the value before is written back, while what it wrote still stands; answers the card.

        ``POST /v1/applications/{application}/radeef/owner/changes/{change}/undo``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_OWNER_CHANGES_UNDO,
            path={"application": application, "change": change},
            given={"edits": edits},
            params=AccountRadeefOwnerChangesUndoParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefPages:
    """``radeef.pages``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        url: str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Add a page of the business's website for Radeef to read (`url`, https); it is read in the background: answers the source, `state` reading until then (radeef.sources.show).

        ``POST /v1/applications/{application}/radeef/knowledge/pages``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PAGES_CREATE,
            path={"application": application},
            given={"url": url},
            params=AccountRadeefPagesCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a website page and what Radeef read from it; answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/pages/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PAGES_DELETE,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def sync(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read a website page of Radeef's again now, in the background; answers the source.

        ``POST /v1/applications/{application}/radeef/knowledge/pages/{source}/sync``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PAGES_SYNC,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefPlayground:
    """``radeef.playground``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def preview(
        self,
        application: str,
        *,
        text: str,
        topic: Literal["shipping", "returns", "payment", "warranty", "contact", "about", "other"]
        | str,
        question: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Try a topic's text before saving it: Radeef answers `question` (else the question customers ask most on that `topic`) from `text` as typed; answers the reply and the question. Nothing is saved or sent.

        ``POST /v1/applications/{application}/radeef/playground/preview``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_PREVIEW,
            path={"application": application},
            given={"text": text, "topic": topic, "question": question},
            params=AccountRadeefPlaygroundPreviewParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def reset(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start a new test conversation in the playground (the person's open one is closed); answers ok.

        ``POST /v1/applications/{application}/radeef/playground/reset``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_RESET,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send(
        self,
        application: str,
        *,
        text: str,
        phone: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Write to Radeef as a customer (`text`; `phone` a real customer's number to try order questions) and get how it would answer: the reply parts or the handoff to the team with its reason, the sources and tools it used, the `turn_id`. Nothing is sent to anyone, nothing is charged.

        ``POST /v1/applications/{application}/radeef/playground/messages``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_SEND,
            path={"application": application},
            given={"text": text, "phone": phone},
            params=AccountRadeefPlaygroundSendParams,
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
        """Read the playground: the day's messages left, whether Radeef knows anything yet, whether a real customer's phone may be used for order questions, suggested questions (from its knowledge, and hard cases), and the person's open test conversation.

        ``GET /v1/applications/{application}/radeef/playground``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PLAYGROUND_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefProducts:
    """``radeef.products``."""

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
        """List the store's products Radeef knows (Salla or Zid), ten a page, searched by name or code with `q`.

        ``GET /v1/applications/{application}/radeef/knowledge/products``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_RADEEF_PRODUCTS_LIST,
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
            _E.A_RADEEF_PRODUCTS_LIST,
            _PAGE_A_RADEEF_PRODUCTS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefProposals:
    """``radeef.proposals``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def reject(
        self,
        application: str,
        proposal: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set aside one proposal of a reading (it stays among the set-aside ones, to restore); answers its id and status.

        ``POST /v1/applications/{application}/radeef/knowledge/review/{proposal}/reject``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PROPOSALS_REJECT,
            path={"application": application, "proposal": proposal},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def restore(
        self,
        application: str,
        proposal: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Bring a set-aside proposal back to the review; answers its id and status.

        ``POST /v1/applications/{application}/radeef/knowledge/review/{proposal}/restore``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_PROPOSALS_RESTORE,
            path={"application": application, "proposal": proposal},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefReview:
    """``radeef.review``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def apply(
        self,
        application: str,
        *,
        add_pages: Sequence[str] | NotGiven = NOT_GIVEN,
        edits: Sequence[Any] | NotGiven = NOT_GIVEN,
        follow: Sequence[str] | NotGiven = NOT_GIVEN,
        kept: Sequence[str] | NotGiven = NOT_GIVEN,
        merge: Sequence[Literal["append", "replace"] | str] | NotGiven = NOT_GIVEN,
        rejected: Sequence[str] | NotGiven = NOT_GIVEN,
        scan: str | NotGiven | None = NOT_GIVEN,
        vanished: Sequence[Literal["keep", "delete"] | str] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Apply the owner's choices on what a reading found: `kept` (proposal ids that become knowledge), `rejected`, `edits`, `merge` (append or replace a topic's text), `follow` (pages to keep reading), `add_pages`, `vanished` (keep or delete); answers the result and the review left.

        ``POST /v1/applications/{application}/radeef/knowledge/review``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_REVIEW_APPLY,
            path={"application": application},
            given={
                "add_pages": add_pages,
                "edits": edits,
                "follow": follow,
                "kept": kept,
                "merge": merge,
                "rejected": rejected,
                "scan": scan,
                "vanished": vanished,
            },
            params=AccountRadeefReviewApplyParams,
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
        """Read what readings of the site found and wait for the owner: the proposals by topic with their facts and quotes, how sure each is, the text Radeef holds there, the set-aside ones, and a re-read's new and vanished pages.

        ``GET /v1/applications/{application}/radeef/knowledge/review``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_REVIEW_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefScans:
    """``radeef.scans``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def create(
        self,
        application: str,
        *,
        url: str,
        mine: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start reading the business's website for Radeef (`url`, `mine: true` for a site that is not the store's or the reviewed one); answers the reading. Poll radeef.scans.show, then radeef.review.show.

        ``POST /v1/applications/{application}/radeef/knowledge/scans``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SCANS_CREATE,
            path={"application": application},
            given={"url": url, "mine": mine},
            params=AccountRadeefScansCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def resume(
        self,
        application: str,
        scan: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Resume a stopped or failed reading of the site from where it stopped; answers the reading.

        ``POST /v1/applications/{application}/radeef/knowledge/scans/{scan}/resume``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SCANS_RESUME,
            path={"application": application, "scan": scan},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        scan: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read a reading of the site: its status (running until done, stopped or failed), its counts, each page with its state, and what it proposed.

        ``GET /v1/applications/{application}/radeef/knowledge/scans/{scan}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SCANS_SHOW,
            path={"application": application, "scan": scan},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def stop(
        self,
        application: str,
        scan: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Stop a reading of the site that is running; what it read so far stays for review. Answers the reading.

        ``POST /v1/applications/{application}/radeef/knowledge/scans/{scan}/stop``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SCANS_STOP,
            path={"application": application, "scan": scan},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def summary(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read what a reading of the site would start from (the address and where it came from), the latest reading, and the readings left today.

        ``GET /v1/applications/{application}/radeef/knowledge/scans``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SCANS_SUMMARY,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefSettings:
    """``radeef.settings``."""

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
        """Read Radeef's settings: every section (persona, pace, handoff, hours, limits, store) in the shape radeef.settings.update takes, the mode, the character and the price per conversation.

        ``GET /v1/applications/{application}/radeef/settings``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETTINGS_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        section: str,
        *,
        assign_mode: Literal["auto", "member", "none"] | str,
        csat: bool,
        emoji: Literal["none", "few"] | str,
        etiquette: bool,
        idle_minutes: int,
        intro: Literal["warm", "brief"] | str,
        mode: Literal["always", "outside", "inside"] | str,
        orders: bool,
        persona_name: str,
        products: bool,
        read_receipts: bool,
        register: Literal["saudi", "msa", "mirror"] | str,
        reply_cap: int,
        reply_length: Literal["short", "standard"] | str,
        speed: Literal["fast", "natural", "relaxed"] | str,
        split: bool,
        strict: bool,
        topics: Mapping[str, Any],
        typing: bool,
        assign_member_id: str | NotGiven | None = NOT_GIVEN,
        custom_enabled: bool | NotGiven = NOT_GIVEN,
        custom_topics: Sequence[str] | NotGiven = NOT_GIVEN,
        keywords: Sequence[str] | NotGiven = NOT_GIVEN,
        keywords_enabled: bool | NotGiven = NOT_GIVEN,
        messages: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        monthly_cap_halalas: int | NotGiven | None = NOT_GIVEN,
        order_status: bool | NotGiven = NOT_GIVEN,
        persona_name_en: str | NotGiven | None = NOT_GIVEN,
        ramadan: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        return_after_hours: Literal["12", "24", "48"] | str | int | NotGiven | None = NOT_GIVEN,
        week: Mapping[str, Any] | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save one section of Radeef's settings (`persona`, `pace`, `handoff`, `hours`, `limits` or `store`), the whole section as radeef.settings.show answers it; answers the settings.

        ``PUT /v1/applications/{application}/radeef/settings/{section}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETTINGS_UPDATE,
            path={"application": application, "section": section},
            given={
                "assign_mode": assign_mode,
                "csat": csat,
                "emoji": emoji,
                "etiquette": etiquette,
                "idle_minutes": idle_minutes,
                "intro": intro,
                "mode": mode,
                "orders": orders,
                "persona_name": persona_name,
                "products": products,
                "read_receipts": read_receipts,
                "register": register,
                "reply_cap": reply_cap,
                "reply_length": reply_length,
                "speed": speed,
                "split": split,
                "strict": strict,
                "topics": topics,
                "typing": typing,
                "assign_member_id": assign_member_id,
                "custom_enabled": custom_enabled,
                "custom_topics": custom_topics,
                "keywords": keywords,
                "keywords_enabled": keywords_enabled,
                "messages": messages,
                "monthly_cap_halalas": monthly_cap_halalas,
                "order_status": order_status,
                "persona_name_en": persona_name_en,
                "ramadan": ramadan,
                "return_after_hours": return_after_hours,
                "week": week,
            },
            params=AccountRadeefSettingsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def when(
        self,
        application: str,
        *,
        hours_mode: Literal["always", "outside", "inside"] | str,
        mode: Literal["live", "draft"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Set when Radeef answers: `hours_mode` (always, outside the team's hours, inside them) with `mode` (live answers customers, draft suggests to the team); answers Radeef.

        ``PUT /v1/applications/{application}/radeef/settings/when``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETTINGS_WHEN,
            path={"application": application},
            given={"hours_mode": hours_mode, "mode": mode},
            params=AccountRadeefSettingsWhenParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefSetup:
    """``radeef.setup``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def character(
        self,
        application: str,
        *,
        character: Literal["close", "formal", "brief", "mirror"] | str,
        persona_name: str,
        persona_name_en: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Choose Radeef's character from the deck (`character`) and its name (`persona_name`, optional `persona_name_en`); answers Radeef.

        ``PUT /v1/applications/{application}/radeef/setup/character``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETUP_CHARACTER,
            path={"application": application},
            given={
                "character": character,
                "persona_name": persona_name,
                "persona_name_en": persona_name_en,
            },
            params=AccountRadeefSetupCharacterParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def confirm_fact(
        self,
        application: str,
        topic: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm a fact of the setup's brief as right: the topic's text (shipping, returns, payment, warranty, contact, about) stands as Radeef holds it; answers the setup.

        ``POST /v1/applications/{application}/radeef/setup/facts/{topic}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETUP_CONFIRM_FACT,
            path={"application": application, "topic": topic},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def live(
        self,
        application: str,
        *,
        choice: Literal["always", "outside", "suggest"] | str,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn Radeef on to answer customers: `choice` always (every hour), outside (only outside the team's hours) or suggest (draft replies for the team only); answers Radeef with its state.

        ``POST /v1/applications/{application}/radeef/setup/live``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETUP_LIVE,
            path={"application": application},
            given={"choice": choice},
            params=AccountRadeefSetupLiveParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def read(
        self,
        application: str,
        *,
        url: str,
        mine: bool | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Start reading the business's website for Radeef (`url`, `mine: true` when it is not the store's or the reviewed site); answers the reading, which runs for a few minutes: poll radeef.scans.show, then review what it found with radeef.review.show.

        ``POST /v1/applications/{application}/radeef/setup/read``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETUP_READ,
            path={"application": application},
            given={"url": url, "mine": mine},
            params=AccountRadeefSetupReadParams,
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
        """Read Radeef's setup: the current move (read, character, meet), the site address to read and the latest reading, the character deck and the chosen one, the brief of what it learned, and how it may go live.

        ``GET /v1/applications/{application}/radeef/setup``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SETUP_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefSources:
    """``radeef.sources``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def confirm(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Confirm a read website page's text as facts Radeef may state (prices, policies), not just describe; answers the source.

        ``POST /v1/applications/{application}/radeef/knowledge/sources/{source}/confirm``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SOURCES_CONFIRM,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        source: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Remove a source from what Radeef knows (any kind); a read page's address is never read again. Answers ok.

        ``DELETE /v1/applications/{application}/radeef/knowledge/sources/{source}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SOURCES_DELETE,
            path={"application": application, "source": source},
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
        """List what Radeef knows from, ten a page: FAQs, corrections, website pages and files, each with its kind, title, tier, topic, state (confirmed, reference, needs_confirm, reading, review, unreadable, gone, off) and uses; filter by `type`, `tier`, `topic`, `state`, `q`.

        ``GET /v1/applications/{application}/radeef/knowledge/sources``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_RADEEF_SOURCES_LIST,
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
            _E.A_RADEEF_SOURCES_LIST,
            _PAGE_A_RADEEF_SOURCES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def set_enabled(
        self,
        application: str,
        source: str,
        *,
        enabled: bool,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Stop Radeef using a source (`enabled: false`) or use it again (`enabled: true`), without deleting it; answers the source.

        ``PUT /v1/applications/{application}/radeef/knowledge/sources/{source}/enabled``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SOURCES_SET_ENABLED,
            path={"application": application, "source": source},
            given={"enabled": enabled},
            params=AccountRadeefSourcesSetEnabledParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        source: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one source of Radeef's knowledge (an FAQ, a correction, a page or a file): its state, what Radeef takes from it, its text or question and answer, passages, versions, the customer questions it answered and any disagreement.

        ``GET /v1/applications/{application}/radeef/knowledge/sources/{source}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_SOURCES_SHOW,
            path={"application": application, "source": source},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefState:
    """``radeef.state``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def update(
        self,
        application: str,
        *,
        enabled: bool | NotGiven = NOT_GIVEN,
        mode: Literal["live", "draft"] | str | NotGiven = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Turn Radeef on (`enabled: true`, optionally with `mode` live or draft) or off, or switch only its `mode`; answers Radeef with its new state.

        ``PUT /v1/applications/{application}/radeef/state``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_RADEEF_STATE_UPDATE,
            path={"application": application},
            given={"enabled": enabled, "mode": mode},
            params=AccountRadeefStateUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefStore:
    """``radeef.store``."""

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
        """Read the store Radeef answers from (Salla or Zid): whether it is connected, its products and when they were last read, and which store tools (orders, order status, products) are on.

        ``GET /v1/applications/{application}/radeef/store``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_STORE_SHOW,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def sync(
        self,
        application: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read the store's product catalogue again for Radeef now (Salla or Zid), queued; answers ok. Follow it with radeef.store.show.

        ``POST /v1/applications/{application}/radeef/store/sync``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_STORE_SYNC,
            path={"application": application},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefTopics:
    """``radeef.topics``."""

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
        """List the topics Radeef knows the business by (shipping, returns, payment, warranty, contact, about), each with its text, its state (known, incomplete, unknown), what is missing and what customers asked about it. The six topics in one answer (no paging).

        ``GET /v1/applications/{application}/radeef/knowledge/topics``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_RADEEF_TOPICS_LIST,
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
            _E.A_RADEEF_TOPICS_LIST,
            _PAGE_A_RADEEF_TOPICS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        topic: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Read one topic of Radeef's knowledge: its text and state, what is missing, where each line came from, what customers asked about it in 30 days, its FAQs and a change a re-read proposes.

        ``GET /v1/applications/{application}/radeef/knowledge/topics/{topic}``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_RADEEF_TOPICS_SHOW,
            path={"application": application, "topic": topic},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        topic: str,
        *,
        text: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace a topic's text (`text`, null or empty clears it): what Radeef says about shipping, returns, payment, warranty, contact, or the business (about); answers the topic.

        ``PUT /v1/applications/{application}/radeef/knowledge/topics/{topic}``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_TOPICS_UPDATE,
            path={"application": application, "topic": topic},
            given={"text": text},
            params=AccountRadeefTopicsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeefUnanswered:
    """``radeef.unanswered``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def answer(
        self,
        application: str,
        turn: str,
        *,
        answer: str,
        question: str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Answer a question Radeef could not (its `turn_id`, from radeef.unanswered.list, a playground reply or an exam): the `answer` (and optionally the `question` reworded) becomes an FAQ, and every customer who asked it is marked answered; answers the FAQ and how many questions it closed.

        ``POST /v1/applications/{application}/radeef/unanswered/{turn}/answer``, permission ``radeef:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_RADEEF_UNANSWERED_ANSWER,
            path={"application": application, "turn": turn},
            given={"answer": answer, "question": question},
            params=AccountRadeefUnansweredAnswerParams,
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
        """List the questions Radeef could not answer and handed to the team, grouped, the most asked first: the question, how many asked it, its other wordings, its topic, and the `turn_id` to answer it with radeef.unanswered.answer.

        ``GET /v1/applications/{application}/radeef/unanswered``, permission ``radeef:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_RADEEF_UNANSWERED_LIST,
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
            _E.A_RADEEF_UNANSWERED_LIST,
            _PAGE_A_RADEEF_UNANSWERED_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountRadeef:
    """``radeef``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.agent = AsyncAccountRadeefAgent(client)
        self.conversations = AsyncAccountRadeefConversations(client)
        self.faqs = AsyncAccountRadeefFaqs(client)
        self.files = AsyncAccountRadeefFiles(client)
        self.hours = AsyncAccountRadeefHours(client)
        self.insights = AsyncAccountRadeefInsights(client)
        self.knowledge = AsyncAccountRadeefKnowledge(client)
        self.notes = AsyncAccountRadeefNotes(client)
        self.notices = AsyncAccountRadeefNotices(client)
        self.owner = AsyncAccountRadeefOwner(client)
        self.owner_changes = AsyncAccountRadeefOwnerChanges(client)
        self.pages = AsyncAccountRadeefPages(client)
        self.playground = AsyncAccountRadeefPlayground(client)
        self.products = AsyncAccountRadeefProducts(client)
        self.proposals = AsyncAccountRadeefProposals(client)
        self.review = AsyncAccountRadeefReview(client)
        self.scans = AsyncAccountRadeefScans(client)
        self.settings = AsyncAccountRadeefSettings(client)
        self.setup = AsyncAccountRadeefSetup(client)
        self.sources = AsyncAccountRadeefSources(client)
        self.state = AsyncAccountRadeefState(client)
        self.store = AsyncAccountRadeefStore(client)
        self.topics = AsyncAccountRadeefTopics(client)
        self.unanswered = AsyncAccountRadeefUnanswered(client)
