"""The hand-written core without the mock: transport rules, errors, models."""

from __future__ import annotations

import json
import os
from datetime import datetime, timedelta, timezone
from email.utils import format_datetime
from pathlib import Path
from typing import Any

import httpx
import pytest

import tawked
from tawked import (
    NOT_GIVEN,
    APIConnectionError,
    AsyncTawked,
    IdempotencyError,
    InsufficientScopeError,
    RateLimitError,
    SecretNotReplayableError,
    Tawked,
    TawkedAccount,
    UnexpectedResponseError,
)
from tawked._client import key_mode_of
from tawked._errors import ROLES
from tawked.attachments import attachment, check_attachments

KEY = "tk_live_" + "s3cr3t" * 6


def client(handler: Any, **kwargs: Any) -> tuple[Tawked, list[float]]:
    sleeps: list[float] = []
    c = Tawked(
        api_key=KEY,
        base_url="https://api.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
        **kwargs,
    )
    c._transport.sleep = sleeps.append
    return c, sleeps


def answer(status: int, body: Any = None, headers: dict[str, str] | None = None) -> httpx.Response:
    return httpx.Response(
        status,
        json=body if body is not None else {},
        headers={"x-request-id": "req_1", **(headers or {})},
    )


def send(c: Tawked) -> Any:
    return c.email.messages.send(
        to="sara@example.com", subject="طلبك رقم 1042", text="مرحبا", idempotency_key="order-1042"
    )


def test_retry_after_one_second_waits_then_retries() -> None:
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        if len(calls) == 1:
            return answer(429, {"error": "too_many_requests"}, {"retry-after": "1"})
        return answer(202, {"id": "m1", "status": "accepted"})

    c, sleeps = client(handler)
    assert send(c).id == "m1"
    assert sleeps == [1.0] and len(calls) == 2


def test_retry_after_beyond_sixty_seconds_fails_at_once() -> None:
    c, sleeps = client(
        lambda r: answer(429, {"error": "too_many_requests"}, {"retry-after": "120"})
    )
    with pytest.raises(RateLimitError) as info:
        send(c)
    assert info.value.retry_after == 120.0 and sleeps == []


def test_retry_after_as_an_http_date() -> None:
    when = format_datetime(datetime.now(timezone.utc) + timedelta(seconds=30), usegmt=True)
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return (
            answer(429, {"error": "too_many_requests"}, {"retry-after": when})
            if len(calls) == 1
            else answer(202, {"id": "m1"})
        )

    c, sleeps = client(handler)
    send(c)
    assert 25 <= sleeps[0] <= 31


@pytest.mark.parametrize(
    ("body", "headers"),
    [
        ({"error": "daily_cap_reached"}, {}),
        ({"error": "spend_cap_reached"}, {}),
        ({"error": "rate_limited"}, {}),
        ({"error": "too_many_requests"}, {}),
        ({"error": "rate_limited"}, {"retry-after": "600"}),
    ],
    ids=[
        "daily_cap_reached",
        "spend_cap_reached",
        "rate_limited",
        "no-retry-after",
        "retry-after-600",
    ],
)
def test_a_business_limit_or_a_429_without_retry_after_is_not_retried(
    body: dict[str, str], headers: dict[str, str]
) -> None:
    """A 429 is waited on only when its Retry-After is 60 s or less, as in @tawked/sdk and
    tawked-php: a business limit sends none, and a longer one fails the call."""
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return answer(429, body, headers) if len(calls) == 1 else answer(202, {"id": "m1"})

    c, sleeps = client(handler)
    with pytest.raises(RateLimitError) as info:
        send(c)
    assert info.value.code == body["error"]
    assert len(calls) == 1 and sleeps == []


def test_email_rate_limited_with_a_short_retry_after_is_waited_on() -> None:
    """Email's per-second limit answers ``rate_limited`` with Retry-After: 1:
    the Retry-After, not the code, says the wait is worth it."""
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        if len(calls) == 1:
            return answer(429, {"error": "rate_limited"}, {"retry-after": "1"})
        return answer(202, {"id": "m1"})

    c, sleeps = client(handler)
    send(c)
    assert len(calls) == 2 and sleeps == [1.0]


