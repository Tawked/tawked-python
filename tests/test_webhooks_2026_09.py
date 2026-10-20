"""Deliveries exactly as the API's webhook sender of version 2026-09 builds them.

User-Agent Tawked-Webhooks/2: the envelope ``{event, data}`` with ``sent_at`` (and ``"test": true``
on a test event), signed with ``tawked-signature`` alone. No ``tawked-webhook-id``, no Standard
Webhooks headers, no ``type``, ``timestamp`` or ``mode`` in the body. Every release must keep
accepting them.
"""

from __future__ import annotations

import json
from pathlib import Path
from typing import Any

import pytest

from tawked import webhooks
from tawked.webhooks import UnknownEvent

FIXTURE: dict[str, Any] = json.loads(
    (Path(__file__).resolve().parent / "fixtures" / "webhooks-2026-09.json").read_text("utf-8")
)
SECRET: str = FIXTURE["secret"]


@pytest.mark.parametrize(
    "delivery", FIXTURE["deliveries"], ids=[d["label"] for d in FIXTURE["deliveries"]]
)
def test_a_delivery_verifies_and_is_typed(delivery: dict[str, Any]) -> None:
    now = delivery["now_ms"] / 1000
    body: str = delivery["body"]
    headers: dict[str, str] = delivery["headers"]
    lowercase = {name.lower(): value for name, value in headers.items()}

    assert webhooks.verify(body, headers, SECRET, now=now)
    assert webhooks.verify(body.encode(), lowercase, ["a-new-secret", SECRET], now=now)

    event = webhooks.construct_event(body, lowercase, SECRET, now=now)
    sent = json.loads(body)
    assert not isinstance(event, UnknownEvent)
    assert event.event == delivery["event"]
    # Every field arrives (times parsed as datetimes), and the plain ones as sent.
    data = event.model_dump(by_alias=True, exclude_unset=True)["data"]
    assert set(data) == set(sent["data"])
    for key in ("id", "status", "application_id", "external_id", "reference", "to"):
        if key in sent["data"]:
            assert data[key] == sent["data"][key]
    assert bool(getattr(event, "test", False)) is delivery["test"]

    changed = body.replace('"data":{', '"data":{"x":1,', 1)
    assert not webhooks.verify(changed, lowercase, SECRET, now=now)
    assert not webhooks.verify(body, lowercase, "another-secret", now=now)
