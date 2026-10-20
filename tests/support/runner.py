"""What every generated contract test does, against the mock.

The generated modules in ``tests/generated`` hold one case per endpoint, error, retry class and page
style, read from the contract; these helpers run a case with the sync or the async client and, for
``scripts/surface.py``, record the behaviour they observe.
"""

from __future__ import annotations

import base64
import json
import re
from typing import Any

import pytest

import tawked
from tawked import (
    APIConnectionError,
    APITimeoutError,
    ApprovalRequiredError,
    IdempotencyError,
    InternalServerError,
    Page,
    RateLimitError,
    TawkedError,
)
from tawked._errors import role_of
from tawked._generated import types as product_types
from tests.support.mock import (
    APP_KEY,
    PARTNER_KEY,
    Answer429Transport,
    AsyncFlakyTransport,
    FlakyTransport,
    Mock,
)

UA = re.compile(r"^tawked-python/\d+\.\d+\.\d+ \([A-Za-z]+/[\d.]+[a-z0-9+]*; api \d{4}-\d{2}\)$")
UUID = re.compile(r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$")


def resolve(client: Any, call: str) -> Any:
    target = client
    for part in call.split("."):
        target = getattr(target, part)
    return target


def materialize(kwargs: dict[str, Any]) -> dict[str, Any]:
    out = {}
    for name, value in kwargs.items():
        if isinstance(value, dict) and "__file__" in value:
            f = value["__file__"]
            out[name] = (f["filename"], base64.b64decode(f["content_base64"]), f["content_type"])
        else:
            out[name] = value
    return out


def key_for(case: dict[str, Any]) -> str:
    return PARTNER_KEY if case.get("auth") == "partner" else APP_KEY


def client_for(mock: Mock, case: dict[str, Any], *, async_: bool = False, **kwargs: Any) -> Any:
    if "auth" in case:
        return (
            mock.aproduct(key_for(case), **kwargs)
            if async_
            else mock.product(key_for(case), **kwargs)
        )
    return mock.aaccount(**kwargs) if async_ else mock.account(**kwargs)


def surface_of(case: dict[str, Any]) -> str:
    return "product" if "auth" in case else "account"


def sends_key(case: dict[str, Any]) -> bool:
    return bool(case["takes_key"]) and case["retry"] in ("idempotent", "write_once")


def wire_str(value: Any) -> str:
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def expected_query(case: dict[str, Any]) -> dict[str, str]:
    if "auth" in case:
        return {k: wire_str(v) for k, v in case["query"].items()}
    if case["in"] == "query":
        return {k: wire_str(v) for k, v in case["wire"].items() if not isinstance(v, (list, dict))}
    return {}


def check_request(case: dict[str, Any], row: dict[str, Any], key: str) -> None:
    assert row["method"] == case["method"]
    assert row["path"] == case["path"]
    assert row["query"] == expected_query(case)
    headers = row["headers"]
    assert headers["authorization"] == f"Bearer {key}"
    assert UA.match(headers["user-agent"]), headers["user-agent"]
    assert headers["accept"] == "application/json"
    if "auth" in case:
        if case["body"] is not None:
            assert json.loads(row["body"]) == case["body"]
        for name, filename in case["multipart"].items():
            assert f'name="{name}"; filename="{filename}"' in row["body"]
    elif case["in"] == "body":
        if case["body"] == "multipart":
            assert headers["content-type"].startswith("multipart/form-data")
            for name, value in case["wire"].items():
                if isinstance(value, dict) and "file" in value:
                    assert f'name="{name}"; filename="{value["file"]}"' in row["body"]
                elif isinstance(value, list):
                    # A list goes as `name[]` parts, the form Laravel reads.
                    assert f'name="{name}[]"' in row["body"]
                else:
                    assert f'name="{name}"' in row["body"]
        elif case["body"] == "json":
            assert json.loads(row["body"] or "{}") == case["wire"]
    if sends_key(case):
        sent = headers.get("idempotency-key")
        assert sent is not None
        assert sent == case.get("key") or (case.get("key") is None and UUID.match(sent)), sent
    else:
        assert "idempotency-key" not in headers


def check_result(case: dict[str, Any], result: Any) -> None:
    if "auth" not in case:
        if case["pagination"]:
            assert isinstance(result, tawked.AccountPage)
        else:
            assert isinstance(result, tawked.AccountResponse)
        assert result._meta is not None and result._meta.request_id
        return
    if case["pagination"]:
        assert isinstance(result, Page)
        item = getattr(product_types, case["item"])
        assert all(isinstance(i, item) for i in result.items)
        assert isinstance(result.response, getattr(product_types, case["response"]))
    elif case["binary"]:
        assert isinstance(result, bytes)
        return
    else:
        assert isinstance(result, getattr(product_types, case["response"]))
    assert result._meta is not None and result._meta.request_id


def iterate_call(case: dict[str, Any]) -> str:
    namespace, method = case["call"].rsplit(".", 1)
    return f"{namespace}.iterate" if method == "list" else f"{namespace}.iterate_{method}"


def params(cases: list[dict[str, Any]], key: str = "id") -> list[Any]:
    """The cases as pytest params, each named by its id."""
    return [pytest.param(case, id=str(case[key])) for case in cases]


def prepared(mock: Mock, case: dict[str, Any]) -> dict[str, Any]:
    """``approvals.show`` reads an approval the mock made: ask for one first."""
    if case["id"] != "approvals.show":
        return case
    account = mock.account()
    try:
        account.automations.automations.publish("app_1", "wf_1")
    except ApprovalRequiredError as error:
        return {**case, "args": [error.approval_id], "path": f"/v1/approvals/{error.approval_id}"}
    raise AssertionError("a consequential write did not answer 428")


def call(client: Any, case: dict[str, Any], **extra: Any) -> Any:
    kwargs = {**materialize(case["kwargs"]), **extra}
    return resolve(client, case["call"])(*case["args"], **kwargs)


def approve(client: Any, error: ApprovalRequiredError) -> Any:
    return client.approvals.wait_and_retry(error, poll_every=0)


# ---------------------------------------------------------------------------------------- item 1


def run_example(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    if case.get("approval"):
        with pytest.raises(ApprovalRequiredError) as info:
            call(client, case, extra_headers={"X-Mock-Approval": "approved"})
        error = info.value
        assert error.human_action is not None and error.approval_id
        result = approve(client, error)
        first, again = mock.requests(case["path"])
        assert again["headers"]["tawked-approval"] == error.approval_id
        assert (
            again["headers"].get("idempotency-key")
            == first["headers"].get("idempotency-key")
            == error.idempotency_key
        )
        assert again["body"] == first["body"]
        check_request(case, first, client._transport._auth_header[7:])
    else:
        result = call(client, case)
        rows = mock.requests(case["path"])
        assert len(rows) == 1, rows
        check_request(case, rows[0], client._transport._auth_header[7:])
    check_result(case, result)


async def run_example_async(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case, async_=True)
    kwargs = {**materialize(case["kwargs"])}
    if case.get("approval"):
        with pytest.raises(ApprovalRequiredError) as info:
            await resolve(client, case["call"])(
                *case["args"], **kwargs, extra_headers={"X-Mock-Approval": "approved"}
            )
        result = await client.approvals.wait_and_retry(info.value, poll_every=0)
        check_request(case, mock.requests(case["path"])[0], client._transport._auth_header[7:])
    else:
        result = await resolve(client, case["call"])(*case["args"], **kwargs)
        rows = mock.requests(case["path"])
        assert len(rows) == 1
        check_request(case, rows[0], client._transport._auth_header[7:])
    check_result(case, result)
    await client.close()


# ---------------------------------------------------------------------------------------- item 2


def run_error(mock: Mock, case: dict[str, Any], error: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    with pytest.raises(TawkedError) as info:
        call(client, case, extra_headers={"X-Mock-Error": error["code"]}, max_retries=0)
    e = info.value
    code = error["code"].split(":")[0]
    assert role_of(type(e)) == error["role"], (type(e).__name__, error)
    assert getattr(e, "code", None) == code
    assert getattr(e, "status", None) == error["status"]
    assert getattr(e, "request_id", None)
    if code == "insufficient_scope":
        assert e.required_scope  # type: ignore[attr-defined]
    if code == "template_in_use":
        assert e.used_by is not None  # type: ignore[attr-defined]
    if code in ("not_resendable", "template_not_editable"):
        assert e.resource_status  # type: ignore[attr-defined]
    if code == "approval_required":
        assert isinstance(e, ApprovalRequiredError) and e.approval_id and e.human_action
    if surface_of(case) == "account":
        assert e.next  # type: ignore[attr-defined]


# ---------------------------------------------------------------------------------------- item 3


def _same_path(mock: Mock, case: dict[str, Any]) -> list[dict[str, Any]]:
    return mock.requests(case["path"])


def run_after_500(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    retried = case["retry"] in ("safe", "idempotent")
    try:
        call(client, case, extra_headers={"X-Mock-Fault": mock.fault("500")})
        outcome: Any = None
    except TawkedError as error:
        outcome = error
    rows = _same_path(mock, case)
    keys = [r["headers"].get("idempotency-key") for r in rows]
    mock.record(
        surface_of(case),
        case["call"],
        "after_500",
        {"requests": len(rows), "key": keys[0] is not None, "same_key": len(set(keys)) == 1},
    )
    if retried:
        assert len(rows) == 2
        assert outcome is None or isinstance(outcome, ApprovalRequiredError)
        assert len(set(keys)) == 1
    else:
        assert len(rows) == 1
        assert isinstance(outcome, InternalServerError), outcome
        if sends_key(case):
            assert outcome.idempotency_key == keys[0]
            assert str(outcome).startswith(f"Idempotency-Key {keys[0]}"), str(outcome)
        if case.get("secret"):
            assert "rotate or revoke" in str(outcome)


def run_read_timeout(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    retried = case["retry"] in ("safe", "idempotent")
    try:
        call(
            client,
            case,
            extra_headers={"X-Mock-Fault": mock.fault("read-timeout", delay=1000)},
            timeout=0.25,
        )
        outcome: Any = None
    except TawkedError as error:
        outcome = error
    rows = _same_path(mock, case)
    mock.record(surface_of(case), case["call"], "after_timeout", {"requests": len(rows)})
    if retried:
        assert len(rows) == 2
        assert outcome is None or isinstance(outcome, ApprovalRequiredError)
    else:
        assert len(rows) == 1
        assert isinstance(outcome, APITimeoutError), outcome
        if sends_key(case):
            key = rows[0]["headers"]["idempotency-key"]
            assert outcome.idempotency_key == key and str(outcome).startswith(
                f"Idempotency-Key {key}"
            )


def run_drop(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    retried = case["retry"] in ("safe", "idempotent")
    try:
        call(client, case, extra_headers={"X-Mock-Fault": mock.fault("drop-before-send")})
        outcome: Any = None
    except TawkedError as error:
        outcome = error
    rows = _same_path(mock, case)
    assert rows[0]["fault"] == "drop-before-send" and rows[0]["acted"] is False
    if retried:
        assert len(rows) == 2
        assert outcome is None or isinstance(outcome, ApprovalRequiredError)
    else:
        assert len(rows) == 1
        assert isinstance(outcome, APIConnectionError) and outcome.sent, outcome


def run_pre_send(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    flaky = FlakyTransport(failures=1)
    client = client_for(mock, case, http_client=__import__("httpx").Client(transport=flaky))
    try:
        call(client, case)
    except ApprovalRequiredError:
        pass
    rows = _same_path(mock, case)
    mock.record(
        surface_of(case), case["call"], "pre_send", {"attempts": flaky.calls, "requests": len(rows)}
    )
    assert flaky.calls == 2
    assert len(rows) == 1


def run_429(mock: Mock, case: dict[str, Any]) -> None:
    """The per-key throttle (``too_many_requests``, Retry-After: 1) is waited on by every class
    but ``never``; a business limit without Retry-After (``daily_cap_reached``) by none."""
    case = prepared(mock, case)
    throttle = Answer429Transport("too_many_requests", retry_after="1")
    client = client_for(mock, case, http_client=__import__("httpx").Client(transport=throttle))
    try:
        call(client, case)
        outcome: Any = None
    except TawkedError as error:
        outcome = error
    mock.record(surface_of(case), case["call"], "after_429", {"requests": throttle.calls})
    if case["retry"] == "never":
        assert throttle.calls == 1
        assert isinstance(outcome, RateLimitError), outcome
    else:
        assert throttle.calls == 2
        assert not isinstance(outcome, RateLimitError), outcome
        assert mock.sleeps == [1.0]

    business = Answer429Transport("daily_cap_reached")
    client = client_for(mock, case, http_client=__import__("httpx").Client(transport=business))
    with pytest.raises(RateLimitError):
        call(client, case)
    assert business.calls == 1


def run_in_progress(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    try:
        call(client, case, extra_headers={"X-Mock-Fault": mock.fault("in-progress:3", times=3)})
    except ApprovalRequiredError:
        pass
    rows = _same_path(mock, case)
    keys = {r["headers"]["idempotency-key"] for r in rows}
    assert len(rows) == 4 and len(keys) == 1
    assert mock.sleeps == [1.0, 2.0, 4.0]


def run_in_progress_window(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    with pytest.raises(IdempotencyError) as info:
        call(client, case, extra_headers={"X-Mock-Fault": mock.fault("in-progress:99", times=99)})
    key = info.value.idempotency_key
    assert key and str(info.value).startswith(f"`Idempotency-Key {key}`")
    assert sum(mock.sleeps) == 30.0


async def run_after_500_async(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case, async_=True)
    retried = case["retry"] in ("safe", "idempotent")
    try:
        await resolve(client, case["call"])(
            *case["args"],
            **materialize(case["kwargs"]),
            extra_headers={"X-Mock-Fault": mock.fault("500")},
        )
        outcome: Any = None
    except TawkedError as error:
        outcome = error
    rows = _same_path(mock, case)
    assert len(rows) == (2 if retried else 1)
    if not retried:
        assert isinstance(outcome, InternalServerError)
    await client.close()


async def run_pre_send_async(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    import httpx

    flaky = AsyncFlakyTransport(failures=1)
    client = client_for(mock, case, async_=True, http_client=httpx.AsyncClient(transport=flaky))
    try:
        await resolve(client, case["call"])(*case["args"], **materialize(case["kwargs"]))
    except ApprovalRequiredError:
        pass
    assert flaky.calls == 2
    assert len(_same_path(mock, case)) == 1


# ---------------------------------------------------------------------------------------- item 4


def run_pages(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case)
    first = call(client, case, extra_headers={"X-Mock-Pages": "1"})
    per_page = len(first.items)
    mock.test_id += "-walk"
    client = client_for(mock, case)
    method = resolve(client, iterate_call(case))
    items = list(
        method(*case["args"], **materialize(case["kwargs"]), extra_headers={"X-Mock-Pages": "3"})
    )
    rows = _same_path(mock, case)
    second = rows[1]["query"] if len(rows) > 1 else {}
    style = "offset" if "offset" in second else ("cursor" if "cursor" in second else None)
    mock.record(
        surface_of(case),
        case["call"],
        "pages",
        {"requests": len(rows), "items": len(items), "per_page": per_page, "style": style},
    )
    assert per_page > 0
    assert len(rows) == 3, rows
    assert len(items) == 3 * per_page


async def run_pages_async(mock: Mock, case: dict[str, Any]) -> None:
    case = prepared(mock, case)
    client = client_for(mock, case, async_=True)
    method = resolve(client, iterate_call(case))
    items = [
        i
        async for i in method(
            *case["args"], **materialize(case["kwargs"]), extra_headers={"X-Mock-Pages": "3"}
        )
    ]
    rows = _same_path(mock, case)
    assert len(rows) == 3 and len(items) > 0
    await client.close()
