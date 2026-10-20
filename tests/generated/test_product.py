"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

# Every product endpoint of the contract against the mock: its first example request (item 1),
# every documented error (item 2), its retry class (item 3) and its pages (item 4).

import pytest

from tests.generated.contract_data import PRODUCT
from tests.support import runner

ERRORS = [(case, error) for case in PRODUCT for error in case["errors"]]
KEYED = [c for c in PRODUCT if runner.sends_key(c)]
PAGED = [c for c in PRODUCT if c["pagination"]]


def _id(case):
    return case["id"]


@pytest.mark.parametrize("case", PRODUCT, ids=_id)
def test_example(mock, case):
    runner.run_example(mock, case)


@pytest.mark.anyio
@pytest.mark.parametrize("case", PRODUCT, ids=_id)
async def test_example_async(mock, case):
    await runner.run_example_async(mock, case)


@pytest.mark.parametrize(
    ("case", "error"), ERRORS, ids=[f"{c['id']}-{e['code']}" for c, e in ERRORS]
)
def test_error(mock, case, error):
    runner.run_error(mock, case, error)


@pytest.mark.parametrize("case", PRODUCT, ids=_id)
def test_after_500(mock, case):
    runner.run_after_500(mock, case)


@pytest.mark.anyio
@pytest.mark.parametrize("case", PRODUCT, ids=_id)
async def test_after_500_async(mock, case):
    await runner.run_after_500_async(mock, case)


@pytest.mark.parametrize("case", PRODUCT, ids=_id)
def test_read_timeout(mock, case):
    runner.run_read_timeout(mock, case)


@pytest.mark.parametrize("case", PRODUCT, ids=_id)
def test_drop_after_sending(mock, case):
    runner.run_drop(mock, case)


@pytest.mark.parametrize("case", PRODUCT, ids=_id)
def test_pre_send(mock, case):
    runner.run_pre_send(mock, case)


@pytest.mark.anyio
@pytest.mark.parametrize("case", PRODUCT, ids=_id)
async def test_pre_send_async(mock, case):
    await runner.run_pre_send_async(mock, case)


@pytest.mark.parametrize("case", PRODUCT, ids=_id)
def test_429(mock, case):
    runner.run_429(mock, case)


@pytest.mark.parametrize("case", KEYED, ids=_id)
def test_in_progress(mock, case):
    runner.run_in_progress(mock, case)


@pytest.mark.parametrize("case", KEYED, ids=_id)
def test_in_progress_window(mock, case):
    runner.run_in_progress_window(mock, case)


@pytest.mark.parametrize("case", PAGED, ids=_id)
def test_pages(mock, case):
    runner.run_pages(mock, case)


@pytest.mark.anyio
@pytest.mark.parametrize("case", PAGED, ids=_id)
async def test_pages_async(mock, case):
    await runner.run_pages_async(mock, case)


def test_counts():
    print(f"product: {len(PRODUCT)} endpoints, {len(ERRORS)} documented errors")
    assert len(PRODUCT) > 0
