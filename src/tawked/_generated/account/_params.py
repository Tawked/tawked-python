"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from typing import Any, ClassVar

from pydantic import Field

from tawked._models import DateTimeIn, TawkedParams

_ = (Any, ClassVar, DateTimeIn)


class AccountAccountAlertsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)
    group: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountAccountDocumentUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    business_document_number: Any = Field(default=None)
    business_document_type: Any = Field(default=None)


class AccountAccountEmailConfirmParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["application", "then"])
    code: Any = Field(default=None)
    application: Any = Field(default=None)
    then: Any = Field(default=None)


class AccountAccountEmailSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    email: Any = Field(default=None)


class AccountAccountMeUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["email"])
    name: Any = Field(default=None)
    email: Any = Field(default=None)


class AccountAccountProfileUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["contact_email"])
    business_document_number: Any = Field(default=None)
    business_document_type: Any = Field(default=None)
    contact_name: Any = Field(default=None)
    contact_email: Any = Field(default=None)


class AccountApplicationsAppealsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["document"])
    note: Any = Field(default=None)
    document: Any = Field(default=None)


class AccountApplicationsApplicationsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    industry: Any = Field(default=None)
    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    products: Any = Field(default=None)
    website_url: Any = Field(default=None)
    integration: Any = Field(default=None)


class AccountApplicationsApplicationsDeleteParams(TawkedParams):
    """The fields of the request, by their wire names."""

    confirm_name: Any = Field(default=None)


class AccountApplicationsApplicationsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["logo"])
    industry: Any = Field(default=None)
    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    website_url: Any = Field(default=None)
    integration: Any = Field(default=None)
    logo: Any = Field(default=None)
    remove_logo: Any = Field(default=None)


class AccountApplicationsKeysCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "email_domain_id",
            "expires_in_days",
            "inbound",
            "ip_allowlist",
            "name",
            "scopes",
            "webhooks",
        ]
    )
    mode: Any = Field(default=None)
    access: Any = Field(default=None)
    email_domain_id: Any = Field(default=None)
    expires_in_days: Any = Field(default=None)
    inbound: Any = Field(default=None)
    ip_allowlist: Any = Field(default=None)
    name: Any = Field(default=None)
    scope: Any = Field(default=None)
    scopes: Any = Field(default=None)
    webhooks: Any = Field(default=None)


class AccountApplicationsLogoUploadParams(TawkedParams):
    """The fields of the request, by their wire names."""

    logo: Any = Field(default=None)


class AccountApplicationsProductsAddParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["then"])
    product: Any = Field(default=None)
    then: Any = Field(default=None)


class AccountApplicationsWebhookDeliveriesListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    endpoint: Any = Field(default=None)
    event: Any = Field(default=None)
    log: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountApplicationsWebhooksCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    events: Any = Field(default=None)
    url: Any = Field(default=None)
    enabled: Any = Field(default=None)
    receives_test: Any = Field(default=None)
    signing: Any = Field(default=None)
    standard_webhooks: Any = Field(default=None)


class AccountApplicationsWebhooksRotateSecretParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["scheme"])
    scheme: Any = Field(default=None)


class AccountApplicationsWebhooksTestParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["event"])
    event: Any = Field(default=None)


class AccountApplicationsWebhooksUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    events: Any = Field(default=None)
    url: Any = Field(default=None)
    enabled: Any = Field(default=None)
    receives_test: Any = Field(default=None)
    signing: Any = Field(default=None)
    standard_webhooks: Any = Field(default=None)


class AccountAutomationsAutomationsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["recipe"])
    recipe: Any = Field(default=None)


class AccountAutomationsAutomationsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["name"])
    definition: Any = Field(default=None)
    name: Any = Field(default=None)


class AccountAutomationsRunsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountCampaignsCampaignsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "audience",
            "campaign",
            "date",
            "header_image_path",
            "mapping",
            "name",
            "template_language",
            "template_name",
            "time",
        ]
    )
    audience: Any = Field(default=None)
    campaign: Any = Field(default=None)
    date: DateTimeIn | None = Field(default=None)
    header_image_path: Any = Field(default=None)
    intent: Any = Field(default=None)
    mapping: Any = Field(default=None)
    name: Any = Field(default=None)
    send_mode: Any = Field(default=None)
    template_language: Any = Field(default=None)
    template_name: Any = Field(default=None)
    time: DateTimeIn | None = Field(default=None)


