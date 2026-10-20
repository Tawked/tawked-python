"""Pages and iteration.

``list()`` answers one page as the wire has it, a :class:`Page`; ``iterate()`` walks every item,
following the style the endpoint uses: a cursor with ``has_more``, a cursor alone (null at the
end), or an offset with ``total``. It never sends more requests than needed: it stops on an empty
page and on a cursor that repeats.
"""

from __future__ import annotations

from collections.abc import AsyncIterator, Awaitable, Callable, Iterator, Mapping
from dataclasses import dataclass
from typing import Any, Generic, TypeVar

from tawked._models import ResponseMeta

__all__ = ["AccountPage", "Page", "Pagination", "async_iterate", "iterate"]

T = TypeVar("T")


@dataclass(frozen=True)
class Pagination:
    style: str
    items: str
    cursor_param: str | None = None
    next: str | None = None
    has_more: str | None = None
    limit_param: str | None = None
    max_limit: int | None = None
    offset_param: str | None = None
    total: str | None = None


class Page(Generic[T]):
    """One page of a list, as the API answered it.

    ``items`` are this page's items (also ``for item in page``); ``response`` is the whole typed
    answer; ``next_cursor``, ``has_more`` and ``total`` are the wire's own, ``None`` where the
    endpoint does not send them. ``iterate()`` on the same resource walks every page.
    """

    def __init__(
        self,
        items: list[T],
        *,
        response: Any = None,
        next_cursor: str | None = None,
        has_more: bool | None = None,
        total: int | None = None,
        meta: ResponseMeta | None = None,
    ) -> None:
        self.items = items
        self.response = response
        self.next_cursor = next_cursor
        self.has_more = has_more
        self.total = total
        self._meta = meta

    def __iter__(self) -> Iterator[T]:
        return iter(self.items)

    def __len__(self) -> int:
        return len(self.items)

    def __getitem__(self, index: int) -> T:
        return self.items[index]

    def __repr__(self) -> str:
        return f"{type(self).__name__}(items={len(self.items)}, next_cursor={self.next_cursor!r}, has_more={self.has_more!r}, total={self.total!r})"


class AccountPage(Page[Any]):
    """One page of an Account API list: ``data`` (the items, untyped JSON) and ``next_cursor``."""

    @property
    def data(self) -> list[Any]:
        return self.items


def _next_query(
    p: Pagination, page: Page[Any], query: dict[str, Any], seen: set[str]
) -> dict[str, Any] | None:
    if not page.items:
        return None
    if p.style == "offset":
        offset = int(query.get(p.offset_param or "offset") or 0) + len(page.items)
        if page.total is not None and offset >= page.total:
            return None
        return {**query, (p.offset_param or "offset"): offset}
    if p.has_more is not None and page.has_more is False:
        return None
    cursor = page.next_cursor
    if not cursor or cursor in seen:
        return None
    seen.add(cursor)
    return {**query, (p.cursor_param or "cursor"): cursor}


def iterate(
    p: Pagination, fetch: Callable[[dict[str, Any]], Page[T]], query: Mapping[str, Any]
) -> Iterator[T]:
    current: dict[str, Any] | None = dict(query)
    seen: set[str] = set()
    while current is not None:
        page = fetch(current)
        yield from page.items
        current = _next_query(p, page, current, seen)


async def async_iterate(
    p: Pagination, fetch: Callable[[dict[str, Any]], Awaitable[Page[T]]], query: Mapping[str, Any]
) -> AsyncIterator[T]:
    current: dict[str, Any] | None = dict(query)
    seen: set[str] = set()
    while current is not None:
        page = await fetch(current)
        for item in page.items:
            yield item
        current = _next_query(p, page, current, seen)
