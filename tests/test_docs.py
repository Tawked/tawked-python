"""Every Python block of the README, python.mdx and account-api.mdx (docs/site-held/sdks) runs on the mock.

A block fenced ```python runs, in order, in one namespace per page; a block with a title after the
language (```python Django) is a framework snippet and is compiled, not run (its framework is not a
dependency of this package).
"""

from __future__ import annotations

import re
from pathlib import Path
from typing import Any

import pytest

import tawked._transport as transport
from tests.support.mock import ACCOUNT_TOKEN, APP_KEY, PARTNER_KEY, Mock

ROOT = Path(__file__).resolve().parent.parent
PAGES = [
    p
    for p in (
        ROOT / "README.md",
        ROOT.parent.parent / "docs" / "site-held" / "sdks" / "python.mdx",
        ROOT.parent.parent / "docs" / "site-held" / "sdks" / "account-api.mdx",
    )
    if p.exists()
]
FENCE = re.compile(r"^```python([^\n]*)\n(.*?)^```", re.M | re.S)


def blocks(page: Path) -> list[tuple[str, str]]:
    return [(info.strip(), body) for info, body in FENCE.findall(page.read_text(encoding="utf-8"))]


@pytest.mark.parametrize("page", PAGES, ids=[p.name for p in PAGES])
def test_page_blocks_run(page: Path, mock: Mock, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setenv("TAWKED_API_KEY", APP_KEY)
    monkeypatch.setenv("TAWKED_PARTNER_KEY", PARTNER_KEY)
    monkeypatch.setenv("CONNECTION_KEY", APP_KEY)  # the mock's connected-app key (tk_live_app_)
    monkeypatch.setenv("TAWKED_TOKEN", ACCOUNT_TOKEN)
    monkeypatch.setenv("TAWKED_BASE_URL", mock.url)
    monkeypatch.setenv("TAWKED_WEBHOOK_SECRET", "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx")
    monkeypatch.setenv("TAWKED_APP_SECRET", "app-secret-for-the-mock")
    original = transport._Decider.__init__

    def approved(self: Any, **kwargs: Any) -> None:
        # The mock keeps a consequential write pending unless asked otherwise; the pages show the
        # approved path. The sleeps are skipped.
        kwargs["default_headers"] = {
            **(kwargs.get("default_headers") or {}),
            "X-Mock-Approval": "approved",
        }
        original(self, **kwargs)

    monkeypatch.setattr(transport._Decider, "__init__", approved)
    monkeypatch.setattr(transport.time, "sleep", lambda s: None)
    namespace: dict[str, Any] = {"__name__": "docs", "code": "doc-code-1"}
    found = blocks(page)
    assert found, f"{page.name} has no python block"
    for info, body in found:
        compiled = compile(body, f"{page.name}:{info or 'block'}", "exec")
        if info:
            continue
        exec(compiled, namespace)  # the docs' own code, against the local mock