class AccountCampaignsCampaignsPreviewEstimateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "audience",
            "campaign",
            "date",
            "header_image_path",
            "mapping",
            "name",
            "template_language",
            "template_name",
            "time",
        ]
    )
    audience: Any = Field(default=None)
    campaign: Any = Field(default=None)
    date: DateTimeIn | None = Field(default=None)
    header_image_path: Any = Field(default=None)
    intent: Any = Field(default=None)
    mapping: Any = Field(default=None)
    name: Any = Field(default=None)
    send_mode: Any = Field(default=None)
    template_language: Any = Field(default=None)
    template_name: Any = Field(default=None)
    time: DateTimeIn | None = Field(default=None)


class AccountCampaignsCampaignsSendTestParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "audience",
            "campaign",
            "date",
            "header_image_path",
            "mapping",
            "name",
            "template_language",
            "template_name",
            "time",
        ]
    )
    audience: Any = Field(default=None)
    campaign: Any = Field(default=None)
    date: DateTimeIn | None = Field(default=None)
    header_image_path: Any = Field(default=None)
    intent: Any = Field(default=None)
    mapping: Any = Field(default=None)
    name: Any = Field(default=None)
    send_mode: Any = Field(default=None)
    template_language: Any = Field(default=None)
    template_name: Any = Field(default=None)
    time: DateTimeIn | None = Field(default=None)


class AccountCampaignsCampaignsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "audience",
            "campaign",
            "date",
            "header_image_path",
            "mapping",
            "name",
            "template_language",
            "template_name",
            "time",
        ]
    )
    audience: Any = Field(default=None)
    campaign_: Any = Field(default=None, alias="campaign")
    date: DateTimeIn | None = Field(default=None)
    header_image_path: Any = Field(default=None)
    intent: Any = Field(default=None)
    mapping: Any = Field(default=None)
    name: Any = Field(default=None)
    send_mode: Any = Field(default=None)
    template_language: Any = Field(default=None)
    template_name: Any = Field(default=None)
    time: DateTimeIn | None = Field(default=None)


class AccountCampaignsImagesUploadParams(TawkedParams):
    """The fields of the request, by their wire names."""

    image: Any = Field(default=None)


class AccountCampaignsRecipientsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountChatAttendantLogParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["cursor", "limit", "q"])
    cursor: Any = Field(default=None)
    limit: Any = Field(default=None)
    outcome: Any = Field(default=None)
    q: Any = Field(default=None)


class AccountChatAttendantSaveDraftParams(TawkedParams):
    """The fields of the request, by their wire names."""

    definition: Any = Field(default=None)


class AccountChatAttendantSwitchParams(TawkedParams):
    """The fields of the request, by their wire names."""

    enabled: Any = Field(default=None)


class AccountChatAttendantUpdateSettingsParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["fallback_member_id"])
    fallback_assign: Any = Field(default=None)
    fallback_member_id: Any = Field(default=None)
    language: Any = Field(default=None)
    mode: Any = Field(default=None)


class AccountChatMenusCheckParams(TawkedParams):
    """The fields of the request, by their wire names."""

    url: Any = Field(default=None)


class AccountChatMenusCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["icon"])
    title: Any = Field(default=None)
    url: Any = Field(default=None)
    icon: Any = Field(default=None)
    icon_mode: Any = Field(default=None)


class AccountChatMenusUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["icon"])
    title: Any = Field(default=None)
    url: Any = Field(default=None)
    icon: Any = Field(default=None)
    icon_mode: Any = Field(default=None)


class AccountChatTeamAddParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["email", "language", "member_id", "phone"]
    )
    role: Any = Field(default=None)
    email: Any = Field(default=None)
    language: Any = Field(default=None)
    member_id: Any = Field(default=None)
    name: Any = Field(default=None)
    phone: Any = Field(default=None)


class AccountChatTeamUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name: Any = Field(default=None)
    role: Any = Field(default=None)


class AccountClientsApiKeyCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["expires_in_days", "ip_allowlist"])
    expires_in_days: Any = Field(default=None)
    ip_allowlist: Any = Field(default=None)


class AccountClientsAppealsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["document"])
    note: Any = Field(default=None)
    document: Any = Field(default=None)


class AccountClientsApplicationsBulkApproveParams(TawkedParams):
    """The fields of the request, by their wire names."""

    ids: Any = Field(default=None)


class AccountClientsApplicationsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    external_id: Any = Field(default=None)
    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    website_url: Any = Field(default=None)
    industry: Any = Field(default=None)


class AccountClientsApplicationsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    archived: Any = Field(default=None)
    page: Any = Field(default=None)
    period: Any = Field(default=None)
    q: Any = Field(default=None)
    sort: Any = Field(default=None)
    state: Any = Field(default=None)


class AccountClientsApplicationsRejectParams(TawkedParams):
    """The fields of the request, by their wire names."""

    reason: Any = Field(default=None)


class AccountClientsApplicationsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    website_url: Any = Field(default=None)
    industry: Any = Field(default=None)


class AccountClientsDeliveriesListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    event: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountClientsReviewsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)
    queue: Any = Field(default=None)


class AccountClientsUsageShowParams(TawkedParams):
    """The fields of the request, by their wire names."""

    from_: DateTimeIn | None = Field(default=None, alias="from")
    month: DateTimeIn | None = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    to: DateTimeIn | None = Field(default=None)


class AccountClientsWebhookUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["events", "threshold_sar", "url"])
    events: Any = Field(default=None)
    threshold_sar: Any = Field(default=None)
    url: Any = Field(default=None)


class AccountContactsContactsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)
    source: Any = Field(default=None)
    status: Any = Field(default=None)
    tag: Any = Field(default=None)


class AccountContactsContactsRecordOptInParams(TawkedParams):
    """The fields of the request, by their wire names."""

    method: Any = Field(default=None)
    note: Any = Field(default=None)
    attested: Any = Field(default=None)


class AccountContactsContactsTagParams(TawkedParams):
    """The fields of the request, by their wire names."""

    tags: Any = Field(default=None)


class AccountContactsImportsConfirmParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["consent_since", "consent_text"])
    basis: Any = Field(default=None)
    attested: Any = Field(default=None)
    consent_since: DateTimeIn | None = Field(default=None)
    consent_text: Any = Field(default=None)


class AccountContactsImportsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["csv", "file", "file_name"])
    csv: Any = Field(default=None)
    file: Any = Field(default=None)
    file_name: Any = Field(default=None)


class AccountContactsOptInUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    keyword: Any = Field(default=None)
    welcome_reply: Any = Field(default=None)


class AccountEmailAccessRequestParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["domain", "note"])
    volume: Any = Field(default=None)
    domain: Any = Field(default=None)
    note: Any = Field(default=None)
    transactional_only: Any = Field(default=None)


class AccountEmailInboundAddressesStoreParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["domain_id", "label", "slug"])
    kind: Any = Field(default=None)
    domain_id: Any = Field(default=None)
    label: Any = Field(default=None)
    slug: Any = Field(default=None)


class AccountEmailInboundAddressesUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["forward_from_local", "forward_to"])
    forward_from_local: Any = Field(default=None)
    forward_to: Any = Field(default=None)
    spam_policy: Any = Field(default=None)
    state: Any = Field(default=None)


class AccountEmailLimitRequestParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["note"])
    requested_limit: Any = Field(default=None)
    note: Any = Field(default=None)


class AccountEmailMessagesListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    domain: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountEmailMessagesPreviewParams(TawkedParams):
    """The fields of the request, by their wire names."""

    domain: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountEmailMessagesShowParams(TawkedParams):
    """The fields of the request, by their wire names."""

    domain: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountEmailReceivedForwardParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["from", "from_name", "note"])
    to: Any = Field(default=None)
    from_: Any = Field(default=None, alias="from")
    from_name: Any = Field(default=None)
    note: Any = Field(default=None)


class AccountEmailReviewRequestParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["fixes"])
    note: Any = Field(default=None)
    fixes: Any = Field(default=None)


class AccountEmailSendersCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    domain: Any = Field(default=None)


class AccountEmailSendersSendTestParams(TawkedParams):
    """The fields of the request, by their wire names."""

    to: Any = Field(default=None)


class AccountEmailSendersSetMailFromParams(TawkedParams):
    """The fields of the request, by their wire names."""

    label: Any = Field(default=None)


class AccountEmailSendersTrackingUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["label"])
    clicks: Any = Field(default=None)
    label: Any = Field(default=None)
    opens: Any = Field(default=None)


class AccountEmailSendersUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["from_name"])
    from_local: Any = Field(default=None)
    from_name: Any = Field(default=None)


class AccountEmailSettingsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    keep_previews: Any = Field(default=None)


class AccountEmailSuppressionsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    addresses: Any = Field(default=None)


class AccountEmailSuppressionsDeleteParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["note", "reason"])
    note: Any = Field(default=None)
    reason: Any = Field(default=None)


class AccountEmailSuppressionsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)
    reason: Any = Field(default=None)


class AccountEmailTestAddressConfirmParams(TawkedParams):
    """The fields of the request, by their wire names."""

    code: Any = Field(default=None)


class AccountEmailTestAddressSendCodeParams(TawkedParams):
    """The fields of the request, by their wire names."""

    email: Any = Field(default=None)


class AccountIntegrationAppsAppsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["connect_url", "description", "logo"]
    )
    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    redirect_uris: Any = Field(default=None)
    site_url: Any = Field(default=None)
    connect_url: Any = Field(default=None)
    description: Any = Field(default=None)
    logo: Any = Field(default=None)
    remove_logo: Any = Field(default=None)


class AccountIntegrationAppsAppsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["connect_url", "description", "logo"]
    )
    name_ar: Any = Field(default=None)
    name_en: Any = Field(default=None)
    redirect_uris: Any = Field(default=None)
    site_url: Any = Field(default=None)
    connect_url: Any = Field(default=None)
    description: Any = Field(default=None)
    logo: Any = Field(default=None)
    remove_logo: Any = Field(default=None)


class AccountIntegrationsLarmConsentUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    attested: Any = Field(default=None)


class AccountIntegrationsLarmMessagesUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    enabled: Any = Field(default=None)
    statuses: Any = Field(default=None)


class AccountMembersMembersCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["email", "language"])
    name: Any = Field(default=None)
    phone: Any = Field(default=None)
    role: Any = Field(default=None)
    access: Any = Field(default=None)
    all_applications: Any = Field(default=None)
    clients_access: Any = Field(default=None)
    email: Any = Field(default=None)
    language: Any = Field(default=None)


class AccountMembersMembersUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["email"])
    name: Any = Field(default=None)
    role: Any = Field(default=None)
    access: Any = Field(default=None)
    all_applications: Any = Field(default=None)
    clients_access: Any = Field(default=None)
    email: Any = Field(default=None)


class AccountRadeefConversationsCorrectParams(TawkedParams):
    """The fields of the request, by their wire names."""

    answer: Any = Field(default=None)
    question: Any = Field(default=None)


class AccountRadeefConversationsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    outcome: Any = Field(default=None)
    page: Any = Field(default=None)
    period: Any = Field(default=None)
    q: Any = Field(default=None)
    reason: Any = Field(default=None)


class AccountRadeefFaqsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    answer: Any = Field(default=None)
    question: Any = Field(default=None)


class AccountRadeefFaqsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    answer: Any = Field(default=None)
    question: Any = Field(default=None)


class AccountRadeefFilesApproveParams(TawkedParams):
    """The fields of the request, by their wire names."""

    content: Any = Field(default=None)


class AccountRadeefFilesCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    file: Any = Field(default=None)


class AccountRadeefNotesCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["answer", "question", "text"])
    as_: Any = Field(default=None, alias="as")
    answer: Any = Field(default=None)
    question: Any = Field(default=None)
    text: Any = Field(default=None)
    topic: Any = Field(default=None)


class AccountRadeefNotesGuessParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["text", "url"])
    text: Any = Field(default=None)
    url: Any = Field(default=None)


