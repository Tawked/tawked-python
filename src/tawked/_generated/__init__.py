"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""

from __future__ import annotations

from collections.abc import Callable
from typing import TypeVar

F = TypeVar("F", bound=Callable[..., object])


def early_access(fn: F) -> F:
    """Marks a method of a product in early access (read by scripts/surface.py)."""
    fn.__tawked_stability__ = "early_access"  # type: ignore[attr-defined]
    return fn
