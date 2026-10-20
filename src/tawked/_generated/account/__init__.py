"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from tawked._generated.account.account import AccountAccount, AsyncAccountAccount
from tawked._generated.account.applications import AccountApplications, AsyncAccountApplications
from tawked._generated.account.approvals import AccountApprovals, AsyncAccountApprovals
from tawked._generated.account.automations import AccountAutomations, AsyncAccountAutomations
from tawked._generated.account.campaigns import AccountCampaigns, AsyncAccountCampaigns
from tawked._generated.account.chat import AccountChat, AsyncAccountChat
from tawked._generated.account.clients import AccountClients, AsyncAccountClients
from tawked._generated.account.contacts import AccountContacts, AsyncAccountContacts
from tawked._generated.account.email import AccountEmail, AsyncAccountEmail
from tawked._generated.account.integration_apps import (
    AccountIntegrationApps,
    AsyncAccountIntegrationApps,
)
from tawked._generated.account.integrations import AccountIntegrations, AsyncAccountIntegrations
from tawked._generated.account.me import AccountMe, AsyncAccountMe
from tawked._generated.account.members import AccountMembers, AsyncAccountMembers
from tawked._generated.account.operations import AccountOperations, AsyncAccountOperations
from tawked._generated.account.radeef import AccountRadeef, AsyncAccountRadeef
from tawked._generated.account.stores import AccountStores, AsyncAccountStores
from tawked._generated.account.verify import AccountVerify, AsyncAccountVerify
from tawked._generated.account.wallet import AccountWallet, AsyncAccountWallet
from tawked._generated.account.whatsapp import AccountWhatsApp, AsyncAccountWhatsApp


class AccountNamespaces:
    """The top-level namespaces of the Account API."""

    account: AccountAccount
    applications: AccountApplications
    approvals: AccountApprovals
    automations: AccountAutomations
    campaigns: AccountCampaigns
    chat: AccountChat
    clients: AccountClients
    contacts: AccountContacts
    email: AccountEmail
    integration_apps: AccountIntegrationApps
    integrations: AccountIntegrations
    me: AccountMe
    members: AccountMembers
    operations: AccountOperations
    radeef: AccountRadeef
    stores: AccountStores
    verify: AccountVerify
    wallet: AccountWallet
    whatsapp: AccountWhatsApp

    def _init_namespaces(self) -> None:
        self.account = AccountAccount(self)  # type: ignore[arg-type]
        self.applications = AccountApplications(self)  # type: ignore[arg-type]
        self.approvals = AccountApprovals(self)  # type: ignore[arg-type]
        self.automations = AccountAutomations(self)  # type: ignore[arg-type]
        self.campaigns = AccountCampaigns(self)  # type: ignore[arg-type]
        self.chat = AccountChat(self)  # type: ignore[arg-type]
        self.clients = AccountClients(self)  # type: ignore[arg-type]
        self.contacts = AccountContacts(self)  # type: ignore[arg-type]
        self.email = AccountEmail(self)  # type: ignore[arg-type]
        self.integration_apps = AccountIntegrationApps(self)  # type: ignore[arg-type]
        self.integrations = AccountIntegrations(self)  # type: ignore[arg-type]
        self.me = AccountMe(self)  # type: ignore[arg-type]
        self.members = AccountMembers(self)  # type: ignore[arg-type]
        self.operations = AccountOperations(self)  # type: ignore[arg-type]
        self.radeef = AccountRadeef(self)  # type: ignore[arg-type]
        self.stores = AccountStores(self)  # type: ignore[arg-type]
        self.verify = AccountVerify(self)  # type: ignore[arg-type]
        self.wallet = AccountWallet(self)  # type: ignore[arg-type]
        self.whatsapp = AccountWhatsApp(self)  # type: ignore[arg-type]


class AsyncAccountNamespaces:
    """The top-level namespaces of the Account API (async)."""

    account: AsyncAccountAccount
    applications: AsyncAccountApplications
    approvals: AsyncAccountApprovals
    automations: AsyncAccountAutomations
    campaigns: AsyncAccountCampaigns
    chat: AsyncAccountChat
    clients: AsyncAccountClients
    contacts: AsyncAccountContacts
    email: AsyncAccountEmail
    integration_apps: AsyncAccountIntegrationApps
    integrations: AsyncAccountIntegrations
    me: AsyncAccountMe
    members: AsyncAccountMembers
    operations: AsyncAccountOperations
    radeef: AsyncAccountRadeef
    stores: AsyncAccountStores
    verify: AsyncAccountVerify
    wallet: AsyncAccountWallet
    whatsapp: AsyncAccountWhatsApp

    def _init_namespaces(self) -> None:
        self.account = AsyncAccountAccount(self)  # type: ignore[arg-type]
        self.applications = AsyncAccountApplications(self)  # type: ignore[arg-type]
        self.approvals = AsyncAccountApprovals(self)  # type: ignore[arg-type]
        self.automations = AsyncAccountAutomations(self)  # type: ignore[arg-type]
        self.campaigns = AsyncAccountCampaigns(self)  # type: ignore[arg-type]
        self.chat = AsyncAccountChat(self)  # type: ignore[arg-type]
        self.clients = AsyncAccountClients(self)  # type: ignore[arg-type]
        self.contacts = AsyncAccountContacts(self)  # type: ignore[arg-type]
        self.email = AsyncAccountEmail(self)  # type: ignore[arg-type]
        self.integration_apps = AsyncAccountIntegrationApps(self)  # type: ignore[arg-type]
        self.integrations = AsyncAccountIntegrations(self)  # type: ignore[arg-type]
        self.me = AsyncAccountMe(self)  # type: ignore[arg-type]
        self.members = AsyncAccountMembers(self)  # type: ignore[arg-type]
        self.operations = AsyncAccountOperations(self)  # type: ignore[arg-type]
        self.radeef = AsyncAccountRadeef(self)  # type: ignore[arg-type]
        self.stores = AsyncAccountStores(self)  # type: ignore[arg-type]
        self.verify = AsyncAccountVerify(self)  # type: ignore[arg-type]
        self.wallet = AsyncAccountWallet(self)  # type: ignore[arg-type]
        self.whatsapp = AsyncAccountWhatsApp(self)  # type: ignore[arg-type]
