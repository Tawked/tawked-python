"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

# Every Account API operation against the mock: a request with its required fields (item 1), an
# error per documented status (item 2), its retry class (item 3), its pages (item 4) and, on a
# consequential write, the 428 loop (item 7).

import pytest

from tests.generated.contract_data import ACCOUNT
from tests.support import runner

ERRORS = [(case, error) for case in ACCOUNT for error in case["errors"]]
KEYED = [c for c in ACCOUNT if runner.sends_key(c) and not c["approval"]]
PAGED = [c for c in ACCOUNT if c["pagination"]]


def _id(case):
    return case["id"]


@pytest.mark.parametrize("case", runner.params(ACCOUNT))
def test_example(mock, case):
    runner.run_example(mock, case)


@pytest.mark.anyio
@pytest.mark.parametrize("case", runner.params(ACCOUNT))
async def test_example_async(mock, case):
    await runner.run_example_async(mock, case)


@pytest.mark.parametrize(
    ("case", "error"), ERRORS, ids=[f"{c['id']}-{e['status']}" for c, e in ERRORS]
)
def test_error(mock, case, error):
    runner.run_error(mock, case, error)


@pytest.mark.parametrize("case", runner.params(ACCOUNT))
def test_after_500(mock, case):
    runner.run_after_500(mock, case)


@pytest.mark.parametrize("case", runner.params(ACCOUNT))
def test_read_timeout(mock, case):
    runner.run_read_timeout(mock, case)


@pytest.mark.parametrize("case", runner.params(ACCOUNT))
def test_pre_send(mock, case):
    runner.run_pre_send(mock, case)


@pytest.mark.parametrize("case", runner.params(ACCOUNT))
def test_429(mock, case):
    runner.run_429(mock, case)


@pytest.mark.parametrize("case", runner.params(KEYED))
def test_in_progress(mock, case):
    runner.run_in_progress(mock, case)


@pytest.mark.parametrize("case", runner.params(PAGED))
def test_pages(mock, case):
    runner.run_pages(mock, case)


def test_counts():
    print(f"account: {len(ACCOUNT)} operations, {len(ERRORS)} documented statuses")
    assert len(ACCOUNT) > 0
