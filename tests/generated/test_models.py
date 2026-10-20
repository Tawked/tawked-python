"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

# Every response model parses an unknown enum value and an extra field, and every
# aliased request field goes out under its wire name.

import pytest

from tawked._generated import types
from tawked._generated.account import _params as account_params
from tests.generated.contract_data import ALIASES, MODELS


@pytest.mark.parametrize("model", MODELS, ids=[m["name"] for m in MODELS])
def test_unknown_value_and_extra_field(model):
    cls = getattr(types, model["name"])
    sample = dict(model["sample"])
    sample["x_extra_field"] = {"kept": True}
    if model["enum_field"]:
        sample[model["enum_field"]] = "x_value_from_the_future"
    parsed = cls.model_validate(sample)
    assert parsed.x_extra_field == {"kept": True}
    assert parsed["x_extra_field"] == {"kept": True}
    if model["enum_field"]:
        assert parsed[model["enum_field"]] == "x_value_from_the_future"


@pytest.mark.parametrize("model", MODELS, ids=[m["name"] for m in MODELS])
def test_missing_required_fields_read_as_none(model, caplog):
    cls = getattr(types, model["name"])
    parsed = cls.model_validate({})
    for name in model["fields"]:
        assert parsed[name] is None
    if getattr(cls, "__tawked_required__", ()):
        assert any("read as None" in r.message for r in caplog.records)


@pytest.mark.parametrize("alias", ALIASES, ids=[f"{a['model']}.{a['py']}" for a in ALIASES])
def test_alias(alias):
    module = account_params if alias["module"] == "account" else types
    cls = getattr(module, alias["model"])
    assert cls.model_validate({alias["wire"]: "value"}).to_wire() == {alias["wire"]: "value"}
    name = next(n for n, f in cls.model_fields.items() if f.alias == alias["wire"])
    assert cls(**{name: "value"}).to_wire() == {alias["wire"]: "value"}
