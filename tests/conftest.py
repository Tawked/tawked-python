"""Fixtures: the API mock (sdks/mock-server, one per test worker) and clients pointed at it.

The mock lives beside this package (``../mock-server``) or at ``TAWKED_MOCK_SERVER``; it needs Node
18 or newer (``node`` on the PATH, or ``TAWKED_NODE``).
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
import uuid
from collections.abc import Iterator
from pathlib import Path
from typing import Any

import httpx
import pytest

from tests.support.mock import Mock

ROOT = Path(__file__).resolve().parent.parent
MOCK_DIR = Path(os.environ.get("TAWKED_MOCK_SERVER") or (ROOT.parent / "mock-server"))
BEHAVIOUR_DIR = ROOT / "build" / "behaviour"


def pytest_sessionstart(session: pytest.Session) -> None:
    if not hasattr(session.config, "workerinput"):
        shutil.rmtree(BEHAVIOUR_DIR, ignore_errors=True)
    BEHAVIOUR_DIR.mkdir(parents=True, exist_ok=True)


@pytest.fixture(scope="session")
def mock_url() -> Iterator[str]:
    node = os.environ.get("TAWKED_NODE") or shutil.which("node") or "node"
    script = MOCK_DIR / "bin" / "tawked-mock.mjs"
    if not script.exists():
        raise RuntimeError(
            f"the API mock is not at {MOCK_DIR}: check out sdks/mock-server beside this package or set TAWKED_MOCK_SERVER"
        )
    process = subprocess.Popen(
        [node, str(script), "--port", "0", "--host", "127.0.0.1"],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
    )
    assert process.stdout is not None
    line = process.stdout.readline()
    if "http://" not in line:
        process.kill()
        raise RuntimeError(
            f"the API mock did not start: {line}{process.stderr.read() if process.stderr else ''}"
        )
    url = line.split(" on ", 1)[1].split(" ", 1)[0]
    try:
        yield url
    finally:
        process.terminate()
        try:
            process.wait(timeout=5)
        except subprocess.TimeoutExpired:
            process.kill()


@pytest.fixture
def mock(mock_url: str, worker_id: str) -> Mock:
    httpx.post(f"{mock_url}/__mock/reset", timeout=10).raise_for_status()
    return Mock(mock_url, test_id=str(uuid.uuid4()), behaviour=BEHAVIOUR_DIR / f"{worker_id}.jsonl")


@pytest.fixture
def anyio_backend() -> str:
    return "asyncio"


def record_json(path: Path, row: dict[str, Any]) -> None:
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(row, sort_keys=True) + "\n")