def test_429_on_a_never_call_is_not_retried() -> None:
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return answer(429, {"error": "too_many_requests"}, {"retry-after": "1"})

    c, _ = client(handler)
    with pytest.raises(RateLimitError):
        c.verify.check(id="v1", code="123456")
    assert len(calls) == 1


def test_in_progress_window_is_thirty_seconds_and_names_the_key() -> None:
    c, sleeps = client(lambda r: answer(409, {"error": "idempotency_in_progress"}))
    with pytest.raises(IdempotencyError) as info:
        send(c)
    assert sleeps == [1.0, 2.0, 4.0, 5.0, 5.0, 5.0, 5.0, 3.0]
    assert str(info.value).startswith(
        "`Idempotency-Key order-1042` is still being processed: call again with `idempotency_key='order-1042'`"
    )


def test_in_progress_window_is_an_option() -> None:
    c, sleeps = client(
        lambda r: answer(409, {"error": "idempotency_in_progress"}), in_progress_wait=3
    )
    with pytest.raises(IdempotencyError):
        send(c)
    assert sleeps == [1.0, 2.0]


def test_a_minted_key_is_reused_for_every_attempt() -> None:
    keys = []

    def handler(request: httpx.Request) -> httpx.Response:
        keys.append(request.headers["idempotency-key"])
        return (
            answer(500, {"error": "internal_error"}) if len(keys) < 3 else answer(202, {"id": "m1"})
        )

    c, _ = client(handler)
    result = c.email.messages.send(to="sara@example.com", subject="s", text="t")
    assert len(set(keys)) == 1 and len(keys) == 3
    assert result._meta is not None and result._meta.idempotency_key == keys[0]


def test_max_retries_zero_turns_retries_off_and_cannot_be_negative() -> None:
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return answer(500, {"error": "internal_error"})

    c, _ = client(handler, max_retries=0)
    with pytest.raises(tawked.InternalServerError):
        c.chat.menus.list()
    assert len(calls) == 1
    with pytest.raises(ValueError):
        c.chat.menus.list(max_retries=-1)


def test_malformed_idempotency_keys_are_refused_before_sending() -> None:
    c, _ = client(lambda r: pytest.fail("nothing is sent"))
    for bad in ("", "has space", "x" * 257, "مفتاح"):
        with pytest.raises(ValueError, match="printable ASCII"):
            c.email.messages.send(to="a@b.sa", subject="s", text="t", idempotency_key=bad)
    with pytest.raises(ValueError, match="1-128"):
        c.verify.start(to="0551234567", idempotency_key="x" * 129)


def test_email_keys_take_up_to_256_characters() -> None:
    seen = []
    c, _ = client(lambda r: seen.append(r.headers["idempotency-key"]) or answer(202, {"id": "m1"}))
    c.email.messages.send(to="a@b.sa", subject="s", text="t", idempotency_key="k" * 256)
    assert seen == ["k" * 256]


def test_arabic_is_sent_as_raw_utf8() -> None:
    bodies = []
    c, _ = client(lambda r: bodies.append(r.content) or answer(202, {"id": "m1"}))
    send(c)
    assert "طلبك رقم 1042".encode() in bodies[0]
    assert b"\\u" not in bodies[0]
    assert json.loads(bodies[0])["subject"] == "طلبك رقم 1042"


def test_not_given_is_left_out_and_none_is_sent_as_null_where_nullable() -> None:
    bodies = []
    c, _ = client(lambda r: bodies.append(json.loads(r.content)) or answer(202, {"id": "m1"}))
    c.email.messages.send(to="a@b.sa", subject="s", text="t", html=None, reference=NOT_GIVEN)
    assert bodies[0] == {"to": "a@b.sa", "subject": "s", "text": "t", "html": None}


def test_from_is_sent_as_from() -> None:
    bodies = []
    c, _ = client(lambda r: bodies.append(json.loads(r.content)) or answer(202, {"id": "m1"}))
    c.email.messages.send(
        from_={"name": "متجر", "address": "orders@acme.sa"}, to="a@b.sa", subject="s", text="t"
    )
    assert bodies[0]["from"] == {"name": "متجر", "address": "orders@acme.sa"}


