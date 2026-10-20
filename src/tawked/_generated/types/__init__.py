"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Any, ClassVar, Literal

from pydantic import Field

from tawked._models import DateTimeIn, Lenient, TawkedModel, TawkedParams, absent

__all__ = [
    "AppConnection",
    "AppConnectionApplication",
    "ApplicationRow",
    "ApplicationSummary",
    "Attendant",
    "AttendantChoice",
    "AttendantChoiceActionVariant1",
    "AttendantChoiceActionVariant2",
    "AttendantChoiceActionVariant3",
    "AttendantChoiceActionVariant3Assign",
    "AttendantChoiceActionVariant4",
    "AttendantChoiceActionVariant4Assign",
    "AttendantChoiceActionVariant5",
    "AttendantMenu",
    "AttendantProblem",
    "AttendantPublished",
    "ChatAttendantDraftSaveParams",
    "ChatAttendantDraftSaveResponse",
    "ChatAttendantGetResponse",
    "ChatAttendantPublishResponse",
    "ChatAttendantSettingsUpdateParams",
    "ChatAttendantSettingsUpdateResponse",
    "ChatAttendantStateSetParams",
    "ChatAttendantStateSetResponse",
    "ChatMenu",
    "ChatMenuCreateParams",
    "ChatMenuCreateResponse",
    "ChatMenuDeleteResponse",
    "ChatMenuGetResponse",
    "ChatMenuListResponse",
    "ChatMenuUpdateParams",
    "ChatMenuUpdateResponse",
    "EmailAccepted",
    "EmailAcceptedFrom",
    "EmailBatchError",
    "EmailBatchSendParams",
    "EmailBatchSendResponse",
    "EmailBounce",
    "EmailCost",
    "EmailDomain",
    "EmailDomainCreateParams",
    "EmailDomainCreateResponse",
    "EmailDomainDefaults",
    "EmailDomainDeleteResponse",
    "EmailDomainGetResponse",
    "EmailDomainListParams",
    "EmailDomainListResponse",
    "EmailDomainReceiving",
    "EmailDomainRecordsItem",
    "EmailDomainTracking",
    "EmailDomainUpdateParams",
    "EmailDomainUpdateResponse",
    "EmailDomainVerifyResponse",
    "EmailError",
    "EmailInboundAddress",
    "EmailInboundAddressForward",
    "EmailInboundAddressHeld",
    "EmailInboundAddressListResponse",
    "EmailKeyCheckParams",
    "EmailKeyCheckResponse",
    "EmailKeyCheckResponseApplication",
    "EmailMessage",
    "EmailMessageAttachmentsItem",
    "EmailMessageCancelParams",
    "EmailMessageCancelResponse",
    "EmailMessageContentResponse",
    "EmailMessageExtended",
    "EmailMessageExtendedAttachmentsItem",
    "EmailMessageExtendedFrom",
    "EmailMessageExtendedTemplate",
    "EmailMessageFrom",
    "EmailMessageGetParams",
    "EmailMessageGetResponse",
    "EmailMessageGetResponseAttachmentsItem",
    "EmailMessageGetResponseFrom",
    "EmailMessageGetResponseTemplate",
    "EmailMessageListParams",
    "EmailMessageListResponse",
    "EmailMessageRescheduleParams",
    "EmailMessageRescheduleResponse",
    "EmailMetrics",
    "EmailMetricsDataItem",
    "EmailMetricsDomain",
    "EmailMetricsGetParams",
    "EmailMetricsGetResponse",
    "EmailMetricsRates",
    "EmailMetricsTotals",
    "EmailReceived",
    "EmailReceivedAddress",
    "EmailReceivedAttachment",
    "EmailReceivedAuthentication",
    "EmailReceivedCcItem",
    "EmailReceivedDeleteResponse",
    "EmailReceivedEventData",
    "EmailReceivedEventDataAddress",
    "EmailReceivedEventDataAttachmentsItem",
    "EmailReceivedEventDataAuthentication",
    "EmailReceivedEventDataFrom",
    "EmailReceivedEventDataThread",
    "EmailReceivedForwardParams",
    "EmailReceivedForwardResponse",
    "EmailReceivedForwardedVariant1Variant1",
    "EmailReceivedForwardedVariant1Variant2",
    "EmailReceivedFrom",
    "EmailReceivedGetResponse",
    "EmailReceivedHeaderToItem",
    "EmailReceivedHeadersItem",
    "EmailReceivedListItem",
    "EmailReceivedListItemAddress",
    "EmailReceivedListItemFrom",
    "EmailReceivedListItemThread",
    "EmailReceivedListParams",
    "EmailReceivedListResponse",
    "EmailReceivedRaw",
    "EmailReceivedReplyHeaders",
    "EmailReceivedReplyToItem",
    "EmailReceivedTestResponse",
    "EmailReceivedThread",
    "EmailRecipient",
    "EmailRecipientAccepted",
    "EmailSendParams",
    "EmailSendResponse",
    "EmailSendResponseFrom",
    "EmailSuppression",
    "EmailSuppressionAddParams",
    "EmailSuppressionAddResponse",
    "EmailSuppressionAddResponseInvalidItem",
    "EmailSuppressionGetResponse",
    "EmailSuppressionImport",
    "EmailSuppressionImportCreateParams",
    "EmailSuppressionImportCreateResponse",
    "EmailSuppressionImportGetResponse",
    "EmailSuppressionListParams",
    "EmailSuppressionListResponse",
    "EmailSuppressionLookup",
    "EmailSuppressionRemoveParams",
    "EmailSuppressionRemoveResponse",
    "EmailTag",
    "EmailTemplate",
    "EmailTemplateCreateParams",
    "EmailTemplateCreateResponse",
    "EmailTemplateDeleteResponse",
    "EmailTemplateGetResponse",
    "EmailTemplateListParams",
    "EmailTemplateListResponse",
    "EmailTemplateProblem",
    "EmailTemplatePublishResponse",
    "EmailTemplateUpdateParams",
    "EmailTemplateUpdateResponse",
    "EmailTemplateVersion",
    "EmailTemplateVersionFrom",
    "EmailTemplateVersionGetResponse",
    "EmailTemplateVersionListResponse",
    "EmailTemplateVersionRestoreResponse",
    "EmailTemplateVersionRow",
    "EmailTemplateVersionVariablesItem",
    "PartnerApplicationArchiveResponse",
    "PartnerApplicationBatchResponse",
    "PartnerApplicationBatchResponseResultsItem",
    "PartnerApplicationCreateParams",
    "PartnerApplicationCreateResponse",
    "PartnerApplicationGetResponse",
    "PartnerApplicationHistoryResponse",
    "PartnerApplicationHistoryResponseEventsItem",
    "PartnerApplicationListParams",
    "PartnerApplicationListResponse",
    "PartnerApplicationRestoreResponse",
    "PartnerApplicationResumeResponse",
    "PartnerApplicationSuspendResponse",
    "PartnerApplicationUnpauseResponse",
    "PartnerApplicationUpdateParams",
    "PartnerApplicationUpdateResponse",
    "PartnerDeliveryListParams",
    "PartnerDeliveryListResponse",
    "PartnerDeliveryRetryResponse",
    "PartnerEventListItem",
    "PartnerEventListItemDelivery",
    "PartnerEventListParams",
    "PartnerEventListResponse",
    "PartnerLogoRemoveResponse",
    "PartnerLogoUploadParams",
    "PartnerLogoUploadResponse",
    "PartnerProfileResponse",
    "PartnerProfileResponseKey",
    "PartnerProfileResponsePrices",
    "PartnerProfileResponseWebhook",
    "PartnerScreeningParams",
    "PartnerScreeningResponse",
    "PartnerScreeningResponseReview",
    "PartnerUsageParams",
    "PartnerUsageResponse",
    "PartnerUsageResponseApplicationsItem",
    "PartnerVerificationListItem",
    "PartnerVerificationListParams",
    "PartnerVerificationListResponse",
    "PartnerVerifySettingsUpdateParams",
    "PartnerVerifySettingsUpdateResponse",
    "PartnerWebhook",
    "PartnerWebhookGetResponse",
    "PartnerWebhookUpdateParams",
    "PartnerWebhookUpdateResponse",
    "Screening",
    "Verification",
    "VerifyCancelParams",
    "VerifyCancelResponse",
    "VerifyCheckParams",
    "VerifyCheckResponse",
    "VerifyGetParams",
    "VerifyGetResponse",
    "VerifyResendParams",
    "VerifyResendResponse",
    "VerifySettings",
    "VerifyStartParams",
    "VerifyStartResponse",
    "WebhookDelivery",
    "WebhookDeliveryGetResponse",
    "WebhookDeliveryListParams",
    "WebhookDeliveryListResponse",
    "WebhookDeliveryReplayResponse",
    "WebhookEndpoint",
    "WebhookEndpointCreateParams",
    "WebhookEndpointCreateResponse",
    "WebhookEndpointDeleteResponse",
    "WebhookEndpointDelivery",
    "WebhookEndpointGetResponse",
    "WebhookEndpointLastDelivery",
    "WebhookEndpointListResponse",
    "WebhookEndpointSecrets",
    "WebhookEndpointSigning",
    "WebhookEndpointUpdateParams",
    "WebhookEndpointUpdateResponse",
    "WebhookReplay",
    "WebhookReplayCreateParams",
    "WebhookReplayCreateResponse",
    "WebhookReplayGetResponse",
    "WebhookSecretRotateParams",
    "WebhookSecretRotateResponse",
    "WebhookSecretRotateResponseSecrets",
    "WebhookTestSendParams",
    "WebhookTestSendResponse",
    "WhatsAppMessage",
    "WhatsAppMessageError",
    "WhatsAppMessageGetParams",
    "WhatsAppMessageGetResponse",
    "WhatsAppSendParams",
    "WhatsAppSendResponse",
    "WhatsAppTemplate",
    "WhatsAppTemplateComponentsItem",
    "WhatsAppTemplateComponentsItemButtonsItem",
    "WhatsAppTemplateCreateParams",
    "WhatsAppTemplateCreateResponse",
    "WhatsAppTemplateDeleteResponse",
    "WhatsAppTemplateGetResponse",
    "WhatsAppTemplateListParams",
    "WhatsAppTemplateListResponse",
    "WhatsAppTemplateListResponseDataItem",
    "WhatsAppTemplateListResponseDataItemPlaceholders",
    "WhatsAppTemplateListResponseDataItemPlaceholdersButtonsItem",
    "WhatsAppTemplatePlaceholders",
    "WhatsAppTemplatePlaceholdersButtonsItem",
    "WhatsAppTemplateUpdateParams",
    "WhatsAppTemplateUpdateResponse",
]

_ = (builtins, datetime, Any, ClassVar, Literal, DateTimeIn)


class VerifyStartResponse(TawkedModel):
    """Start a verification: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "status", "expires_at")

    id: Lenient[str] = absent()
    status: Lenient[Literal["pending"] | str] = absent()
    expires_at: Lenient[datetime] = absent()
    reference: Lenient[str | None] = absent()


class VerifyCheckResponse(TawkedModel):
    """Check a code: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("verified", "status")

    verified: Lenient[bool] = absent()
    status: Lenient[
        Literal["verified", "invalid_code", "too_many_attempts", "failed", "expired", "canceled"]
        | str
    ] = absent()
    attempts_remaining: Lenient[int | None] = absent()


class Verification(TawkedModel):
    """The Verification object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "channel",
        "to",
        "reference",
        "attempts_remaining",
        "resends_remaining",
        "expires_at",
        "verified_at",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["pending", "verified", "failed", "expired", "canceled"] | str] = (
        absent()
    )
    channel: Lenient[str] = absent()
    to: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    attempts_remaining: Lenient[int] = absent()
    resends_remaining: Lenient[int] = absent()
    expires_at: Lenient[datetime] = absent()
    verified_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class VerifyGetResponse(Verification):
    """Get a verification: the answer."""


class VerifyResendResponse(TawkedModel):
    """Resend a code: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "expires_at",
        "resends_remaining",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["pending"] | str] = absent()
    expires_at: Lenient[datetime] = absent()
    resends_remaining: Lenient[int] = absent()


class VerifyCancelResponse(TawkedModel):
    """Cancel a verification: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "status")

    id: Lenient[str] = absent()
    status: Lenient[Literal["canceled"] | str] = absent()


class WhatsAppSendResponse(TawkedModel):
    """Send a template message: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "to",
        "template",
        "lang",
        "reference",
        "price_halalas",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["accepted", "sent", "delivered", "read", "failed"] | str] = absent()
    to: Lenient[str] = absent()
    template: Lenient[str] = absent()
    lang: Lenient[str | None] = absent()
    reference: Lenient[str | None] = absent()
    price_halalas: Lenient[int] = absent()
    created_at: Lenient[datetime | None] = absent()


