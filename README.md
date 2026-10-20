<p>
  <a href="https://tawked.com">
    <picture>
      <source media="(prefers-color-scheme: dark)" srcset="https://docs.tawked.com/logo/dark.svg">
      <img alt="Tawked" src="https://docs.tawked.com/logo/light.svg" width="172" height="48">
    </picture>
  </a>
</p>

# Tawked SDK for Python

[![PyPI](https://img.shields.io/pypi/v/tawked)](https://pypi.org/project/tawked/) [![Python versions](https://img.shields.io/pypi/pyversions/tawked)](https://pypi.org/project/tawked/) [![CI](https://github.com/tawked/tawked-python/actions/workflows/ci.yml/badge.svg?branch=main)](https://github.com/tawked/tawked-python/actions/workflows/ci.yml) [![License: MIT](https://img.shields.io/badge/license-MIT-blue)](https://github.com/tawked/tawked-python/blob/main/LICENSE)

The official Tawked SDK for Python. Use it to send SMS OTP verification codes to Saudi mobile numbers and check them, send WhatsApp Business API template messages from your business's own number, send transactional email from your own domain, and verify Tawked's signed webhooks. It also covers Tawked Chat for connected apps, the Partner API and the Account API. It has a sync and an async client on httpx, typed models (`py.typed`, mypy strict), and supports Python 3.10 or newer.

Tawked (توكيد) is a Saudi messaging platform at [tawked.com](https://tawked.com) and a Meta Tech Provider: businesses send WhatsApp Business API notifications from their own number and SMS OTP verification codes, and answer customers in Tawked Chat, a shared WhatsApp inbox for teams. Tawked Email, in early access, sends a business's mail from its own domain.

[Documentation](https://docs.tawked.com) · [API reference](https://docs.tawked.com/api-reference/verify/start-a-verification) · [Changelog](https://github.com/tawked/tawked-python/blob/main/CHANGELOG.md) · [Pricing](https://tawked.com/en/pricing)

## Installation

```bash
pip install tawked        # or: uv add tawked
```

## Before you start

- [Sign up](https://tawked.com/en/signup) and create an application in the console.
- Create an API key on your application's API keys page: `tk_live_…` once the application is approved, or `tk_test_…` before that (see Testing). [Keys and authentication](https://docs.tawked.com/authentication).
- Put the key in the `TAWKED_API_KEY` environment variable. Partner keys (`tk_partner_…`) and account tokens (`tk_acct_…`) are named in their own sections.
- Every product draws on one prepaid balance in Saudi riyals: see [pricing](https://tawked.com/en/pricing).

## Quick start

```python
from tawked import Tawked

tawked = Tawked()  # reads TAWKED_API_KEY

# 1. Send a code by SMS. Any Saudi mobile format works: 0512345678, +966512345678, ٠٥١٢٣٤٥٦٧٨.
started = tawked.verify.start(to="0512345678", idempotency_key="signin-7781")

# 2. Check the code the person typed.
result = tawked.verify.check(id=started.id, code="482913")
print("signed in" if result.verified else result.status)
```

A wrong or late code is an answer, not an exception: read `verified`. Keep the key on your server: see Security.

## What you can do

| Task | Call | Docs |
|---|---|---|
| Send an SMS OTP code to a Saudi mobile number | `tawked.verify.start()` | [Quickstart](https://docs.tawked.com/quickstart) |
| Check the code the user typed | `tawked.verify.check()` | [Sign-in flow](https://docs.tawked.com/verify/sign-in-flow) |
| Send a WhatsApp template message from your number | `tawked.whatsapp.messages.send()` | [Messages](https://docs.tawked.com/whatsapp/messages) |
| Read a WhatsApp message's status | `tawked.whatsapp.messages.get()` | [Messages](https://docs.tawked.com/whatsapp/messages) |
| List your approved WhatsApp templates | `tawked.whatsapp.templates.list()` | [Templates](https://docs.tawked.com/whatsapp/templates) |
| Send a transactional email from your domain | `tawked.email.messages.send()` | [Email](https://docs.tawked.com/email/messages) |
| Send up to 100 emails in one call | `tawked.email.messages.send_batch()` | [Email](https://docs.tawked.com/email/messages) |
| Verify a webhook and read its event | `webhooks.construct_event()` | [Webhooks](https://docs.tawked.com/webhooks) |
| Add your app's menu to Tawked Chat (connected app) | `tawked.chat.menus.create()` | [Chat menus](https://docs.tawked.com/chat-menus) |
| Connect your app to a business's account | `apps.authorize_url()`, `apps.exchange_code()` | [Connected apps](https://docs.tawked.com/integrations/connected-apps) |
| Open a Verify application per merchant (platforms) | `partner.partner.applications.create()` | [Partner API](https://docs.tawked.com/partners/overview) |
| Run anything the console does, for a script or an AI agent | `TawkedAccount()` | [Account API](https://docs.tawked.com/account-api/overview) |

## Requirements

| Requirement | Version |
|---|---|
| Python | 3.10 or newer (tested on 3.10 to 3.14) |
| Dependencies | httpx 0.27+, pydantic 2.7+ (2.12+ on Python 3.14), typing-extensions |
| Clients | `Tawked` (sync) and `AsyncTawked` (async) |
| Typing | `py.typed`, checked with mypy strict |

## Configuration

| Option | Default | Notes |
|---|---|---|
| `api_key` | `TAWKED_API_KEY` | The key, read from the environment when not given |
| `base_url` | `TAWKED_BASE_URL`, else `https://tawked.com` | Point it at a local stand-in for the API in your tests |
| `max_retries` | `2` | See Retries and idempotency; `0` turns retries off |
| `in_progress_wait` | `30.0` | Seconds to wait on a call with the same key that is still running |
| `default_headers` | none | Headers sent with every call |
| `http_client` | a new `httpx.Client` | Your own client, for proxies, timeouts or transports |

```python
import os

import httpx

from tawked import Tawked

tawked = Tawked(
    api_key=os.environ["TAWKED_API_KEY"],
    max_retries=3,
    http_client=httpx.Client(timeout=20.0),
)
```

Every method also takes, last, the keyword arguments `idempotency_key=`, `timeout=` (seconds per attempt), `max_retries=` and `extra_headers=` for that one call. Fields are keyword arguments named as the API names them; a Python keyword gets a trailing underscore (`from_` is sent as `from`).

## Tawked Verify

Tawked makes the code, sends it by SMS to a Saudi mobile number and checks it. It needs an application key.

```python
# tawked = Tawked(), as in Quick start
started = tawked.verify.start(
    to="0551234567",
    reference="signin-7781",
    idempotency_key="signin-7781",  # one key per business event: a retry never sends twice
)

result = tawked.verify.check(id=started.id, code="123456")
if result.verified:
    print("signed in")
else:
    print(result.status)  # invalid_code, too_many_attempts, expired, canceled or failed
```

Also `verify.get(id)`, `verify.resend(id)` and `verify.cancel(id)`. With a partner key, add `application="…"` to each call. Number formats: [destinations](https://docs.tawked.com/destinations).

## WhatsApp Business API

Template messages from the application's own number. It needs a live key: WhatsApp has no test mode.

```python
# tawked = Tawked(), as in Quick start; WhatsApp needs a live key
sent = tawked.whatsapp.messages.send(
    to="+966551234567",
    template="order_shipped",
    lang="ar",
    params={"name": "سارة", "order": "1042"},
    reference="order-1042",
    idempotency_key="order-1042-shipped",
)
message = tawked.whatsapp.messages.get(sent.id)
templates = tawked.whatsapp.templates.list()
```

Meta reviews every template and sets its category before it can be sent. A connected app's key also creates, edits and deletes templates (`whatsapp.templates.create()`, `.update(template_id, …)`, `.delete(template_id)`).

## Tawked Email (Early Access)

Tawked's team opens Email for an account on request, from the console. Until then every Email call answers `email_early_access`.

Email sends from a domain you verified in the console. `from_` is an object with a `name` and an `address` on that domain.

```python
# tawked = Tawked(), as in Quick start
sender = {"name": "متجر أكمي", "address": "orders@acme.sa"}

sent = tawked.email.messages.send(
    from_=sender,
    to=["sara@example.com"],
    subject="طلبك رقم 1042 قيد التجهيز",
    html="<p>استلمنا طلبك رقم 1042.</p>",
    text="استلمنا طلبك رقم 1042.",
    tags=[{"name": "category", "value": "order"}],
    reference="order-1042",
    idempotency_key="order-1042-confirmation",
)

batch = tawked.email.messages.send_batch(
    [
        {"from": sender, "to": "sara@example.com", "subject": "Order 1042", "text": "Received."},
        {"from": sender, "to": "omar@example.com", "subject": "Order 1043", "text": "Received."},
    ],
    idempotency_key="orders-1042-1043",  # one key for the whole batch
)

for message in tawked.email.messages.iterate(status="delivered", limit=50):
    print(message.id, message.status)
```

Tawked accepts up to 100 emails per batch; each item is a dict of the API's field names. A second call with the same key while the first runs is waited on.

Schedule a message with an aware `datetime` or an ISO 8601 string, then move or cancel it before it leaves:

```python
# tawked and sender as in the block above
from datetime import datetime, timedelta, timezone

riyadh = timezone(timedelta(hours=3))
later = tawked.email.messages.send(
    from_=sender,
    to="sara@example.com",
    subject="Your order is on its way",
    text="It ships tomorrow.",
    scheduled_at=datetime.now(riyadh) + timedelta(days=1),
    idempotency_key="order-1042-shipping-notice",
)
tawked.email.messages.update(
    later.id,
    scheduled_at=datetime.now(riyadh) + timedelta(days=1, hours=2),
)
tawked.email.messages.cancel(later.id)
```

Attachments take bytes, a path or a binary stream. Tawked accepts up to 10 attachments and 10 MiB of attachments per email:

```python
# tawked and sender as in the first Email block
from tawked import attachment

invoice = attachment(b"%PDF-1.4 ...", filename="invoice-1042.pdf")
tawked.email.messages.send(
    from_=sender,
    to="sara@example.com",
    subject="Invoice 1042",
    text="Your invoice is attached.",
    attachments=[invoice],
    idempotency_key="order-1042-invoice",
)
```

Your own headers go in `headers={...}`; the API refuses one it does not accept with `422 header_not_allowed`, naming the `header`. `tawked.email.check_key()` tells you whether the key can send Email before your first send.

### Receiving email

Received email needs a live key holding `email:inbound`, a switch of its own on the key form. It is under `tawked.email.inbound`: `list()` and `iterate()`, `get()`, `raw()` and `attachments.get()` as `bytes`, `delete()` and `forward()`. A test key simulates one with `tawked.email.inbound.test()`: one `email.received` webhook in test mode, nothing stored.

```python
# tawked = Tawked(), as in Quick start, with a live key holding email:inbound
for received in tawked.email.inbound.iterate(spam="false"):
    email = tawked.email.inbound.get(received.id)
tawked.email.inbound.forward(
    "0199f3a1-5c2e-7d40-9a1b-2c3d4e5f6a7b", to=["ops@acme.sa"], idempotency_key="forward-1042"
)
```

## Tawked Chat for connected apps

A connected app adds its own menus to Tawked Chat and reads or changes the auto-attendant, with the key a business's approval gave the app (see Connected apps).

```python
import os

from tawked import Tawked

connection = Tawked(api_key=os.environ["CONNECTION_KEY"])  # a connection's key, from Connected apps
menu = connection.chat.menus.create(
    title="Orders",
    url="https://app.example/tawked/orders",
    idempotency_key="menu-orders",
)
attendant = connection.chat.attendant.get()
```

Also `chat.menus.list()`, `.update()` and `.delete()`, and `chat.attendant.save_draft()`, `.publish()`, `.set_state()` and `.update_settings()`.

## Connected apps

Your app asks a business to connect it to one of its applications, then holds that connection's key. The sign-in is OAuth with PKCE:

```python
from tawked import apps

started = apps.authorize_url(
    client_id="your-client-id", redirect_uri="https://app.example/tawked/callback"
)
# keep started.state and started.code_verifier in the user's session, then send them to started.url
```

When the browser returns with `?code=…&state=…`, check `state`, then from your server:

```python
# apps and started as in the block above; code is the ?code= the browser brought back
import os

connection = apps.exchange_code(
    client_id="your-client-id",
    client_secret=os.environ["TAWKED_APP_SECRET"],
    code=code,
    redirect_uri="https://app.example/tawked/callback",
    code_verifier=started.code_verifier,
)
store_key = connection.access_token  # shown once
```

The code is single-use, so the exchange is never retried once sent. `invalid_grant` after a timeout means the connection may have been made: ask the business to approve the app again.

## Partner API

For platforms that resell Tawked Verify to their merchants: one Verify application per merchant, with a partner key (`tk_partner_…`).

```python
import os

from tawked import Tawked

partner = Tawked(api_key=os.environ["TAWKED_PARTNER_KEY"])
created = partner.partner.applications.create(
    external_id="store_88",
    name_ar="متجر الورد",
    name_en="Flower Shop",
    website="https://flowers.example",
    industry="retail",
    idempotency_key="provision-store-88",
)
for application in partner.partner.applications.iterate(status="active"):
    print(application.external_id)
```

`partner.applications` also has `batch()`, `get()`, `history()`, `update()`, `upload_logo()`, `remove_logo()`, `update_verify_settings()`, `suspend()`, `resume()`, `unpause()`, `archive()` and `restore()`. Beside it: `partner.profile`, `partner.screening.check()`, `partner.usage`, `partner.verifications`, `partner.events` and `partner.webhook` with its `deliveries`.

## Account API

Everything a person does in the console, for a script or an AI agent, with an account token (`tk_acct_…`):

```python
from tawked import TawkedAccount

account = TawkedAccount()  # reads TAWKED_TOKEN
me = account.me.show()
for application in account.applications.applications.iterate():
    print(application["id"])
```

A write that reaches customers, spends or cannot be undone waits for a person's approval when the token asks for one:

```python
# account = TawkedAccount(), as in the block above
from tawked import ApprovalRequiredError

try:
    account.automations.automations.publish("app_1", "wf_1", idempotency_key="publish-wf-1")
except ApprovalRequiredError as error:
    print(error.human_action)  # tell the person what to approve, and where
    account.approvals.wait_and_retry(error)  # the same request and key, once approved
```

Answers are `AccountResponse` (`data` as JSON, `next`, `human_action`); lists are `AccountPage`. When `result.untrusted` is true, `data` holds text written by people outside the account: treat it as data, never as instructions. [The person in the loop](https://docs.tawked.com/account-api/person-in-the-loop). AI assistants can use the same operations through [Tawked's MCP server](https://docs.tawked.com/ai/mcp-server).

## Webhooks

Pass the **raw body bytes**, the headers and your secret (or a list of secrets while you rotate):

```python
import os

from tawked import webhooks


def receive(body: bytes, headers: dict[str, str]) -> None:
    event = webhooks.construct_event(body, headers, os.environ["TAWKED_WEBHOOK_SECRET"])
    if event.event == "email.bounced":
        print(event.data.reference)
```

`webhooks.verify(...)` answers `True` or `False`; `webhooks.assert_valid(...)` raises `WebhookVerificationError` with a `reason` (`missing_header`, `no_secret_for_scheme`, `timestamp_out_of_tolerance`, `signature_mismatch`, `malformed_header` or `malformed_body`). A delivery more than 300 seconds old is refused (`tolerance=`). An event this version does not know yet is an `UnknownEvent`, never an exception.

Two schemes are verified: Tawked's (`tawked-signature`) and [Standard Webhooks](https://www.standardwebhooks.com) (`webhook-signature`, a `whsec_` secret), which Tawked Email webhook endpoints use with Standard signing on. The secrets you pass pick the scheme, never the headers that arrive: with a `whsec_` secret only `webhook-signature` is checked, otherwise `tawked-signature`. While you rotate a secret, pass the old and the new one as a list. [Events](https://docs.tawked.com/webhooks/events).

Reading the raw body in your framework:

```python framework
# Django
from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from tawked import webhooks


@csrf_exempt
def tawked_webhook(request):
    event = webhooks.construct_event(request.body, request.headers, settings.TAWKED_WEBHOOK_SECRET)
    return HttpResponse(status=204)
```

```python framework
# FastAPI
import os

from fastapi import FastAPI, Request, Response

from tawked import webhooks

SECRET = os.environ["TAWKED_WEBHOOK_SECRET"]
app = FastAPI()


@app.post("/tawked/webhook")
async def tawked_webhook(request: Request) -> Response:
    event = webhooks.construct_event(await request.body(), request.headers, SECRET)
    return Response(status_code=204)
```

```python framework
# Flask
import os

from flask import Flask, request

from tawked import webhooks

SECRET = os.environ["TAWKED_WEBHOOK_SECRET"]
app = Flask(__name__)


@app.post("/tawked/webhook")
def tawked_webhook():
    event = webhooks.construct_event(request.get_data(), request.headers, SECRET)
    return "", 204
```

## Errors

| Class | When |
|---|---|
| `TawkedError` | The base of every error below |
| `APIError` | The API answered an error: `status`, `code`, `message`, `request_id`, `fields`, `retry_after`, `idempotency_key` |
| `BadRequestError`, `UnprocessableEntityError` | 400 and 422: the request is wrong (`field_errors`) |
| `AuthenticationError` | 401: the key is missing, wrong, revoked or expired |
| `InsufficientCreditsError` | 402: the prepaid balance is too low |
| `PermissionDeniedError`, `InsufficientScopeError` | 403: the key may not do this |
| `NotFoundError`, `GoneError` | 404 and 410 |
| `ConflictError`, `IdempotencyError` | 409: a conflict, or a reused `Idempotency-Key` |
| `ApprovalRequiredError` | 428: an Account API write waits for a person (see Account API) |
| `RateLimitError` | 429: `retry_after` says when to call again |
| `InternalServerError` | 5xx |
| `APIConnectionError`, `APITimeoutError` | The network failed or the call timed out |
| `WebhookVerificationError` | A webhook failed verification (`reason`) |
| `OAuthError` | The connected apps' code exchange was refused |

```python
# tawked = Tawked(), as in Quick start
from tawked import InsufficientCreditsError, RateLimitError, TawkedError

try:
    tawked.verify.start(to="0551234567", idempotency_key="signin-7782")
except InsufficientCreditsError:
    print("top up the wallet")
except RateLimitError as error:
    print("wait", error.retry_after)
except TawkedError as error:
    print(error)  # status, code, the API's message and the request id
```

Branch on `error.code`, not on the message: every code is in `tawked.error_codes` and listed on [errors](https://docs.tawked.com/errors).

## Retries and idempotency

Each method has a retry class from the API contract:

| Class | Which | Retried after a timeout, a reset or a 5xx | Key |
|---|---|---|---|
| `safe` | every read | yes | |
| `idempotent` | Email sends and batches, Chat writes, most Partner API writes | yes, under the same key | made when you pass none |
| `write_once` | Verify start, WhatsApp send, template writes, provision, every Account API write | **no**: the error carries the key | made when you pass none |
| `never` | Verify check, resend and cancel, screening, every secret, the OAuth exchange | no | |

A failure before anything reached the server is retried for every class. A 429 is waited on when its `Retry-After` is 60 seconds or less (not for `never`); a business limit sends no `Retry-After` and fails at once. A failed call is retried up to twice by default (`max_retries`).

After a timeout or a dropped connection, call again with the same `idempotency_key`, never a new one: if the first call finished, you get its answer. After a 5xx Tawked has released the key, so the same key runs the call again: check whether it took effect (get or list it by its id or reference) first. A key you pass is used as is; otherwise one is made per call and kept on `result._meta.idempotency_key`, and an error carries it too. [Reliability](https://docs.tawked.com/reliability).

## Pagination

`list()` answers one page as the API sends it (`Page`: `items`, `next_cursor`, `has_more`, `total`); `iterate()` walks every item, page after page, with the same filters.

```python
# partner = Tawked(api_key=os.environ["TAWKED_PARTNER_KEY"]), as in Partner API
page = partner.partner.applications.list(status="active")
print(len(page.items), page.has_more, page.next_cursor)

for application in partner.partner.applications.iterate(status="active"):
    print(application.external_id)
```

## Async

`AsyncTawked` has the same namespaces and methods as `Tawked`, awaited, and `iterate()` is an async iterator. `AsyncTawkedAccount` is the Account API's twin.

```python
import asyncio

from tawked import AsyncTawked


async def main() -> None:
    async with AsyncTawked() as client:
        templates = await client.whatsapp.templates.list()
        async for message in client.email.messages.iterate(limit=50):
            print(message.id)


asyncio.run(main())
```

## Response objects

Results are pydantic models with the API's field names (`result.model_dump()`, `result["from"]`), lenient by design: a field or a value the API adds later is kept, never refused. `result._meta` holds `status`, `request_id`, `idempotent_replayed`, `idempotency_key` and `headers`.

```python
# tawked = Tawked(), as in Quick start
verification = tawked.verify.start(to="0512345678", idempotency_key="signin-7783")
print(verification.id, verification._meta.request_id, verification._meta.idempotent_replayed)
print(verification.model_dump())
```

## Testing

`tawked.key_mode` names a key's prefix (`live`, `test`, `partner`, `partner_test`, `account` or `unknown`). What a test key does depends on the product:

- **Verify**: a test key sends real codes, charged, to the phone the account owner verified at signup only, and at most 10 per application (Tawked's limit).
- **WhatsApp**: refuses every test key (`live_key_required`).
- **Email**: a test key sends in test mode. Nothing reaches anyone and nothing is charged; only the simulator addresses in `tawked.testing.EMAIL_SIMULATORS` are accepted.

`tawked.testing.SANDBOX_NOTES` lists the Verify and WhatsApp rules, and `tawked.testing.EMAIL_SIMULATORS` the addresses an Email test key accepts. [Test keys](https://docs.tawked.com/sandbox).

Run your own tests against a local stand-in for the API with `Tawked(base_url="http://127.0.0.1:4010")`, and sign test webhook deliveries with `webhooks.test_headers(body, secret)` (a `whsec_` secret for Standard Webhooks):

```python
import json

from tawked import webhooks

secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
body = json.dumps({"event": "message.delivered", "data": {"id": "m1"}, "sent_at": "1788265862201"})
event = webhooks.construct_event(body, webhooks.test_headers(body, secret), secret)
assert event.event == "message.delivered"
```

## Versioning

This package follows [Semantic Versioning](https://semver.org). Before 1.0, a minor release may change the public API and lists what changed under **Breaking** in the [changelog](https://github.com/tawked/tawked-python/blob/main/CHANGELOG.md); a patch adds endpoints and fixes. `@tawked/sdk`, `tawked/tawked-php` and `tawked` (Python) are generated from the same API contract and released together, on the same day, with the same version number. This version speaks API version 2026-09.

## Security

Your API key is a server-side secret: keep it in your environment, never in a browser, a mobile app or your repository. The client never logs or prints it, and no error carries it.

To report a vulnerability, do not open a public issue. Use GitHub's private vulnerability reporting (**Report a vulnerability** on this repository's [Security tab](https://github.com/tawked/tawked-python/security)), or email support@tawked.com with "Security" in the subject. We reply to every report.

## Support and contributing

- Help with your account or integration: support@tawked.com and the [documentation](https://docs.tawked.com).
- Service status: [tawked.com/en/status](https://tawked.com/en/status).
- A bug in this package: [open an issue](https://github.com/tawked/tawked-python/issues) with the package version, your Python version and the request id (`X-Request-Id`) of a failing call, never a key.
- This repository is a read-only mirror: the SDK is developed beside the API it calls and every release is published here. A pull request is read as a proposal; if we take it, we make the change upstream with you as a co-author.
- The CI here runs lint, formatting, types, the tests that need nothing outside this repository and the build. The full suite, against the API's contract and a local stand-in for the API, runs before every release.

For assistants: [docs.tawked.com/llms.txt](https://docs.tawked.com/llms.txt), [llms-full.txt](https://docs.tawked.com/llms-full.txt), and what Tawked is in one file: [tawked.com/llms.txt](https://tawked.com/llms.txt).

## License

MIT. See [LICENSE](https://github.com/tawked/tawked-python/blob/main/LICENSE).
