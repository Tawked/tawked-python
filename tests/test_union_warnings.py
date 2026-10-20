"""A response with a one-of field warns only about the variant it was read as.

Pydantic tries every variant of a union; a missing-field warning from each variant it did not keep
was noise on a correct answer (found by the local smoke run's ``chat.attendant.get``).
"""

from __future__ import annotations

import logging

import pytest

from tawked._generated.types import AttendantChoice


def test_a_complete_variant_logs_nothing(caplog: pytest.LogCaptureFixture) -> None:
    caplog.set_level(logging.WARNING, logger="tawked")
    choice = AttendantChoice.model_validate(
        {
            "id": "c1",
            "title": "الطلبات",
            "description": None,
            "action": {"type": "submenu", "text": "اختر", "choices": []},
        }
    )
    assert choice.action.type == "submenu"
    assert [r.getMessage() for r in caplog.records] == []


def test_a_missing_field_is_named_once_on_the_variant_kept(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level(logging.WARNING, logger="tawked")
    choice = AttendantChoice.model_validate(
        {"id": "c1", "title": "t", "description": None, "action": {"type": "reply", "text": "x"}}
    )
    assert choice.action.type == "reply"
    messages = [r.getMessage() for r in caplog.records]
    assert len(messages) == 1, messages
    assert "link" in messages[0]
    assert type(choice.action).__name__ in messages[0]


def test_the_tag_picks_the_variant_and_the_top_model_still_warns(
    caplog: pytest.LogCaptureFixture,
) -> None:
    caplog.set_level(logging.WARNING, logger="tawked")
    choice = AttendantChoice.model_validate({"id": "c1", "action": {"type": "radeef"}})
    # Read as the variant its tag names, not the first one that happens to parse.
    assert type(choice.action).__name__ == "AttendantChoiceActionVariant5"
    messages = [r.getMessage() for r in caplog.records]
    assert len(messages) == 1, messages
    assert "AttendantChoice answered without title, description" in messages[0]
