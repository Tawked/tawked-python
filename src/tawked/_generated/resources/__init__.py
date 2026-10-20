"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from tawked._generated.resources.chat import AsyncChat, Chat
from tawked._generated.resources.email import AsyncEmail, Email
from tawked._generated.resources.partner import AsyncPartner, Partner
from tawked._generated.resources.verify import AsyncVerify, Verify
from tawked._generated.resources.webhook_endpoints import AsyncWebhookEndpoints, WebhookEndpoints
from tawked._generated.resources.whatsapp import AsyncWhatsApp, WhatsApp


class ProductNamespaces:
    """The top-level namespaces of the product API."""

    verify: Verify
    whatsapp: WhatsApp
    email: Email
    webhook_endpoints: WebhookEndpoints
    chat: Chat
    partner: Partner

    def _init_namespaces(self) -> None:
        self.verify = Verify(self)  # type: ignore[arg-type]
        self.whatsapp = WhatsApp(self)  # type: ignore[arg-type]
        self.email = Email(self)  # type: ignore[arg-type]
        self.webhook_endpoints = WebhookEndpoints(self)  # type: ignore[arg-type]
        self.chat = Chat(self)  # type: ignore[arg-type]
        self.partner = Partner(self)  # type: ignore[arg-type]


class AsyncProductNamespaces:
    """The top-level namespaces of the product API (async)."""

    verify: AsyncVerify
    whatsapp: AsyncWhatsApp
    email: AsyncEmail
    webhook_endpoints: AsyncWebhookEndpoints
    chat: AsyncChat
    partner: AsyncPartner

    def _init_namespaces(self) -> None:
        self.verify = AsyncVerify(self)  # type: ignore[arg-type]
        self.whatsapp = AsyncWhatsApp(self)  # type: ignore[arg-type]
        self.email = AsyncEmail(self)  # type: ignore[arg-type]
        self.webhook_endpoints = AsyncWebhookEndpoints(self)  # type: ignore[arg-type]
        self.chat = AsyncChat(self)  # type: ignore[arg-type]
        self.partner = AsyncPartner(self)  # type: ignore[arg-type]
