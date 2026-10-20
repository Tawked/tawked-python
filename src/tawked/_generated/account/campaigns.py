"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import AsyncIterator, Iterator, Mapping, Sequence
from datetime import datetime
from typing import TYPE_CHECKING, Any, Literal

from tawked._envelope import AccountResponse
from tawked._generated import endpoints as _E
from tawked._generated.account._params import (
    AccountCampaignsCampaignsCreateParams,
    AccountCampaignsCampaignsPreviewEstimateParams,
    AccountCampaignsCampaignsSendTestParams,
    AccountCampaignsCampaignsUpdateParams,
    AccountCampaignsImagesUploadParams,
    AccountCampaignsRecipientsListParams,
)
from tawked._generated.endpoints import (
    _PAGE_A_CAMPAIGNS_CAMPAIGNS_LIST,
    _PAGE_A_CAMPAIGNS_RECIPIENTS_LIST,
    _PAGE_A_CAMPAIGNS_TEMPLATES_LIST,
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


class AccountCampaignsCampaigns:
    """``campaigns.campaigns``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def cancel(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel a campaign for good: whoever has not got it yet never will (they are skipped). Answers the campaign, cancelled.

        ``POST /v1/applications/{application}/campaigns/{campaign}/cancel``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_CANCEL,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def create(
        self,
        application: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save a new campaign draft (name, audience, template, mapping, schedule): nothing is checked beyond its shape and nothing is sent. Answers the draft; then read campaigns.campaigns.estimate and schedule it with campaigns.campaigns.schedule.

        ``POST /v1/applications/{application}/campaigns``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_CREATE,
            path={"application": application},
            given={
                "audience": audience,
                "campaign": campaign,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def delete(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a draft (nothing was ever sent from it); answers ok. A scheduled or sent campaign is cancelled instead (campaigns.campaigns.cancel): 409 not_draft.

        ``DELETE /v1/applications/{application}/campaigns/{campaign}``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_DELETE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def duplicate(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Copy a campaign into a new draft with the same audience, template, mapping and image; answers the new draft.

        ``POST /v1/applications/{application}/campaigns/{campaign}/duplicate``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_DUPLICATE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def estimate(
        self,
        application: str,
        campaign: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """A saved campaign's estimate, nothing sent: who it reaches and who is left out (and why), Meta's cost, Tawked's fee and the wallet's shortfall (for who may see the money), when it would start (moved out of the quiet hours), and what is still missing.

        ``GET /v1/applications/{application}/campaigns/{campaign}/estimate``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_ESTIMATE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's WhatsApp campaigns, newest first, each with its status, audience, template, when it sends and its figures (sent, delivered, read, replied, unsubscribed, failed). Filter by `status`.

        ``GET /v1/applications/{application}/campaigns``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CAMPAIGNS_CAMPAIGNS_LIST,
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
            _E.A_CAMPAIGNS_CAMPAIGNS_LIST,
            _PAGE_A_CAMPAIGNS_CAMPAIGNS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def pause(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Pause a scheduled or sending campaign: nobody else gets it until it is resumed. Answers the campaign.

        ``POST /v1/applications/{application}/campaigns/{campaign}/pause``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_PAUSE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def preview_estimate(
        self,
        application: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The estimate of a campaign form not saved yet (the same fields as create), nothing written: reach, exclusions, cost, start time and what is missing.

        ``POST /v1/applications/{application}/campaigns/estimate``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_PREVIEW_ESTIMATE,
            path={"application": application},
            given={
                "audience": audience,
                "campaign": campaign,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsPreviewEstimateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def resume(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Resume a paused campaign: sending goes on from where it stopped (within the quiet hours and the wallet). Answers the campaign.

        ``POST /v1/applications/{application}/campaigns/{campaign}/resume``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_RESUME,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def schedule(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Schedule a draft to send: everything is checked, its recipients fixed (subscribed contacts, minus who stopped or already got the day's marketing message), its start moved out of the quiet hours; one due now starts at once. Answers the campaign, scheduled or sending, and `next`: read campaigns.campaigns.show every few minutes for its results.

        ``POST /v1/applications/{application}/campaigns/{campaign}/schedule``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_SCHEDULE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def send_test(
        self,
        application: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send the campaign's template with its mapping to your own Saudi mobile (the token's person), as a test: not a recipient, no Tawked fee, not the day's marketing message (Meta bills the message). Answers ok; then campaigns.campaigns.estimate and campaigns.campaigns.schedule.

        ``POST /v1/applications/{application}/campaigns/test``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_SEND_TEST,
            path={"application": application},
            given={
                "audience": audience,
                "campaign": campaign,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsSendTestParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    def show(
        self,
        application: str,
        campaign: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One campaign: a draft as written (audience, template, mapping, image, schedule), or a scheduled or sent one with its results: the funnel (recipients, sent, delivered, read, replied, unsubscribed, failed, skipped, queued), why some failed or were skipped, the buttons tapped; and `next` from its status (none once completed or cancelled).

        ``GET /v1/applications/{application}/campaigns/{campaign}``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_SHOW,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def update(
        self,
        application: str,
        campaign: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign_: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace a draft's fields (the whole form, as on create); answers the draft. Only a draft changes: 409 not_draft once it is scheduled.

        ``PUT /v1/applications/{application}/campaigns/{campaign}``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_UPDATE,
            path={"application": application, "campaign": campaign},
            given={
                "audience": audience,
                "campaign": campaign_,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AccountCampaignsImages:
    """``campaigns.images``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def upload(
        self,
        application: str,
        *,
        image: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload the image of a template that opens with one (a JPG or PNG up to 5 MB, multipart `image`); answers its `path`, to save on the draft as `header_image_path`, and its public URL.

        ``POST /v1/applications/{application}/campaigns/images``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return self._client._account_call(
            _E.A_CAMPAIGNS_IMAGES_UPLOAD,
            path={"application": application},
            given={"image": image},
            params=AccountCampaignsImagesUploadParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("image",),
        )


class AccountCampaignsRecipients:
    """``campaigns.recipients``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client

    def list(
        self,
        application: str,
        campaign: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["delivered", "read", "replied", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List a scheduled or sent campaign's recipients in the order it reached them, phones masked: each with its status (queued, skipped, failed, sent, delivered, read), why, and the button tapped. Filters: status (delivered, read, replied, failed), q (a name or a whole Saudi mobile).

        ``GET /v1/applications/{application}/campaigns/{campaign}/recipients``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CAMPAIGNS_RECIPIENTS_LIST,
            path={"application": application, "campaign": campaign},
            given={"page": page, "q": q, "status": status},
            params=AccountCampaignsRecipientsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        campaign: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["delivered", "read", "replied", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> Iterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CAMPAIGNS_RECIPIENTS_LIST,
            _PAGE_A_CAMPAIGNS_RECIPIENTS_LIST,
            path={"application": application, "campaign": campaign},
            given={"page": page, "q": q, "status": status},
            params=AccountCampaignsRecipientsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountCampaignsTemplates:
    """``campaigns.templates``."""

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
        """List the number's marketing templates as a campaign may use them: each with its label, language, placeholders to map and, when it cannot be picked, why (`reason`: pending, no_stop…).

        ``GET /v1/applications/{application}/campaigns/templates``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return self._client._account_list(
            _E.A_CAMPAIGNS_TEMPLATES_LIST,
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
            _E.A_CAMPAIGNS_TEMPLATES_LIST,
            _PAGE_A_CAMPAIGNS_TEMPLATES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AccountCampaigns:
    """``campaigns``."""

    _client: TawkedAccount

    def __init__(self, client: TawkedAccount) -> None:
        self._client = client
        self.campaigns = AccountCampaignsCampaigns(client)
        self.images = AccountCampaignsImages(client)
        self.recipients = AccountCampaignsRecipients(client)
        self.templates = AccountCampaignsTemplates(client)


class AsyncAccountCampaignsCampaigns:
    """``campaigns.campaigns``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def cancel(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Cancel a campaign for good: whoever has not got it yet never will (they are skipped). Answers the campaign, cancelled.

        ``POST /v1/applications/{application}/campaigns/{campaign}/cancel``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_CANCEL,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def create(
        self,
        application: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Save a new campaign draft (name, audience, template, mapping, schedule): nothing is checked beyond its shape and nothing is sent. Answers the draft; then read campaigns.campaigns.estimate and schedule it with campaigns.campaigns.schedule.

        ``POST /v1/applications/{application}/campaigns``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_CREATE,
            path={"application": application},
            given={
                "audience": audience,
                "campaign": campaign,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsCreateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def delete(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Delete a draft (nothing was ever sent from it); answers ok. A scheduled or sent campaign is cancelled instead (campaigns.campaigns.cancel): 409 not_draft.

        ``DELETE /v1/applications/{application}/campaigns/{campaign}``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_DELETE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def duplicate(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Copy a campaign into a new draft with the same audience, template, mapping and image; answers the new draft.

        ``POST /v1/applications/{application}/campaigns/{campaign}/duplicate``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_DUPLICATE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def estimate(
        self,
        application: str,
        campaign: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """A saved campaign's estimate, nothing sent: who it reaches and who is left out (and why), Meta's cost, Tawked's fee and the wallet's shortfall (for who may see the money), when it would start (moved out of the quiet hours), and what is still missing.

        ``GET /v1/applications/{application}/campaigns/{campaign}/estimate``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_ESTIMATE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def list(
        self,
        application: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List the application's WhatsApp campaigns, newest first, each with its status, audience, template, when it sends and its figures (sent, delivered, read, replied, unsubscribed, failed). Filter by `status`.

        ``GET /v1/applications/{application}/campaigns``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CAMPAIGNS_CAMPAIGNS_LIST,
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
            _E.A_CAMPAIGNS_CAMPAIGNS_LIST,
            _PAGE_A_CAMPAIGNS_CAMPAIGNS_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def pause(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Pause a scheduled or sending campaign: nobody else gets it until it is resumed. Answers the campaign.

        ``POST /v1/applications/{application}/campaigns/{campaign}/pause``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_PAUSE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def preview_estimate(
        self,
        application: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """The estimate of a campaign form not saved yet (the same fields as create), nothing written: reach, exclusions, cost, start time and what is missing.

        ``POST /v1/applications/{application}/campaigns/estimate``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_PREVIEW_ESTIMATE,
            path={"application": application},
            given={
                "audience": audience,
                "campaign": campaign,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsPreviewEstimateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def resume(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Resume a paused campaign: sending goes on from where it stopped (within the quiet hours and the wallet). Answers the campaign.

        ``POST /v1/applications/{application}/campaigns/{campaign}/resume``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_RESUME,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def schedule(
        self,
        application: str,
        campaign: str,
        *,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Schedule a draft to send: everything is checked, its recipients fixed (subscribed contacts, minus who stopped or already got the day's marketing message), its start moved out of the quiet hours; one due now starts at once. Answers the campaign, scheduled or sending, and `next`: read campaigns.campaigns.show every few minutes for its results.

        ``POST /v1/applications/{application}/campaigns/{campaign}/schedule``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_SCHEDULE,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def send_test(
        self,
        application: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Send the campaign's template with its mapping to your own Saudi mobile (the token's person), as a test: not a recipient, no Tawked fee, not the day's marketing message (Meta bills the message). Answers ok; then campaigns.campaigns.estimate and campaigns.campaigns.schedule.

        ``POST /v1/applications/{application}/campaigns/test``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        Consequential: answers 428 approval_required until a person approves it.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_SEND_TEST,
            path={"application": application},
            given={
                "audience": audience,
                "campaign": campaign,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsSendTestParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )

    async def show(
        self,
        application: str,
        campaign: str,
        *,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """One campaign: a draft as written (audience, template, mapping, image, schedule), or a scheduled or sent one with its results: the funnel (recipients, sent, delivered, read, replied, unsubscribed, failed, skipped, queued), why some failed or were skipped, the buttons tapped; and `next` from its status (none once completed or cancelled).

        ``GET /v1/applications/{application}/campaigns/{campaign}``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_SHOW,
            path={"application": application, "campaign": campaign},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    async def update(
        self,
        application: str,
        campaign: str,
        *,
        audience: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        campaign_: str | NotGiven | None = NOT_GIVEN,
        date: datetime | str | NotGiven | None = NOT_GIVEN,
        header_image_path: str | NotGiven | None = NOT_GIVEN,
        intent: Literal["draft", "schedule"] | str | NotGiven = NOT_GIVEN,
        mapping: Mapping[str, Any] | NotGiven | None = NOT_GIVEN,
        name: str | NotGiven | None = NOT_GIVEN,
        send_mode: Literal["now", "later"] | str | NotGiven = NOT_GIVEN,
        template_language: str | NotGiven | None = NOT_GIVEN,
        template_name: str | NotGiven | None = NOT_GIVEN,
        time: datetime | str | NotGiven | None = NOT_GIVEN,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Replace a draft's fields (the whole form, as on create); answers the draft. Only a draft changes: 409 not_draft once it is scheduled.

        ``PUT /v1/applications/{application}/campaigns/{campaign}``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_CAMPAIGNS_UPDATE,
            path={"application": application, "campaign": campaign},
            given={
                "audience": audience,
                "campaign": campaign_,
                "date": date,
                "header_image_path": header_image_path,
                "intent": intent,
                "mapping": mapping,
                "name": name,
                "send_mode": send_mode,
                "template_language": template_language,
                "template_name": template_name,
                "time": time,
            },
            params=AccountCampaignsCampaignsUpdateParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
        )


class AsyncAccountCampaignsImages:
    """``campaigns.images``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def upload(
        self,
        application: str,
        *,
        image: FileInput,
        idempotency_key: str | None = None,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountResponse:
        """Upload the image of a template that opens with one (a JPG or PNG up to 5 MB, multipart `image`); answers its `path`, to save on the draft as `header_image_path`, and its public URL.

        ``POST /v1/applications/{application}/campaigns/images``, permission ``campaigns:write``.
        Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.
        """
        return await self._client._account_call(
            _E.A_CAMPAIGNS_IMAGES_UPLOAD,
            path={"application": application},
            given={"image": image},
            params=AccountCampaignsImagesUploadParams,
            opts=options(idempotency_key, timeout, max_retries, extra_headers),
            files=("image",),
        )


class AsyncAccountCampaignsRecipients:
    """``campaigns.recipients``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client

    async def list(
        self,
        application: str,
        campaign: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["delivered", "read", "replied", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AccountPage:
        """List a scheduled or sent campaign's recipients in the order it reached them, phones masked: each with its status (queued, skipped, failed, sent, delivered, read), why, and the button tapped. Filters: status (delivered, read, replied, failed), q (a name or a whole Saudi mobile).

        ``GET /v1/applications/{application}/campaigns/{campaign}/recipients``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CAMPAIGNS_RECIPIENTS_LIST,
            path={"application": application, "campaign": campaign},
            given={"page": page, "q": q, "status": status},
            params=AccountCampaignsRecipientsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )

    def iterate(
        self,
        application: str,
        campaign: str,
        *,
        page: int | NotGiven = NOT_GIVEN,
        q: str | NotGiven = NOT_GIVEN,
        status: Literal["delivered", "read", "replied", "failed"] | str | NotGiven = NOT_GIVEN,
        timeout: float | None = None,
        max_retries: int | None = None,
        extra_headers: Mapping[str, str] | None = None,
    ) -> AsyncIterator[Any]:
        """Every item of :meth:`list`, page after page (cursor); the same filters."""
        return self._client._account_iterate(
            _E.A_CAMPAIGNS_RECIPIENTS_LIST,
            _PAGE_A_CAMPAIGNS_RECIPIENTS_LIST,
            path={"application": application, "campaign": campaign},
            given={"page": page, "q": q, "status": status},
            params=AccountCampaignsRecipientsListParams,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountCampaignsTemplates:
    """``campaigns.templates``."""

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
        """List the number's marketing templates as a campaign may use them: each with its label, language, placeholders to map and, when it cannot be picked, why (`reason`: pending, no_stop…).

        ``GET /v1/applications/{application}/campaigns/templates``, permission ``campaigns:read``.
        Retried on a network failure, a timeout, a 5xx and a 429.
        """
        return await self._client._account_list(
            _E.A_CAMPAIGNS_TEMPLATES_LIST,
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
            _E.A_CAMPAIGNS_TEMPLATES_LIST,
            _PAGE_A_CAMPAIGNS_TEMPLATES_LIST,
            path={"application": application},
            given={},
            params=None,
            opts=options(None, timeout, max_retries, extra_headers),
        )


class AsyncAccountCampaigns:
    """``campaigns``."""

    _client: AsyncTawkedAccount

    def __init__(self, client: AsyncTawkedAccount) -> None:
        self._client = client
        self.campaigns = AsyncAccountCampaignsCampaigns(client)
        self.images = AsyncAccountCampaignsImages(client)
        self.recipients = AsyncAccountCampaignsRecipients(client)
        self.templates = AsyncAccountCampaignsTemplates(client)