class WhatsAppMessageError(TawkedModel):
    """The WhatsAppMessageError object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "message")

    code: Lenient[str | None] = absent()
    message: Lenient[str | None] = absent()


class WhatsAppMessage(TawkedModel):
    """The WhatsAppMessage object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "to",
        "template",
        "lang",
        "reference",
        "price_halalas",
        "error",
        "created_at",
        "sent_at",
        "delivered_at",
        "read_at",
        "failed_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["accepted", "sent", "delivered", "read", "failed"] | str] = absent()
    to: Lenient[str] = absent()
    template: Lenient[str] = absent()
    lang: Lenient[str | None] = absent()
    reference: Lenient[str | None] = absent()
    price_halalas: Lenient[int] = absent()
    error: Lenient[WhatsAppMessageError | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    sent_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    read_at: Lenient[datetime | None] = absent()
    failed_at: Lenient[datetime | None] = absent()


class WhatsAppMessageGetResponse(WhatsAppMessage):
    """Get a message: the answer."""


class WhatsAppTemplateListResponseDataItemPlaceholdersButtonsItem(TawkedModel):
    """The WhatsAppTemplateListResponseDataItemPlaceholdersButtonsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("index", "type")

    index: Lenient[int] = absent()
    type: Lenient[Literal["url"] | str] = absent()


class WhatsAppTemplateListResponseDataItemPlaceholders(TawkedModel):
    """The WhatsAppTemplateListResponseDataItemPlaceholders object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("kind", "header", "body", "buttons")

    kind: Lenient[Literal["named", "positional", "none"] | str] = absent()
    header: Lenient[builtins.list[str]] = absent()
    body: Lenient[builtins.list[str]] = absent()
    buttons: Lenient[builtins.list[WhatsAppTemplateListResponseDataItemPlaceholdersButtonsItem]] = (
        absent()
    )


class WhatsAppTemplateListResponseDataItem(TawkedModel):
    """The WhatsAppTemplateListResponseDataItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "name",
        "language",
        "category",
        "status",
        "placeholders",
        "managed",
    )

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    language: Lenient[str] = absent()
    category: Lenient[Literal["AUTHENTICATION", "MARKETING", "UTILITY"] | str] = absent()
    status: Lenient[str] = absent()
    placeholders: Lenient[WhatsAppTemplateListResponseDataItemPlaceholders] = absent()
    managed: Lenient[bool] = absent()


class WhatsAppTemplateListResponse(TawkedModel):
    """List templates: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data",)

    data: Lenient[builtins.list[WhatsAppTemplateListResponseDataItem]] = absent()


class WhatsAppTemplateComponentsItemButtonsItem(TawkedModel):
    """The WhatsAppTemplateComponentsItemButtonsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "text", "url", "phone_number")

    type: Lenient[str] = absent()
    text: Lenient[str | None] = absent()
    url: Lenient[str | None] = absent()
    phone_number: Lenient[str | None] = absent()


class WhatsAppTemplateComponentsItem(TawkedModel):
    """The WhatsAppTemplateComponentsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "format", "text", "buttons")

    type: Lenient[str] = absent()
    format: Lenient[str | None] = absent()
    text: Lenient[str | None] = absent()
    buttons: Lenient[builtins.list[WhatsAppTemplateComponentsItemButtonsItem]] = absent()


class WhatsAppTemplatePlaceholdersButtonsItem(TawkedModel):
    """The WhatsAppTemplatePlaceholdersButtonsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("index", "type")

    index: Lenient[int] = absent()
    type: Lenient[Literal["url"] | str] = absent()


class WhatsAppTemplatePlaceholders(TawkedModel):
    """The WhatsAppTemplatePlaceholders object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("kind", "header", "body", "buttons")

    kind: Lenient[Literal["named", "positional", "none"] | str] = absent()
    header: Lenient[builtins.list[str]] = absent()
    body: Lenient[builtins.list[str]] = absent()
    buttons: Lenient[builtins.list[WhatsAppTemplatePlaceholdersButtonsItem]] = absent()


class WhatsAppTemplate(TawkedModel):
    """The WhatsAppTemplate object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "name",
        "language",
        "category",
        "status",
        "quality",
        "rejected_reason",
        "components",
        "examples",
        "placeholders",
        "managed",
    )

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    language: Lenient[str] = absent()
    category: Lenient[Literal["AUTHENTICATION", "MARKETING", "UTILITY"] | str] = absent()
    status: Lenient[str] = absent()
    quality: Lenient[str | None] = absent()
    rejected_reason: Lenient[str | None] = absent()
    components: Lenient[builtins.list[WhatsAppTemplateComponentsItem]] = absent()
    examples: Lenient[builtins.dict[str, str]] = absent()
    placeholders: Lenient[WhatsAppTemplatePlaceholders] = absent()
    managed: Lenient[bool] = absent()


class WhatsAppTemplateGetResponse(WhatsAppTemplate):
    """Get a template: the answer."""


class WhatsAppTemplateCreateResponse(TawkedModel):
    """Create a template: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "name",
        "language",
        "category",
        "status",
    )

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    language: Lenient[str] = absent()
    category: Lenient[Literal["AUTHENTICATION", "MARKETING", "UTILITY"] | str] = absent()
    status: Lenient[str] = absent()


class WhatsAppTemplateUpdateResponse(WhatsAppTemplate):
    """Update a template: the answer."""


class WhatsAppTemplateDeleteResponse(TawkedModel):
    """Delete a template: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "name", "language", "deleted")

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    language: Lenient[str] = absent()
    deleted: Lenient[Literal[True] | bool] = absent()


class EmailSendResponseFrom(TawkedModel):
    """The EmailSendResponseFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailAcceptedFrom(TawkedModel):
    """The EmailAcceptedFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailTag(TawkedModel):
    """The EmailTag object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "value")

    name: Lenient[str] = absent()
    value: Lenient[str] = absent()


class EmailRecipientAccepted(TawkedModel):
    """The EmailRecipientAccepted object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "address", "name", "type", "status")

    id: Lenient[str] = absent()
    address: Lenient[str] = absent()
    name: Lenient[str | None] = absent()
    type: Lenient[Literal["to", "cc", "bcc"] | str] = absent()
    status: Lenient[
        Literal[
            "queued",
            "scheduled",
            "sent",
            "delivered",
            "bounced",
            "failed",
            "suppressed",
            "canceled",
        ]
        | str
    ] = absent()


class EmailCost(TawkedModel):
    """The EmailCost object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "emails",
        "suppressed",
        "free",
        "billed",
        "halalas",
    )

    emails: Lenient[int] = absent()
    suppressed: Lenient[int] = absent()
    free: Lenient[int] = absent()
    billed: Lenient[int] = absent()
    halalas: Lenient[str] = absent()


class EmailAccepted(TawkedModel):
    """The EmailAccepted object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "from",
        "to",
        "cc",
        "bcc",
        "reply_to",
        "subject",
        "reference",
        "tags",
        "scheduled_at",
        "recipients",
        "price_halalas",
        "cost",
        "created_at",
        "mode",
    )

    id: Lenient[str] = absent()
    status: Lenient[
        Literal["accepted", "scheduled", "delivered", "bounced", "failed", "canceled"] | str
    ] = absent()
    from_: Lenient[EmailAcceptedFrom] = absent("from")
    to: Lenient[builtins.list[str]] = absent()
    cc: Lenient[builtins.list[str]] = absent()
    bcc: Lenient[builtins.list[str]] = absent()
    reply_to: Lenient[builtins.list[str]] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    tags: Lenient[builtins.list[EmailTag]] = absent()
    scheduled_at: Lenient[datetime | None] = absent()
    recipients: Lenient[builtins.list[EmailRecipientAccepted]] = absent()
    price_halalas: Lenient[int] = absent()
    cost: Lenient[EmailCost] = absent()
    created_at: Lenient[datetime | None] = absent()
    mode: Lenient[Literal["live", "test"] | str] = absent()


class EmailSendResponse(TawkedModel):
    """Send an email: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "from",
        "to",
        "subject",
        "reference",
        "price_halalas",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[
        Literal["accepted", "delivered", "bounced", "failed"]
        | str
        | Literal["accepted", "scheduled", "delivered", "bounced", "failed", "canceled"]
    ] = absent()
    from_: Lenient[EmailSendResponseFrom] = absent("from")
    to: Lenient[str | builtins.list[str]] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    price_halalas: Lenient[int] = absent()
    created_at: Lenient[datetime | None] = absent()
    cc: Lenient[builtins.list[str] | None] = absent()
    bcc: Lenient[builtins.list[str] | None] = absent()
    reply_to: Lenient[builtins.list[str] | None] = absent()
    tags: Lenient[builtins.list[EmailTag] | None] = absent()
    scheduled_at: Lenient[datetime | None] = absent()
    recipients: Lenient[builtins.list[EmailRecipientAccepted] | None] = absent()
    cost: Lenient[EmailCost | None] = absent()
    mode: Lenient[Literal["live", "test"] | str | None] = absent()


class EmailBatchError(TawkedModel):
    """The EmailBatchError object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("index", "error", "message")

    index: Lenient[int] = absent()
    error: Lenient[str] = absent()
    message: Lenient[str] = absent()
    field: Lenient[str | None] = absent()
    field_index: Lenient[int | None] = absent()
    header: Lenient[str | None] = absent()
    host: Lenient[str | None] = absent()


class EmailBatchSendResponse(TawkedModel):
    """Send a batch of emails: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data",)

    data: Lenient[builtins.list[EmailAccepted]] = absent()
    errors: Lenient[builtins.list[EmailBatchError] | None] = absent()


class EmailMessageExtendedFrom(TawkedModel):
    """The EmailMessageExtendedFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailBounce(TawkedModel):
    """The EmailBounce object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "subtype")

    type: Lenient[Literal["Permanent", "Transient", "Undetermined"] | str] = absent()
    subtype: Lenient[str | None] = absent()


class EmailError(TawkedModel):
    """The EmailError object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "message")

    code: Lenient[
        Literal[
            "bounced",
            "complaint",
            "rejected",
            "rendering_failed",
            "send_failed",
            "email_paused",
            "email_early_access",
            "sender_not_verified",
            "recipient_suppressed",
            "queue_expired",
        ]
        | str
    ] = absent()
    message: Lenient[str | None] = absent()


class EmailRecipient(TawkedModel):
    """The EmailRecipient object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "name",
        "type",
        "status",
        "sent_at",
        "delivered_at",
        "bounced_at",
        "complained_at",
        "delayed_at",
        "failed_at",
        "bounce",
        "error",
        "opened_at",
        "clicked_at",
        "opens",
        "clicks",
    )

    id: Lenient[str] = absent()
    address: Lenient[str] = absent()
    name: Lenient[str | None] = absent()
    type: Lenient[Literal["to", "cc", "bcc"] | str] = absent()
    status: Lenient[
        Literal[
            "queued",
            "scheduled",
            "sent",
            "delivered",
            "bounced",
            "failed",
            "suppressed",
            "canceled",
        ]
        | str
    ] = absent()
    sent_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    bounced_at: Lenient[datetime | None] = absent()
    complained_at: Lenient[datetime | None] = absent()
    delayed_at: Lenient[datetime | None] = absent()
    failed_at: Lenient[datetime | None] = absent()
    bounce: Lenient[Any] = absent()
    error: Lenient[Any] = absent()
    opened_at: Lenient[datetime | None] = absent()
    clicked_at: Lenient[datetime | None] = absent()
    opens: Lenient[int] = absent()
    clicks: Lenient[int] = absent()


class EmailMessageExtendedAttachmentsItem(TawkedModel):
    """The EmailMessageExtendedAttachmentsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("filename", "content_type", "size", "inline")

    filename: Lenient[str] = absent()
    content_type: Lenient[str] = absent()
    size: Lenient[int] = absent()
    inline: Lenient[bool] = absent()


class EmailMessageExtendedTemplate(TawkedModel):
    """The EmailMessageExtendedTemplate object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "version_id")

    id: Lenient[str] = absent()
    version_id: Lenient[str] = absent()


class EmailMessageExtended(TawkedModel):
    """The EmailMessageExtended object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "from",
        "to",
        "cc",
        "bcc",
        "reply_to",
        "subject",
        "reference",
        "tags",
        "scheduled_at",
        "recipients",
        "price_halalas",
        "cost",
        "attachments",
        "header_names",
        "error",
        "created_at",
        "sent_at",
        "delivered_at",
        "bounced_at",
        "complained_at",
        "failed_at",
        "canceled_at",
        "batch_id",
        "mode",
        "template",
        "tracking",
        "opened_at",
        "clicked_at",
        "opens",
        "clicks",
    )

    id: Lenient[str] = absent()
    status: Lenient[
        Literal["queued", "scheduled", "sent", "delivered", "bounced", "failed", "canceled"] | str
    ] = absent()
    from_: Lenient[EmailMessageExtendedFrom] = absent("from")
    to: Lenient[builtins.list[str]] = absent()
    cc: Lenient[builtins.list[str]] = absent()
    bcc: Lenient[builtins.list[str]] = absent()
    reply_to: Lenient[builtins.list[str]] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    tags: Lenient[builtins.list[EmailTag]] = absent()
    scheduled_at: Lenient[datetime | None] = absent()
    recipients: Lenient[builtins.list[EmailRecipient]] = absent()
    price_halalas: Lenient[int] = absent()
    cost: Lenient[EmailCost] = absent()
    attachments: Lenient[builtins.list[EmailMessageExtendedAttachmentsItem]] = absent()
    header_names: Lenient[builtins.list[str]] = absent()
    error: Lenient[Any] = absent()
    created_at: Lenient[datetime | None] = absent()
    sent_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    bounced_at: Lenient[datetime | None] = absent()
    complained_at: Lenient[datetime | None] = absent()
    failed_at: Lenient[datetime | None] = absent()
    canceled_at: Lenient[datetime | None] = absent()
    batch_id: Lenient[str | None] = absent()
    mode: Lenient[Literal["live", "test"] | str] = absent()
    template: Lenient[EmailMessageExtendedTemplate | None] = absent()
    tracking: Lenient[Literal["open", "click", "both"] | str | None] = absent()
    opened_at: Lenient[datetime | None] = absent()
    clicked_at: Lenient[datetime | None] = absent()
    opens: Lenient[int] = absent()
    clicks: Lenient[int] = absent()


class EmailMessageListResponse(TawkedModel):
    """List emails: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[EmailMessageExtended]] = absent()
    has_more: Lenient[bool] = absent()
    next_cursor: Lenient[str | None] = absent()


