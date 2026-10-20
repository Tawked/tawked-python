"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

# Webhooks (item 5): every worked example of both schemes, the Standard Webhooks published vector,
# every verification case of the contract (cross-scheme, rotation, units), and every
# event typed by construct_event. OAuth (item 6): the PKCE worked example.

import json

import pytest

from tawked import webhooks
from tawked._generated import events
from tawked.oauth import code_challenge
from tests.generated.contract_data import (
    BOTH_HEADERS,
    EVENT_EXAMPLES,
    EVENTS,
    PKCE,
    WEBHOOK_CASES,
    WEBHOOK_SCHEMES,
)

TAWKED = next(s for s in WEBHOOK_SCHEMES if s["name"] == "tawked")
STANDARD = next(s for s in WEBHOOK_SCHEMES if s["name"] == "standard_webhooks")


@pytest.mark.parametrize(
    "example", TAWKED["worked_examples"], ids=[e["label"] for e in TAWKED["worked_examples"]]
)
def test_tawked_worked_example(example):
    assert (
        webhooks.sign(example["body"], example["secret"], example["timestamp"])
        == example["signature"]
    )
    headers = {"tawked-timestamp": example["timestamp"], "tawked-signature": example["signature"]}
    assert webhooks.verify(
        example["body"].encode(), headers, example["secret"], now=int(example["timestamp"]) / 1000
    )
    assert not webhooks.verify(
        example["body"] + " ", headers, example["secret"], now=int(example["timestamp"]) / 1000
    )


@pytest.mark.parametrize(
    "example", STANDARD["worked_examples"], ids=[e["label"] for e in STANDARD["worked_examples"]]
)
def test_standard_worked_example(example):
    signed = webhooks.sign(
        example["body"], example["secret"], example["timestamp"], id=example["id"]
    )
    assert signed == example["signature"]
    headers = {
        "webhook-id": example["id"],
        "webhook-timestamp": str(example["timestamp"]),
        "webhook-signature": signed,
    }
    assert webhooks.verify(example["body"], headers, example["secret"], now=example["timestamp"])
    assert not webhooks.verify(
        example["body"] + " ", headers, example["secret"], now=example["timestamp"]
    )


@pytest.mark.parametrize("case", WEBHOOK_CASES, ids=[c["label"] for c in WEBHOOK_CASES])
def test_verification_case(case):
    now = case["now_ms"] / 1000
    assert (
        webhooks.verify(case["body"].encode(), case["headers"], case["secrets"], now=now)
        is case["valid"]
    )
    if case["valid"]:
        webhooks.assert_valid(case["body"], case["headers"], case["secrets"], now=now)
    else:
        with pytest.raises(webhooks.WebhookVerificationError) as info:
            webhooks.assert_valid(case["body"], case["headers"], case["secrets"], now=now)
        assert info.value.reason == case["reason"]


# one real delivery carrying both header sets. The scheme is chosen by the secrets
# given, never by the headers present, and never falls back from one scheme to the other.
@pytest.mark.parametrize(
    "case", BOTH_HEADERS["cases"], ids=[c["label"] for c in BOTH_HEADERS["cases"]]
)
def test_both_header_sets(case):
    body, headers, now = BOTH_HEADERS["body"], BOTH_HEADERS["headers"], BOTH_HEADERS["now_seconds"]
    expected = case["expected"]
    assert webhooks.verify(body, headers, case["secrets"], now=now) is expected["valid"]
    assert (
        webhooks.verify(body, headers, case["secrets"], now=now, scheme=expected["scheme"])
        is expected["valid"]
    )
    # The chosen scheme alone decides: the other scheme's headers taken away, the answer does not change.
    if expected["scheme"] == "tawked":
        own = {k: v for k, v in headers.items() if not k.startswith("webhook-")}
    else:
        own = {k: v for k, v in headers.items() if k != "tawked-signature"}
    assert webhooks.verify(body, own, case["secrets"], now=now) is expected["valid"]
    if expected["valid"]:
        event = webhooks.construct_event(body, headers, case["secrets"], now=now)
        assert not isinstance(event, events.UnknownEvent) and event.event == "email.delivered"
    else:
        with pytest.raises(webhooks.WebhookVerificationError) as info:
            webhooks.assert_valid(body, headers, case["secrets"], now=now)
        assert info.value.reason == "signature_mismatch"


@pytest.mark.parametrize(
    "example", EVENT_EXAMPLES, ids=[f"{e['side']}-{e['body']['event']}" for e in EVENT_EXAMPLES]
)
def test_construct_event(example):
    body = json.dumps(example["body"], ensure_ascii=False)
    secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
    event = webhooks.construct_event(body, webhooks.test_headers(body, secret), secret)
    assert type(event) is events.EVENT_TYPES[example["body"]["event"]]
    assert event.event == example["body"]["event"]
    assert event.data is not None and not isinstance(event.data, dict)


def test_every_contract_event_has_a_class():
    assert {e["event"] for e in EVENTS} == set(events.EVENT_TYPES)


def test_unknown_event():
    # A name no contract has (email.opened became a typed event).
    body = json.dumps(
        {"event": "email.teleported", "data": {"id": "x"}, "sent_at": "1788265862201"}
    )
    secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
    event = webhooks.construct_event(body, webhooks.test_headers(body, secret), secret)
    assert isinstance(event, events.UnknownEvent)
    assert event.event == "email.teleported" and event.data == {"id": "x"}


def test_malformed_body():
    secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
    with pytest.raises(webhooks.WebhookVerificationError) as info:
        webhooks.construct_event("not json", webhooks.test_headers("not json", secret), secret)
    assert info.value.reason == "malformed_body"


def test_pkce_worked_example():
    assert code_challenge(PKCE["code_verifier"]) == PKCE["code_challenge"]
