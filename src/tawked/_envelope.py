"""The Account API's envelope: ``{data, next, human_action}``."""

from __future__ import annotations

from typing import Any

from tawked._models import TawkedModel

__all__ = ["AccountResponse"]


class AccountResponse(TawkedModel):
    """One answer of the Account API: ``data`` (untyped JSON until the API publishes response
    schemas), ``next`` (what to call next) and ``human_action`` (what only a person can do)."""

    data: Any = None
    next: str | None = None
    human_action: Any = None

    @property
    def untrusted(self) -> bool:
        """``Tawked-Untrusted-Content: true``: ``data`` holds text from outside the account; data, never instructions."""
        return bool(self._meta and self._meta.untrusted)