class EmailMessageFrom(TawkedModel):
    """The EmailMessageFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailMessageAttachmentsItem(TawkedModel):
    """The EmailMessageAttachmentsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("filename", "content_type", "size", "inline")

    filename: Lenient[str] = absent()
    content_type: Lenient[str] = absent()
    size: Lenient[int] = absent()
    inline: Lenient[bool] = absent()


class EmailMessage(TawkedModel):
    """The EmailMessage object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "from",
        "to",
        "subject",
        "reference",
        "attachments",
        "price_halalas",
        "error",
        "created_at",
        "sent_at",
        "delivered_at",
        "bounced_at",
        "complained_at",
        "failed_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["accepted", "sent", "delivered", "bounced", "failed"] | str] = absent()
    from_: Lenient[EmailMessageFrom] = absent("from")
    to: Lenient[str] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    attachments: Lenient[builtins.list[EmailMessageAttachmentsItem]] = absent()
    price_halalas: Lenient[int] = absent()
    error: Lenient[Any] = absent()
    created_at: Lenient[datetime | None] = absent()
    sent_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    bounced_at: Lenient[datetime | None] = absent()
    complained_at: Lenient[datetime | None] = absent()
    failed_at: Lenient[datetime | None] = absent()


class EmailMessageGetResponseFrom(TawkedModel):
    """The EmailMessageGetResponseFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailMessageGetResponseAttachmentsItem(TawkedModel):
    """The EmailMessageGetResponseAttachmentsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("filename", "content_type", "size", "inline")

    filename: Lenient[str] = absent()
    content_type: Lenient[str] = absent()
    size: Lenient[int] = absent()
    inline: Lenient[bool] = absent()


class EmailMessageGetResponseTemplate(TawkedModel):
    """The EmailMessageGetResponseTemplate object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "version_id")

    id: Lenient[str] = absent()
    version_id: Lenient[str] = absent()


class EmailMessageGetResponse(TawkedModel):
    """Get an email: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "from",
        "to",
        "subject",
        "reference",
        "attachments",
        "price_halalas",
        "error",
        "created_at",
        "sent_at",
        "delivered_at",
        "bounced_at",
        "complained_at",
        "failed_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[
        Literal["accepted", "sent", "delivered", "bounced", "failed"]
        | str
        | Literal["queued", "scheduled", "sent", "delivered", "bounced", "failed", "canceled"]
    ] = absent()
    from_: Lenient[EmailMessageGetResponseFrom] = absent("from")
    to: Lenient[str | builtins.list[str]] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    attachments: Lenient[builtins.list[EmailMessageGetResponseAttachmentsItem]] = absent()
    price_halalas: Lenient[int] = absent()
    error: Lenient[Any] = absent()
    created_at: Lenient[datetime | None] = absent()
    sent_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    bounced_at: Lenient[datetime | None] = absent()
    complained_at: Lenient[datetime | None] = absent()
    failed_at: Lenient[datetime | None] = absent()
    cc: Lenient[builtins.list[str] | None] = absent()
    bcc: Lenient[builtins.list[str] | None] = absent()
    reply_to: Lenient[builtins.list[str] | None] = absent()
    tags: Lenient[builtins.list[EmailTag] | None] = absent()
    scheduled_at: Lenient[datetime | None] = absent()
    recipients: Lenient[builtins.list[EmailRecipient] | None] = absent()
    cost: Lenient[EmailCost | None] = absent()
    header_names: Lenient[builtins.list[str] | None] = absent()
    canceled_at: Lenient[datetime | None] = absent()
    batch_id: Lenient[str | None] = absent()
    mode: Lenient[Literal["live", "test"] | str | None] = absent()
    template: Lenient[EmailMessageGetResponseTemplate | None] = absent()
    tracking: Lenient[Literal["open", "click", "both"] | str | None] = absent()
    opened_at: Lenient[datetime | None] = absent()
    clicked_at: Lenient[datetime | None] = absent()
    opens: Lenient[int | None] = absent()
    clicks: Lenient[int | None] = absent()


class EmailMessageRescheduleResponse(EmailMessageExtended):
    """Reschedule an email: the answer."""


class EmailMessageCancelResponse(EmailMessageExtended):
    """Cancel a scheduled email: the answer."""


class EmailKeyCheckResponseApplication(TawkedModel):
    """The EmailKeyCheckResponseApplication object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "name")

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()


class EmailKeyCheckResponse(TawkedModel):
    """Check an email key: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("application", "can_send")

    application: Lenient[EmailKeyCheckResponseApplication] = absent()
    can_send: Lenient[Literal[True] | bool] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()


class EmailMessageContentResponse(TawkedModel):
    """Get an email's content: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "subject", "html", "text", "kept_until")

    id: Lenient[str] = absent()
    subject: Lenient[str] = absent()
    html: Lenient[str | None] = absent()
    text: Lenient[str | None] = absent()
    kept_until: Lenient[datetime | None] = absent()


class EmailDomainRecordsItem(TawkedModel):
    """The EmailDomainRecordsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("purpose", "type", "name", "value", "state")

    purpose: Lenient[Literal["dkim", "return_path", "tracking"] | str] = absent()
    type: Lenient[Literal["TXT", "MX", "CNAME"] | str] = absent()
    name: Lenient[str] = absent()
    value: Lenient[str] = absent()
    priority: Lenient[int | None] = absent()
    state: Lenient[str] = absent()


class EmailDomainDefaults(TawkedModel):
    """The EmailDomainDefaults object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("from_name", "from_local")

    from_name: Lenient[str | None] = absent()
    from_local: Lenient[str | None] = absent()


class EmailDomainTracking(TawkedModel):
    """The EmailDomainTracking object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "opens",
        "clicks",
        "subdomain",
        "state",
        "problem",
        "checked_at",
    )

    opens: Lenient[bool] = absent()
    clicks: Lenient[bool] = absent()
    subdomain: Lenient[str | None] = absent()
    state: Lenient[Literal["off", "awaiting_dns", "awaiting_tls", "active", "failing"] | str] = (
        absent()
    )
    problem: Lenient[str | None] = absent()
    checked_at: Lenient[datetime | None] = absent()


class EmailDomainReceiving(TawkedModel):
    """The EmailDomainReceiving object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("address_id", "domain", "state")

    address_id: Lenient[str] = absent()
    domain: Lenient[str] = absent()
    state: Lenient[Literal["awaiting", "active", "partial", "lost", "off"] | str] = absent()


class EmailDomain(TawkedModel):
    """The EmailDomain object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "name",
        "state",
        "created_at",
        "verified_at",
        "pending_until",
        "records",
        "defaults",
        "authentication",
        "tracking",
        "receiving",
    )

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    state: Lenient[Literal["pending", "verified", "failed"] | str] = absent()
    created_at: Lenient[datetime | None] = absent()
    verified_at: Lenient[datetime | None] = absent()
    pending_until: Lenient[datetime | None] = absent()
    records: Lenient[builtins.list[EmailDomainRecordsItem]] = absent()
    defaults: Lenient[EmailDomainDefaults] = absent()
    authentication: Lenient[builtins.dict[str, Any] | None] = absent()
    tracking: Lenient[EmailDomainTracking | None] = absent()
    receiving: Lenient[EmailDomainReceiving | None] = absent()


class EmailDomainListResponse(TawkedModel):
    """List domains: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[EmailDomain]] = absent()
    has_more: Lenient[bool] = absent()
    next_cursor: Lenient[str | None] = absent()


class EmailDomainCreateResponse(EmailDomain):
    """Add a domain: the answer."""


class EmailDomainGetResponse(EmailDomain):
    """Get a domain: the answer."""


class EmailDomainUpdateResponse(EmailDomain):
    """Update a domain: the answer."""


class EmailDomainVerifyResponse(EmailDomain):
    """Check a domain now: the answer."""


class EmailDomainDeleteResponse(TawkedModel):
    """Remove a domain: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "name", "deleted")

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    deleted: Lenient[Literal[True] | bool] = absent()


class EmailSuppression(TawkedModel):
    """The EmailSuppression object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "suppressed",
        "visible",
        "reason",
        "source",
        "application_id",
        "email_id",
        "created_at",
        "lift",
    )

    id: Lenient[str] = absent()
    address: Lenient[str] = absent()
    suppressed: Lenient[Literal[True] | bool] = absent()
    visible: Lenient[Literal[True] | bool] = absent()
    reason: Lenient[Literal["bounce", "complaint", "manual"] | str] = absent()
    source: Lenient[str] = absent()
    application_id: Lenient[str | None] = absent()
    email_id: Lenient[str | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    lift: Lenient[Literal["free", "needs_reason", "team_only"] | str] = absent()


class EmailSuppressionListResponse(TawkedModel):
    """List suppressed addresses: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[EmailSuppression]] = absent()
    has_more: Lenient[bool] = absent()
    next_cursor: Lenient[str | None] = absent()


class EmailSuppressionAddResponseInvalidItem(TawkedModel):
    """The EmailSuppressionAddResponseInvalidItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("index", "code")

    index: Lenient[int] = absent()
    code: Lenient[str] = absent()


class EmailSuppressionAddResponse(TawkedModel):
    """Suppress addresses: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("added", "existing", "invalid")

    added: Lenient[int] = absent()
    existing: Lenient[int] = absent()
    invalid: Lenient[builtins.list[EmailSuppressionAddResponseInvalidItem]] = absent()


class EmailSuppressionLookup(TawkedModel):
    """The EmailSuppressionLookup object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("address", "suppressed", "visible", "lift")

    id: Lenient[str | None] = absent()
    address: Lenient[str] = absent()
    suppressed: Lenient[Literal[True] | bool] = absent()
    visible: Lenient[bool] = absent()
    reason: Lenient[Literal["bounce", "complaint", "manual"] | str | None] = absent()
    source: Lenient[str | None] = absent()
    application_id: Lenient[str | None] = absent()
    email_id: Lenient[str | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    lift: Lenient[Literal["free", "needs_reason", "team_only"] | str] = absent()


class EmailSuppressionGetResponse(EmailSuppressionLookup):
    """Look up an address: the answer."""


class EmailSuppressionRemoveResponse(TawkedModel):
    """Lift an address: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("address", "removed")

    address: Lenient[str] = absent()
    removed: Lenient[Literal[True] | bool] = absent()


class EmailSuppressionImport(TawkedModel):
    """The EmailSuppressionImport object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "state",
        "filename",
        "rows_total",
        "rows_added",
        "rows_existing",
        "rows_invalid",
        "invalid_lines",
        "failure",
        "created_at",
        "finished_at",
    )

    id: Lenient[str] = absent()
    state: Lenient[Literal["queued", "running", "done", "failed"] | str] = absent()
    filename: Lenient[str | None] = absent()
    rows_total: Lenient[int | None] = absent()
    rows_added: Lenient[int] = absent()
    rows_existing: Lenient[int] = absent()
    rows_invalid: Lenient[int] = absent()
    invalid_lines: Lenient[builtins.list[int]] = absent()
    failure: Lenient[str | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    finished_at: Lenient[datetime | None] = absent()


class EmailSuppressionImportCreateResponse(EmailSuppressionImport):
    """Import suppressed addresses: the answer."""


class EmailSuppressionImportGetResponse(EmailSuppressionImport):
    """Get an import: the answer."""


class EmailMetricsDomain(TawkedModel):
    """The EmailMetricsDomain object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "name")

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()


class EmailMetricsTotals(TawkedModel):
    """The EmailMetricsTotals object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "sent",
        "delivered",
        "delivery_delayed",
        "bounced",
        "bounced_permanent",
        "bounced_transient",
        "complained",
        "failed",
        "suppressed",
        "opened",
        "unique_opened",
        "clicked",
        "unique_clicked",
        "open_tracked_targets",
        "click_tracked_targets",
    )

    sent: Lenient[int] = absent()
    delivered: Lenient[int] = absent()
    delivery_delayed: Lenient[int] = absent()
    bounced: Lenient[int] = absent()
    bounced_permanent: Lenient[int] = absent()
    bounced_transient: Lenient[int] = absent()
    complained: Lenient[int] = absent()
    failed: Lenient[int] = absent()
    suppressed: Lenient[int] = absent()
    opened: Lenient[int] = absent()
    unique_opened: Lenient[int] = absent()
    clicked: Lenient[int] = absent()
    unique_clicked: Lenient[int] = absent()
    open_tracked_targets: Lenient[int] = absent()
    click_tracked_targets: Lenient[int] = absent()


class EmailMetricsRates(TawkedModel):
    """The EmailMetricsRates object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "delivery_rate",
        "bounce_rate",
        "complaint_rate",
        "open_rate",
        "click_rate",
    )

    delivery_rate: Lenient[float | None] = absent()
    bounce_rate: Lenient[float | None] = absent()
    complaint_rate: Lenient[float | None] = absent()
    open_rate: Lenient[float | None] = absent()
    click_rate: Lenient[float | None] = absent()


class EmailMetricsDataItem(TawkedModel):
    """The EmailMetricsDataItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "period",
        "sent",
        "delivered",
        "delivery_delayed",
        "bounced",
        "bounced_permanent",
        "bounced_transient",
        "complained",
        "failed",
        "suppressed",
        "opened",
        "unique_opened",
        "clicked",
        "unique_clicked",
        "open_tracked_targets",
        "click_tracked_targets",
    )

    period: Lenient[str] = absent()
    sent: Lenient[int] = absent()
    delivered: Lenient[int] = absent()
    delivery_delayed: Lenient[int] = absent()
    bounced: Lenient[int] = absent()
    bounced_permanent: Lenient[int] = absent()
    bounced_transient: Lenient[int] = absent()
    complained: Lenient[int] = absent()
    failed: Lenient[int] = absent()
    suppressed: Lenient[int] = absent()
    opened: Lenient[int] = absent()
    unique_opened: Lenient[int] = absent()
    clicked: Lenient[int] = absent()
    unique_clicked: Lenient[int] = absent()
    open_tracked_targets: Lenient[int] = absent()
    click_tracked_targets: Lenient[int] = absent()


