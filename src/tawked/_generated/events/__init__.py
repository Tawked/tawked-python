"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

import builtins
from datetime import datetime
from typing import Any, ClassVar, Literal

from pydantic import Field

from tawked._generated.types import EmailReceivedEventData, EmailTag
from tawked._models import Lenient, TawkedModel, absent

_ = (builtins, datetime, Any, ClassVar, Literal)


class BalanceLowData(TawkedModel):
    """The BalanceLowData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("balance_halalas", "threshold_halalas")

    balance_halalas: Lenient[int] = absent()
    threshold_halalas: Lenient[int] = absent()


class DomainEventDataRecordsItem(TawkedModel):
    """The DomainEventDataRecordsItem object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("purpose", "type", "name", "value", "state")

    purpose: Lenient[Literal["dkim", "return_path", "tracking"] | str] = absent()
    type: Lenient[Literal["TXT", "MX", "CNAME"] | str] = absent()
    name: Lenient[str] = absent()
    value: Lenient[str] = absent()
    priority: Lenient[int | None] = absent()
    state: Lenient[str] = absent()


class DomainEventDataDefaults(TawkedModel):
    """The DomainEventDataDefaults object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("from_name", "from_local")

    from_name: Lenient[str | None] = absent()
    from_local: Lenient[str | None] = absent()


class DomainEventDataTracking(TawkedModel):
    """The DomainEventDataTracking object."""

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


class DomainEventDataReceiving(TawkedModel):
    """The DomainEventDataReceiving object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("address_id", "domain", "state")

    address_id: Lenient[str] = absent()
    domain: Lenient[str] = absent()
    state: Lenient[Literal["awaiting", "active", "partial", "lost", "off"] | str] = absent()


class DomainEventData(TawkedModel):
    """The DomainEventData object."""

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
        "previous_state",
        "reason",
    )

    id: Lenient[str] = absent()
    name: Lenient[str] = absent()
    state: Lenient[Literal["pending", "verified", "failed", "removed"] | str] = absent()
    created_at: Lenient[datetime | None] = absent()
    verified_at: Lenient[datetime | None] = absent()
    pending_until: Lenient[datetime | None] = absent()
    records: Lenient[builtins.list[DomainEventDataRecordsItem]] = absent()
    defaults: Lenient[DomainEventDataDefaults] = absent()
    authentication: Lenient[builtins.dict[str, Any] | None] = absent()
    tracking: Lenient[DomainEventDataTracking | None] = absent()
    receiving: Lenient[DomainEventDataReceiving | None] = absent()
    previous_state: Lenient[str | None] = absent()
    reason: Lenient[
        Literal["dkim_record_missing", "timed_out", "removed_by_client", "released_by_team"]
        | str
        | None
    ] = absent()


class EmailEventDataFrom(TawkedModel):
    """The EmailEventDataFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailEventDataError(TawkedModel):
    """The EmailEventDataError object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "message")

    code: Lenient[str] = absent()
    message: Lenient[str | None] = absent()


class EmailEventDataBounce(TawkedModel):
    """The EmailEventDataBounce object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "subtype")

    type: Lenient[Literal["Permanent", "Transient", "Undetermined"] | str] = absent()
    subtype: Lenient[str | None] = absent()


class EmailEventDataDelay(TawkedModel):
    """The EmailEventDataDelay object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "expires_at", "diagnostic")

    type: Lenient[str | None] = absent()
    expires_at: Lenient[datetime | None] = absent()
    diagnostic: Lenient[str | None] = absent()


class EmailEventDataSuppressed(TawkedModel):
    """The EmailEventDataSuppressed object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("reason", "by")

    reason: Lenient[Literal["bounce", "complaint", "manual"] | str] = absent()
    by: Lenient[Literal["tawked", "ses"] | str] = absent()


class EmailEventDataOpen(TawkedModel):
    """The EmailEventDataOpen object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("user_agent", "ip")

    user_agent: Lenient[str | None] = absent()
    ip: Lenient[str | None] = absent()


