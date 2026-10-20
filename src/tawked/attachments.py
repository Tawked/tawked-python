"""Files: an e-mail attachment for the wire, and an upload part for a multipart call.

``attachment()`` turns bytes, a path or a binary stream into ``{filename, content, content_type}``
(``content`` in base64) for ``email.messages.send(attachments=[...])``, refusing above the
contract's bound before anything is sent.
"""

from __future__ import annotations

import base64
import mimetypes
import os
from collections.abc import Sequence
from pathlib import Path
from typing import IO, Any

from tawked._generated.contract import EMAIL_ATTACHMENTS_MAX_BYTES, EMAIL_ATTACHMENTS_MAX_ITEMS

__all__ = ["FileInput", "attachment", "check_attachments", "file_part"]

#: bytes, a path (``str`` or ``os.PathLike``), a binary stream, or ``(filename, bytes or stream[, content_type])``.
FileInput = bytes | str | os.PathLike[str] | IO[bytes] | tuple[str, bytes] | tuple[str, bytes, str]


def _read(value: Any, fallback_name: str) -> tuple[str, bytes, str | None]:
    if isinstance(value, tuple):
        name = str(value[0])
        content = value[1].read() if hasattr(value[1], "read") else bytes(value[1])
        content_type = str(value[2]) if len(value) > 2 else None
        return name, content, content_type
    if isinstance(value, (bytes, bytearray, memoryview)):
        return fallback_name, bytes(value), None
    if isinstance(value, (str, os.PathLike)):
        path = Path(value)
        return path.name, path.read_bytes(), None
    if hasattr(value, "read"):
        content = value.read()
        if isinstance(content, str):
            raise TypeError("open the file in binary mode ('rb')")
        stream_name = getattr(value, "name", None)
        return (
            (Path(stream_name).name if isinstance(stream_name, str) else fallback_name),
            bytes(content),
            None,
        )
    raise TypeError(
        f"a file is bytes, a path, a binary stream or (filename, bytes): got {type(value).__name__}"
    )


def _guess(name: str, given: str | None) -> str:
    if given:
        return given
    guessed, _ = mimetypes.guess_type(name)
    return guessed or "application/octet-stream"


def attachment(
    file: FileInput,
    *,
    filename: str | None = None,
    content_type: str | None = None,
) -> dict[str, str]:
    """One e-mail attachment as the wire takes it: ``{filename, content, content_type}``."""
    name, content, found_type = _read(file, filename or "attachment")
    name = filename or name
    if len(content) > EMAIL_ATTACHMENTS_MAX_BYTES:
        raise ValueError(
            f"{name} is {len(content)} bytes; the attachments of one e-mail hold at most {EMAIL_ATTACHMENTS_MAX_BYTES} bytes"
        )
    return {
        "filename": name,
        "content": base64.b64encode(content).decode("ascii"),
        "content_type": _guess(name, content_type or found_type),
    }


def check_attachments(items: Sequence[Any]) -> None:
    """Refuse, before sending, more attachments or more bytes than the contract allows."""
    if len(items) > EMAIL_ATTACHMENTS_MAX_ITEMS:
        raise ValueError(f"an e-mail holds at most {EMAIL_ATTACHMENTS_MAX_ITEMS} attachments")
    total = 0
    for item in items:
        if isinstance(item, dict) and isinstance(item.get("content"), str):
            total += len(item["content"]) * 3 // 4
    if total > EMAIL_ATTACHMENTS_MAX_BYTES:
        raise ValueError(
            f"the attachments of one e-mail hold at most {EMAIL_ATTACHMENTS_MAX_BYTES} bytes"
        )


def file_part(value: Any, field: str) -> tuple[str, bytes, str]:
    """A multipart part ``(filename, bytes, content_type)`` for an upload field."""
    name, content, found_type = _read(value, field)
    return name, content, _guess(name, found_type)