def test_dates_in_aware_or_string_never_naive() -> None:
    bodies = []
    c, _ = client(lambda r: bodies.append(json.loads(r.content)) or answer(202, {"id": "m1"}))
    riyadh = timezone(timedelta(hours=3))
    c.email.messages.send(
        to="a@b.sa", subject="s", text="t", scheduled_at=datetime(2026, 10, 22, 9, 0, tzinfo=riyadh)
    )
    assert bodies[0]["scheduled_at"] == "2026-10-22T09:00:00+03:00"
    with pytest.raises(ValueError, match="naive"):
        c.email.messages.send(
            to="a@b.sa", subject="s", text="t", scheduled_at=datetime(2026, 10, 22, 9, 0)
        )


def test_dates_out_are_datetimes() -> None:
    c, _ = client(
        lambda r: answer(
            200,
            {
                "id": "v1",
                "status": "pending",
                "expires_at": "2026-09-01T12:34:56.789Z",
                "verified_at": None,
            },
        )
    )
    result = c.verify.get("v1")
    assert result.expires_at == datetime(2026, 9, 1, 12, 34, 56, 789000, tzinfo=timezone.utc)
    assert result.verified_at is None


def test_a_wrong_type_in_an_answer_is_kept_not_refused(caplog: pytest.LogCaptureFixture) -> None:
    c, _ = client(
        lambda r: answer(
            200, {"id": 7, "status": "a_new_status", "attempts_remaining": "lots", "brand_new": [1]}
        )
    )
    result = c.verify.get("v1")
    assert result.status == "a_new_status"
    assert result.attempts_remaining == "lots"  # type: ignore[comparison-overlap]
    assert result.brand_new == [1]
    assert any("kept a response value" in r.message for r in caplog.records)


def test_a_2xx_that_is_not_json_is_an_unexpected_response() -> None:
    c, _ = client(
        lambda r: httpx.Response(200, content=b"<html>", headers={"x-request-id": "req_9"})
    )
    with pytest.raises(UnexpectedResponseError) as info:
        c.chat.menus.list()
    assert info.value.request_id == "req_9"


def test_error_fields_and_scope() -> None:
    headers = {
        "www-authenticate": 'Bearer error="insufficient_scope", scope="notifications:templates"'
    }
    c, _ = client(lambda r: answer(403, {"error": "insufficient_scope"}, headers))
    with pytest.raises(InsufficientScopeError) as info:
        c.whatsapp.templates.create(
            name="order_shipped", language="ar", category="UTILITY", body="x"
        )
    error = info.value
    assert error.required_scope == "notifications:templates"
    assert (
        error.status == 403 and error.code == "insufficient_scope" and error.request_id == "req_1"
    )
    assert "req_1" in str(error)


def test_secret_not_replayable_carries_id_and_original_status() -> None:
    a = TawkedAccount(
        token="tk_acct_" + "x" * 20,
        base_url="https://api.test",
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda r: answer(
                    409,
                    {
                        "error": "idempotency_secret_not_replayable",
                        "id": "key_1",
                        "original_status": 201,
                        "next": "…",
                    },
                )
            )
        ),
    )
    with pytest.raises(SecretNotReplayableError) as info:
        a.applications.keys.create("app_1", name="ci", mode="live", idempotency_key="k1")
    assert info.value.id == "key_1" and info.value.original_status == 201


def test_secret_calls_are_sent_once_and_say_rotate_or_revoke() -> None:
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return answer(500, {"error": "internal_error"})

    a = TawkedAccount(
        token="tk_acct_" + "x" * 20,
        base_url="https://api.test",
        http_client=httpx.Client(transport=httpx.MockTransport(handler)),
    )
    with pytest.raises(tawked.InternalServerError) as info:
        a.applications.keys.create("app_1", name="ci", mode="live")
    assert len(calls) == 1
    assert "idempotency-key" not in calls[0].headers
    assert "rotate or revoke" in str(info.value)


def test_no_secret_in_repr_or_errors() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ConnectError("refused", request=request)

    c, _ = client(handler)
    assert KEY not in repr(c) and "s3cr3t" not in repr(c)
    with pytest.raises(APIConnectionError) as info:
        c.chat.menus.list()
    assert "s3cr3t" not in str(info.value) and "s3cr3t" not in repr(info.value)
    c2, _ = client(lambda r: answer(401, {"error": "unauthorized"}, {"authorization": KEY}))
    with pytest.raises(tawked.AuthenticationError) as info2:
        c2.chat.menus.list()
    assert "authorization" not in info2.value.headers
    assert "s3cr3t" not in str(info2.value) and "s3cr3t" not in repr(info2.value)
    account = TawkedAccount(token="tk_acct_s3cr3ts3cr3t")
    assert "s3cr3t" not in repr(account)