class EmailMetrics(TawkedModel):
    """The EmailMetrics object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "from",
        "to",
        "timezone",
        "granularity",
        "domain",
        "totals",
        "rates",
        "data",
    )

    from_: Lenient[str] = absent("from")
    to: Lenient[str] = absent()
    timezone: Lenient[Literal["Asia/Riyadh"] | str] = absent()
    granularity: Lenient[Literal["day", "week", "month"] | str] = absent()
    domain: Lenient[EmailMetricsDomain | None] = absent()
    totals: Lenient[EmailMetricsTotals] = absent()
    rates: Lenient[EmailMetricsRates] = absent()
    data: Lenient[builtins.list[EmailMetricsDataItem]] = absent()


class EmailMetricsGetResponse(EmailMetrics):
    """Get email metrics: the answer."""


class EmailTemplateVersionFrom(TawkedModel):
    """The EmailTemplateVersionFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailTemplateVersionVariablesItem(TawkedModel):
    """The EmailTemplateVersionVariablesItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("key", "fallback")

    key: Lenient[str] = absent()
    fallback: Lenient[str | None] = absent()


class EmailTemplateProblem(TawkedModel):
    """The EmailTemplateProblem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "severity")

    code: Lenient[str] = absent()
    key: Lenient[str | None] = absent()
    severity: Lenient[Literal["error", "warning"] | str] = absent()


class EmailTemplateVersion(TawkedModel):
    """The EmailTemplateVersion object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "number",
        "state",
        "subject",
        "from",
        "reply_to",
        "variables",
        "placeholders",
        "problems",
        "published_at",
        "updated_at",
    )

    id: Lenient[str] = absent()
    number: Lenient[int | None] = absent()
    state: Lenient[Literal["draft", "published", "superseded"] | str] = absent()
    subject: Lenient[str] = absent()
    html: Lenient[str | None] = absent()
    text: Lenient[str | None] = absent()
    from_: Lenient[EmailTemplateVersionFrom | None] = absent("from")
    reply_to: Lenient[builtins.list[str]] = absent()
    variables: Lenient[builtins.list[EmailTemplateVersionVariablesItem]] = absent()
    placeholders: Lenient[builtins.list[str]] = absent()
    problems: Lenient[builtins.list[EmailTemplateProblem]] = absent()
    published_at: Lenient[datetime | None] = absent()
    updated_at: Lenient[datetime | None] = absent()


class EmailTemplate(TawkedModel):
    """The EmailTemplate object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "alias",
        "name",
        "state",
        "published_version",
        "published",
        "draft",
        "created_at",
        "updated_at",
    )

    id: Lenient[str] = absent()
    alias: Lenient[str | None] = absent()
    name: Lenient[str] = absent()
    state: Lenient[Literal["draft", "published", "published_with_draft"] | str] = absent()
    published_version: Lenient[int | None] = absent()
    published: Lenient[Any] = absent()
    draft: Lenient[Any] = absent()
    created_at: Lenient[datetime | None] = absent()
    updated_at: Lenient[datetime | None] = absent()


class EmailTemplateListResponse(TawkedModel):
    """List templates: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[EmailTemplate]] = absent()
    has_more: Lenient[bool] = absent()
    next_cursor: Lenient[str | None] = absent()


class EmailTemplateCreateResponse(EmailTemplate):
    """Create a template: the answer."""


class EmailTemplateGetResponse(EmailTemplate):
    """Get a template: the answer."""


class EmailTemplateUpdateResponse(EmailTemplate):
    """Update a template: the answer."""


class EmailTemplateDeleteResponse(TawkedModel):
    """Delete a template: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "deleted")

    id: Lenient[str] = absent()
    deleted: Lenient[Literal[True] | bool] = absent()


class EmailTemplatePublishResponse(EmailTemplate):
    """Publish a template: the answer."""


class EmailTemplateVersionRow(TawkedModel):
    """The EmailTemplateVersionRow object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "number",
        "state",
        "subject",
        "published_at",
    )

    id: Lenient[str] = absent()
    number: Lenient[int] = absent()
    state: Lenient[Literal["published", "superseded"] | str] = absent()
    subject: Lenient[str] = absent()
    published_at: Lenient[datetime | None] = absent()


class EmailTemplateVersionListResponse(TawkedModel):
    """List a template's versions: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[EmailTemplateVersionRow]] = absent()
    has_more: Lenient[Literal[False] | bool] = absent()
    next_cursor: Lenient[Any] = absent()


class EmailTemplateVersionGetResponse(EmailTemplateVersion):
    """Get a template version: the answer."""


class EmailTemplateVersionRestoreResponse(EmailTemplate):
    """Restore a template version: the answer."""


class WebhookEndpointLastDelivery(TawkedModel):
    """The WebhookEndpointLastDelivery object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("status", "code", "at")

    status: Lenient[str] = absent()
    code: Lenient[int | None] = absent()
    at: Lenient[datetime | None] = absent()


class WebhookEndpointSigning(TawkedModel):
    """The WebhookEndpointSigning object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "schemes",
        "standard_since",
        "previous_valid_until",
    )

    schemes: Lenient[builtins.list[Literal["tawked", "standard_webhooks"] | str]] = absent()
    standard_since: Lenient[datetime | None] = absent()
    previous_valid_until: Lenient[datetime | None] = absent()


class WebhookEndpointSecrets(TawkedModel):
    """The WebhookEndpointSecrets object."""

    standard: Lenient[str | None] = absent()
    tawked: Lenient[str | None] = absent()


class WebhookEndpoint(TawkedModel):
    """The WebhookEndpoint object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "url",
        "events",
        "enabled",
        "state",
        "disabled_reason",
        "failing_since",
        "receives_test",
        "last_delivery",
        "signing",
        "created_at",
        "updated_at",
    )

    id: Lenient[str] = absent()
    url: Lenient[str] = absent()
    events: Lenient[
        builtins.list[
            Literal[
                "service.approved",
                "service.rejected",
                "service.suspended",
                "service.paused",
                "service.resumed",
                "service.unpaused",
                "service.review_requested",
                "service.archived",
                "service.restored",
                "balance.low",
                "verification.verified",
                "verification.failed",
                "verification.expired",
                "message.sent",
                "message.delivered",
                "message.read",
                "message.failed",
                "email.delivered",
                "email.bounced",
                "email.complained",
                "email.failed",
                "email.received",
                "email.sent",
                "email.delivery_delayed",
                "email.suppressed",
                "email.scheduled",
                "email.canceled",
                "email.opened",
                "email.clicked",
                "domain.created",
                "domain.verified",
                "domain.failed",
                "domain.removed",
                "suppression.added",
                "suppression.removed",
            ]
            | str
        ]
    ] = absent()
    enabled: Lenient[bool] = absent()
    state: Lenient[str] = absent()
    disabled_reason: Lenient[Literal["failing"] | str | None] = absent()
    failing_since: Lenient[datetime | None] = absent()
    receives_test: Lenient[bool] = absent()
    last_delivery: Lenient[WebhookEndpointLastDelivery | None] = absent()
    signing: Lenient[WebhookEndpointSigning] = absent()
    created_at: Lenient[datetime | None] = absent()
    updated_at: Lenient[datetime | None] = absent()
    secrets: Lenient[WebhookEndpointSecrets | None] = absent()


class WebhookEndpointListResponse(TawkedModel):
    """List webhook endpoints: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data",)

    data: Lenient[builtins.list[WebhookEndpoint]] = absent()


class WebhookEndpointCreateResponse(WebhookEndpoint):
    """Create a webhook endpoint: the answer."""


class WebhookEndpointGetResponse(WebhookEndpoint):
    """Get a webhook endpoint: the answer."""


class WebhookEndpointUpdateResponse(WebhookEndpoint):
    """Update a webhook endpoint: the answer."""


class WebhookEndpointDeleteResponse(TawkedModel):
    """Delete a webhook endpoint: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "deleted")

    id: Lenient[str] = absent()
    deleted: Lenient[Literal[True] | bool] = absent()


class WebhookSecretRotateResponseSecrets(TawkedModel):
    """The WebhookSecretRotateResponseSecrets object."""

    standard: Lenient[str | None] = absent()
    tawked: Lenient[str | None] = absent()


class WebhookSecretRotateResponse(TawkedModel):
    """Rotate a webhook secret: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "previous_valid_until",
        "tawked_switched_at",
        "secrets",
    )

    id: Lenient[str] = absent()
    previous_valid_until: Lenient[datetime | None] = absent()
    tawked_switched_at: Lenient[datetime | None] = absent()
    secrets: Lenient[WebhookSecretRotateResponseSecrets] = absent()


class WebhookEndpointDelivery(TawkedModel):
    """The WebhookEndpointDelivery object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "event_id",
        "event",
        "mode",
        "status",
        "attempts",
        "last_status_code",
        "last_error",
        "replay_of_id",
        "created_at",
        "delivered_at",
        "next_attempt_at",
    )

    id: Lenient[str] = absent()
    event_id: Lenient[str | None] = absent()
    event: Lenient[
        Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
    ] = absent()
    mode: Lenient[Literal["live", "test"] | str] = absent()
    status: Lenient[Literal["pending", "delivered", "failed"] | str] = absent()
    attempts: Lenient[int] = absent()
    last_status_code: Lenient[int | None] = absent()
    last_error: Lenient[str | None] = absent()
    replay_of_id: Lenient[str | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    next_attempt_at: Lenient[datetime | None] = absent()
    payload: Lenient[builtins.dict[str, Any] | None] = absent()
    attempt_log: Lenient[builtins.list[builtins.dict[str, Any]] | None] = absent()


class WebhookTestSendResponse(WebhookEndpointDelivery):
    """Send a test event: the answer."""


class WebhookDeliveryListResponse(TawkedModel):
    """List deliveries: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[WebhookEndpointDelivery]] = absent()
    has_more: Lenient[bool] = absent()
    next_cursor: Lenient[str | None] = absent()


class WebhookDeliveryGetResponse(WebhookEndpointDelivery):
    """Get a delivery: the answer."""


class WebhookDeliveryReplayResponse(WebhookEndpointDelivery):
    """Send a delivery again: the answer."""


class WebhookReplay(TawkedModel):
    """The WebhookReplay object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "state", "matched")

    id: Lenient[str] = absent()
    state: Lenient[Literal["queued", "running", "done"] | str] = absent()
    matched: Lenient[int] = absent()
    queued: Lenient[int | None] = absent()
    since: Lenient[datetime | None] = absent()
    until: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    finished_at: Lenient[datetime | None] = absent()


class WebhookReplayCreateResponse(WebhookReplay):
    """Replay deliveries: the answer."""


class WebhookReplayGetResponse(WebhookReplay):
    """Get a replay: the answer."""


class EmailReceivedListItemAddress(TawkedModel):
    """The EmailReceivedListItemAddress object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "domain", "kind")

    id: Lenient[str] = absent()
    domain: Lenient[str] = absent()
    kind: Lenient[Literal["domain", "hosted"] | str] = absent()


class EmailReceivedListItemFrom(TawkedModel):
    """The EmailReceivedListItemFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailReceivedListItemThread(TawkedModel):
    """The EmailReceivedListItemThread object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("email_id", "received_id")

    email_id: Lenient[str | None] = absent()
    received_id: Lenient[str | None] = absent()


