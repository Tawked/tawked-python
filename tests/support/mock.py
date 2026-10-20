"""The test side of sdks/mock-server: clients pointed at it, its request log, faults."""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import httpx

from tawked import AsyncTawked, AsyncTawkedAccount, Tawked, TawkedAccount

APP_KEY = "tk_live_app_" + "A" * 28
PARTNER_KEY = "tk_partner_" + "B" * 32
ACCOUNT_TOKEN = "tk_acct_" + "C" * 24


class FlakyTransport(httpx.BaseTransport):
    """Fails the first ``failures`` sends before any byte leaves (a connect error)."""

    def __init__(self, failures: int = 1) -> None:
        self.failures = failures
        self.calls = 0
        self.inner = httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.calls += 1
        if self.calls <= self.failures:
            raise httpx.ConnectError("connection refused (test)", request=request)
        return self.inner.handle_request(request)

    def close(self) -> None:
        self.inner.close()


class Answer429Transport(httpx.BaseTransport):
    """Answers the first ``times`` sends with a 429 of ``code`` (and ``retry_after`` when given)
    without reaching the mock, then passes every send through to it."""

    def __init__(self, code: str, retry_after: str | None = None, times: int = 1) -> None:
        self.code = code
        self.retry_after = retry_after
        self.times = times
        self.calls = 0
        self.inner = httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        self.calls += 1
        if self.calls <= self.times:
            headers = {"retry-after": self.retry_after} if self.retry_after is not None else {}
            return httpx.Response(429, json={"error": self.code}, headers=headers, request=request)
        return self.inner.handle_request(request)

    def close(self) -> None:
        self.inner.close()


class AsyncFlakyTransport(httpx.AsyncBaseTransport):
    def __init__(self, failures: int = 1) -> None:
        self.failures = failures
        self.calls = 0
        self.inner = httpx.AsyncHTTPTransport()

    async def handle_async_request(self, request: httpx.Request) -> httpx.Response:
        self.calls += 1
        if self.calls <= self.failures:
            raise httpx.ConnectError("connection refused (test)", request=request)
        return await self.inner.handle_async_request(request)

    async def aclose(self) -> None:
        await self.inner.aclose()


class Mock:
    def __init__(self, url: str, *, test_id: str, behaviour: Path) -> None:
        self.url = url
        self.test_id = test_id
        self.behaviour = behaviour
        self.sleeps: list[float] = []

    # ------------------------------------------------------------------ clients

    def _headers(self) -> dict[str, str]:
        return {"X-Test-Id": self.test_id}

    def _fast(self, client: Any) -> Any:
        client._transport.sleep = self.sleeps.append
        return client

    def _afast(self, client: Any) -> Any:
        async def sleep(seconds: float) -> None:
            self.sleeps.append(seconds)

        client._transport.sleep = sleep
        return client

    def product(self, key: str = APP_KEY, **kwargs: Any) -> Tawked:
        return self._fast(
            Tawked(api_key=key, base_url=self.url, default_headers=self._headers(), **kwargs)
        )

    def aproduct(self, key: str = APP_KEY, **kwargs: Any) -> AsyncTawked:
        return self._afast(
            AsyncTawked(api_key=key, base_url=self.url, default_headers=self._headers(), **kwargs)
        )

    def account(self, **kwargs: Any) -> TawkedAccount:
        return self._fast(
            TawkedAccount(
                token=ACCOUNT_TOKEN, base_url=self.url, default_headers=self._headers(), **kwargs
            )
        )

    def aaccount(self, **kwargs: Any) -> AsyncTawkedAccount:
        return self._afast(
            AsyncTawkedAccount(
                token=ACCOUNT_TOKEN, base_url=self.url, default_headers=self._headers(), **kwargs
            )
        )

    # ------------------------------------------------------------------ the log

    def requests(self, path: str | None = None) -> list[dict[str, Any]]:
        rows = httpx.get(f"{self.url}/__mock/requests", timeout=10).json()["data"]
        mine = [r for r in rows if r["headers"].get("x-test-id") == self.test_id]
        return [r for r in mine if path is None or r["path"] == path]

    def record(self, surface: str, call: str, probe: str, value: Any) -> None:
        with self.behaviour.open("a", encoding="utf-8") as handle:
            handle.write(
                json.dumps(
                    {"surface": surface, "call": call, "probe": probe, "value": value},
                    sort_keys=True,
                )
                + "\n"
            )

    def fault(self, name: str, **options: Any) -> str:
        parts = [name, f"id={self.test_id}", *(f"{k}={v}" for k, v in options.items())]
        return ";".join(parts)