class EmailEventDataClick(TawkedModel):
    """The EmailEventDataClick object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("link", "user_agent", "ip")

    link: Lenient[str] = absent()
    user_agent: Lenient[str | None] = absent()
    ip: Lenient[str | None] = absent()


class EmailEventData(TawkedModel):
    """The EmailEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "application_id",
        "from",
        "to",
        "subject",
        "reference",
        "price_halalas",
        "error",
        "bounce",
        "occurred_at",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["accepted", "sent", "delivered", "bounced", "failed"] | str] = absent()
    application_id: Lenient[str] = absent()
    from_: Lenient[EmailEventDataFrom] = absent("from")
    to: Lenient[str] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    price_halalas: Lenient[int] = absent()
    error: Lenient[EmailEventDataError | None] = absent()
    bounce: Lenient[EmailEventDataBounce | None] = absent()
    scheduled_at: Lenient[datetime | None] = absent()
    delay: Lenient[EmailEventDataDelay | None] = absent()
    suppressed: Lenient[EmailEventDataSuppressed | None] = absent()
    open: Lenient[EmailEventDataOpen | None] = absent()
    click: Lenient[EmailEventDataClick | None] = absent()
    occurred_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class EmailRecipientEventDataFrom(TawkedModel):
    """The EmailRecipientEventDataFrom object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("name", "address")

    name: Lenient[str | None] = absent()
    address: Lenient[str] = absent()


class EmailRecipientEventDataRecipient(TawkedModel):
    """The EmailRecipientEventDataRecipient object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "address", "type", "status")

    id: Lenient[str] = absent()
    address: Lenient[str] = absent()
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


class EmailRecipientEventDataTemplate(TawkedModel):
    """The EmailRecipientEventDataTemplate object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("id", "alias", "version")

    id: Lenient[str] = absent()
    alias: Lenient[str | None] = absent()
    version: Lenient[int | None] = absent()


class EmailRecipientEventDataError(TawkedModel):
    """The EmailRecipientEventDataError object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "message")

    code: Lenient[str] = absent()
    message: Lenient[str | None] = absent()


class EmailRecipientEventDataBounce(TawkedModel):
    """The EmailRecipientEventDataBounce object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "subtype")

    type: Lenient[Literal["Permanent", "Transient", "Undetermined"] | str] = absent()
    subtype: Lenient[str | None] = absent()


class EmailRecipientEventDataDelay(TawkedModel):
    """The EmailRecipientEventDataDelay object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("type", "expires_at", "diagnostic")

    type: Lenient[str | None] = absent()
    expires_at: Lenient[datetime | None] = absent()
    diagnostic: Lenient[str | None] = absent()


class EmailRecipientEventDataSuppressed(TawkedModel):
    """The EmailRecipientEventDataSuppressed object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("reason", "by")

    reason: Lenient[Literal["bounce", "complaint", "manual"] | str] = absent()
    by: Lenient[Literal["tawked", "ses"] | str] = absent()


class EmailRecipientEventDataOpen(TawkedModel):
    """The EmailRecipientEventDataOpen object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("user_agent", "ip")

    user_agent: Lenient[str | None] = absent()
    ip: Lenient[str | None] = absent()