class AccountRadeefNoticesChooseParams(TawkedParams):
    """The fields of the request, by their wire names."""

    key: Any = Field(default=None)
    side: Any = Field(default=None)


class AccountRadeefOwnerExamParams(TawkedParams):
    """The fields of the request, by their wire names."""

    count: Any = Field(default=None)


class AccountRadeefOwnerRehearseParams(TawkedParams):
    """The fields of the request, by their wire names."""

    count: Any = Field(default=None)


class AccountRadeefOwnerResetParams(TawkedParams):
    """The fields of the request, by their wire names."""

    count: Any = Field(default=None)


class AccountRadeefOwnerSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    text: Any = Field(default=None)


class AccountRadeefOwnerChangesApplyParams(TawkedParams):
    """The fields of the request, by their wire names."""

    edits: Any = Field(default=None)


class AccountRadeefOwnerChangesDismissParams(TawkedParams):
    """The fields of the request, by their wire names."""

    edits: Any = Field(default=None)


class AccountRadeefOwnerChangesUndoParams(TawkedParams):
    """The fields of the request, by their wire names."""

    edits: Any = Field(default=None)


class AccountRadeefPagesCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    url: Any = Field(default=None)


class AccountRadeefPlaygroundPreviewParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["question"])
    text: Any = Field(default=None)
    topic: Any = Field(default=None)
    question: Any = Field(default=None)


class AccountRadeefPlaygroundSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["phone"])
    text: Any = Field(default=None)
    phone: Any = Field(default=None)


class AccountRadeefReviewApplyParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["scan"])
    add_pages: Any = Field(default=None)
    edits: Any = Field(default=None)
    follow: Any = Field(default=None)
    kept: Any = Field(default=None)
    merge: Any = Field(default=None)
    rejected: Any = Field(default=None)
    scan: Any = Field(default=None)
    vanished: Any = Field(default=None)


class AccountRadeefScansCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    url: Any = Field(default=None)
    mine: Any = Field(default=None)


class AccountRadeefSettingsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "assign_member_id",
            "monthly_cap_halalas",
            "persona_name_en",
            "ramadan",
            "return_after_hours",
        ]
    )
    assign_mode: Any = Field(default=None)
    csat: Any = Field(default=None)
    emoji: Any = Field(default=None)
    etiquette: Any = Field(default=None)
    idle_minutes: Any = Field(default=None)
    intro: Any = Field(default=None)
    mode: Any = Field(default=None)
    orders: Any = Field(default=None)
    persona_name: Any = Field(default=None)
    products: Any = Field(default=None)
    read_receipts: Any = Field(default=None)
    register_: Any = Field(default=None, alias="register")
    reply_cap: Any = Field(default=None)
    reply_length: Any = Field(default=None)
    speed: Any = Field(default=None)
    split: Any = Field(default=None)
    strict: Any = Field(default=None)
    topics: Any = Field(default=None)
    typing: Any = Field(default=None)
    assign_member_id: Any = Field(default=None)
    custom_enabled: Any = Field(default=None)
    custom_topics: Any = Field(default=None)
    keywords: Any = Field(default=None)
    keywords_enabled: Any = Field(default=None)
    messages: Any = Field(default=None)
    monthly_cap_halalas: Any = Field(default=None)
    order_status: Any = Field(default=None)
    persona_name_en: Any = Field(default=None)
    ramadan: Any = Field(default=None)
    return_after_hours: Any = Field(default=None)
    week: Any = Field(default=None)


class AccountRadeefSettingsWhenParams(TawkedParams):
    """The fields of the request, by their wire names."""

    hours_mode: Any = Field(default=None)
    mode: Any = Field(default=None)


class AccountRadeefSetupCharacterParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["persona_name_en"])
    character: Any = Field(default=None)
    persona_name: Any = Field(default=None)
    persona_name_en: Any = Field(default=None)


class AccountRadeefSetupLiveParams(TawkedParams):
    """The fields of the request, by their wire names."""

    choice: Any = Field(default=None)


class AccountRadeefSetupReadParams(TawkedParams):
    """The fields of the request, by their wire names."""

    url: Any = Field(default=None)
    mine: Any = Field(default=None)


