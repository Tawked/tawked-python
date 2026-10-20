#!/usr/bin/env python3
"""The smoke run against the LOCAL app.

This package calls Tawked's app running locally with the keys ``php artisan sdk:smoke-keys`` wrote, in the
order every language follows. Never Verify (the local SMS gateways are live), never a key on the
screen, never an address that is not loopback.

    TAWKED_SMOKE_BASE_URL=http://127.0.0.1:8000 TAWKED_SMOKE_KEYS=.build/smoke-keys.json \\
        uv run python scripts/smoke_local.py
"""

from __future__ import annotations

import base64
import json
import os
import subprocess
import sys
import time
from collections.abc import Callable
from pathlib import Path
from typing import Any
from urllib.parse import urlsplit

import tawked
from tawked import ApprovalRequiredError, InsufficientCreditsError, Tawked, TawkedAccount

REPO = Path(__file__).resolve().parents[3]
BASE_URL = os.environ.get("TAWKED_SMOKE_BASE_URL", "http://127.0.0.1:8000")
KEYS_PATH = Path(os.environ.get("TAWKED_SMOKE_KEYS", ".build/smoke-keys.json"))

if (urlsplit(BASE_URL).hostname or "") not in {"127.0.0.1", "localhost", "::1"}:
    print(f"Refused: {BASE_URL} is not a loopback address. The smoke run only calls the local app.")
    sys.exit(2)

KEYS: dict[str, Any] = json.loads(
    (KEYS_PATH if KEYS_PATH.is_absolute() else REPO / KEYS_PATH).read_text("utf-8")
)
CONTRACT: dict[str, Any] = json.loads((REPO / "sdks/contract/api.json").read_text("utf-8"))
STAMP = str(int(time.time() * 1000))
passed = 0


def example(endpoint_id: str) -> dict[str, Any]:
    return next(e for e in CONTRACT["endpoints"] if e["id"] == endpoint_id)["sdk"]["example"]


def step(label: str, run: Callable[[], str | None]) -> None:
    global passed
    try:
        note = run()
    except Exception as error:
        # The message only: an SDK error never carries a key, and nothing here prints one.
        print(f"FAIL  {label}: {type(error).__name__}: {error}", file=sys.stderr)
        sys.exit(1)
    passed += 1
    print(f"pass  {label}" + (f": {note}" if note else ""))


state: dict[str, Any] = {}

# 1. e-mail: send → get → list (fake SES).
email = Tawked(api_key=KEYS["email"]["key"], base_url=BASE_URL)


def email_send() -> str:
    try:
        sent = email.email.messages.send(
            to=["sara@example.com"],
            subject="تجربة الحزمة المحلية",
            text="رسالة تجربة من حزمة Python.",
            tags=[{"name": "smoke", "value": "python"}],
            idempotency_key=f"smoke-py-email-{STAMP}",
        )
    except InsufficientCreditsError:
        return (
            "answered 402 insufficient_credits (the demo account has no balance left; "
            "the request reached the app and was refused as documented)"
        )
    state["email"] = sent.id
    return str(sent.status)


step("email.messages.send", email_send)
if state.get("email"):
    step("email.messages.get", lambda: str(email.email.messages.get(state["email"]).status))
step(
    "email.messages.list",
    lambda: f"{len(email.email.messages.list(limit=5))} on the first page",
)

# 2. WhatsApp: templates list, message send → get (fake Meta).
whatsapp = Tawked(api_key=KEYS["whatsapp"]["key"], base_url=BASE_URL)


def templates_list() -> str:
    templates = whatsapp.whatsapp.templates.list().data
    approved = [t for t in templates if t.status == "APPROVED"]
    plain = [t for t in approved if t.placeholders.kind == "none"]
    state["template"] = (plain or approved or [None])[0]
    return f"{len(templates)} templates"


def whatsapp_send() -> str:
    template = state.get("template")
    if template is None:
        raise RuntimeError("no approved template on the demo number")
    names = [*template.placeholders.header, *template.placeholders.body]
    params = {"params": {str(name): "تجربة" for name in names}} if names else {}
    sent = whatsapp.whatsapp.messages.send(
        to="0550000000",
        template=template.name,
        lang=template.language,
        idempotency_key=f"smoke-py-wa-{STAMP}",
        **params,
    )
    state["message"] = sent.id
    return str(sent.status)