class EmailRecipientEventDataClick(TawkedModel):
    """The EmailRecipientEventDataClick object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("link", "user_agent", "ip")

    link: Lenient[str] = absent()
    user_agent: Lenient[str | None] = absent()
    ip: Lenient[str | None] = absent()


class EmailRecipientEventData(TawkedModel):
    """The EmailRecipientEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "application_id",
        "from",
        "to",
        "recipient",
        "tags",
        "subject",
        "reference",
        "price_halalas",
        "error",
        "bounce",
        "occurred_at",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[
        Literal["queued", "scheduled", "sent", "delivered", "bounced", "failed", "canceled"] | str
    ] = absent()
    application_id: Lenient[str] = absent()
    from_: Lenient[EmailRecipientEventDataFrom] = absent("from")
    to: Lenient[str | None] = absent()
    recipient: Lenient[EmailRecipientEventDataRecipient | None] = absent()
    recipients: Lenient[builtins.list[str] | None] = absent()
    tags: Lenient[builtins.list[EmailTag]] = absent()
    mode: Lenient[Literal["live", "test"] | str | None] = absent()
    template: Lenient[EmailRecipientEventDataTemplate | None] = absent()
    subject: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    price_halalas: Lenient[int] = absent()
    error: Lenient[EmailRecipientEventDataError | None] = absent()
    bounce: Lenient[EmailRecipientEventDataBounce | None] = absent()
    scheduled_at: Lenient[datetime | None] = absent()
    delay: Lenient[EmailRecipientEventDataDelay | None] = absent()
    suppressed: Lenient[EmailRecipientEventDataSuppressed | None] = absent()
    open: Lenient[EmailRecipientEventDataOpen | None] = absent()
    click: Lenient[EmailRecipientEventDataClick | None] = absent()
    occurred_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class MessageEventDataError(TawkedModel):
    """The MessageEventDataError object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("code", "message")

    code: Lenient[str | None] = absent()
    message: Lenient[str | None] = absent()


class MessageEventData(TawkedModel):
    """The MessageEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "application_id",
        "to",
        "template",
        "lang",
        "reference",
        "price_halalas",
        "error",
        "occurred_at",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["accepted", "sent", "delivered", "read", "failed"] | str] = absent()
    application_id: Lenient[str] = absent()
    to: Lenient[str] = absent()
    template: Lenient[str] = absent()
    lang: Lenient[str | None] = absent()
    reference: Lenient[str | None] = absent()
    price_halalas: Lenient[int] = absent()
    error: Lenient[MessageEventDataError | None] = absent()
    occurred_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class ServiceApprovedData(TawkedModel):
    """The ServiceApprovedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "status",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    status: Lenient[Literal["active"] | str] = absent()


class ServiceArchivedData(TawkedModel):
    """The ServiceArchivedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "archived_at",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    archived_at: Lenient[datetime | None] = absent()


class ServicePausedData(TawkedModel):
    """The ServicePausedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "reason",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    reason: Lenient[str] = absent()


class ServiceRejectedData(TawkedModel):
    """The ServiceRejectedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "status",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    status: Lenient[Literal["rejected"] | str] = absent()
    reason: Lenient[str | None] = absent()
    reason_code: Lenient[str | None] = absent()


class ServiceRestoredData(TawkedModel):
    """The ServiceRestoredData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("service_id", "application_id", "external_id")

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()


class ServiceResumedData(TawkedModel):
    """The ServiceResumedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("service_id", "application_id", "external_id")

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()


class ServiceReviewRequestedData(TawkedModel):
    """The ServiceReviewRequestedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "service_id",
        "application_id",
        "external_id",
        "status",
        "reason",
    )

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()
    status: Lenient[Literal["review"] | str] = absent()
    reason: Lenient[Literal["brand_changed"] | str] = absent()


class ServiceSuspendedData(TawkedModel):
    """The ServiceSuspendedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("service_id", "application_id", "external_id")

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()


class ServiceUnpausedData(TawkedModel):
    """The ServiceUnpausedData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("service_id", "application_id", "external_id")

    service_id: Lenient[str] = absent()
    application_id: Lenient[str] = absent()
    external_id: Lenient[str | None] = absent()


class SuppressionAddedEventData(TawkedModel):
    """The SuppressionAddedEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "reason",
        "source",
        "application_id",
        "email_id",
        "created_at",
    )

    id: Lenient[str | None] = absent()
    address: Lenient[str] = absent()
    reason: Lenient[Literal["bounce", "complaint", "manual"] | str] = absent()
    source: Lenient[Literal["event", "manual", "import", "api", "ses"] | str] = absent()
    application_id: Lenient[str | None] = absent()
    email_id: Lenient[str | None] = absent()
    created_at: Lenient[datetime] = absent()