class AccountRadeefSourcesSetEnabledParams(TawkedParams):
    """The fields of the request, by their wire names."""

    enabled: Any = Field(default=None)


class AccountRadeefStateUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    enabled: Any = Field(default=None)
    mode: Any = Field(default=None)


class AccountRadeefTopicsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["text"])
    text: Any = Field(default=None)


class AccountRadeefUnansweredAnswerParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["question"])
    answer: Any = Field(default=None)
    question: Any = Field(default=None)


class AccountStoresSallaEmployeesAddParams(TawkedParams):
    """The fields of the request, by their wire names."""

    people: Any = Field(default=None)


class AccountVerifySettingsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "android_app_hash",
            "autofill_domain_enabled",
            "daily_spend_cap_halalas",
            "max_new_destinations_per_hour",
            "max_per_ip_per_hour",
        ]
    )
    android_app_hash: Any = Field(default=None)
    autofill_domain: Any = Field(default=None)
    autofill_domain_enabled: Any = Field(default=None)
    code_length: Any = Field(default=None)
    daily_spend_cap_halalas: Any = Field(default=None)
    max_attempts: Any = Field(default=None)
    max_new_destinations_per_hour: Any = Field(default=None)
    max_per_hour: Any = Field(default=None)
    max_per_ip_per_hour: Any = Field(default=None)
    ttl_seconds: Any = Field(default=None)


class AccountVerifyTestCheckParams(TawkedParams):
    """The fields of the request, by their wire names."""

    code: Any = Field(default=None)
    id: Any = Field(default=None)


class AccountVerifyUsageShowParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["period"])
    period: Any = Field(default=None)


class AccountVerifyVerificationsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    mode: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    range: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountWalletAutoTopupUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["payment_method_id"])
    amount_halalas: Any = Field(default=None)
    enabled: Any = Field(default=None)
    threshold_halalas: Any = Field(default=None)
    payment_method_id: Any = Field(default=None)


class AccountWalletBillingUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["building_number", "district", "other_id", "postal_code", "street", "vat_number"]
    )
    city: Any = Field(default=None)
    email: Any = Field(default=None)
    legal_name: Any = Field(default=None)
    building_number: Any = Field(default=None)
    district: Any = Field(default=None)
    other_id: Any = Field(default=None)
    other_id_type: Any = Field(default=None)
    postal_code: Any = Field(default=None)
    street: Any = Field(default=None)
    vat_number: Any = Field(default=None)


class AccountWalletInvoicesListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    document_kind: Any = Field(default=None)
    document_month: DateTimeIn | None = Field(default=None)
    number: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)


class AccountWalletProformasCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    amount_halalas: Any = Field(default=None)
    billing: Any = Field(default=None)


class AccountWalletSettingsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["alert_email"])
    alert_enabled: Any = Field(default=None)
    alert_email: Any = Field(default=None)
    alert_threshold_halalas: Any = Field(default=None)
    auto_topup: Any = Field(default=None)


class AccountWalletStatementListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)
    day: DateTimeIn | None = Field(default=None)
    kind: Any = Field(default=None)
    month: DateTimeIn | None = Field(default=None)
    page: Any = Field(default=None)
    product: Any = Field(default=None)
    q: Any = Field(default=None)
    reference: Any = Field(default=None)
    side: Any = Field(default=None)


class AccountWalletStatementsShowParams(TawkedParams):
    """The fields of the request, by their wire names."""

    application: Any = Field(default=None)
    day: DateTimeIn | None = Field(default=None)
    kind: Any = Field(default=None)
    month: DateTimeIn | None = Field(default=None)
    page: Any = Field(default=None)
    product: Any = Field(default=None)
    q: Any = Field(default=None)
    reference: Any = Field(default=None)
    side: Any = Field(default=None)


class AccountWalletTopupsLinkParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["amount_halalas"])
    amount_halalas: Any = Field(default=None)


class AccountWhatsAppMessagesListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)
    range: Any = Field(default=None)
    status: Any = Field(default=None)
    template: Any = Field(default=None)


class AccountWhatsAppMessagesPreviewParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["header", "lang", "language", "reference"]
    )
    template: Any = Field(default=None)
    to: Any = Field(default=None)
    buttons: Any = Field(default=None)
    header: Any = Field(default=None)
    lang: Any = Field(default=None)
    language: Any = Field(default=None)
    params: Any = Field(default=None)
    reference: Any = Field(default=None)


class AccountWhatsAppMessagesSendParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["header", "lang", "language", "reference"]
    )
    template: Any = Field(default=None)
    to: Any = Field(default=None)
    buttons: Any = Field(default=None)
    header: Any = Field(default=None)
    lang: Any = Field(default=None)
    language: Any = Field(default=None)
    params: Any = Field(default=None)
    reference: Any = Field(default=None)


class AccountWhatsAppNumberChangePinParams(TawkedParams):
    """The fields of the request, by their wire names."""

    pin: Any = Field(default=None)


class AccountWhatsAppNumberRequestDisplayNameParams(TawkedParams):
    """The fields of the request, by their wire names."""

    name: Any = Field(default=None)


class AccountWhatsAppNumberRequestOfficialBadgeParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["note", "parent_brand"])
    country: Any = Field(default=None)
    language: Any = Field(default=None)
    links: Any = Field(default=None)
    website: Any = Field(default=None)
    note: Any = Field(default=None)
    parent_brand: Any = Field(default=None)


class AccountWhatsAppNumberUpdateComponentsParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["commands", "prompts"])
    welcome_message: Any = Field(default=None)
    commands: Any = Field(default=None)
    prompts: Any = Field(default=None)


class AccountWhatsAppNumberUpdateProfileParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        ["address", "description", "email", "picture", "vertical", "websites"]
    )
    about: Any = Field(default=None)
    address: Any = Field(default=None)
    description: Any = Field(default=None)
    email: Any = Field(default=None)
    picture: Any = Field(default=None)
    vertical: Any = Field(default=None)
    websites: Any = Field(default=None)


class AccountWhatsAppTemplateDraftsAssistantParams(TawkedParams):
    """The fields of the request, by their wire names."""

    draft_: Any = Field(default=None, alias="draft")
    message: Any = Field(default=None)
    revision: Any = Field(default=None)
    retry: Any = Field(default=None)


class AccountWhatsAppTemplateDraftsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    duplicate: Any = Field(default=None)
    source: Any = Field(default=None)


class AccountWhatsAppTemplateDraftsListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    page: Any = Field(default=None)
    q: Any = Field(default=None)


class AccountWhatsAppTemplateDraftsSubmitParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "autofill_text",
            "category",
            "code_expiry_minutes",
            "message_send_ttl_seconds",
            "name",
            "otp_type",
            "package_name",
            "security_recommendation",
            "signature_hash",
            "zero_tap_terms_accepted",
        ]
    )
    revision: Any = Field(default=None)
    autofill_text: Any = Field(default=None)
    category: Any = Field(default=None)
    code_expiry_minutes: Any = Field(default=None)
    message_send_ttl_seconds: Any = Field(default=None)
    name: Any = Field(default=None)
    otp_type: Any = Field(default=None)
    package_name: Any = Field(default=None)
    security_recommendation: Any = Field(default=None)
    signature_hash: Any = Field(default=None)
    variants: Any = Field(default=None)
    zero_tap_terms_accepted: Any = Field(default=None)


class AccountWhatsAppTemplateDraftsUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "autofill_text",
            "category",
            "code_expiry_minutes",
            "message_send_ttl_seconds",
            "name",
            "otp_type",
            "package_name",
            "security_recommendation",
            "signature_hash",
            "zero_tap_terms_accepted",
        ]
    )
    revision: Any = Field(default=None)
    autofill_text: Any = Field(default=None)
    category: Any = Field(default=None)
    code_expiry_minutes: Any = Field(default=None)
    message_send_ttl_seconds: Any = Field(default=None)
    name: Any = Field(default=None)
    otp_type: Any = Field(default=None)
    package_name: Any = Field(default=None)
    security_recommendation: Any = Field(default=None)
    signature_hash: Any = Field(default=None)
    variants: Any = Field(default=None)
    zero_tap_terms_accepted: Any = Field(default=None)


class AccountWhatsAppTemplateLibraryCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["library_id"])
    language: Any = Field(default=None)
    library_name: Any = Field(default=None)
    name: Any = Field(default=None)
    buttons: Any = Field(default=None)
    library_id: Any = Field(default=None)


class AccountWhatsAppTemplateLibraryListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    industry: Any = Field(default=None)
    language: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    topic: Any = Field(default=None)
    usecase: Any = Field(default=None)


class AccountWhatsAppTemplateSamplesCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    image: Any = Field(default=None)


class AccountWhatsAppTemplateSuggestionsCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    keys: Any = Field(default=None)


class AccountWhatsAppTemplateSuggestionsStartParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["description", "website_url"])
    description: Any = Field(default=None)
    website_url: Any = Field(default=None)


class AccountWhatsAppTemplatesCheckParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "autofill_text",
            "footer",
            "header",
            "header_format",
            "header_sample",
            "message_send_ttl_seconds",
        ]
    )
    category: Any = Field(default=None)
    language: Any = Field(default=None)
    name: Any = Field(default=None)
    autofill_text: Any = Field(default=None)
    body: Any = Field(default=None)
    buttons: Any = Field(default=None)
    code_expiry_minutes: Any = Field(default=None)
    examples: Any = Field(default=None)
    footer: Any = Field(default=None)
    header: Any = Field(default=None)
    header_format: Any = Field(default=None)
    header_sample: Any = Field(default=None)
    message_send_ttl_seconds: Any = Field(default=None)
    otp_type: Any = Field(default=None)
    package_name: Any = Field(default=None)
    security_recommendation: Any = Field(default=None)
    signature_hash: Any = Field(default=None)
    zero_tap_terms_accepted: Any = Field(default=None)


class AccountWhatsAppTemplatesCreateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "autofill_text",
            "footer",
            "header",
            "header_format",
            "header_sample",
            "message_send_ttl_seconds",
        ]
    )
    category: Any = Field(default=None)
    language: Any = Field(default=None)
    name: Any = Field(default=None)
    autofill_text: Any = Field(default=None)
    body: Any = Field(default=None)
    buttons: Any = Field(default=None)
    code_expiry_minutes: Any = Field(default=None)
    examples: Any = Field(default=None)
    footer: Any = Field(default=None)
    header: Any = Field(default=None)
    header_format: Any = Field(default=None)
    header_sample: Any = Field(default=None)
    message_send_ttl_seconds: Any = Field(default=None)
    otp_type: Any = Field(default=None)
    package_name: Any = Field(default=None)
    security_recommendation: Any = Field(default=None)
    signature_hash: Any = Field(default=None)
    zero_tap_terms_accepted: Any = Field(default=None)


class AccountWhatsAppTemplatesListParams(TawkedParams):
    """The fields of the request, by their wire names."""

    category: Any = Field(default=None)
    language: Any = Field(default=None)
    page: Any = Field(default=None)
    q: Any = Field(default=None)
    status: Any = Field(default=None)


class AccountWhatsAppTemplatesUpdateParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(
        [
            "autofill_text",
            "footer",
            "header",
            "header_format",
            "header_sample",
            "message_send_ttl_seconds",
        ]
    )
    category: Any = Field(default=None)
    language: Any = Field(default=None)
    name: Any = Field(default=None)
    autofill_text: Any = Field(default=None)
    body: Any = Field(default=None)
    buttons: Any = Field(default=None)
    code_expiry_minutes: Any = Field(default=None)
    examples: Any = Field(default=None)
    footer: Any = Field(default=None)
    header: Any = Field(default=None)
    header_format: Any = Field(default=None)
    header_sample: Any = Field(default=None)
    message_send_ttl_seconds: Any = Field(default=None)
    otp_type: Any = Field(default=None)
    package_name: Any = Field(default=None)
    security_recommendation: Any = Field(default=None)
    signature_hash: Any = Field(default=None)
    zero_tap_terms_accepted: Any = Field(default=None)


class AccountWhatsAppUsageShowParams(TawkedParams):
    """The fields of the request, by their wire names."""

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset(["period"])
    period: Any = Field(default=None)
