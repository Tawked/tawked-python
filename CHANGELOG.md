# Changelog

`tawked` is the Python client for Tawked (Python 3.10+, sync and async): Verify, WhatsApp, Tawked
Email, Chat for connected apps, the Partner API, the Account API, connected apps' OAuth and webhook
signatures. All notable changes are listed here. The format follows
[Keep a Changelog](https://keepachangelog.com/en/1.1.0/) and the package follows semantic
versioning; before 1.0 a minor may break, under a "Breaking" heading. `tawked` (Python),
`@tawked/sdk` (JavaScript) and `tawked/tawked-php` move in lockstep from the same contract.

## 0.1.0 - 2026-10-21

The first release, covering every Tawked product, generated from Tawked's API contract (API
version 2026-09).

### Added

- `Tawked` and `AsyncTawked` (API keys): Tawked Verify (`verify.start`, `check`, `get`, `resend`,
  `cancel`), WhatsApp messages and templates, Tawked Email (`email.messages.send`, `send_batch`,
  `list`/`iterate`, `get`, `update`, `cancel`, `email.check_key`; early access), Tawked Chat's
  menus and auto-attendant for connected apps, and the Partner API with `iterate()` over every
  list.
- `TawkedAccount` and `AsyncTawkedAccount` (account tokens): every Account API operation, the
  `{data, next, human_action}` envelope, `AccountPage`, and `approvals.wait_and_retry()` for the
  428 approval loop.
- `tawked.apps`: `authorize_url()` with PKCE (S256) and `exchange_code()` / `exchange_code_async()`
  for connected apps.
- `tawked.webhooks`: `verify`, `assert_valid`, `construct_event` (typed events, `UnknownEvent` for
  new ones), `sign` and `test_headers`, over Tawked's `tawked-signature` and Standard Webhooks
  (`whsec_` secrets), domain-separated, with secret rotation.
- Retries by class: reads retried; writes retried after sending only where the server keeps the
  key through a failure; `Idempotency-Key` minted per call when none is given and carried first in
  every after-send error; a 30-second wait on `idempotency_in_progress`; `Retry-After` up to 60 s.
- One error hierarchy (`TawkedError`, `APIError` and a class per status, `APIConnectionError`,
  `APITimeoutError`, `SecretNotReplayableError`, `ApprovalRequiredError`, `OAuthError`,
  `WebhookVerificationError`) and every error code in `tawked.error_codes` and `tawked.ErrorCode`.
- Lenient pydantic models: unknown fields and values are kept, never refused.
- `attachment()` for Email attachments; `key_mode`; `tawked.testing` constants.