class SuppressionRemovedEventData(TawkedModel):
    """The SuppressionRemovedEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "address",
        "reason",
        "lift_reason",
        "by",
        "removed_at",
        "application_id",
    )

    id: Lenient[Any] = absent()
    address: Lenient[str] = absent()
    reason: Lenient[Literal["bounce", "complaint", "manual"] | str] = absent()
    lift_reason: Lenient[str | None] = absent()
    by: Lenient[Literal["client", "team"] | str] = absent()
    removed_at: Lenient[datetime] = absent()
    application_id: Lenient[str | None] = absent()


class VerificationEventData(TawkedModel):
    """The VerificationEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "application_id",
        "reference",
        "channel",
        "to",
        "mode",
        "attempts",
        "expires_at",
        "verified_at",
        "created_at",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["pending", "verified", "failed", "expired", "canceled"] | str] = (
        absent()
    )
    application_id: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    channel: Lenient[str] = absent()
    to: Lenient[str] = absent()
    mode: Lenient[Literal["live", "test", "partner", "partner_test"] | str] = absent()
    attempts: Lenient[int] = absent()
    expires_at: Lenient[datetime] = absent()
    verified_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()


class PartnerVerificationEventData(TawkedModel):
    """The PartnerVerificationEventData object."""

    __tawked_required__: ClassVar[tuple[str, ...]] = (
        "id",
        "status",
        "application_id",
        "reference",
        "channel",
        "to",
        "mode",
        "attempts",
        "expires_at",
        "verified_at",
        "created_at",
        "external_id",
    )

    id: Lenient[str] = absent()
    status: Lenient[Literal["pending", "verified", "failed", "expired", "canceled"] | str] = (
        absent()
    )
    application_id: Lenient[str] = absent()
    reference: Lenient[str | None] = absent()
    channel: Lenient[str] = absent()
    to: Lenient[str] = absent()
    mode: Lenient[Literal["live", "test", "partner", "partner_test"] | str] = absent()
    attempts: Lenient[int] = absent()
    expires_at: Lenient[datetime] = absent()
    verified_at: Lenient[datetime | None] = absent()
    created_at: Lenient[datetime | None] = absent()
    external_id: Lenient[str | None] = absent()