class EmailReceivedListItem(TawkedModel):
    """The EmailReceivedListItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "to",
        "from",
        "subject",
        "spam",
        "has_attachments",
        "attachments_count",
        "size",
        "status",
        "thread",
        "received_at",
    )

    id: Lenient[str] = absent()
    address: Lenient[EmailReceivedListItemAddress | None] = absent()
    to: Lenient[builtins.list[str]] = absent()
    from_: Lenient[EmailReceivedListItemFrom | None] = absent("from")
    subject: Lenient[str | None] = absent()
    spam: Lenient[bool] = absent()
    has_attachments: Lenient[bool] = absent()
    attachments_count: Lenient[int] = absent()
    size: Lenient[int | None] = absent()
    status: Lenient[Literal["received", "ready", "failed"] | str] = absent()
    thread: Lenient[EmailReceivedListItemThread | None] = absent()
    received_at: Lenient[datetime] = absent()


class EmailReceivedListResponse(TawkedModel):
    """List received emails: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "has_more", "next_cursor")

    data: Lenient[builtins.list[EmailReceivedListItem]] = absent()
    has_more: Lenient[bool] = absent()
    next_cursor: Lenient[str | None] = absent()


class EmailReceivedAddress(TawkedModel):
    """The EmailReceivedAddress object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "domain", "kind")

    id: Lenient[str] = absent()
    domain: Lenient[str] = absent()
    kind: Lenient[Literal["domain", "hosted"] | str] = absent()


class EmailReceivedFrom(TawkedModel):
    """The EmailReceivedFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailReceivedThread(TawkedModel):
    """The EmailReceivedThread object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("email_id", "received_id")

    email_id: Lenient[str | None] = absent()
    received_id: Lenient[str | None] = absent()


class EmailReceivedHeaderToItem(TawkedModel):
    """The EmailReceivedHeaderToItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailReceivedCcItem(TawkedModel):
    """The EmailReceivedCcItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailReceivedReplyToItem(TawkedModel):
    """The EmailReceivedReplyToItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailReceivedReplyHeaders(TawkedModel):
    """The EmailReceivedReplyHeaders object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("In-Reply-To", "References")

    References: Lenient[str] = absent()


class EmailReceivedHeadersItem(TawkedModel):
    """The EmailReceivedHeadersItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "value")

    name: Lenient[str] = absent()
    value: Lenient[str] = absent()


class EmailReceivedAttachment(TawkedModel):
    """The EmailReceivedAttachment object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "filename",
        "content_type",
        "content_id",
        "inline",
        "size",
        "risky",
        "download_url",
        "download_expires_at",
    )

    id: Lenient[str] = absent()
    filename: Lenient[str | None] = absent()
    content_type: Lenient[str] = absent()
    content_id: Lenient[str | None] = absent()
    inline: Lenient[bool] = absent()
    size: Lenient[int] = absent()
    risky: Lenient[bool] = absent()
    download_url: Lenient[str] = absent()
    download_expires_at: Lenient[datetime] = absent()


class EmailReceivedRaw(TawkedModel):
    """The EmailReceivedRaw object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("download_url", "expires_at")

    download_url: Lenient[str] = absent()
    expires_at: Lenient[datetime] = absent()


class EmailReceivedAuthentication(TawkedModel):
    """The EmailReceivedAuthentication object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("spf", "dkim", "dmarc", "dmarc_policy")

    spf: Lenient[str | None] = absent()
    dkim: Lenient[str | None] = absent()
    dmarc: Lenient[str | None] = absent()
    dmarc_policy: Lenient[Literal["none", "quarantine", "reject"] | str | None] = absent()


class EmailReceivedForwardedVariant1Variant1(TawkedModel):
    """The EmailReceivedForwardedVariant1Variant1 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("email_id", "to", "at", "auto")
    __tawked_variant__: ClassVar[bool] = True

    email_id: Lenient[str] = absent()
    to: Lenient[builtins.list[str]] = absent()
    at: Lenient[datetime | None] = absent()
    auto: Lenient[bool] = absent()


class EmailReceivedForwardedVariant1Variant2(TawkedModel):
    """The EmailReceivedForwardedVariant1Variant2 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("error", "at")
    __tawked_variant__: ClassVar[bool] = True

    error: Lenient[str] = absent()
    at: Lenient[datetime | None] = absent()


class EmailReceived(TawkedModel):
    """The EmailReceived object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "to",
        "from",
        "subject",
        "spam",
        "has_attachments",
        "attachments_count",
        "size",
        "status",
        "thread",
        "received_at",
        "envelope_from",
        "header_to",
        "cc",
        "reply_to",
        "message_id",
        "in_reply_to",
        "references",
        "reply_headers",
        "date",
        "text",
        "html",
        "text_truncated",
        "html_truncated",
        "headers",
        "attachments",
        "attachments_skipped",
        "raw",
        "authentication",
        "virus",
        "spam_verdict",
        "parse_error",
        "forwarded",
        "price_halalas",
        "billing",
        "expires_at",
    )

    id: Lenient[str] = absent()
    address: Lenient[EmailReceivedAddress | None] = absent()
    to: Lenient[builtins.list[str]] = absent()
    from_: Lenient[EmailReceivedFrom | None] = absent("from")
    subject: Lenient[str | None] = absent()
    spam: Lenient[bool] = absent()
    has_attachments: Lenient[bool] = absent()
    attachments_count: Lenient[int] = absent()
    size: Lenient[int | None] = absent()
    status: Lenient[Literal["received", "ready", "failed"] | str] = absent()
    thread: Lenient[EmailReceivedThread | None] = absent()
    received_at: Lenient[datetime] = absent()
    envelope_from: Lenient[str | None] = absent()
    header_to: Lenient[builtins.list[EmailReceivedHeaderToItem]] = absent()
    cc: Lenient[builtins.list[EmailReceivedCcItem]] = absent()
    reply_to: Lenient[builtins.list[EmailReceivedReplyToItem]] = absent()
    message_id: Lenient[str | None] = absent()
    in_reply_to: Lenient[str | None] = absent()
    references: Lenient[builtins.list[str]] = absent()
    reply_headers: Lenient[EmailReceivedReplyHeaders | None] = absent()
    date: Lenient[datetime | None] = absent()
    text: Lenient[str | None] = absent()
    html: Lenient[str | None] = absent()
    text_truncated: Lenient[bool] = absent()
    html_truncated: Lenient[bool] = absent()
    headers: Lenient[builtins.list[EmailReceivedHeadersItem]] = absent()
    attachments: Lenient[builtins.list[EmailReceivedAttachment]] = absent()
    attachments_skipped: Lenient[int] = absent()
    raw: Lenient[EmailReceivedRaw] = absent()
    authentication: Lenient[EmailReceivedAuthentication] = absent()
    virus: Lenient[str | None] = absent()
    spam_verdict: Lenient[str | None] = absent()
    parse_error: Lenient[str | None] = absent()
    forwarded: Lenient[Any] = absent()
    price_halalas: Lenient[int] = absent()
    billing: Lenient[Literal["free", "billed", "unpaid", "none"] | str] = absent()
    expires_at: Lenient[datetime | None] = absent()


class EmailReceivedGetResponse(EmailReceived):
    """Get a received email: the answer."""


class EmailReceivedDeleteResponse(TawkedModel):
    """Delete a received email: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "deleted")

    id: Lenient[str] = absent()
    deleted: Lenient[Literal[True] | bool] = absent()


class EmailReceivedForwardResponse(EmailAccepted):
    """Forward a received email: the answer."""


class EmailInboundAddressHeld(TawkedModel):
    """The EmailInboundAddressHeld object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("reason", "until")

    reason: Lenient[Literal["team", "balance", "daily_limit", "burst"] | str] = absent()
    until: Lenient[datetime | None] = absent()


class EmailInboundAddressForward(TawkedModel):
    """The EmailInboundAddressForward object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("to", "from")

    to: Lenient[str] = absent()
    from_: Lenient[str | None] = absent("from")


class EmailInboundAddress(TawkedModel):
    """The EmailInboundAddress object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "kind",
        "domain",
        "example",
        "state",
        "held",
        "spam_policy",
        "forward",
        "created_at",
    )

    id: Lenient[str] = absent()
    kind: Lenient[Literal["domain", "hosted"] | str] = absent()
    domain: Lenient[str] = absent()
    example: Lenient[str] = absent()
    state: Lenient[Literal["awaiting", "active", "partial", "lost", "off"] | str] = absent()
    held: Lenient[EmailInboundAddressHeld | None] = absent()
    spam_policy: Lenient[Literal["keep", "drop"] | str] = absent()
    forward: Lenient[EmailInboundAddressForward | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class EmailInboundAddressListResponse(TawkedModel):
    """List receiving addresses: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data",)

    data: Lenient[builtins.list[EmailInboundAddress]] = absent()


class EmailReceivedEventDataAddress(TawkedModel):
    """The EmailReceivedEventDataAddress object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "domain", "kind")

    id: Lenient[str] = absent()
    domain: Lenient[str] = absent()
    kind: Lenient[Literal["domain", "hosted"] | str] = absent()


class EmailReceivedEventDataFrom(TawkedModel):
    """The EmailReceivedEventDataFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailReceivedEventDataThread(TawkedModel):
    """The EmailReceivedEventDataThread object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("email_id", "received_id")

    email_id: Lenient[str | None] = absent()
    received_id: Lenient[str | None] = absent()


class EmailReceivedEventDataAuthentication(TawkedModel):
    """The EmailReceivedEventDataAuthentication object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("spf", "dkim", "dmarc", "dmarc_policy")

    spf: Lenient[str | None] = absent()
    dkim: Lenient[str | None] = absent()
    dmarc: Lenient[str | None] = absent()
    dmarc_policy: Lenient[Literal["none", "quarantine", "reject"] | str | None] = absent()


class EmailReceivedEventDataAttachmentsItem(TawkedModel):
    """The EmailReceivedEventDataAttachmentsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "filename",
        "content_type",
        "size",
        "inline",
        "risky",
    )

    id: Lenient[str] = absent()
    filename: Lenient[str | None] = absent()
    content_type: Lenient[str] = absent()
    size: Lenient[int] = absent()
    inline: Lenient[bool] = absent()
    risky: Lenient[bool] = absent()


class EmailReceivedEventData(TawkedModel):
    """The EmailReceivedEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "to",
        "from",
        "subject",
        "spam",
        "has_attachments",
        "attachments_count",
        "size",
        "status",
        "thread",
        "received_at",
        "envelope_from",
        "message_id",
        "in_reply_to",
        "authentication",
        "parse",
        "attachments",
    )

    id: Lenient[str] = absent()
    address: Lenient[EmailReceivedEventDataAddress | None] = absent()
    to: Lenient[builtins.list[str]] = absent()
    from_: Lenient[EmailReceivedEventDataFrom | None] = absent("from")
    subject: Lenient[str | None] = absent()
    spam: Lenient[bool] = absent()
    has_attachments: Lenient[bool] = absent()
    attachments_count: Lenient[int] = absent()
    size: Lenient[int | None] = absent()
    status: Lenient[Literal["received", "ready", "failed"] | str] = absent()
    thread: Lenient[EmailReceivedEventDataThread | None] = absent()
    received_at: Lenient[datetime] = absent()
    envelope_from: Lenient[str | None] = absent()
    message_id: Lenient[str | None] = absent()
    in_reply_to: Lenient[str | None] = absent()
    authentication: Lenient[EmailReceivedEventDataAuthentication] = absent()
    parse: Lenient[Literal["ready", "failed"] | str] = absent()
    attachments: Lenient[builtins.list[EmailReceivedEventDataAttachmentsItem]] = absent()


class EmailReceivedTestResponse(TawkedModel):
    """Simulate a received email: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "event", "mode", "deliveries", "data")

    id: Lenient[str] = absent()
    event: Lenient[Literal["email.received"] | str] = absent()
    mode: Lenient[Literal["test"] | str] = absent()
    deliveries: Lenient[int] = absent()
    data: Lenient[EmailReceivedEventData] = absent()


class ChatMenu(TawkedModel):
    """The ChatMenu object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "title",
        "url",
        "icon_url",
        "frame",
        "created_at",
        "updated_at",
    )

    id: Lenient[str] = absent()
    title: Lenient[str] = absent()
    url: Lenient[str] = absent()
    icon_url: Lenient[str | None] = absent()
    frame: Lenient[Literal["opens", "window", "unknown"] | str] = absent()
    created_at: Lenient[datetime | None] = absent()
    updated_at: Lenient[datetime | None] = absent()


class ChatMenuListResponse(TawkedModel):
    """List menus: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data",)

    data: Lenient[builtins.list[ChatMenu]] = absent()


class ChatMenuCreateResponse(ChatMenu):
    """Add a menu: the answer."""


class ChatMenuGetResponse(ChatMenu):
    """Get a menu: the answer."""


class ChatMenuUpdateResponse(ChatMenu):
    """Update a menu: the answer."""


class ChatMenuDeleteResponse(TawkedModel):
    """Delete a menu: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "deleted")

    id: Lenient[str] = absent()
    deleted: Lenient[Literal[True] | bool] = absent()


class AttendantChoiceActionVariant1(TawkedModel):
    """The AttendantChoiceActionVariant1 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "text", "link")
    __tawked_variant__: ClassVar[bool] = True

    type: Lenient[Literal["reply"] | str] = absent()
    text: Lenient[str] = absent()
    link: Lenient[str | None] = absent()