step("whatsapp.templates.list", templates_list)
step("whatsapp.messages.send", whatsapp_send)
step("whatsapp.messages.get", lambda: str(whatsapp.whatsapp.messages.get(state["message"]).status))

# 3. The connected app: chat menus create → get → update → delete; attendant get and a draft.
app = Tawked(api_key=KEYS["connected_app"]["key"], base_url=BASE_URL)


def menu_create() -> str:
    menu = app.chat.menus.create(
        title=f"تجربة {STAMP}"[:30],
        url="https://example.com/tawked-smoke",
        idempotency_key=f"smoke-py-menu-{STAMP}",
    )
    state["menu"] = menu.id
    return str(menu.id)


step("chat.menus.create", menu_create)
step("chat.menus.get", lambda: str(app.chat.menus.get(state["menu"]).title))
step(
    "chat.menus.update",
    lambda: str(app.chat.menus.update(state["menu"], title="تجربة معدّلة").title),
)
step(
    "chat.menus.delete",
    lambda: "deleted" if app.chat.menus.delete(state["menu"]).deleted else "kept",
)
step("chat.attendant.get", lambda: str(app.chat.attendant.get().state))
step(
    "chat.attendant.save_draft",
    lambda: (
        type(
            app.chat.attendant.save_draft(
                **example("chat-attendant-draft")["body"],
                idempotency_key=f"smoke-py-attendant-{STAMP}",
            )
        ).__name__
    ),
)

# 4. Partner: proved against sdks/mock-server only. A partner key cannot be narrowed, and even the
# sandbox one texts its owner's phone through the live local gateways (sdks/smoke/README.md).

# 5. Account: me.show, operations.search, one consequential call stopped at its 428 (never approved).
account = TawkedAccount(token=KEYS["account"]["token"], base_url=BASE_URL, language="en")
step("me.show", lambda: ", ".join(list(dict(account.me.show().data or {}))[:3]))
step("operations.search", lambda: f"{len(account.operations.search())} on the first page")


def stops_at_428() -> str:
    if KEYS["account"].get("approvals", "off") == "off":
        raise RuntimeError(
            "the smoke token must have approvals on, or the consequential call would run"
        )
    try:
        account.email.keys.create(KEYS["account"]["application_id"])
    except ApprovalRequiredError as error:
        if error.approval_id and (error.human_action or {}).get("url"):
            return f"approval {(error.approval or {}).get('status', 'pending')}"
        raise
    raise RuntimeError("a consequential call ran without approval")


step("email.keys.create stops at 428", stops_at_428)


# 6. Webhooks: a delivery signed by the app's own signer (App\Partners\WebhookSigner).
def webhook() -> str:
    secret = f"smoke-py-{STAMP}-secret-0000000000"
    timestamp = str(int(time.time() * 1000))
    body = json.dumps(
        {
            "event": "service.approved",
            "data": {"external_id": "متجر/88", "status": "active"},
            "sent_at": timestamp,
        },
        ensure_ascii=False,
        separators=(",", ":"),
    )

    def b64(text: str) -> str:
        return base64.b64encode(text.encode("utf-8")).decode("ascii")

    code = (
        f"echo App\\Partners\\WebhookSigner::sign(base64_decode('{b64(secret)}'), "
        f"'{timestamp}', base64_decode('{b64(body)}'));"
    )
    php = os.environ.get("PHP", "php")
    out = subprocess.run(
        [php, "artisan", "tinker", "--execute", code],
        cwd=REPO,
        capture_output=True,
        text=True,
        check=False,
    )
    signature = (out.stdout.strip().splitlines() or [""])[-1]
    if len(signature) != 64:
        raise RuntimeError("the app's signer did not answer")
    headers = {"tawked-timestamp": timestamp, "tawked-signature": signature}
    if not tawked.webhooks.verify(body.encode("utf-8"), headers, secret):
        raise RuntimeError("the SDK refused the app's signature")
    return "the app's bytes verify"


step("webhooks.verify (signed by the app)", webhook)

print(f"\n{passed} steps passed against {BASE_URL}; no Verify call was made.")