class BalanceLowEvent(TawkedModel):
    """``balance.low``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["balance.low"] = Field(default="balance.low")
    data: Lenient[BalanceLowData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["balance.low"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class DomainCreatedEvent(TawkedModel):
    """``domain.created``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["domain.created"] = Field(default="domain.created")
    data: Lenient[DomainEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["domain.created"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class DomainFailedEvent(TawkedModel):
    """``domain.failed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["domain.failed"] = Field(default="domain.failed")
    data: Lenient[DomainEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["domain.failed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class DomainRemovedEvent(TawkedModel):
    """``domain.removed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["domain.removed"] = Field(default="domain.removed")
    data: Lenient[DomainEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["domain.removed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class DomainVerifiedEvent(TawkedModel):
    """``domain.verified``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["domain.verified"] = Field(default="domain.verified")
    data: Lenient[DomainEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["domain.verified"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailBouncedEvent(TawkedModel):
    """``email.bounced``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.bounced"] = Field(default="email.bounced")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.bounced"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailCanceledEvent(TawkedModel):
    """``email.canceled``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.canceled"] = Field(default="email.canceled")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.canceled"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailClickedEvent(TawkedModel):
    """``email.clicked``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.clicked"] = Field(default="email.clicked")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.clicked"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailComplainedEvent(TawkedModel):
    """``email.complained``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.complained"] = Field(default="email.complained")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.complained"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailDeliveredEvent(TawkedModel):
    """``email.delivered``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.delivered"] = Field(default="email.delivered")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.delivered"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailDeliveryDelayedEvent(TawkedModel):
    """``email.delivery_delayed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.delivery_delayed"] = Field(default="email.delivery_delayed")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.delivery_delayed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailFailedEvent(TawkedModel):
    """``email.failed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.failed"] = Field(default="email.failed")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.failed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailOpenedEvent(TawkedModel):
    """``email.opened``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.opened"] = Field(default="email.opened")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.opened"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailReceivedEvent(TawkedModel):
    """``email.received``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.received"] = Field(default="email.received")
    data: Lenient[EmailReceivedEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.received"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailScheduledEvent(TawkedModel):
    """``email.scheduled``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.scheduled"] = Field(default="email.scheduled")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.scheduled"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailSentEvent(TawkedModel):
    """``email.sent``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.sent"] = Field(default="email.sent")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.sent"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class EmailSuppressedEvent(TawkedModel):
    """``email.suppressed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["email.suppressed"] = Field(default="email.suppressed")
    data: Lenient[EmailEventData | EmailRecipientEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["email.suppressed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class MessageDeliveredEvent(TawkedModel):
    """``message.delivered``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["message.delivered"] = Field(default="message.delivered")
    data: Lenient[MessageEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["message.delivered"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class MessageFailedEvent(TawkedModel):
    """``message.failed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["message.failed"] = Field(default="message.failed")
    data: Lenient[MessageEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["message.failed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class MessageReadEvent(TawkedModel):
    """``message.read``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["message.read"] = Field(default="message.read")
    data: Lenient[MessageEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["message.read"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class MessageSentEvent(TawkedModel):
    """``message.sent``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["message.sent"] = Field(default="message.sent")
    data: Lenient[MessageEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["message.sent"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceApprovedEvent(TawkedModel):
    """``service.approved``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.approved"] = Field(default="service.approved")
    data: Lenient[ServiceApprovedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.approved"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceArchivedEvent(TawkedModel):
    """``service.archived``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.archived"] = Field(default="service.archived")
    data: Lenient[ServiceArchivedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.archived"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServicePausedEvent(TawkedModel):
    """``service.paused``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.paused"] = Field(default="service.paused")
    data: Lenient[ServicePausedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.paused"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceRejectedEvent(TawkedModel):
    """``service.rejected``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.rejected"] = Field(default="service.rejected")
    data: Lenient[ServiceRejectedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.rejected"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceRestoredEvent(TawkedModel):
    """``service.restored``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.restored"] = Field(default="service.restored")
    data: Lenient[ServiceRestoredData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.restored"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceResumedEvent(TawkedModel):
    """``service.resumed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.resumed"] = Field(default="service.resumed")
    data: Lenient[ServiceResumedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.resumed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceReviewRequestedEvent(TawkedModel):
    """``service.review_requested``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.review_requested"] = Field(default="service.review_requested")
    data: Lenient[ServiceReviewRequestedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.review_requested"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceSuspendedEvent(TawkedModel):
    """``service.suspended``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.suspended"] = Field(default="service.suspended")
    data: Lenient[ServiceSuspendedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.suspended"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class ServiceUnpausedEvent(TawkedModel):
    """``service.unpaused``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["service.unpaused"] = Field(default="service.unpaused")
    data: Lenient[ServiceUnpausedData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["service.unpaused"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class SuppressionAddedEvent(TawkedModel):
    """``suppression.added``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["suppression.added"] = Field(default="suppression.added")
    data: Lenient[SuppressionAddedEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["suppression.added"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class SuppressionRemovedEvent(TawkedModel):
    """``suppression.removed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["suppression.removed"] = Field(default="suppression.removed")
    data: Lenient[SuppressionRemovedEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["suppression.removed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class VerificationExpiredEvent(TawkedModel):
    """``verification.expired``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["verification.expired"] = Field(default="verification.expired")
    data: Lenient[VerificationEventData | PartnerVerificationEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["verification.expired"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class VerificationFailedEvent(TawkedModel):
    """``verification.failed``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["verification.failed"] = Field(default="verification.failed")
    data: Lenient[VerificationEventData | PartnerVerificationEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["verification.failed"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class VerificationVerifiedEvent(TawkedModel):
    """``verification.verified``."""

    __tawked_required__: ClassVar[tuple[str, ...]] = ("event", "data", "sent_at")

    event: Literal["verification.verified"] = Field(default="verification.verified")
    data: Lenient[VerificationEventData | PartnerVerificationEventData] = absent()
    test: bool | None = absent()
    type: Lenient[Literal["verification.verified"] | str | None] = absent()
    timestamp: Lenient[str | None] = absent()
    mode: Lenient[Literal["test"] | str | None] = absent()
    sent_at: Lenient[str] = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``): nothing was sent or received."""
        return self.mode == "test"


class UnknownEvent(TawkedModel):
    """An event this version of the SDK does not know yet: ``event`` (or ``type``) and raw ``data``."""

    event: str | None = absent()
    type: str | None = absent()
    data: Any = absent()
    test: bool | None = absent()
    timestamp: str | None = absent()
    mode: str | None = absent()
    sent_at: str | None = absent()

    @property
    def is_test_mode(self) -> bool:
        """Whether a test key simulated the event (``mode == 'test'``)."""
        return self.mode == "test"


WebhookEvent = (
    BalanceLowEvent
    | DomainCreatedEvent
    | DomainFailedEvent
    | DomainRemovedEvent
    | DomainVerifiedEvent
    | EmailBouncedEvent
    | EmailCanceledEvent
    | EmailClickedEvent
    | EmailComplainedEvent
    | EmailDeliveredEvent
    | EmailDeliveryDelayedEvent
    | EmailFailedEvent
    | EmailOpenedEvent
    | EmailReceivedEvent
    | EmailScheduledEvent
    | EmailSentEvent
    | EmailSuppressedEvent
    | MessageDeliveredEvent
    | MessageFailedEvent
    | MessageReadEvent
    | MessageSentEvent
    | ServiceApprovedEvent
    | ServiceArchivedEvent
    | ServicePausedEvent
    | ServiceRejectedEvent
    | ServiceRestoredEvent
    | ServiceResumedEvent
    | ServiceReviewRequestedEvent
    | ServiceSuspendedEvent
    | ServiceUnpausedEvent
    | SuppressionAddedEvent
    | SuppressionRemovedEvent
    | VerificationExpiredEvent
    | VerificationFailedEvent
    | VerificationVerifiedEvent
    | UnknownEvent
)

EVENT_TYPES: dict[str, type[TawkedModel]] = {
    "balance.low": BalanceLowEvent,
    "domain.created": DomainCreatedEvent,
    "domain.failed": DomainFailedEvent,
    "domain.removed": DomainRemovedEvent,
    "domain.verified": DomainVerifiedEvent,
    "email.bounced": EmailBouncedEvent,
    "email.canceled": EmailCanceledEvent,
    "email.clicked": EmailClickedEvent,
    "email.complained": EmailComplainedEvent,
    "email.delivered": EmailDeliveredEvent,
    "email.delivery_delayed": EmailDeliveryDelayedEvent,
    "email.failed": EmailFailedEvent,
    "email.opened": EmailOpenedEvent,
    "email.received": EmailReceivedEvent,
    "email.scheduled": EmailScheduledEvent,
    "email.sent": EmailSentEvent,
    "email.suppressed": EmailSuppressedEvent,
    "message.delivered": MessageDeliveredEvent,
    "message.failed": MessageFailedEvent,
    "message.read": MessageReadEvent,
    "message.sent": MessageSentEvent,
    "service.approved": ServiceApprovedEvent,
    "service.archived": ServiceArchivedEvent,
    "service.paused": ServicePausedEvent,
    "service.rejected": ServiceRejectedEvent,
    "service.restored": ServiceRestoredEvent,
    "service.resumed": ServiceResumedEvent,
    "service.review_requested": ServiceReviewRequestedEvent,
    "service.suspended": ServiceSuspendedEvent,
    "service.unpaused": ServiceUnpausedEvent,
    "suppression.added": SuppressionAddedEvent,
    "suppression.removed": SuppressionRemovedEvent,
    "verification.expired": VerificationExpiredEvent,
    "verification.failed": VerificationFailedEvent,
    "verification.verified": VerificationVerifiedEvent,
}


def parse_event(body: builtins.dict[str, Any]) -> WebhookEvent:
    """The typed event of a webhook body (the tawked envelope's ``event``, or ``type``)."""
    name = body.get("event", body.get("type"))
    cls = EVENT_TYPES.get(name) if isinstance(name, str) else None
    event: WebhookEvent = (cls or UnknownEvent).model_validate(body)  # type: ignore[assignment]
    return event


__all__ = [
    "EVENT_TYPES",
    "BalanceLowEvent",
    "DomainCreatedEvent",
    "DomainFailedEvent",
    "DomainRemovedEvent",
    "DomainVerifiedEvent",
    "EmailBouncedEvent",
    "EmailCanceledEvent",
    "EmailClickedEvent",
    "EmailComplainedEvent",
    "EmailDeliveredEvent",
    "EmailDeliveryDelayedEvent",
    "EmailFailedEvent",
    "EmailOpenedEvent",
    "EmailReceivedEvent",
    "EmailScheduledEvent",
    "EmailSentEvent",
    "EmailSuppressedEvent",
    "MessageDeliveredEvent",
    "MessageFailedEvent",
    "MessageReadEvent",
    "MessageSentEvent",
    "ServiceApprovedEvent",
    "ServiceArchivedEvent",
    "ServicePausedEvent",
    "ServiceRejectedEvent",
    "ServiceRestoredEvent",
    "ServiceResumedEvent",
    "ServiceReviewRequestedEvent",
    "ServiceSuspendedEvent",
    "ServiceUnpausedEvent",
    "SuppressionAddedEvent",
    "SuppressionRemovedEvent",
    "UnknownEvent",
    "VerificationExpiredEvent",
    "VerificationFailedEvent",
    "VerificationVerifiedEvent",
    "WebhookEvent",
    "parse_event",
]

for _model in (
    BalanceLowData,
    DomainEventDataRecordsItem,
    DomainEventDataDefaults,
    DomainEventDataTracking,
    DomainEventDataReceiving,
    DomainEventData,
    EmailEventDataFrom,
    EmailEventDataError,
    EmailEventDataBounce,
    EmailEventDataDelay,
    EmailEventDataSuppressed,
    EmailEventDataOpen,
    EmailEventDataClick,
    EmailEventData,
    EmailRecipientEventDataFrom,
    EmailRecipientEventDataRecipient,
    EmailRecipientEventDataTemplate,
    EmailRecipientEventDataError,
    EmailRecipientEventDataBounce,
    EmailRecipientEventDataDelay,
    EmailRecipientEventDataSuppressed,
    EmailRecipientEventDataOpen,
    EmailRecipientEventDataClick,
    EmailRecipientEventData,
    MessageEventDataError,
    MessageEventData,
    ServiceApprovedData,
    ServiceArchivedData,
    ServicePausedData,
    ServiceRejectedData,
    ServiceRestoredData,
    ServiceResumedData,
    ServiceReviewRequestedData,
    ServiceSuspendedData,
    ServiceUnpausedData,
    SuppressionAddedEventData,
    SuppressionRemovedEventData,
    VerificationEventData,
    PartnerVerificationEventData,
):
    _model.model_rebuild()