class AttendantChoiceActionVariant2(TawkedModel):
    """The AttendantChoiceActionVariant2 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "text", "choices")
    __tawked_variant__: ClassVar[bool] = True

    type: Lenient[Literal["submenu"] | str] = absent()
    text: Lenient[str] = absent()
    choices: Lenient[builtins.list[AttendantChoice]] = absent()


class AttendantChoiceActionVariant3Assign(TawkedModel):
    """The AttendantChoiceActionVariant3Assign object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("mode", "member_id")

    mode: Lenient[Literal["auto", "member"] | str] = absent()
    member_id: Lenient[str | None] = absent()


class AttendantChoiceActionVariant3(TawkedModel):
    """The AttendantChoiceActionVariant3 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "type",
        "detail",
        "label",
        "question",
        "tag",
        "assign",
    )
    __tawked_variant__: ClassVar[bool] = True

    type: Lenient[Literal["ask"] | str] = absent()
    detail: Lenient[Literal["order_number", "name", "city", "custom"] | str] = absent()
    label: Lenient[str | None] = absent()
    question: Lenient[str] = absent()
    tag: Lenient[str] = absent()
    assign: Lenient[AttendantChoiceActionVariant3Assign] = absent()


class AttendantChoiceActionVariant4Assign(TawkedModel):
    """The AttendantChoiceActionVariant4Assign object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("mode", "member_id")

    mode: Lenient[Literal["auto", "member"] | str] = absent()
    member_id: Lenient[str | None] = absent()


class AttendantChoiceActionVariant4(TawkedModel):
    """The AttendantChoiceActionVariant4 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "line", "tag", "assign")
    __tawked_variant__: ClassVar[bool] = True

    type: Lenient[Literal["team"] | str] = absent()
    line: Lenient[str | None] = absent()
    tag: Lenient[str] = absent()
    assign: Lenient[AttendantChoiceActionVariant4Assign] = absent()


class AttendantChoiceActionVariant5(TawkedModel):
    """The AttendantChoiceActionVariant5 object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type",)
    __tawked_variant__: ClassVar[bool] = True

    type: Lenient[Literal["radeef"] | str] = absent()


class AttendantChoice(TawkedModel):
    """The AttendantChoice object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "title", "description", "action")

    id: Lenient[str] = absent()
    title: Lenient[str] = absent()
    description: Lenient[str | None] = absent()
    action: Lenient[
        AttendantChoiceActionVariant1
        | AttendantChoiceActionVariant2
        | AttendantChoiceActionVariant3
        | AttendantChoiceActionVariant4
        | AttendantChoiceActionVariant5
    ] = absent()


class AttendantMenu(TawkedModel):
    """The AttendantMenu object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "version",
        "opening",
        "list_button",
        "away",
        "fallback",
        "choices",
    )

    version: Lenient[Literal[1] | int] = absent()
    opening: Lenient[str] = absent()
    list_button: Lenient[str] = absent()
    away: Lenient[str | None] = absent()
    fallback: Lenient[str | None] = absent()
    choices: Lenient[builtins.list[AttendantChoice]] = absent()


class AttendantProblem(TawkedModel):
    """The AttendantProblem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "choice_id", "field", "max")

    code: Lenient[
        Literal[
            "opening_empty",
            "text_long",
            "list_button_empty",
            "list_button_long",
            "choices_empty",
            "too_many",
            "title_empty",
            "title_long",
            "title_duplicate",
            "title_reserved",
            "description_long",
            "submenu_empty",
            "submenu_text_empty",
            "depth",
            "reply_empty",
            "link_invalid",
            "question_empty",
            "label_empty",
            "label_long",
            "tag_invalid",
            "member_missing",
            "action_unknown",
            "no_team_choice",
            "duplicate_id",
            "bad_id",
        ]
        | str
    ] = absent()
    choice_id: Lenient[str | None] = absent()
    field: Lenient[str] = absent()
    max: Lenient[int | None] = absent()


class AttendantPublished(TawkedModel):
    """The AttendantPublished object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("version", "published_at", "menu")

    version: Lenient[int] = absent()
    published_at: Lenient[datetime] = absent()
    menu: Lenient[AttendantMenu] = absent()


class Attendant(TawkedModel):
    """The Attendant object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "state",
        "lock",
        "enabled",
        "mode",
        "language",
        "draft",
        "draft_saved_at",
        "problems",
        "published",
        "changed",
    )

    state: Lenient[
        Literal["first", "draft", "off", "live", "no_number", "no_chat", "blocked"] | str
    ] = absent()
    lock: Lenient[Literal["payment", "blocked"] | str | None] = absent()
    enabled: Lenient[bool] = absent()
    mode: Lenient[Literal["menu_only", "menu_then_radeef"] | str] = absent()
    language: Lenient[Literal["ar", "en"] | str] = absent()
    draft: Lenient[AttendantMenu] = absent()
    draft_saved_at: Lenient[datetime | None] = absent()
    problems: Lenient[builtins.list[AttendantProblem]] = absent()
    published: Lenient[AttendantPublished | None] = absent()
    changed: Lenient[bool] = absent()


class ChatAttendantGetResponse(Attendant):
    """Get the auto-attendant: the answer."""


class ChatAttendantDraftSaveResponse(TawkedModel):
    """Save the auto-attendant draft: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("draft_saved_at", "problems", "menu")

    draft_saved_at: Lenient[datetime] = absent()
    problems: Lenient[builtins.list[AttendantProblem]] = absent()
    menu: Lenient[AttendantMenu] = absent()


class ChatAttendantPublishResponse(TawkedModel):
    """Publish the auto-attendant: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("version", "published_at")

    version: Lenient[int] = absent()
    published_at: Lenient[datetime] = absent()


class ChatAttendantStateSetResponse(Attendant):
    """Switch the auto-attendant on or off: the answer."""


class ChatAttendantSettingsUpdateResponse(Attendant):
    """Update the auto-attendant settings: the answer."""


class PartnerProfileResponsePrices(TawkedModel):
    """The PartnerProfileResponsePrices object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("sms_code_halalas",)

    sms_code_halalas: Lenient[int] = absent()


class PartnerProfileResponseKey(TawkedModel):
    """The PartnerProfileResponseKey object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "prefix",
        "mode",
        "created_at",
        "expires_at",
        "ip_allowlist",
    )

    prefix: Lenient[str] = absent()
    mode: Lenient[Literal["partner", "partner_test"] | str] = absent()
    created_at: Lenient[datetime | None] = absent()
    expires_at: Lenient[datetime | None] = absent()
    ip_allowlist: Lenient[builtins.list[str]] = absent()


class PartnerProfileResponseWebhook(TawkedModel):
    """The PartnerProfileResponseWebhook object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("configured", "url")

    configured: Lenient[bool] = absent()
    url: Lenient[str | None] = absent()


class PartnerProfileResponse(TawkedModel):
    """Get the profile: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "name_ar",
        "name_en",
        "slug",
        "approval_mode",
        "balance_halalas",
        "low_balance_threshold_halalas",
        "prices",
        "rate_limit_per_minute",
        "key",
        "webhook",
    )

    name_ar: Lenient[str] = absent()
    name_en: Lenient[str | None] = absent()
    slug: Lenient[str | None] = absent()
    approval_mode: Lenient[
        Literal["tawked", "partner_clean", "partner_all", "auto_clean"] | str
    ] = absent()
    balance_halalas: Lenient[int] = absent()
    low_balance_threshold_halalas: Lenient[int] = absent()
    prices: Lenient[PartnerProfileResponsePrices] = absent()
    rate_limit_per_minute: Lenient[int] = absent()
    key: Lenient[PartnerProfileResponseKey] = absent()
    webhook: Lenient[PartnerProfileResponseWebhook] = absent()


class PartnerScreeningResponseReview(TawkedModel):
    """The PartnerScreeningResponseReview object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("needed", "decided_by")

    needed: Lenient[bool] = absent()
    decided_by: Lenient[Literal["partner", "tawked"] | str | None] = absent()


class PartnerScreeningResponse(TawkedModel):
    """Preview the screening: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("result", "rules", "review")

    result: Lenient[Literal["clean", "flagged"] | str] = absent()
    rules: Lenient[builtins.list[str]] = absent()
    review: Lenient[PartnerScreeningResponseReview] = absent()


class Screening(TawkedModel):
    """The Screening object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("result", "rules")

    result: Lenient[Literal["clean", "flagged"] | str] = absent()
    rules: Lenient[builtins.list[str]] = absent()


class VerifySettings(TawkedModel):
    """The VerifySettings object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "code_length",
        "ttl_seconds",
        "max_attempts",
        "max_per_hour",
        "autofill_domain",
        "autofill_domain_enabled",
        "android_app_hash",
        "daily_spend_cap_halalas",
        "max_per_ip_per_hour",
        "max_new_destinations_per_hour",
    )

    code_length: Lenient[int] = absent()
    ttl_seconds: Lenient[Literal[60, 120, 180, 300, 600, 900] | int] = absent()
    max_attempts: Lenient[int] = absent()
    max_per_hour: Lenient[int] = absent()
    autofill_domain: Lenient[str | None] = absent()
    autofill_domain_enabled: Lenient[bool] = absent()
    android_app_hash: Lenient[str | None] = absent()
    daily_spend_cap_halalas: Lenient[int | None] = absent()
    max_per_ip_per_hour: Lenient[int] = absent()
    max_new_destinations_per_hour: Lenient[int] = absent()


class ApplicationSummary(TawkedModel):
    """The ApplicationSummary object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "status",
        "screening",
        "verify",
        "paused",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    status: Lenient[Literal["review", "active", "rejected", "suspended"] | str] = absent()
    screening: Lenient[Any] = absent()
    verify: Lenient[VerifySettings] = absent()
    paused: Lenient[bool] = absent()


class PartnerApplicationCreateResponse(ApplicationSummary):
    """Provision an application: the answer."""


class PartnerApplicationBatchResponseResultsItem(TawkedModel):
    """The PartnerApplicationBatchResponseResultsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "index",
        "external_id",
        "outcome",
        "application",
    )

    index: Lenient[int] = absent()
    external_id: Lenient[str | None] = absent()
    outcome: Lenient[Literal["created", "existing", "refused"] | str] = absent()
    fields_: Lenient[builtins.list[str] | None] = absent("fields")
    application: Lenient[Any] = absent()


class PartnerApplicationBatchResponse(TawkedModel):
    """Provision in bulk: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("created", "existing", "refused", "results")

    created: Lenient[int] = absent()
    existing: Lenient[int] = absent()
    refused: Lenient[int] = absent()
    results: Lenient[builtins.list[PartnerApplicationBatchResponseResultsItem]] = absent()


class ApplicationRow(TawkedModel):
    """The ApplicationRow object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "status",
        "screening",
        "verify",
        "paused",
        "name_ar",
        "name_en",
        "website",
        "industry",
        "merchant",
        "logo_url",
        "metadata",
        "status_message",
        "approved_at",
        "disabled",
        "disabled_at",
        "archived",
        "archived_at",
        "paused_at",
        "pause_reason",
        "created_at",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    status: Lenient[Literal["review", "active", "rejected", "suspended"] | str] = absent()
    screening: Lenient[Any] = absent()
    verify: Lenient[VerifySettings] = absent()
    paused: Lenient[bool] = absent()
    name_ar: Lenient[str] = absent()
    name_en: Lenient[str] = absent()
    website: Lenient[str | None] = absent()
    industry: Lenient[str | None] = absent()
    merchant: Lenient[builtins.dict[str, Any] | None] = absent()
    logo_url: Lenient[str | None] = absent()
    metadata: Lenient[builtins.dict[str, str] | None] = absent()
    status_message: Lenient[str | None] = absent()
    approved_at: Lenient[datetime | None] = absent()
    disabled: Lenient[bool] = absent()
    disabled_at: Lenient[datetime | None] = absent()
    archived: Lenient[bool] = absent()
    archived_at: Lenient[datetime | None] = absent()
    paused_at: Lenient[datetime | None] = absent()
    pause_reason: Lenient[str | None] = absent()
    created_at: Lenient[datetime] = absent()


class PartnerApplicationListResponse(TawkedModel):
    """List applications: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("total", "applications")

    total: Lenient[int] = absent()
    applications: Lenient[builtins.list[ApplicationRow]] = absent()


class PartnerApplicationGetResponse(ApplicationRow):
    """Get an application: the answer."""


class PartnerApplicationHistoryResponseEventsItem(TawkedModel):
    """The PartnerApplicationHistoryResponseEventsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "action",
        "actor",
        "reason",
        "screening",
        "created_at",
    )

    action: Lenient[
        Literal[
            "provisioned",
            "submitted",
            "approve",
            "reject",
            "suspend",
            "resume",
            "renamed",
            "settings_changed",
            "brand_changed",
            "archived",
            "restored",
        ]
        | str
    ] = absent()
    actor: Lenient[Literal["tawked", "partner", "client", "system"] | str] = absent()
    reason: Lenient[str | None] = absent()
    screening: Lenient[Any] = absent()
    created_at: Lenient[datetime] = absent()


class PartnerApplicationHistoryResponse(TawkedModel):
    """Get the history: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("external_id", "events")

    external_id: Lenient[str | None] = absent()
    events: Lenient[builtins.list[PartnerApplicationHistoryResponseEventsItem]] = absent()


class PartnerApplicationUpdateResponse(ApplicationSummary):
    """Update the brand: the answer."""


