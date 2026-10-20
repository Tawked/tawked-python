"""Connected apps and the Account API's 428 loop, against the mock."""

from __future__ import annotations

from urllib.parse import parse_qs, urlparse

import httpx
import pytest

from tawked import (
    ApprovalRequiredError,
    GoneError,
    OAuthError,
    PermissionDeniedError,
    RateLimitError,
    apps,
)
from tawked._generated.types import AppConnection
from tests.generated.contract_data import OAUTH_ERRORS
from tests.support.mock import Mock

CLIENT_ID = "9c1d7e8a-0000-4000-8000-000000000001"
SECRET = "app-secret-for-the-mock"
REDIRECT = "https://app.example/tawked/callback"


def approve_in_browser(mock: Mock) -> tuple[str, apps.AuthorizeUrl]:
    started = apps.authorize_url(client_id=CLIENT_ID, redirect_uri=REDIRECT, base_url=mock.url)
    query = parse_qs(urlparse(started.url).query)
    assert query["response_type"] == ["code"] and query["code_challenge_method"] == ["S256"]
    assert "scope" not in query and query["state"] == [started.state]
    assert query["code_challenge"] == [apps.code_challenge(started.code_verifier)]
    back = httpx.get(started.url, follow_redirects=False)
    assert back.status_code == 302
    returned = parse_qs(urlparse(back.headers["location"]).query)
    assert returned["state"] == [started.state]
    return returned["code"][0], started


def exchange(mock: Mock, code: str, verifier: str, **kwargs: object) -> AppConnection:
    return apps.exchange_code(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        code=code,
        redirect_uri=REDIRECT,
        code_verifier=verifier,
        base_url=mock.url,
        **kwargs,  # type: ignore[arg-type]
    )


def test_authorize_then_exchange(mock: Mock) -> None:
    code, started = approve_in_browser(mock)
    connection = exchange(mock, code, started.code_verifier)
    assert isinstance(connection, AppConnection)
    assert connection.access_token.startswith("tk_live_") and connection.token_type == "Bearer"
    assert connection.application.id
    assert SECRET not in repr(started) and started.code_verifier not in repr(started)
    with pytest.raises(OAuthError) as info:
        exchange(mock, code, started.code_verifier)
    assert info.value.error == "invalid_grant" and info.value.status == 400


@pytest.mark.anyio
async def test_exchange_async(mock: Mock) -> None:
    code, started = approve_in_browser(mock)
    connection = await apps.exchange_code_async(
        client_id=CLIENT_ID,
        client_secret=SECRET,
        code=code,
        redirect_uri=REDIRECT,
        code_verifier=started.code_verifier,
        base_url=mock.url,
    )
    assert connection.access_token


@pytest.mark.parametrize("error", OAUTH_ERRORS, ids=[e["code"] for e in OAUTH_ERRORS])
def test_exchange_errors_are_oauth_errors(mock: Mock, error: dict[str, object]) -> None:
    http = httpx.Client(headers={"X-Mock-Error": str(error["code"]), "X-Test-Id": mock.test_id})
    with pytest.raises(OAuthError) as info:
        exchange(mock, "code-1", "v" * 43, http_client=http)
    assert info.value.error == error["code"] and info.value.status == error["status"]


def test_exchange_rate_limit_is_a_rate_limit_error(mock: Mock) -> None:
    http = httpx.Client(headers={"X-Mock-Error": "too_many_requests", "X-Test-Id": mock.test_id})
    with pytest.raises(RateLimitError) as info:
        exchange(mock, "code-1", "v" * 43, http_client=http)
    assert info.value.retry_after == 60.0
    assert len(mock.requests("/oauth/apps/token")) == 1
    mock.record("oauth", "apps.exchange_code", "after_429", {"requests": 1})


@pytest.mark.parametrize("fault", ["500", "read-timeout;delay=1500"])
def test_exchange_is_sent_once_after_sending(mock: Mock, fault: str) -> None:
    code, started = approve_in_browser(mock)
    http = httpx.Client(
        headers={"X-Mock-Fault": f"{fault};id={mock.test_id}", "X-Test-Id": mock.test_id}
    )
    with pytest.raises(Exception):  # noqa: B017 (OAuthError for the 500, APITimeoutError for the timeout)
        exchange(mock, code, started.code_verifier, http_client=http, timeout=0.4)
    rows = mock.requests("/oauth/apps/token")
    assert len(rows) == 1
    if fault == "500":
        mock.record(
            "oauth",
            "apps.exchange_code",
            "after_500",
            {"requests": len(rows), "key": False, "same_key": True},
        )


def test_exchange_sends_client_secret_basic(mock: Mock) -> None:
    code, started = approve_in_browser(mock)
    http = httpx.Client(headers={"X-Test-Id": mock.test_id})
    exchange(mock, code, started.code_verifier, http_client=http)
    row = mock.requests("/oauth/apps/token")[0]
    assert row["headers"]["authorization"].startswith("Basic ")
    assert row["headers"]["content-type"] == "application/x-www-form-urlencoded"
    assert SECRET not in row["body"]


def test_verifier_shape_is_checked() -> None:
    with pytest.raises(ValueError, match="RFC 7636"):
        apps.authorize_url(client_id=CLIENT_ID, redirect_uri=REDIRECT, code_verifier="short")


# ---------------------------------------------------------------------------------------- approvals


def consequential_call(client: object, **extra: object) -> object:
    return client.automations.automations.publish("app_1", "wf_1", **extra)  # type: ignore[attr-defined]


def test_wait_and_retry_after_some_pending_reads(mock: Mock) -> None:
    account = mock.account()
    with pytest.raises(ApprovalRequiredError) as info:
        consequential_call(account, extra_headers={"X-Mock-Approval": "approved;after=2"})
    result = account.approvals.wait_and_retry(info.value, poll_every=7)
    assert result.data is not None
    assert mock.sleeps == [7, 7]
    shows = [r for r in mock.requests() if r["path"].startswith("/v1/approvals/")]
    assert len(shows) == 3


def test_declined_raises_the_apis_own_code(mock: Mock) -> None:
    account = mock.account()
    with pytest.raises(ApprovalRequiredError) as info:
        consequential_call(account, extra_headers={"X-Mock-Approval": "declined"})
    with pytest.raises(PermissionDeniedError) as declined:
        account.approvals.wait_and_retry(info.value, poll_every=0)
    assert declined.value.code == "approval_declined"


def test_expired_raises_gone(mock: Mock) -> None:
    account = mock.account()
    with pytest.raises(ApprovalRequiredError) as info:
        consequential_call(account, extra_headers={"X-Mock-Approval": "expired"})
    with pytest.raises(GoneError) as expired:
        account.approvals.wait_and_retry(info.value, poll_every=0)
    assert expired.value.code == "approval_expired"


def test_still_pending_after_the_timeout_raises_the_428(mock: Mock) -> None:
    account = mock.account()
    with pytest.raises(ApprovalRequiredError) as info:
        consequential_call(account)
    with pytest.raises(ApprovalRequiredError):
        account.approvals.wait_and_retry(info.value, poll_every=0, timeout=0)


def test_a_428_is_never_retried_by_itself(mock: Mock) -> None:
    account = mock.account()
    with pytest.raises(ApprovalRequiredError):
        consequential_call(account)
    assert len([r for r in mock.requests() if not r["path"].startswith("/v1/approvals")]) == 1