def test_headers_on_every_call() -> None:
    seen = []
    c, _ = client(lambda r: seen.append(r.headers) or answer(200, {"data": []}))
    c.chat.menus.list()
    headers = seen[0]
    assert headers["authorization"] == f"Bearer {KEY}"
    assert headers["accept"] == "application/json"
    assert headers["user-agent"].startswith(f"tawked-python/{tawked.__version__} (")
    assert headers["user-agent"].endswith(f"; api {tawked.API_VERSION})")
    assert "idempotency-key" not in headers


def test_account_language_header() -> None:
    seen = []
    a = TawkedAccount(
        token="tk_acct_" + "x" * 20,
        base_url="https://api.test",
        language="ar",
        http_client=httpx.Client(
            transport=httpx.MockTransport(
                lambda r: seen.append(r.headers) or answer(200, {"data": {}})
            )
        ),
    )
    result = a.account.show()
    assert seen[0]["accept-language"] == "ar"
    assert result.data == {}


def test_environment_defaults(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TAWKED_API_KEY", "tk_test_abc")
    monkeypatch.setenv("TAWKED_BASE_URL", "http://127.0.0.1:9")
    monkeypatch.setenv("TAWKED_TOKEN", "tk_acct_abcdefgh")
    assert Tawked().base_url == "http://127.0.0.1:9" and Tawked().key_mode == "test"
    assert TawkedAccount().key_mode == "account"
    monkeypatch.delenv("TAWKED_API_KEY")
    monkeypatch.delenv("TAWKED_TOKEN")
    with pytest.raises(ValueError, match="TAWKED_API_KEY"):
        Tawked()
    with pytest.raises(ValueError, match="TAWKED_TOKEN"):
        TawkedAccount()


@pytest.mark.parametrize(
    ("key", "mode"),
    [
        ("tk_live_x", "live"),
        ("tk_test_x", "test"),
        ("tk_partner_x", "partner"),
        ("tk_partner_test_x", "partner_test"),
        ("tk_acct_x", "account"),
        ("sk_x", "unknown"),
    ],
)
def test_key_mode(key: str, mode: str) -> None:
    assert key_mode_of(key) == mode
    assert not hasattr(Tawked(api_key=key), "is_test_key")


def test_context_managers_close() -> None:
    with Tawked(api_key=KEY) as c:
        transport = c._transport
    assert transport.http.is_closed


@pytest.mark.anyio
async def test_async_context_manager_closes() -> None:
    async with AsyncTawked(api_key=KEY) as c:
        transport = c._transport
    assert transport.http.is_closed


def test_every_role_has_a_class_named_as_the_table() -> None:
    names = {cls.__name__ for cls in ROLES}
    assert names == {
        "TawkedError", "APIConnectionError", "APITimeoutError", "APIError", "BadRequestError",
        "AuthenticationError", "InsufficientCreditsError", "PermissionDeniedError", "InsufficientScopeError",
        "NotFoundError", "ConflictError", "IdempotencyError", "SecretNotReplayableError", "GoneError",
        "UnprocessableEntityError", "ApprovalRequiredError", "RateLimitError", "InternalServerError",
        "UnexpectedResponseError", "WebhookVerificationError", "OAuthError",
    }  # fmt: skip
    assert not issubclass(tawked.APIConnectionError, ConnectionError)
    assert not issubclass(tawked.APITimeoutError, TimeoutError)


def test_attachments(tmp_path: Any) -> None:
    path = tmp_path / "invoice.pdf"
    path.write_bytes(b"%PDF-1.4")
    item = attachment(path)
    assert item == {
        "filename": "invoice.pdf",
        "content": "JVBERi0xLjQ=",
        "content_type": "application/pdf",
    }
    assert attachment(b"hi", filename="a.txt")["content_type"] == "text/plain"
    with open(path, "rb") as stream:
        assert attachment(stream)["filename"] == "invoice.pdf"
    with pytest.raises(ValueError, match="bytes"):
        attachment(b"x" * (10 * 1024 * 1024 + 1), filename="big.bin")
    with pytest.raises(ValueError, match="at most 10"):
        check_attachments([item] * 11)


def test_sync_and_async_namespaces_match() -> None:
    def walk(obj: Any, prefix: str = "") -> set[str]:
        out = set()
        for name in dir(obj):
            if name.startswith("_"):
                continue
            value = getattr(obj, name)
            if callable(value):
                out.add(prefix + name)
            elif type(value).__module__.startswith("tawked._generated"):
                out |= walk(value, prefix + name + ".")
        return out

    assert walk(Tawked(api_key=KEY)) == walk(AsyncTawked(api_key=KEY))
    assert walk(TawkedAccount(token="tk_acct_abcdefgh")) - {"close"} == walk(
        tawked.AsyncTawkedAccount(token="tk_acct_abcdefgh")
    ) - {"close"}


def test_a_write_once_5xx_says_the_key_was_released_and_to_look_before_calling_again() -> None:
    # The server releases the key on a 5xx: the same key would run the send again.
    calls = []

    def handler(request: httpx.Request) -> httpx.Response:
        calls.append(request)
        return answer(502, {"error": "send_failed", "message": "x", "provider_code": None})

    c, _ = client(handler, max_retries=2)
    with pytest.raises(tawked.APIError) as info:
        c.verify.start(to="0551234567", idempotency_key="signin-1")
    assert len(calls) == 1
    text = str(info.value)
    assert text.startswith(
        "Idempotency-Key signin-1: the request may have been applied, and Tawked released the key on this 5xx"
    )
    assert "check whether it took effect" in text and "to retry safely" not in text


def test_a_timeout_after_sending_names_the_key_to_call_again_with() -> None:
    def handler(request: httpx.Request) -> httpx.Response:
        raise httpx.ReadTimeout("slow", request=request)

    c, _ = client(handler, max_retries=2)
    with pytest.raises(tawked.APITimeoutError) as info:
        c.verify.start(to="0551234567", idempotency_key="signin-1")
    assert "call again with idempotency_key='signin-1'" in str(info.value)
    assert "released" not in str(info.value)


def _contract() -> dict[str, Any]:
    """The API contract beside this package in Tawked's monorepo (or in TAWKED_CONTRACT)."""
    directory = (
        os.environ.get("TAWKED_CONTRACT") or Path(__file__).resolve().parents[2] / "contract"
    )
    path = Path(directory) / "api.json"
    if not path.is_file():
        pytest.skip("The API contract is not beside this package.")
    contract: dict[str, Any] = json.loads(path.read_text(encoding="utf-8"))
    return contract


def test_testing_lists_the_email_simulators_of_the_contract() -> None:
    # Test mode: a test key's e-mail goes only to these addresses, each with the events it plays.
    from tawked.testing import EMAIL_SIMULATORS

    contract = _contract()
    assert list(EMAIL_SIMULATORS) == contract["sandbox"]["email"]["simulators"]
    assert all(s["address"].endswith("@sim.tawked.com") for s in EMAIL_SIMULATORS)


def test_a_test_keys_simulated_email_received_is_known_by_its_envelopes_mode() -> None:
    # The received data has no `mode`: the envelope's `"mode": "test"` is the only sign it is simulated.
    from tawked import webhooks
    from tawked._generated.events import EmailReceivedEvent

    contract = _contract()
    example = contract["webhooks"]["application"]["test_mode_example"]
    body = json.dumps(example, ensure_ascii=False)
    secret = "tawked-test-secret-0000000000000001"
    event = webhooks.construct_event(body, webhooks.test_headers(body, secret), secret)

    assert isinstance(event, EmailReceivedEvent)
    assert event.mode == "test"
    assert event.is_test_mode
    assert event.type == "email.received"
    assert event.timestamp == example["timestamp"]
    assert "mode" not in example["data"]

    live = json.dumps({k: v for k, v in example.items() if k != "mode"})
    live_event = webhooks.construct_event(live, webhooks.test_headers(live, secret), secret)
    assert live_event.mode is None
    assert not live_event.is_test_mode
