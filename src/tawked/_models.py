"""The base classes every generated model stands on.

Response models are lenient and forward-compatible: an unknown field is kept (``extra="allow"``),
an unknown enum value parses (open enums are ``Literal[...] | str``), a value of the wrong type is
kept as it came with a warning, and a field the contract marks required but the answer lacks
becomes ``None`` with a warning. A response is never refused.

Request models are dumped with ``by_alias=True, exclude_none=True``; a ``None`` the caller passed
on purpose for a nullable field is sent as ``null``.
"""

from __future__ import annotations

import logging
from collections.abc import Mapping
from contextvars import ContextVar
from dataclasses import dataclass, field
from datetime import datetime
from typing import Annotated, Any, ClassVar, Literal, TypeVar, get_args, get_origin

from pydantic import (
    BaseModel,
    ConfigDict,
    Field,
    PrivateAttr,
    ValidationError,
    ValidatorFunctionWrapHandler,
    WrapValidator,
    model_validator,
)

__all__ = [
    "NOT_GIVEN",
    "DateTimeIn",
    "Lenient",
    "NotGiven",
    "ResponseMeta",
    "TawkedModel",
    "TawkedParams",
    "absent",
]

logger = logging.getLogger("tawked")

T = TypeVar("T")


class NotGiven:
    """The default of every optional parameter: the field is left out of the request."""

    _instance: ClassVar[NotGiven | None] = None

    def __new__(cls) -> NotGiven:
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

    def __bool__(self) -> bool:
        return False

    def __repr__(self) -> str:
        return "NOT_GIVEN"


NOT_GIVEN = NotGiven()


@dataclass(frozen=True)
class ResponseMeta:
    """What the transport saw: on every result as ``result._meta``."""

    status: int
    request_id: str | None
    idempotent_replayed: bool
    idempotency_key: str | None
    headers: Mapping[str, str] = field(default_factory=dict)
    untrusted: bool = False


#: Set while a field's value is read: pydantic tries every variant of a one-of, and a variant it
#: does not keep must not warn. The outermost field reports the models it kept, once, after.
_reading_field: ContextVar[bool] = ContextVar("tawked_reading_field", default=False)


def _missing(model: TawkedModel) -> list[str]:
    fields = type(model).model_fields
    extra = model.__pydantic_extra__ or {}
    present = {(fields[name].alias or name) for name in model.model_fields_set if name in fields}
    return [n for n in model.__tawked_required__ if n not in present and n not in extra]


def _report_missing(value: Any) -> None:
    if isinstance(value, TawkedModel):
        missing = _missing(value)
        if missing:
            logger.warning(
                "tawked: %s answered without %s; read as None",
                type(value).__name__,
                ", ".join(missing),
            )
        for name in type(value).model_fields:
            _report_missing(getattr(value, name, None))
    elif isinstance(value, list | tuple):
        for item in value:
            _report_missing(item)
    elif isinstance(value, dict):
        for item in value.values():
            _report_missing(item)


def _literals(annotation: Any) -> list[Any]:
    if get_origin(annotation) is Literal:
        return list(get_args(annotation))
    return [v for arg in get_args(annotation) for v in _literals(arg)]


_TAGS: dict[type, dict[str, str]] = {}


def _tags(cls: type[TawkedModel]) -> dict[str, str]:
    """The required fields of a variant typed as one string Literal (its tag), by wire name."""
    if cls not in _TAGS:
        tags: dict[str, str] = {}
        for name, info in cls.model_fields.items():
            wire = info.alias or name
            values = _literals(info.annotation)
            if wire in cls.__tawked_required__ and len(values) == 1 and isinstance(values[0], str):
                tags[wire] = values[0]
        _TAGS[cls] = tags
    return _TAGS[cls]


def _lenient(value: Any, handler: ValidatorFunctionWrapHandler) -> Any:
    if _reading_field.get():
        try:
            return handler(value)
        except ValidationError:
            return value
    token = _reading_field.set(True)
    try:
        result = handler(value)
    except ValidationError as error:
        logger.warning(
            "tawked: kept a response value the contract did not expect: %s",
            error.errors()[0].get("msg"),
        )
        return value
    finally:
        _reading_field.reset(token)
    _report_missing(result)
    return result