class PartnerLogoUploadResponse(ApplicationRow):
    """Upload the logo: the answer."""


class PartnerLogoRemoveResponse(ApplicationRow):
    """Remove the logo: the answer."""


class PartnerVerifySettingsUpdateResponse(TawkedModel):
    """Update the verify settings: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("external_id", "verify")

    external_id: Lenient[str | None] = absent()
    verify: Lenient[VerifySettings] = absent()


class PartnerApplicationSuspendResponse(TawkedModel):
    """Suspend an application: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("external_id", "disabled")

    external_id: Lenient[str | None] = absent()
    disabled: Lenient[Literal[True] | bool] = absent()


class PartnerApplicationResumeResponse(TawkedModel):
    """Resume an application: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("external_id", "disabled")

    external_id: Lenient[str | None] = absent()
    disabled: Lenient[Literal[False] | bool] = absent()


class PartnerApplicationUnpauseResponse(TawkedModel):
    """Unpause an application: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("external_id", "paused")

    external_id: Lenient[str | None] = absent()
    paused: Lenient[Literal[False] | bool] = absent()


class PartnerApplicationArchiveResponse(ApplicationRow):
    """Archive an application: the answer."""


class PartnerApplicationRestoreResponse(ApplicationRow):
    """Restore an application: the answer."""


class PartnerUsageResponseApplicationsItem(TawkedModel):
    """The PartnerUsageResponseApplicationsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "external_id",
        "application_id",
        "name_ar",
        "sent",
        "verified",
        "spend_halalas",
    )

    external_id: Lenient[str | None] = absent()
    application_id: Lenient[str] = absent()
    name_ar: Lenient[str] = absent()
    sent: Lenient[int] = absent()
    verified: Lenient[int] = absent()
    spend_halalas: Lenient[int] = absent()


class PartnerUsageResponse(TawkedModel):
    """Get usage: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "from",
        "to",
        "balance_halalas",
        "applications",
    )

    from_: Lenient[datetime] = absent("from")
    to: Lenient[datetime] = absent()
    balance_halalas: Lenient[int] = absent()
    applications: Lenient[builtins.list[PartnerUsageResponseApplicationsItem]] = absent()


class PartnerVerificationListItem(TawkedModel):
    """One item of List verifications."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "application_id",
        "external_id",
        "status",
        "channel",
        "to",
        "reference",
        "attempts_remaining",
        "resends_remaining",
        "expires_at",
        "verified_at",
        "created_at",
        "mode",
        "lang",
        "price_halalas",
    )

    id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    status: Lenient[Literal["pending", "verified", "failed", "expired", "canceled"] | str] = (
        absent()
    )
    channel: Lenient[str] = absent()
    to: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    attempts_remaining: Lenient[int] = absent()
    resends_remaining: Lenient[int] = absent()
    expires_at: Lenient[datetime] = absent()
    verified_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    mode: Lenient[Literal["live", "test", "partner", "partner_test"] | str] = absent()
    lang: Lenient[str] = absent()
    price_halalas: Lenient[int] = absent()


class PartnerVerificationListResponse(TawkedModel):
    """List verifications: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "next_cursor", "has_more")

    data: Lenient[builtins.list[PartnerVerificationListItem]] = absent()
    next_cursor: Lenient[str | None] = absent()
    has_more: Lenient[bool] = absent()


class PartnerEventListItemDelivery(TawkedModel):
    """The PartnerEventListItemDelivery object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "status", "attempts", "delivered_at")

    id: Lenient[str] = absent()
    status: Lenient[Literal["pending", "delivered", "failed"] | str] = absent()
    attempts: Lenient[int] = absent()
    delivered_at: Lenient[datetime | None] = absent()


class PartnerEventListItem(TawkedModel):
    """One item of Get the event feed."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "event",
        "external_id",
        "data",
        "created_at",
        "delivery",
    )

    id: Lenient[str] = absent()
    event: Lenient[
        Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
        ]
        | str
    ] = absent()
    external_id: Lenient[str | None] = absent()
    data: Lenient[builtins.dict[str, Any]] = absent()
    created_at: Lenient[datetime] = absent()
    delivery: Lenient[PartnerEventListItemDelivery | None] = absent()


class PartnerEventListResponse(TawkedModel):
    """Get the event feed: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "next_cursor", "has_more")

    data: Lenient[builtins.list[PartnerEventListItem]] = absent()
    next_cursor: Lenient[str | None] = absent()
    has_more: Lenient[bool] = absent()


class PartnerWebhook(TawkedModel):
    """The PartnerWebhook object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "url",
        "configured",
        "low_balance_threshold_halalas",
        "events",
        "default_events",
        "available_events",
    )

    url: Lenient[str | None] = absent()
    configured: Lenient[bool] = absent()
    low_balance_threshold_halalas: Lenient[int] = absent()
    events: Lenient[
        builtins.list[
            Literal[
                "service.approved",
                "service.rejected",
                "service.suspended",
                "service.paused",
                "service.resumed",
                "service.unpaused",
                "service.review_requested",
                "service.archived",
                "service.restored",
                "balance.low",
                "verification.verified",
                "verification.failed",
                "verification.expired",
            ]
            | str
        ]
    ] = absent()
    default_events: Lenient[
        builtins.list[
            Literal[
                "service.approved",
                "service.rejected",
                "service.suspended",
                "service.paused",
                "service.resumed",
                "service.unpaused",
                "service.review_requested",
                "service.archived",
                "service.restored",
                "balance.low",
                "verification.verified",
                "verification.failed",
                "verification.expired",
            ]
            | str
        ]
    ] = absent()
    available_events: Lenient[
        builtins.list[
            Literal[
                "service.approved",
                "service.rejected",
                "service.suspended",
                "service.paused",
                "service.resumed",
                "service.unpaused",
                "service.review_requested",
                "service.archived",
                "service.restored",
                "balance.low",
                "verification.verified",
                "verification.failed",
                "verification.expired",
            ]
            | str
        ]
    ] = absent()


class PartnerWebhookGetResponse(PartnerWebhook):
    """Get the webhook: the answer."""


class PartnerWebhookUpdateResponse(PartnerWebhook):
    """Update the webhook: the answer."""


class WebhookDelivery(TawkedModel):
    """The WebhookDelivery object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "event",
        "status",
        "attempts",
        "last_status_code",
        "last_error",
        "next_attempt_at",
        "delivered_at",
        "created_at",
    )

    id: Lenient[str] = absent()
    event: Lenient[
        Literal[
            "service.approved",
            "service.rejected",
            "service.suspended",
            "service.paused",
            "service.resumed",
            "service.unpaused",
            "service.review_requested",
            "service.archived",
            "service.restored",
            "balance.low",
            "verification.verified",
            "verification.failed",
            "verification.expired",
            "message.sent",
            "message.delivered",
            "message.read",
            "message.failed",
            "email.delivered",
            "email.bounced",
            "email.complained",
            "email.failed",
            "email.received",
            "email.sent",
            "email.delivery_delayed",
            "email.suppressed",
            "email.scheduled",
            "email.canceled",
            "email.opened",
            "email.clicked",
            "domain.created",
            "domain.verified",
            "domain.failed",
            "domain.removed",
            "suppression.added",
            "suppression.removed",
        ]
        | str
    ] = absent()
    status: Lenient[Literal["pending", "delivered", "failed"] | str] = absent()
    attempts: Lenient[int] = absent()
    last_status_code: Lenient[int | None] = absent()
    last_error: Lenient[str | None] = absent()
    next_attempt_at: Lenient[datetime | None] = absent()
    delivered_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class PartnerDeliveryListResponse(TawkedModel):
    """List deliveries: the answer."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("data", "next_cursor")

    data: Lenient[builtins.list[WebhookDelivery]] = absent()
    next_cursor: Lenient[str | None] = absent()


class PartnerDeliveryRetryResponse(WebhookDelivery):
    """Retry a delivery: the answer."""


class AppConnectionApplication(TawkedModel):
    """The AppConnectionApplication object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "name_ar", "name_en")

    id: Lenient[str] = absent()
    name_ar: Lenient[str] = absent()
    name_en: Lenient[str] = absent()


class AppConnection(TawkedModel):
    """The connection a merchant approved: its key (``access_token``, shown once), its application and permissions."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "access_token",
        "token_type",
        "connection_id",
        "application",
        "permissions",
    )

    access_token: Lenient[str] = absent()
    token_type: Lenient[Literal["Bearer"] | str] = absent()
    connection_id: Lenient[str] = absent()
    application: Lenient[AppConnectionApplication] = absent()
    permissions: Lenient[builtins.list[str]] = absent()


class VerifyStartParams(TawkedParams):
    """The fields of the request, by their wire names."""

    to: Any = Field(default=None)
    phone: Any = Field(default=None)
    channel: Any = Field(default=None)
    lang: Any = Field(default=None)
    application: Any = Field(default=None)
    reference: Any = Field(default=None)
    client_ip: Any = Field(default=None)
    autofill: Any = Field(default=None)


class VerifyCheckParams(TawkedParams):
    """The fields of the request, by their wire names."""

    id: Any = Field(default=None)
    code: Any = Field(default=None)
    application: Any = Field(default=None)


class VerifyGetParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class VerifyResendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class VerifyCancelParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class WhatsAppSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["lang"])
    to: Any = Field(default=None)
    template: Any = Field(default=None)
    lang: Any = Field(default=None)
    params: Any = Field(default=None)
    header: Any = Field(default=None)
    buttons: Any = Field(default=None)
    reference: Any = Field(default=None)
    application: Any = Field(default=None)


class WhatsAppMessageGetParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class WhatsAppTemplateListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class WhatsAppTemplateCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["footer", "header"])
    name: Any = Field(default=None)
    language: Any = Field(default=None)
    category: Any = Field(default=None)
    header: Any = Field(default=None)
    body: Any = Field(default=None)
    footer: Any = Field(default=None)
    buttons: Any = Field(default=None)
    examples: Any = Field(default=None)


class WhatsAppTemplateUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["footer", "header"])
    category: Any = Field(default=None)
    header: Any = Field(default=None)
    body: Any = Field(default=None)
    footer: Any = Field(default=None)
    buttons: Any = Field(default=None)
    examples: Any = Field(default=None)


class EmailSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "attachments",
            "bcc",
            "cc",
            "from",
            "headers",
            "html",
            "reference",
            "reply_to",
            "scheduled_at",
            "tags",
            "text",
            "to",
        ]
    )
    from_: Any = Field(default=None, alias="from")
    to: Any = Field(default=None)
    cc: Any = Field(default=None)
    bcc: Any = Field(default=None)
    reply_to: Any = Field(default=None)
    subject: Any = Field(default=None)
    html: Any = Field(default=None)
    text: Any = Field(default=None)
    template: Any = Field(default=None)
    reference: Any = Field(default=None)
    headers: Any = Field(default=None)
    tags: Any = Field(default=None)
    scheduled_at: DateTimeIn | None = Field(default=None)
    attachments: Any = Field(default=None)
    application: Any = Field(default=None)


class EmailBatchSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class EmailMessageListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    limit: Any = Field(default=None)
    cursor: Any = Field(default=None)
    status: Any = Field(default=None)
    to: Any = Field(default=None)
    reference: Any = Field(default=None)
    tag: Any = Field(default=None)
    created_after: DateTimeIn | None = Field(default=None)
    created_before: DateTimeIn | None = Field(default=None)
    application: Any = Field(default=None)


class EmailMessageGetParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class EmailMessageRescheduleParams(TawkedParams):
    """The fields of the request, by their wire names."""

    scheduled_at: DateTimeIn | None = Field(default=None)
    application: Any = Field(default=None)


class EmailMessageCancelParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class EmailKeyCheckParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)


class EmailDomainListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    state: Any = Field(default=None)
    limit: Any = Field(default=None)
    cursor: Any = Field(default=None)


class EmailDomainCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name: Any = Field(default=None)


class EmailDomainUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    from_name: Any = Field(default=None)
    from_local: Any = Field(default=None)
    tracking: Any = Field(default=None)


class EmailSuppressionListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    reason: Any = Field(default=None)
    source: Any = Field(default=None)
    address: Any = Field(default=None)
    created_after: DateTimeIn | None = Field(default=None)
    created_before: DateTimeIn | None = Field(default=None)
    limit: Any = Field(default=None)
    cursor: Any = Field(default=None)


class EmailSuppressionAddParams(TawkedParams):
    """The fields of the request, by their wire names."""

    addresses: Any = Field(default=None)
    address: Any = Field(default=None)


class EmailSuppressionRemoveParams(TawkedParams):
    """The fields of the request, by their wire names."""

    reason: Any = Field(default=None)
    note: Any = Field(default=None)


class EmailSuppressionImportCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    file: Any = Field(default=None)


class EmailMetricsGetParams(TawkedParams):
    """The fields of the request, by their wire names."""

    from_: Any = Field(default=None, alias="from")
    to: Any = Field(default=None)
    granularity: Any = Field(default=None)
    domain: Any = Field(default=None)
    timezone: Any = Field(default=None)


class EmailTemplateListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    limit: Any = Field(default=None)
    cursor: Any = Field(default=None)


class EmailTemplateCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name: Any = Field(default=None)
    alias: Any = Field(default=None)
    subject: Any = Field(default=None)
    html: Any = Field(default=None)
    text: Any = Field(default=None)
    from_: Any = Field(default=None, alias="from")
    reply_to: Any = Field(default=None)
    variables: Any = Field(default=None)
    publish: Any = Field(default=None)


class EmailTemplateUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name: Any = Field(default=None)
    alias: Any = Field(default=None)
    subject: Any = Field(default=None)
    html: Any = Field(default=None)
    text: Any = Field(default=None)
    from_: Any = Field(default=None, alias="from")
    reply_to: Any = Field(default=None)
    variables: Any = Field(default=None)
    publish: Any = Field(default=None)


class WebhookEndpointCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    url: Any = Field(default=None)
    events: Any = Field(default=None)
    receives_test: Any = Field(default=None)


class WebhookEndpointUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    url: Any = Field(default=None)
    events: Any = Field(default=None)
    enabled: Any = Field(default=None)
    receives_test: Any = Field(default=None)
    signing: Any = Field(default=None)


class WebhookSecretRotateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    scheme: Any = Field(default=None)


class WebhookTestSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    event: Any = Field(default=None)


class WebhookDeliveryListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    status: Any = Field(default=None)
    event: Any = Field(default=None)
    created_after: DateTimeIn | None = Field(default=None)
    created_before: DateTimeIn | None = Field(default=None)
    limit: Any = Field(default=None)
    cursor: Any = Field(default=None)


class WebhookReplayCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    since: DateTimeIn | None = Field(default=None)
    until: DateTimeIn | None = Field(default=None)
    status: Any = Field(default=None)
    events: Any = Field(default=None)


class EmailReceivedListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    limit: Any = Field(default=None)
    cursor: Any = Field(default=None)
    address_id: Any = Field(default=None)
    to: Any = Field(default=None)
    from_: Any = Field(default=None, alias="from")
    spam: Any = Field(default=None)
    has_attachments: Any = Field(default=None)
    received_after: DateTimeIn | None = Field(default=None)
    received_before: DateTimeIn | None = Field(default=None)


class EmailReceivedForwardParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["from", "note"])
    to: Any = Field(default=None)
    from_: Any = Field(default=None, alias="from")
    note: Any = Field(default=None)


class ChatMenuCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    title: Any = Field(default=None)
    url: Any = Field(default=None)
    icon: Any = Field(default=None)


class ChatMenuUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    title: Any = Field(default=None)
    url: Any = Field(default=None)
    icon: Any = Field(default=None)


class ChatAttendantDraftSaveParams(TawkedParams):
    """The fields of the request, by their wire names."""

    menu: Any = Field(default=None)


class ChatAttendantStateSetParams(TawkedParams):
    """The fields of the request, by their wire names."""

    enabled: Any = Field(default=None)


class ChatAttendantSettingsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    mode: Any = Field(default=None)
    language: Any = Field(default=None)


class PartnerScreeningParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)


class PartnerApplicationCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    external_id: Any = Field(default=None)
    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    website: Any = Field(default=None)
    industry: Any = Field(default=None)
    merchant: Any = Field(default=None)
    verify: Any = Field(default=None)
    metadata: Any = Field(default=None)


class PartnerApplicationListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    status: Any = Field(default=None)
    disabled: Any = Field(default=None)
    archived: Any = Field(default=None)
    metadata: Any = Field(default=None)
    limit: Any = Field(default=None)
    offset: Any = Field(default=None)


class PartnerApplicationUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    website: Any = Field(default=None)
    industry: Any = Field(default=None)
    merchant: Any = Field(default=None)
    verify: Any = Field(default=None)
    metadata: Any = Field(default=None)


class PartnerLogoUploadParams(TawkedParams):
    """The fields of the request, by their wire names."""

    logo: Any = Field(default=None)


class PartnerVerifySettingsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["android_app_hash", "daily_spend_cap_halalas"]
    )
    code_length: Any = Field(default=None)
    ttl_seconds: Any = Field(default=None)
    max_attempts: Any = Field(default=None)
    max_per_hour: Any = Field(default=None)
    autofill_domain_enabled: Any = Field(default=None)
    android_app_hash: Any = Field(default=None)
    daily_spend_cap_halalas: Any = Field(default=None)
    max_per_ip_per_hour: Any = Field(default=None)
    max_new_destinations_per_hour: Any = Field(default=None)


class PartnerUsageParams(TawkedParams):
    """The fields of the request, by their wire names."""

    from_: DateTimeIn | None = Field(default=None, alias="from")
    to: DateTimeIn | None = Field(default=None)


class PartnerVerificationListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)
    status: Any = Field(default=None)
    mode: Any = Field(default=None)
    reference: Any = Field(default=None)
    from_: DateTimeIn | None = Field(default=None, alias="from")
    to: DateTimeIn | None = Field(default=None)
    cursor: Any = Field(default=None)
    limit: Any = Field(default=None)


class PartnerEventListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    since: DateTimeIn | None = Field(default=None)
    cursor: Any = Field(default=None)
    event: Any = Field(default=None)
    application: Any = Field(default=None)
    limit: Any = Field(default=None)


class PartnerWebhookUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["events"])
    events: Any = Field(default=None)
    low_balance_threshold_halalas: Any = Field(default=None)


class PartnerDeliveryListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    status: Any = Field(default=None)
    event: Any = Field(default=None)
    cursor: Any = Field(default=None)
    limit: Any = Field(default=None)


for _model in (
    VerifyStartResponse,
    VerifyCheckResponse,
    Verification,
    VerifyGetResponse,
    VerifyResendResponse,
    VerifyCancelResponse,
    WhatsAppSendResponse,
    WhatsAppMessageError,
    WhatsAppMessage,
    WhatsAppMessageGetResponse,
    WhatsAppTemplateListResponseDataItemPlaceholdersButtonsItem,
    WhatsAppTemplateListResponseDataItemPlaceholders,
    WhatsAppTemplateListResponseDataItem,
    WhatsAppTemplateListResponse,
    WhatsAppTemplateComponentsItemButtonsItem,
    WhatsAppTemplateComponentsItem,
    WhatsAppTemplatePlaceholdersButtonsItem,
    WhatsAppTemplatePlaceholders,
    WhatsAppTemplate,
    WhatsAppTemplateGetResponse,
    WhatsAppTemplateCreateResponse,
    WhatsAppTemplateUpdateResponse,
    WhatsAppTemplateDeleteResponse,
    EmailSendResponseFrom,
    EmailAcceptedFrom,
    EmailTag,
    EmailRecipientAccepted,
    EmailCost,
    EmailAccepted,
    EmailSendResponse,
    EmailBatchError,
    EmailBatchSendResponse,
    EmailMessageExtendedFrom,
    EmailBounce,
    EmailError,
    EmailRecipient,
    EmailMessageExtendedAttachmentsItem,
    EmailMessageExtendedTemplate,
    EmailMessageExtended,
    EmailMessageListResponse,
    EmailMessageFrom,
    EmailMessageAttachmentsItem,
    EmailMessage,
    EmailMessageGetResponseFrom,
    EmailMessageGetResponseAttachmentsItem,
    EmailMessageGetResponseTemplate,
    EmailMessageGetResponse,
    EmailMessageRescheduleResponse,
    EmailMessageCancelResponse,
    EmailKeyCheckResponseApplication,
    EmailKeyCheckResponse,
    EmailMessageContentResponse,
    EmailDomainRecordsItem,
    EmailDomainDefaults,
    EmailDomainTracking,
    EmailDomainReceiving,
    EmailDomain,
    EmailDomainListResponse,
    EmailDomainCreateResponse,
    EmailDomainGetResponse,
    EmailDomainUpdateResponse,
    EmailDomainVerifyResponse,
    EmailDomainDeleteResponse,
    EmailSuppression,
    EmailSuppressionListResponse,
    EmailSuppressionAddResponseInvalidItem,
    EmailSuppressionAddResponse,
    EmailSuppressionLookup,
    EmailSuppressionGetResponse,
    EmailSuppressionRemoveResponse,
    EmailSuppressionImport,
    EmailSuppressionImportCreateResponse,
    EmailSuppressionImportGetResponse,
    EmailMetricsDomain,
    EmailMetricsTotals,
    EmailMetricsRates,
    EmailMetricsDataItem,
    EmailMetrics,
    EmailMetricsGetResponse,
    EmailTemplateVersionFrom,
    EmailTemplateVersionVariablesItem,
    EmailTemplateProblem,
    EmailTemplateVersion,
    EmailTemplate,
    EmailTemplateListResponse,
    EmailTemplateCreateResponse,
    EmailTemplateGetResponse,
    EmailTemplateUpdateResponse,
    EmailTemplateDeleteResponse,
    EmailTemplatePublishResponse,
    EmailTemplateVersionRow,
    EmailTemplateVersionListResponse,
    EmailTemplateVersionGetResponse,
    EmailTemplateVersionRestoreResponse,
    WebhookEndpointLastDelivery,
    WebhookEndpointSigning,
    WebhookEndpointSecrets,
    WebhookEndpoint,
    WebhookEndpointListResponse,
    WebhookEndpointCreateResponse,
    WebhookEndpointGetResponse,
    WebhookEndpointUpdateResponse,
    WebhookEndpointDeleteResponse,
    WebhookSecretRotateResponseSecrets,
    WebhookSecretRotateResponse,
    WebhookEndpointDelivery,
    WebhookTestSendResponse,
    WebhookDeliveryListResponse,
    WebhookDeliveryGetResponse,
    WebhookDeliveryReplayResponse,
    WebhookReplay,
    WebhookReplayCreateResponse,
    WebhookReplayGetResponse,
    EmailReceivedListItemAddress,
    EmailReceivedListItemFrom,
    EmailReceivedListItemThread,
    EmailReceivedListItem,
    EmailReceivedListResponse,
    EmailReceivedAddress,
    EmailReceivedFrom,
    EmailReceivedThread,
    EmailReceivedHeaderToItem,
    EmailReceivedCcItem,
    EmailReceivedReplyToItem,
    EmailReceivedReplyHeaders,
    EmailReceivedHeadersItem,
    EmailReceivedAttachment,
    EmailReceivedRaw,
    EmailReceivedAuthentication,
    EmailReceivedForwardedVariant1Variant1,
    EmailReceivedForwardedVariant1Variant2,
    EmailReceived,
    EmailReceivedGetResponse,
    EmailReceivedDeleteResponse,
    EmailReceivedForwardResponse,
    EmailInboundAddressHeld,
    EmailInboundAddressForward,
    EmailInboundAddress,
    EmailInboundAddressListResponse,
    EmailReceivedEventDataAddress,
    EmailReceivedEventDataFrom,
    EmailReceivedEventDataThread,
    EmailReceivedEventDataAuthentication,
    EmailReceivedEventDataAttachmentsItem,
    EmailReceivedEventData,
    EmailReceivedTestResponse,
    ChatMenu,
    ChatMenuListResponse,
    ChatMenuCreateResponse,
    ChatMenuGetResponse,
    ChatMenuUpdateResponse,
    ChatMenuDeleteResponse,
    AttendantChoiceActionVariant1,
    AttendantChoiceActionVariant2,
    AttendantChoiceActionVariant3Assign,
    AttendantChoiceActionVariant3,
    AttendantChoiceActionVariant4Assign,
    AttendantChoiceActionVariant4,
    AttendantChoiceActionVariant5,
    AttendantChoice,
    AttendantMenu,
    AttendantProblem,
    AttendantPublished,
    Attendant,
    ChatAttendantGetResponse,
    ChatAttendantDraftSaveResponse,
    ChatAttendantPublishResponse,
    ChatAttendantStateSetResponse,
    ChatAttendantSettingsUpdateResponse,
    PartnerProfileResponsePrices,
    PartnerProfileResponseKey,
    PartnerProfileResponseWebhook,
    PartnerProfileResponse,
    PartnerScreeningResponseReview,
    PartnerScreeningResponse,
    Screening,
    VerifySettings,
    ApplicationSummary,
    PartnerApplicationCreateResponse,
    PartnerApplicationBatchResponseResultsItem,
    PartnerApplicationBatchResponse,
    ApplicationRow,
    PartnerApplicationListResponse,
    PartnerApplicationGetResponse,
    PartnerApplicationHistoryResponseEventsItem,
    PartnerApplicationHistoryResponse,
    PartnerApplicationUpdateResponse,
    PartnerLogoUploadResponse,
    PartnerLogoRemoveResponse,
    PartnerVerifySettingsUpdateResponse,
    PartnerApplicationSuspendResponse,
    PartnerApplicationResumeResponse,
    PartnerApplicationUnpauseResponse,
    PartnerApplicationArchiveResponse,
    PartnerApplicationRestoreResponse,
    PartnerUsageResponseApplicationsItem,
    PartnerUsageResponse,
    PartnerVerificationListItem,
    PartnerVerificationListResponse,
    PartnerEventListItemDelivery,
    PartnerEventListItem,
    PartnerEventListResponse,
    PartnerWebhook,
    PartnerWebhookGetResponse,
    PartnerWebhookUpdateResponse,
    WebhookDelivery,
    PartnerDeliveryListResponse,
    PartnerDeliveryRetryResponse,
    AppConnectionApplication,
    AppConnection,
):
    _model.model_rebuild()
