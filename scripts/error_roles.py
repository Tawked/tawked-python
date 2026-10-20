#!/usr/bin/env python3
"""Print ``code → role`` for every documented error code.

The role is the shared role table's column, read from the class the SDK raises for that code at its
documented status; the integrator compares this output across languages, byte for byte.
"""

from __future__ import annotations

from tawked._errors import error_class_for, role_of
from tawked._generated.contract import ERROR_STATUS

# role_of() answers a snake_case id; the printed role is the shared role table's own word, as php prints it.
TABLE_WORD = {"api": "API base", "oauth": "OAuth"}


def word(role: str) -> str:
    return TABLE_WORD.get(role, role.replace("_", " "))


def main() -> None:
    for code, status in sorted(ERROR_STATUS.items()):
        print(f"{code} → {word(role_of(error_class_for(code, status, ERROR_STATUS)))}")


if __name__ == "__main__":
    main()