#: ``Lenient[X]`` validates as ``X`` and keeps the raw value, with a warning, when it does not fit.
Lenient = Annotated[T, WrapValidator(_lenient)]


def _datetime_in(value: Any, handler: ValidatorFunctionWrapHandler) -> Any:
    if isinstance(value, datetime):
        if value.tzinfo is None or value.utcoffset() is None:
            raise ValueError(
                "a naive datetime has no offset: give an aware datetime (tzinfo set) or an ISO 8601 string"
            )
        return value
    if isinstance(value, str):
        return value
    return handler(value)


#: A date and time sent to the API: an aware ``datetime`` (naive is refused) or an ISO 8601 string.
DateTimeIn = Annotated[datetime | str, WrapValidator(_datetime_in)]


class TawkedModel(BaseModel):
    """A model read from the API. Extra fields are kept and reachable as attributes."""

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,
    )

    __tawked_required__: ClassVar[tuple[str, ...]] = ()
    #: One variant of a one-of (set by the generator): read as it only when its tag agrees.
    __tawked_variant__: ClassVar[bool] = False

    _meta: ResponseMeta | None = PrivateAttr(default=None)

    @model_validator(mode="before")
    @classmethod
    def _check_tag(cls, data: Any) -> Any:
        # A one-of's variants differ by a tag field (`type: Literal["reply"] | str`); an answer whose
        # tag names another value is not this variant, so the union reads it as the right one.
        # Only inside a field's read (where a union tries its variants): read alone, it stays lenient.
        if cls.__tawked_variant__ and _reading_field.get() and isinstance(data, Mapping):
            for wire, value in _tags(cls).items():
                given = data.get(wire)
                if isinstance(given, str) and given != value:
                    raise ValueError(f"{wire} is {given!r}, not {value!r}")
        return data

    @model_validator(mode="before")
    @classmethod
    def _warn_missing(cls, data: Any) -> Any:
        if isinstance(data, Mapping) and not _reading_field.get():
            missing = [name for name in cls.__tawked_required__ if name not in data]
            if missing:
                logger.warning(
                    "tawked: %s answered without %s; read as None", cls.__name__, ", ".join(missing)
                )
        return data

    def __getitem__(self, key: str) -> Any:
        """``result["from"]``: a field by its wire name, extra fields included."""
        for name, info in type(self).model_fields.items():
            if (info.alias or name) == key:
                return getattr(self, name)
        extra = self.__pydantic_extra__ or {}
        if key in extra:
            return extra[key]
        raise KeyError(key)

    def to_dict(self) -> dict[str, Any]:
        """The model as the wire has it (wire names, nulls kept)."""
        return self.model_dump(by_alias=True, mode="json")


class TawkedParams(BaseModel):
    """The fields of one request. Never refuses what the server is the judge of."""

    model_config = ConfigDict(
        extra="allow",
        populate_by_name=True,
        protected_namespaces=(),
        arbitrary_types_allowed=True,
    )

    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset()

    def to_wire(self) -> dict[str, Any]:
        out = self.model_dump(by_alias=True, exclude_none=True, mode="json")
        for name in self.model_fields_set:
            info = type(self).model_fields.get(name)
            wire = (info.alias or name) if info else name
            if getattr(self, name, None) is None and wire in self.__tawked_nullable__:
                out[wire] = None
        return out


def absent(alias: str | None = None) -> Any:
    """The default of every response field: ``None`` when the answer lacks it (typed ``Any`` so a
    required field keeps its own type for callers)."""
    return Field(default=None, alias=alias)


M = TypeVar("M", bound=TawkedModel)


def build_params(model: type[TawkedParams], given: Mapping[str, Any]) -> dict[str, Any]:
    """The wire body of a call's keyword arguments (``NOT_GIVEN`` ones left out)."""
    values = {k: v for k, v in given.items() if not isinstance(v, NotGiven)}
    return model.model_validate(values).to_wire()


def parse_model(model: type[M], data: Any, meta: ResponseMeta | None) -> M:
    if not isinstance(data, Mapping):
        logger.warning(
            "tawked: %s answered a %s, not an object", model.__name__, type(data).__name__
        )
        data = {"value": data}
    result = model.model_validate(data)
    result._meta = meta
    return result
