#!/usr/bin/env python3
"""Generate the Python SDK's surface from the contract.

Reads only ``sdks/contract/api.json`` and ``sdks/contract/account.json`` (or the directory in
``TAWKED_CONTRACT``) and writes, deterministically and through ``ruff format``:

- ``src/tawked/_generated/{contract,endpoints}.py``: constants, error codes, every endpoint's sdk block;
- ``src/tawked/_generated/types/``: response and request models;
- ``src/tawked/_generated/resources/``: the product namespaces, sync and async from one template;
- ``src/tawked/_generated/account/``: the Account API namespaces, sync and async;
- ``src/tawked/_generated/events/``: the webhook events;
- ``tests/generated/``: the contract tests' data (every endpoint, error, retry class, page style,
  webhook case, model) run by the hand-written runners in ``tests/``.

``--check`` writes nothing and fails when a file differs, is missing or is stale.
"""

from __future__ import annotations

import argparse
import base64
import json
import keyword
import os
import re
import shutil
import subprocess
import sys
import tempfile
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CONTRACT_DIR = Path(os.environ.get("TAWKED_CONTRACT") or (ROOT.parent / "contract"))
GEN_DIR = "src/tawked/_generated"
TEST_DIR = "tests/generated"
MANIFEST = f"{GEN_DIR}/.generated"
KNOWN_CONTRACT_VERSIONS = {2}
HEADER = '"""Generated from sdks/contract/api.json and sdks/contract/account.json by scripts/generate.py; do not edit."""\n'
OPTION_NAMES = {"self", "idempotency_key", "timeout", "max_retries", "extra_headers"}
WORD_CASE = {"whatsapp": "WhatsApp", "oauth": "OAuth", "sms": "Sms", "api": "Api", "ai": "Ai"}
BASEMODEL_NAMES = {
    "copy", "dict", "json", "schema", "schema_json", "construct", "validate", "fields", "from_orm",
    "parse_obj", "parse_raw", "parse_file", "update_forward_refs", "to_dict", "to_wire", "register",
}  # fmt: skip


class ContractError(Exception):
    pass


# ---------------------------------------------------------------------------------------- names


def words_of(text: str) -> list[str]:
    return [w for w in re.split(r"[^A-Za-z0-9]+", text) if w]


def pascal(*parts: str) -> str:
    out = ""
    for part in parts:
        for word in words_of(part):
            out += WORD_CASE.get(word.lower(), word[:1].upper() + word[1:])
    return out


def camel(words: list[str]) -> str:
    flat = [p for w in words for p in w.split("_") if p]
    return flat[0] + "".join(p[:1].upper() + p[1:] for p in flat[1:])


def snake(words: list[str]) -> str:
    return "_".join(w for w in words if w)


def check_identifier(name: str, where: str) -> None:
    if name == "" or not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", name):
        raise ContractError(f"property `{name}` of `{where}` cannot be a parameter")


def py_param(wire: str, taken: set[str], aliases: dict[str, str], where: str) -> str:
    """The Python name of a wire field: the contract's alias, else the wire name with a ``_`` for
    a keyword or a name the method already uses (a path parameter, an option)."""
    if wire in aliases:
        name = aliases[wire]
    else:
        check_identifier(wire, where)
        name = wire
    while keyword.iskeyword(name) or name in taken or name in OPTION_NAMES:
        name += "_"
    check_identifier(name, where)
    return name


def py_field(wire: str, where: str) -> str:
    """A response model's attribute for a wire field (``from`` → ``from_``)."""
    if wire == "" or not re.match(r"^[A-Za-z_][A-Za-z0-9_]*$", wire):
        return ""  # kept as an extra field, reachable with result["…"]
    name = wire
    while (
        keyword.iskeyword(name)
        or name in BASEMODEL_NAMES
        or name.startswith("model_")
        or name.startswith("_")
    ):
        name = name.lstrip("_") + "_" if name.startswith("_") else name + "_"
    return name


def py_literal(value: Any) -> str:
    """A Python literal of a JSON value, for docstrings and the tests' data."""
    return repr(value)


# ---------------------------------------------------------------------------------------- types


@dataclass
class FieldDef:
    py: str
    wire: str
    annotation: str
    required: bool


@dataclass
class ClassDef:
    name: str
    base: str
    fields: list[FieldDef] = field(default_factory=list)
    doc: str = ""
    required: list[str] = field(default_factory=list)
    enum_fields: dict[str, list[Any]] = field(default_factory=dict)
    sample: dict[str, Any] = field(default_factory=dict)


class Types:
    """Response models: the contract's named types, each endpoint's answer, nested objects."""

    def __init__(self, named: dict[str, Any]) -> None:
        self.named = named
        self.classes: dict[str, ClassDef] = {}
        self.building: set[str] = set()
        self.rename: dict[str, str] = {}

    def ref(self, name: str) -> str:
        if name not in self.named:
            raise ContractError(f"unknown type {name}")
        if name not in self.classes and name not in self.building:
            self.object_class(name, self.named[name])
        return name

    def annotation(self, schema: Any, ctx: str) -> str:
        if not isinstance(schema, dict) or not schema:
            return "Any"
        if "$ref" in schema:
            return self.ref(schema["$ref"].split("/")[-1])
        for key in ("anyOf", "oneOf"):
            if key in schema:
                parts: list[str] = []
                for i, sub in enumerate(schema[key]):
                    ann = self.annotation(sub, f"{ctx}Variant{i + 1}")
                    for piece in split_union(ann):
                        if piece not in parts:
                            parts.append(piece)
                return join_union(parts)
        types = schema.get("type")
        type_list = types if isinstance(types, list) else ([types] if types else [])
        nullable = "null" in type_list
        type_list = [t for t in type_list if t != "null"]
        values = schema.get("enum", schema.get("known_values"))
        if "const" in schema:
            values = [schema["const"]]
        if values is not None:
            nullable = nullable or None in values
            literal = [v for v in values if v is not None]
            base = self.scalar(
                type_list[0]
                if type_list
                else ("string" if all(isinstance(v, str) for v in literal) else ""),
                schema,
                ctx,
            )
            ann = (
                f"Literal[{', '.join(py_literal(v) for v in literal)}] | {base}"
                if literal
                else base
            )
        elif not type_list:
            ann = "Any"
        elif len(type_list) > 1:
            ann = join_union([self.scalar(t, schema, ctx) for t in type_list])
        else:
            ann = self.scalar(type_list[0], schema, ctx)
        return f"{ann} | None" if nullable and ann != "Any" else ann

    def scalar(self, kind: str, schema: dict[str, Any], ctx: str) -> str:
        if kind == "string":
            return "datetime" if schema.get("format") == "date-time" else "str"
        if kind == "integer":
            return "int"
        if kind == "number":
            return "float"
        if kind == "boolean":
            return "bool"
        if kind == "array":
            return f"builtins.list[{self.annotation(schema.get('items', {}), ctx + 'Item')}]"
        if kind == "object":
            ctx = self.rename.get(ctx, ctx)
            if schema.get("properties"):
                if ctx not in self.classes and ctx not in self.building:
                    self.object_class(ctx, schema)
                return ctx
            extra = schema.get("additionalProperties")
            if isinstance(extra, dict) and extra:
                return f"builtins.dict[str, {self.annotation(extra, ctx + 'Value')}]"
            return "builtins.dict[str, Any]"
        return "Any"

    def object_class(
        self, name: str, schema: dict[str, Any], base: str = "TawkedModel", doc: str = ""
    ) -> ClassDef:
        self.building.add(name)
        variants = schema.get("anyOf") or schema.get("oneOf")
        props: dict[str, list[str]] = {}
        required: list[str] | None = None
        enums: dict[str, list[Any]] = {}
        samples: list[dict[str, Any]] = []
        for variant in variants or [schema]:
            resolved = self.resolve(variant)
            if variant is not schema and "$ref" in variant:
                self.ref(variant["$ref"].split("/")[-1])
            vprops = resolved.get("properties") or {}
            vreq = list(resolved.get("required") or [])
            required = vreq if required is None else [r for r in required if r in vreq]
            for prop, sub in vprops.items():
                ann = self.annotation(sub, name + pascal(prop))
                bucket = props.setdefault(prop, [])
                for piece in split_union(ann):
                    if piece not in bucket:
                        bucket.append(piece)
                values = sub.get("enum", sub.get("known_values")) if isinstance(sub, dict) else None
                if (
                    values
                    and all(isinstance(v, str) or v is None for v in values)
                    and prop not in enums
                ):
                    enums[prop] = values
            samples.append(sample_of(resolved, self.named))
        cls = ClassDef(name=name, base=base, doc=doc or (schema.get("description") or ""))
        for prop, pieces in props.items():
            attr = py_field(prop, name)
            if attr == "":
                continue
            cls.fields.append(
                FieldDef(
                    py=attr,
                    wire=prop,
                    annotation=join_union(pieces),
                    required=prop in (required or []),
                )
            )
        cls.required = list(required or [])
        cls.enum_fields = {k: v for k, v in enums.items() if py_field(k, name)}
        cls.sample = samples[0] if samples else {}
        self.building.discard(name)
        self.classes[name] = cls
        return cls

    def resolve(self, schema: dict[str, Any]) -> dict[str, Any]:
        while isinstance(schema, dict) and "$ref" in schema:
            schema = self.named[schema["$ref"].split("/")[-1]]
        return schema


def split_union(ann: str) -> list[str]:
    parts, depth, current = [], 0, ""
    for ch in ann:
        if ch in "[(":
            depth += 1
        elif ch in "])":
            depth -= 1
        if ch == "|" and depth == 0:
            parts.append(current.strip())
            current = ""
        else:
            current += ch
    if current.strip():
        parts.append(current.strip())
    return parts


def join_union(parts: list[str]) -> str:
    if "Any" in parts:
        return "Any"
    nulls = [p for p in parts if p == "None"]
    rest = [p for p in parts if p != "None"]
    return " | ".join(rest + nulls[:1]) if rest else "None"


def sample_of(schema: Any, named: dict[str, Any], depth: int = 0) -> Any:
    """A value that fits ``schema`` (the models' leniency test feeds it, then changes it)."""
    if not isinstance(schema, dict) or depth > 6:
        return None
    if "$ref" in schema:
        return sample_of(named[schema["$ref"].split("/")[-1]], named, depth + 1)
    for key in ("anyOf", "oneOf"):
        if key in schema:
            return sample_of(schema[key][0], named, depth + 1)
    if "const" in schema:
        return schema["const"]
    values = schema.get("enum")
    if values:
        return next((v for v in values if v is not None), None)
    types = schema.get("type")
    kind = next(
        (t for t in (types if isinstance(types, list) else [types]) if t and t != "null"), None
    )
    if kind == "object":
        return {
            k: sample_of(v, named, depth + 1) for k, v in (schema.get("properties") or {}).items()
        }
    if kind == "array":
        item = sample_of(schema.get("items", {}), named, depth + 1)
        return [item] if item is not None else []
    if kind == "string":
        fmt = schema.get("format")
        return (
            "2026-09-01T12:34:56.789Z"
            if fmt == "date-time"
            else ("c2a10f3e-8b7a-4d2e-9c1a-1a2b3c4d5e6f" if fmt == "uuid" else "x")
        )
    if kind == "integer":
        return int(schema.get("minimum", 1))
    if kind == "number":
        return 1.5
    if kind == "boolean":
        return True
    return None


def render_class(cls: ClassDef) -> str:
    lines = [f"class {cls.name}({cls.base}):"]
    doc = cls.doc.strip().replace("\\", "\\\\").replace('"""', "'''")
    lines.append(f'    """{doc}"""' if doc else f'    """The {cls.name} object."""')
    if cls.base == "TawkedModel" and cls.required:
        lines.append("")
        lines.append(
            f"    __tawked_required__: ClassVar[tuple[str, ...]] = {tuple(cls.required)!r}"
        )
    if cls.base == "TawkedModel" and re.search(r"Variant\d+$", cls.name):
        # One variant of a one-of: read as it only when its tag (a one-value Literal) agrees.
        lines.append("    __tawked_variant__: ClassVar[bool] = True")
    if cls.fields:
        lines.append("")
    for f in cls.fields:
        alias = repr(f.wire) if f.py != f.wire else ""
        ann = (
            f.annotation
            if f.required or "None" in split_union(f.annotation) or f.annotation == "Any"
            else f"{f.annotation} | None"
        )
        lines.append(f"    {f.py}: Lenient[{ann}] = absent({alias})")
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------------------------------- request fields


@dataclass
class Param:
    py: str
    wire: str
    annotation: str
    required: bool
    nullable: bool
    date: bool
    file: bool


def product_field_annotation(f: dict[str, Any]) -> tuple[str, bool]:
    kind = f.get("type")
    constraints = f.get("constraints") or {}
    also = list(f.get("also_accepts") or [])
    date = constraints.get("format") == "date-time" or f.get("format") == "date-time"
    enum = constraints.get("enum") or f.get("enum")
    if kind == "file":
        return "FileInput", False
    if kind == "string":
        base = "datetime | str" if date else "str"
        if enum:
            base = f"Literal[{', '.join(py_literal(v) for v in enum if v is not None)}] | str"
    elif kind == "integer":
        base = "int"
    elif kind == "number":
        base = "float"
    elif kind == "boolean":
        base = "bool"
    elif kind == "object":
        base = "Mapping[str, Any]"
    elif kind == "array":
        items = f.get("items")
        if items == "string":
            base = "Sequence[str]"
        elif items == "integer":
            base = "Sequence[int]"
        elif isinstance(items, (dict, list)) or f.get("item_fields"):
            base = "Sequence[Mapping[str, Any]]"
        else:
            base = "Sequence[Any]"
    elif kind == "string|object":
        base = "str | Mapping[str, Any]"
    else:
        base = "Any"
    if "string" in also and kind != "string":
        base = "str | " + base
    return base, date


def account_field_annotation(schema: dict[str, Any]) -> tuple[str, bool, bool]:
    types = schema.get("type")
    type_list = types if isinstance(types, list) else ([types] if types else [])
    nullable = "null" in type_list
    type_list = [t for t in type_list if t != "null"]
    if schema.get("format") == "binary":
        return "FileInput", nullable, False
    date = schema.get("format") == "date-time"
    enum = schema.get("enum")
    pieces: list[str] = []
    if enum:
        literal = [v for v in enum if v is not None]
        nullable = nullable or None in enum
        if all(isinstance(v, str) for v in literal):
            pieces.append(f"Literal[{', '.join(py_literal(v) for v in literal)}] | str")
        else:
            pieces.append("Any")
    for kind in type_list or ([] if enum else ["any"]):
        if enum and kind == "string":
            continue
        if kind == "string":
            pieces.append("datetime | str" if date else "str")
        elif kind == "integer":
            pieces.append("int")
        elif kind == "number":
            pieces.append("float")
        elif kind == "boolean":
            pieces.append("bool")
        elif kind == "array":
            items = schema.get("items") or {}
            inner = account_field_annotation(items)[0] if items else "Any"
            pieces.append(f"Sequence[{inner}]")
        elif kind == "object":
            pieces.append("Mapping[str, Any]")
        else:
            pieces.append("Any")
    ann = join_union([p for piece in pieces for p in split_union(piece)]) if pieces else "Any"
    return ann, nullable, date


# ---------------------------------------------------------------------------------------- methods


@dataclass
class Method:
    surface: str
    endpoint: dict[str, Any]
    const: str
    namespace: list[str]
    name: str
    path_params: list[tuple[str, str]]  # (py, wire)
    params: list[Param]
    params_class: str | None
    response_class: str | None
    item_class: str | None
    list_param: tuple[str, str] | None  # (py, wire)
    list_max: int | None
    files: tuple[str, ...]
    retry: str
    takes_key: bool
    stability: str
    pagination: dict[str, Any] | None
    binary: bool
    summary: str
    example: dict[str, Any] | None
    errors: list[dict[str, Any]]


def endpoint_const(surface: str, ident: str) -> str:
    return ("A_" if surface == "account" else "") + re.sub(r"[^A-Za-z0-9]+", "_", ident).upper()


def product_method(e: dict[str, Any], types: Types) -> Method:
    sdk = e["sdk"]
    taken: set[str] = set()
    path_params = []
    for p in sdk["path_params"]:
        py = p
        while keyword.iskeyword(py) or py in OPTION_NAMES:
            py += "_"
        path_params.append((py, p))
        taken.add(py)
    aliases = dict(sdk.get("param_aliases") or {})
    list_param = None
    list_max = None
    params: list[Param] = []
    files: list[str] = []
    for f in e["request"].get("fields", []):
        if f.get("in") not in ("body", "query", "multipart"):
            continue
        if f["name"] == sdk.get("list_param"):
            py = py_param(f["name"], taken, aliases, e["id"])
            taken.add(py)
            list_param = (py, f["name"])
            list_max = (f.get("constraints") or {}).get("max_items")
            continue
        ann, date = product_field_annotation(f)
        py = py_param(f["name"], taken, aliases, e["id"])
        taken.add(py)
        if f.get("type") == "file":
            files.append(f["name"])
        params.append(
            Param(
                py=py,
                wire=f["name"],
                annotation=ann,
                required=f.get("required") is True,
                nullable=bool(f.get("nullable")),
                date=date,
                file=f.get("type") == "file",
            )
        )
    params_class = sdk["type_base"] + "Params" if params else None
    response_class, item_class = product_response(e, types)
    return Method(
        surface="product",
        endpoint=e,
        const=endpoint_const("product", e["id"]),
        namespace=list(sdk["namespace"]),
        name=snake(sdk["method"]),
        path_params=path_params,
        params=params,
        params_class=params_class,
        response_class=response_class,
        item_class=item_class,
        list_param=list_param,
        list_max=list_max,
        files=tuple(files),
        retry=sdk["retry"],
        takes_key=sdk.get("idempotency") is not None,
        stability=sdk.get("stability", "stable"),
        pagination=sdk.get("pagination"),
        binary=(sdk.get("response") or {}).get("content") == "binary",
        summary=e.get("title") or e.get("summary") or "",
        example=sdk.get("example"),
        errors=e.get("errors", []),
    )


def product_response(e: dict[str, Any], types: Types) -> tuple[str | None, str | None]:
    sdk = e["sdk"]
    if (sdk.get("response") or {}).get("content") == "binary":
        return None, None
    name = sdk["type_base"] + "Response"
    schema = e["response"].get("schema") or {"type": "object"}
    doc = (e.get("title") or "") + ": the answer."
    item = None
    p = sdk.get("pagination")
    if p is not None:
        resolved = types.resolve(schema)
        items = (resolved.get("properties") or {}).get(p["items"], {}).get("items", {})
        if "$ref" in items:
            item = types.ref(items["$ref"].split("/")[-1])
        else:
            item = sdk["type_base"] + "Item"
            types.object_class(item, items, doc=f"One item of {e.get('title', '')}.")
            types.rename[name + pascal(p["items"]) + "Item"] = item
    if "$ref" in schema:
        parent = types.ref(schema["$ref"].split("/")[-1])
        types.classes[name] = ClassDef(
            name=name, base=parent, doc=doc, sample=sample_of(schema, types.named)
        )
    elif schema.get("type") == "object" or "anyOf" in schema or "oneOf" in schema:
        types.object_class(name, schema, doc=doc)
    else:
        types.object_class(name, {"type": "object", "properties": {}}, doc=doc)
    return name, item


def account_method(e: dict[str, Any]) -> Method:
    sdk = e["sdk"]
    taken: set[str] = set()
    path_params = []
    for p in sdk["path_params"]:
        py = p
        while keyword.iskeyword(py) or py in OPTION_NAMES:
            py += "_"
        path_params.append((py, p))
        taken.add(py)
    aliases = dict(sdk.get("param_aliases") or {})
    schema = e["request"].get("schema") or {}
    required = set(schema.get("required") or [])
    params: list[Param] = []
    for prop in sorted(
        (schema.get("properties") or {}).keys(), key=lambda k: (k not in required, k)
    ):
        sub = schema["properties"][prop]
        ann, nullable, date = account_field_annotation(sub if isinstance(sub, dict) else {})
        py = py_param(prop, taken, aliases, e["id"])
        taken.add(py)
        params.append(
            Param(
                py=py,
                wire=prop,
                annotation=ann,
                required=prop in required,
                nullable=nullable,
                date=date,
                file=ann == "FileInput",
            )
        )
    type_base = pascal(*e["id"].split("."))
    return Method(
        surface="account",
        endpoint=e,
        const=endpoint_const("account", e["id"]),
        namespace=list(sdk["namespace"]),
        name=snake(sdk["method"]),
        path_params=path_params,
        params=params,
        params_class=("Account" + type_base + "Params") if params else None,
        response_class=None,
        item_class=None,
        list_param=None,
        list_max=None,
        files=tuple(e["request"].get("files") or []),
        retry=sdk["retry"],
        takes_key=sdk.get("idempotency") is not None,
        stability="stable",
        pagination=sdk.get("pagination"),
        binary=(sdk.get("response") or {}).get("content") == "binary",
        summary=e.get("summary") or "",
        example=None,
        errors=[],
    )


def render_params_class(name: str, params: list[Param]) -> str:
    lines = [
        f"class {name}(TawkedParams):",
        '    """The fields of the request, by their wire names."""',
        "",
    ]
    nullable = sorted(p.wire for p in params if p.nullable)
    if nullable:
        lines.append(f"    __tawked_nullable__: ClassVar[frozenset[str]] = frozenset({nullable!r})")
    for p in params:
        name = p.py
        while name in BASEMODEL_NAMES or name.startswith("model_"):
            name += "_"
        alias = f", alias={p.wire!r}" if name != p.wire else ""
        ann = "DateTimeIn | None" if p.date else "Any"
        lines.append(f"    {name}: {ann} = Field(default=None{alias})")
    return "\n".join(lines) + "\n"


def docstring(m: Method, indent: str) -> str:
    text = " ".join((m.summary or "").split())
    e = m.endpoint
    lines = [text or f"{e['method']} {e['path']}"]
    lines.append("")
    lines.append(
        f"``{e['method']} {e['path']}``"
        + (f", scope ``{e['scope']}``" if e.get("scope") else "")
        + (f", permission ``{e['permission']}``" if e.get("permission") else "")
        + "."
    )
    retry_words = {
        "safe": "Retried on a network failure, a timeout, a 5xx and a 429.",
        "idempotent": "Retried with the same Idempotency-Key on a network failure, a timeout, a 5xx and a 429.",
        "write_once": "Never retried once sent: after a timeout, call again with the error's Idempotency-Key; after a 5xx Tawked released the key, so check whether it took effect before calling again.",
        "never": "Never retried once sent.",
    }
    lines.append(retry_words.get(m.retry, ""))
    if m.stability == "early_access":
        lines.append("Early access: the account must be granted Tawked Email first.")
    if m.endpoint.get("consequential"):
        lines.append("Consequential: answers 428 approval_required until a person approves it.")
    if m.errors:
        codes = sorted({str(x["error"]) for x in m.errors})
        lines.append("")
        lines.append("Errors: " + ", ".join(f"``{c}``" for c in codes) + ".")
    example = example_call(m)
    if example:
        lines.append("")
        lines.append("Example::")
        lines.append("")
        lines.append("    " + example)
    body = "\n".join((indent + line) if line else "" for line in lines)
    body = body.replace("\\", "\\\\").replace('"""', "'''")
    return f'{indent}"""{body.lstrip()}\n{indent}"""'


def call_path(m: Method) -> str:
    return ".".join([*m.namespace, m.name])


def example_args(m: Method) -> tuple[list[Any], dict[str, Any]] | None:
    ex = m.example
    if ex is None:
        return None
    args: list[Any] = [ex["path"].get(wire) for _, wire in m.path_params]
    kwargs: dict[str, Any] = {}
    by_wire = {p.wire: p.py for p in m.params}
    source: dict[str, Any] = {}
    source.update(ex.get("query") or {})
    if isinstance(ex.get("body"), dict):
        source.update(ex["body"])
    if m.list_param is not None:
        args.append(source.pop(m.list_param[1], []))
    for wire, value in (ex.get("multipart") or {}).items():
        if isinstance(value, dict) and "content_base64" in value:
            source[wire] = {"__file__": value}
        else:
            source[wire] = value
    for wire, value in source.items():
        kwargs[by_wire.get(wire, wire)] = value
    key = (ex.get("headers") or {}).get("Idempotency-Key")
    if key and m.takes_key:
        kwargs["idempotency_key"] = key
    return args, kwargs


def example_call(m: Method) -> str:
    found = example_args(m)
    if found is None:
        return ""
    args, kwargs = found
    parts = [py_literal(a) for a in args]
    for k, v in kwargs.items():
        if isinstance(v, dict) and "__file__" in v:
            parts.append(f"{k}=open({v['__file__']['filename']!r}, 'rb')")
        else:
            parts.append(f"{k}={py_literal(v)}")
    root = "tawked" if m.surface == "product" else "account"
    text = f"{root}.{call_path(m)}({', '.join(parts)})"
    return text if len(text) < 400 else f"{root}.{call_path(m)}(...)"


def render_method(m: Method, async_: bool, indent: str = "    ") -> str:
    adef = "async def" if async_ else "def"
    aw = "await " if async_ else ""
    sig = ["self"]
    for py, _wire in m.path_params:
        sig.append(f"{py}: str")
    if m.list_param is not None:
        sig.append(f"{m.list_param[0]}: Sequence[Mapping[str, Any] | TawkedParams]")
    kw = [p for p in m.params if p.required] + [p for p in m.params if not p.required]
    options = []
    if m.takes_key:
        options.append("idempotency_key: str | None = None")
    options += [
        "timeout: float | None = None",
        "max_retries: int | None = None",
        "extra_headers: Mapping[str, str] | None = None",
    ]
    sig.append("*")
    for p in kw:
        ann = p.annotation + (
            " | None" if p.nullable and "None" not in split_union(p.annotation) else ""
        )
        if p.required:
            sig.append(f"{p.py}: {ann}")
        else:
            pieces = split_union(ann)
            tail = " | None" if "None" in pieces else ""
            sig.append(
                f"{p.py}: {join_union([x for x in pieces if x != 'None'])} | NotGiven{tail} = NOT_GIVEN"
            )
    sig += options
    given = "{" + ", ".join(f"{p.wire!r}: {p.py}" for p in m.params) + "}"
    path = "{" + ", ".join(f"{wire!r}: {py}" for py, wire in m.path_params) + "}"
    opts = (
        "options("
        + ("idempotency_key, " if m.takes_key else "None, ")
        + "timeout, max_retries, extra_headers)"
    )
    common = f"path={path}, given={given}, params={m.params_class or 'None'}, opts={opts}"
    if m.files:
        common += f", files={m.files!r}"
    if m.list_param is not None:
        common += f", list_param=({m.list_param[1]!r}, {m.list_param[0]})"
    pre = ""
    if m.list_param is not None and m.list_max:
        pre = f"{indent}    if len({m.list_param[0]}) > {m.list_max}:\n{indent}        raise ValueError({f'{m.list_param[1]} holds at most {m.list_max} items'!r})\n"
    if m.surface == "product":
        if m.binary:
            ret, call = "bytes", f"{aw}self._client._call_binary(_E.{m.const}, {common})"
        elif m.pagination is not None:
            ret = f"Page[{m.item_class}]"
            call = f"{aw}self._client._list(_E.{m.const}, {m.response_class}, {m.item_class}, _PAGE_{m.const}, {common})"
        else:
            ret, call = (
                m.response_class or "TawkedModel",
                f"{aw}self._client._call(_E.{m.const}, {m.response_class}, {common})",
            )
    else:
        if m.pagination is not None:
            ret, call = "AccountPage", f"{aw}self._client._account_list(_E.{m.const}, {common})"
        else:
            ret, call = "AccountResponse", f"{aw}self._client._account_call(_E.{m.const}, {common})"
    deco = f"{indent}@early_access\n" if m.stability == "early_access" else ""
    out = (
        f"{deco}{indent}{adef} {m.name}(\n{indent}    "
        + f",\n{indent}    ".join(sig)
        + f",\n{indent}) -> {ret}:\n"
    )
    out += docstring(m, indent + "    ") + "\n"
    out += pre
    out += f"{indent}    return {call}\n"
    if m.pagination is not None:
        it_name = "iterate" if m.name == "list" else f"iterate_{m.name}"
        item = m.item_class if m.surface == "product" else "Any"
        it_ret = f"AsyncIterator[{item}]" if async_ else f"Iterator[{item}]"
        it_sig = [s for s in sig]
        out += (
            "\n"
            + f"{deco}{indent}def {it_name}(\n{indent}    "
            + f",\n{indent}    ".join(it_sig)
            + f",\n{indent}) -> {it_ret}:\n"
        )
        out += f'{indent}    """Every item of :meth:`{m.name}`, page after page ({m.pagination["style"]}); the same filters."""\n'
        if m.surface == "product":
            out += f"{indent}    return self._client._iterate(_E.{m.const}, {m.response_class}, {m.item_class}, _PAGE_{m.const}, path={path}, given={given}, params={m.params_class or 'None'}, opts={opts})\n"
        else:
            out += (
                f"{indent}    return self._client._account_iterate(_E.{m.const}, _PAGE_{m.const}, path={path}, given={given}, params={m.params_class or 'None'}, opts={opts}"
                + (f", files={m.files!r}" if m.files else "")
                + ")\n"
            )
    return out


# ---------------------------------------------------------------------------------------- namespaces


@dataclass
class Node:
    path: list[str]
    methods: list[Method] = field(default_factory=list)
    children: dict[str, Node] = field(default_factory=dict)


def tree(methods: list[Method]) -> Node:
    root = Node([])
    for m in methods:
        node = root
        for i, seg in enumerate(m.namespace):
            node = node.children.setdefault(seg, Node(m.namespace[: i + 1]))
        node.methods.append(m)
    check_tree(root)
    return root


def check_tree(node: Node) -> None:
    names = [m.name for m in node.methods]
    iter_names = [
        "iterate" if m.name == "list" else f"iterate_{m.name}"
        for m in node.methods
        if m.pagination is not None
    ]
    all_names = names + iter_names + list(node.children)
    for name in all_names:
        if all_names.count(name) > 1:
            raise ContractError(f"`{'.'.join([*node.path, name])}` is two things at once")
        if keyword.iskeyword(name):
            raise ContractError(f"`{'.'.join([*node.path, name])}` is a Python keyword")
    for child in node.children.values():
        check_tree(child)


def class_name(prefix: str, path: list[str], async_: bool) -> str:
    return ("Async" if async_ else "") + prefix + pascal(*path)


def render_namespace(node: Node, prefix: str, async_: bool, client_type: str) -> str:
    """One namespace class and, before it, its children (sync or async, one template)."""
    out = ""
    for child in node.children.values():
        out += render_namespace(child, prefix, async_, client_type)
    name = class_name(prefix, node.path, async_)
    lines = [
        f"class {name}:",
        f'    """``{".".join(node.path)}``."""',
        "",
        "    _client: " + client_type,
        "",
    ]
    lines.append(f"    def __init__(self, client: {client_type}) -> None:")
    lines.append("        self._client = client")
    for seg, child in node.children.items():
        lines.append(f"        self.{seg} = {class_name(prefix, child.path, async_)}(client)")
    out += "\n".join(lines) + "\n"
    for m in node.methods:
        out += "\n" + render_method(m, async_)
    return out + "\n\n"


# ---------------------------------------------------------------------------------------- the generator


class Generator:
    def __init__(self, contract_dir: Path) -> None:
        self.api = json.loads((contract_dir / "api.json").read_text(encoding="utf-8"))
        self.account = json.loads((contract_dir / "account.json").read_text(encoding="utf-8"))
        # The both-headers vector: one delivery carrying both header sets, beside the contract.
        self.both_headers = json.loads(
            (contract_dir / "vectors" / "both-headers.json").read_text(encoding="utf-8")
        )
        for name, doc in (("api.json", self.api), ("account.json", self.account)):
            if doc.get("contract_version") not in KNOWN_CONTRACT_VERSIONS:
                raise ContractError(
                    f"{name} has contract_version {doc.get('contract_version')!r}; this generator knows {sorted(KNOWN_CONTRACT_VERSIONS)}"
                )
        self.files: dict[str, str] = {}
        self.types = Types(self.api["types"])
        self.product = [product_method(e, self.types) for e in self.api["endpoints"]]
        self.account_methods = [account_method(e) for e in self.account["endpoints"]]
        self.oauth = {e["id"]: e for e in self.api["oauth"]["endpoints"]}
        token = self.oauth["oauth-token"]
        self.types.object_class(
            "AppConnection",
            token["response"]["schema"],
            doc="The connection a merchant approved: its key (``access_token``, shown once), its application and permissions.",
        )
        self.error_status = self.documented_errors()

    def documented_errors(self) -> dict[str, int]:
        out: dict[str, int] = {}
        for err in self.api["errors"]:
            out.setdefault(err["error"], err["http"])
        return dict(sorted(out.items()))

    def write(self, rel: str, text: str) -> None:
        self.files[rel] = text

    # -------------------------------------------------------------- contract and endpoints

    def contract_module(self) -> None:
        api = self.api
        prefixes = dict(api["auth"]["key_prefixes"])
        prefixes["account"] = self.account["auth"]["token_prefix"]
        email_send = next(e for e in api["endpoints"] if e["id"] == "email-send")
        attachments = next(f for f in email_send["request"]["fields"] if f["name"] == "attachments")
        constraints = attachments.get("constraints") or {}
        codes = list(self.error_status)
        account_codes = re.findall(
            r"[a-z]+(?:_[a-z]+)+|[a-z]+",
            self.account["account_error_envelope"]["Error"]["properties"]["error"]["description"]
            .split(":", 1)[1]
            .split(", or")[0],
        )
        text = (
            HEADER
            + "\nfrom __future__ import annotations\n\nfrom typing import Any, Final, Literal\n\n"
        )
        text += f"API_VERSION: Final = {api['api_version']!r}\n"
        text += f"BASE_URL: Final = {api['base_url']!r}\n"
        text += f"KEY_PREFIXES: Final[dict[str, str]] = {prefixes!r}\n"
        text += f"SANDBOX_NOTES: Final[tuple[str, ...]] = {tuple(api['sandbox']['notes'])!r}\n"
        text += f"SANDBOX_SEND_CAP: Final = {api['sandbox'].get('send_cap')!r}\n"
        text += f"EMAIL_ATTACHMENTS_MAX_BYTES: Final = {int(constraints.get('max_total_decoded_bytes', 10485760))!r}\n"
        text += f"EMAIL_ATTACHMENTS_MAX_ITEMS: Final = {int(constraints.get('max_items', 10))!r}\n"
        text += f"HEADERS_POLICY: Final[dict[str, Any]] = {api['headers_policy']!r}\n"
        # The simulator addresses (sandbox.email.simulators): each {address, outcome, events}.
        text += f"EMAIL_SIMULATORS: Final[tuple[dict[str, Any], ...]] = {tuple((api['sandbox'].get('email') or {}).get('simulators') or ())!r}\n"
        text += f"OAUTH_ERRORS: Final[tuple[str, ...]] = {tuple(sorted(e['error'] for e in self.oauth['oauth-token']['errors']))!r}\n"
        text += f"ERROR_STATUS: Final[dict[str, int]] = {self.error_status!r}\n"
        text += f"ACCOUNT_ERROR_CODES: Final[tuple[str, ...]] = {tuple(account_codes)!r}\n"
        text += "\n#: Every documented error code of the product API; branch on ``error.code``.\n"
        text += f"ErrorCode = Literal[{', '.join(repr(c) for c in codes)}]\n"
        self.write(f"{GEN_DIR}/contract.py", text)
        consts = (
            HEADER.replace(
                '; do not edit."""',
                '; do not edit.\n\nEvery error code as a constant: ``tawked.error_codes.INSUFFICIENT_CREDITS``.\n"""',
            )
            + "\nfrom typing import Final\n\n"
        )
        for code in sorted(set(codes) | set(account_codes)):
            consts += f"{code.upper()}: Final = {code!r}\n"
        self.write(f"{GEN_DIR}/error_codes.py", consts)

    def endpoints_module(self) -> None:
        text = (
            HEADER
            + "\nfrom __future__ import annotations\n\nfrom tawked._pagination import Pagination\nfrom tawked._transport import Endpoint\n\n"
        )
        idem = self.api["idempotency"]
        default_max = int(idem["format"]["max_length"])
        for m in self.product:
            sdk = m.endpoint["sdk"]
            model = sdk.get("idempotency")
            key_max = (
                int(((idem.get(model) or {}).get("format") or {}).get("max_length", default_max))
                if model
                else default_max
            )
            documented = {str(x["error"]): int(x["http"]) for x in m.errors}
            text += (
                f"{m.const} = Endpoint(id={m.endpoint['id']!r}, surface='product', method={m.endpoint['method']!r}, path={m.endpoint['path']!r}, "
                f"retry={m.retry!r}, idempotency={model!r}, key_max={key_max}, timeout_s={float(sdk['timeout_s'])!r}, secret={bool(sdk['secret'])!r}, "
                f"body={sdk['body']!r}, params_in={sdk['params_in']!r}, response={(sdk.get('response') or {}).get('content', 'json')!r}, documented={documented!r})\n"
            )
        acc_max = int(self.account["idempotency"]["account_writes"]["format"]["max_length"])
        for m in self.account_methods:
            sdk = m.endpoint["sdk"]
            text += (
                f"{m.const} = Endpoint(id={m.endpoint['id']!r}, surface='account', method={m.endpoint['method']!r}, path={m.endpoint['path']!r}, "
                f"retry={m.retry!r}, idempotency={sdk.get('idempotency')!r}, key_max={acc_max}, timeout_s={float(sdk['timeout_s'])!r}, secret={bool(sdk['secret'])!r}, "
                f"body={m.endpoint['request']['body']!r}, params_in={m.endpoint['request']['in']!r}, response={(sdk.get('response') or {}).get('content', 'json')!r}, "
                f"approval={bool(sdk.get('approval'))!r})\n"
            )
        token = self.oauth["oauth-token"]
        documented = {str(x["error"]): int(x["http"]) for x in token["errors"]}
        tsdk = token["sdk"]
        text += (
            f"OAUTH_TOKEN = Endpoint(id='oauth-token', surface='oauth', method={token['method']!r}, path={token['path']!r}, retry={tsdk['retry']!r}, "
            f"timeout_s={float(tsdk['timeout_s'])!r}, secret={bool(tsdk['secret'])!r}, body={tsdk['body']!r}, documented={documented!r})\n"
        )
        text += "\n"
        for m in [*self.product, *self.account_methods]:
            p = m.pagination
            if p is None:
                continue
            args = ", ".join(
                f"{k}={p.get(k)!r}"
                for k in (
                    "style",
                    "items",
                    "cursor_param",
                    "next",
                    "has_more",
                    "limit_param",
                    "max_limit",
                    "offset_param",
                    "total",
                )
                if p.get(k) is not None
            )
            text += f"_PAGE_{m.const} = Pagination({args})\n"
        self.write(f"{GEN_DIR}/endpoints.py", text)

    # -------------------------------------------------------------- types

    def types_module(self) -> None:
        text = HEADER + (
            "\nfrom __future__ import annotations\n\nimport builtins\nfrom datetime import datetime\nfrom typing import Any, ClassVar, Literal\n\n"
            "from pydantic import Field\n\nfrom tawked._models import DateTimeIn, Lenient, TawkedModel, TawkedParams, absent\n\n"
            "__all__ = [\n"
        )
        params = [(m.params_class, m.params) for m in [*self.product] if m.params_class]
        names = sorted([*self.types.classes, *(n for n, _ in params)])
        text += (
            "".join(f"    {n!r},\n" for n in names)
            + "]\n\n_ = (builtins, datetime, Any, ClassVar, Literal, DateTimeIn)\n\n\n"
        )
        for cls in self.types.classes.values():
            text += render_class(cls) + "\n\n"
        for name, ps in params:
            text += render_params_class(name or "", ps) + "\n\n"
        text += (
            "for _model in (" + ", ".join(self.types.classes) + "):\n    _model.model_rebuild()\n"
        )
        self.write(f"{GEN_DIR}/types/__init__.py", text)

    # -------------------------------------------------------------- resources

    def product_resources(self) -> None:
        root = tree(self.product)
        modules = []
        for seg, node in root.children.items():
            ms = collect(node)
            types = sorted(
                {x for m in ms for x in (m.response_class, m.item_class, m.params_class) if x}
            )
            text = HEADER + (
                "\nfrom __future__ import annotations\n\nimport builtins\nfrom collections.abc import AsyncIterator, Iterator, Mapping, Sequence\nfrom datetime import datetime\n"
                "from typing import TYPE_CHECKING, Any, Literal\n\nfrom tawked import _generated as _g\nfrom tawked._transport import options\n"
                "from tawked._generated import endpoints as _E\nfrom tawked._generated.endpoints import "
                + ", ".join(sorted(f"_PAGE_{m.const}" for m in ms if m.pagination))
                + "\n"
                "from tawked._generated.types import "
                + ", ".join(types)
                + "\nfrom tawked._models import NOT_GIVEN, NotGiven, TawkedModel, TawkedParams\n"
                "from tawked._pagination import Page\nfrom tawked.attachments import FileInput\n\n"
                "if TYPE_CHECKING:\n    from tawked._client import AsyncTawked, Tawked\n\n"
                "_ = (builtins, AsyncIterator, Iterator, Mapping, Sequence, datetime, Any, Literal, NOT_GIVEN, NotGiven, TawkedModel, TawkedParams, Page, FileInput, _g)\n"
                "early_access = _g.early_access\n\n\n"
            ).replace("from tawked._generated.endpoints import \n", "")
            text += render_namespace(node, "", False, "Tawked")
            text += render_namespace(node, "", True, "AsyncTawked")
            self.write(f"{GEN_DIR}/resources/{seg}.py", text)
            modules.append((seg, node))
        self.write(
            f"{GEN_DIR}/resources/__init__.py",
            namespaces_module(modules, "", "ProductNamespaces", "resources", "the product API"),
        )

    def account_resources(self) -> None:
        root = tree(self.account_methods)
        modules = []
        for seg, node in root.children.items():
            ms = collect(node)
            text = HEADER + (
                "\nfrom __future__ import annotations\n\nfrom collections.abc import AsyncIterator, Iterator, Mapping, Sequence\nfrom datetime import datetime\n"
                "from typing import TYPE_CHECKING, Any, Literal\n\nfrom tawked._transport import options\nfrom tawked._envelope import AccountResponse\n"
                "from tawked._generated import endpoints as _E\n"
                + (
                    "from tawked._generated.endpoints import "
                    + ", ".join(sorted(f"_PAGE_{m.const}" for m in ms if m.pagination))
                    + "\n"
                    if any(m.pagination for m in ms)
                    else ""
                )
                + (
                    "from tawked._generated.account._params import "
                    + ", ".join(sorted(m.params_class for m in ms if m.params_class))
                    + "\n"
                    if any(m.params_class for m in ms)
                    else ""
                )
                + "from tawked._models import NOT_GIVEN, NotGiven, TawkedParams\nfrom tawked._pagination import AccountPage\nfrom tawked.attachments import FileInput\n\n"
                "if TYPE_CHECKING:\n    from tawked.account import AsyncTawkedAccount, TawkedAccount\n\n"
                "_ = (AsyncIterator, Iterator, Mapping, Sequence, datetime, Any, Literal, NOT_GIVEN, NotGiven, TawkedParams, AccountPage, AccountResponse, FileInput)\n\n\n"
            )
            text += render_namespace(node, "Account", False, "TawkedAccount")
            text += render_namespace(node, "Account", True, "AsyncTawkedAccount")
            # the approvals namespace's classes are subclassed by tawked.account (wait_and_retry)
            if seg == "approvals":
                text += "Approvals = AccountApprovals\nAsyncApprovals = AsyncAccountApprovals\n"
            self.write(f"{GEN_DIR}/account/{seg}.py", text)
            modules.append((seg, node))
        params = HEADER + (
            "\nfrom __future__ import annotations\n\nfrom typing import Any, ClassVar\n\nfrom pydantic import Field\n\nfrom tawked._models import DateTimeIn, TawkedParams\n\n_ = (Any, ClassVar, DateTimeIn)\n\n\n"
        )
        for m in self.account_methods:
            if m.params_class:
                params += render_params_class(m.params_class, m.params) + "\n\n"
        self.write(f"{GEN_DIR}/account/_params.py", params)
        self.write(
            f"{GEN_DIR}/account/__init__.py",
            namespaces_module(
                modules, "Account", "AccountNamespaces", "account", "the Account API"
            ),
        )

    # -------------------------------------------------------------- events

    def events_module(self) -> None:
        hooks = self.api["webhooks"]
        app = hooks["application"]
        partner = hooks["partner"]["events"]
        names = sorted(set(app["events"]) | set(partner))
        text = HEADER + (
            "\nfrom __future__ import annotations\n\nimport builtins\nfrom datetime import datetime\nfrom typing import Any, ClassVar, Literal\n\n"
            "from pydantic import Field\n\nfrom tawked._generated.types import @@TYPES@@\n"
            "from tawked._models import Lenient, TawkedModel, absent\n\n_ = (builtins, datetime, Any, ClassVar, Literal)\n\n\n"
        )
        local = Types(self.api["types"])
        local.classes = {}
        events: list[tuple[str, str]] = []
        for event in names:
            data_types: list[str] = []
            if event in app.get("event_data", {}):
                data_types += split_union(
                    local.annotation(app["event_data"][event]["data"], pascal(event) + "Data")
                )
            if event in partner:
                ann = local.annotation(
                    partner[event]["data"],
                    pascal(event) + "PartnerData"
                    if event in app.get("event_data", {})
                    else pascal(event) + "Data",
                )
                data_types += [p for p in split_union(ann) if p not in data_types]
            cls = pascal(event) + "Event"
            events.append((event, cls))
        for name, cls in local.classes.items():
            if name in self.types.classes:
                continue
            text += render_class(cls) + "\n\n"
        for event, cls in events:
            data_types = []
            if event in app.get("event_data", {}):
                data_types += split_union(
                    local.annotation(app["event_data"][event]["data"], pascal(event) + "Data")
                )
            if event in partner:
                ann = local.annotation(
                    partner[event]["data"],
                    pascal(event) + "PartnerData"
                    if event in app.get("event_data", {})
                    else pascal(event) + "Data",
                )
                data_types += [p for p in split_union(ann) if p not in data_types]
            text += (
                f"class {cls}(TawkedModel):\n    \"\"\"``{event}``.\"\"\"\n\n    __tawked_required__: ClassVar[tuple[str, ...]] = ('event', 'data', 'sent_at')\n\n"
                f"    event: Literal[{event!r}] = Field(default={event!r})\n    data: Lenient[{join_union(data_types)}] = absent()\n"
                "    test: bool | None = absent()\n"
                f"    type: Lenient[Literal[{event!r}] | str | None] = absent()\n"
                "    timestamp: Lenient[str | None] = absent()\n"
                "    mode: Lenient[Literal['test'] | str | None] = absent()\n"
                "    sent_at: Lenient[str] = absent()\n\n"
                "    @property\n"
                "    def is_test_mode(self) -> bool:\n"
                '        """Whether a test key simulated the event (``mode == \'test\'``): nothing was sent or received."""\n'
                "        return self.mode == 'test'\n\n\n"
            )
        text += (
            'class UnknownEvent(TawkedModel):\n    """An event this version of the SDK does not know yet: ``event`` (or ``type``) and raw ``data``."""\n\n'
            "    event: str | None = absent()\n    type: str | None = absent()\n    data: Any = absent()\n"
            "    test: bool | None = absent()\n    timestamp: str | None = absent()\n    mode: str | None = absent()\n"
            "    sent_at: str | None = absent()\n\n"
            "    @property\n"
            "    def is_test_mode(self) -> bool:\n"
            '        """Whether a test key simulated the event (``mode == \'test\'``)."""\n'
            "        return self.mode == 'test'\n\n\n"
        )
        text += (
            "WebhookEvent = (\n    "
            + "\n    | ".join([*(cls for _, cls in events), "UnknownEvent"])
            + "\n)\n\n"
        )
        text += (
            "EVENT_TYPES: dict[str, type[TawkedModel]] = {\n"
            + "".join(f"    {event!r}: {cls},\n" for event, cls in events)
            + "}\n\n"
        )
        text += (
            "\ndef parse_event(body: builtins.dict[str, Any]) -> WebhookEvent:\n"
            '    """The typed event of a webhook body (the tawked envelope\'s ``event``, or ``type``)."""\n'
            "    name = body.get('event', body.get('type'))\n"
            "    cls = EVENT_TYPES.get(name) if isinstance(name, str) else None\n"
            "    event: WebhookEvent = (cls or UnknownEvent).model_validate(body)  # type: ignore[assignment]\n"
            "    return event\n\n\n"
        )
        all_names = [
            "EVENT_TYPES",
            "UnknownEvent",
            "WebhookEvent",
            "parse_event",
            *sorted(c for _, c in events),
        ]
        text += "__all__ = [" + ", ".join(repr(n) for n in all_names) + "]\n"
        local_new = [n for n in local.classes if n not in self.types.classes]
        if local_new:
            text += "\nfor _model in (" + ", ".join(local_new) + "):\n    _model.model_rebuild()\n"
        used = sorted(
            n
            for n in self.types.classes
            if re.search(rf"\b{n}\b", text.split("_ = (builtins", 1)[1])
        )
        text = text.replace("@@TYPES@@", ", ".join(used))
        self.write(f"{GEN_DIR}/events/__init__.py", text)
        self.event_list = events
        self.event_classes = local

    def root_module(self) -> None:
        text = HEADER + (
            "\nfrom __future__ import annotations\n\nfrom collections.abc import Callable\nfrom typing import TypeVar\n\nF = TypeVar('F', bound=Callable[..., object])\n\n\n"
            "def early_access(fn: F) -> F:\n"
            '    """Marks a method of a product in early access (read by scripts/surface.py)."""\n'
            "    fn.__tawked_stability__ = 'early_access'  # type: ignore[attr-defined]\n    return fn\n"
        )
        self.write(f"{GEN_DIR}/__init__.py", text)

    # -------------------------------------------------------------- tests data

    def tests_data(self) -> None:
        product = []
        for m in self.product:
            found = example_args(m)
            assert found is not None, m.endpoint["id"]
            args, kwargs = found
            ex = m.example or {}
            product.append(
                {
                    "id": m.endpoint["id"],
                    "call": call_path(m),
                    "auth": m.endpoint["auth"],
                    "method": m.endpoint["method"],
                    "path": expected_path(m.endpoint["path"], ex.get("path") or {}),
                    "args": args,
                    "kwargs": kwargs,
                    "query": ex.get("query") or {},
                    "body": ex.get("body"),
                    "multipart": {
                        k: (v.get("filename") if isinstance(v, dict) else v)
                        for k, v in (ex.get("multipart") or {}).items()
                    },
                    "retry": m.retry,
                    "takes_key": m.takes_key,
                    "key": (ex.get("headers") or {}).get("Idempotency-Key"),
                    "response": m.response_class,
                    "item": m.item_class,
                    "pagination": m.pagination["style"] if m.pagination else None,
                    "binary": m.binary,
                    "errors": [
                        {
                            "code": x["error"],
                            "status": x["http"],
                            "role": role_for(x["error"], x["http"], self.error_status),
                        }
                        for x in m.errors
                    ],
                }
            )
        account = []
        for m in self.account_methods:
            args, kwargs, wire = account_example(m)
            account.append(
                {
                    "id": m.endpoint["id"],
                    "call": call_path(m),
                    "method": m.endpoint["method"],
                    "path": expected_path(
                        m.endpoint["path"],
                        dict(zip([w for _, w in m.path_params], args, strict=True)),
                    ),
                    "args": args,
                    "kwargs": kwargs,
                    "wire": wire,
                    "in": m.endpoint["request"]["in"],
                    "body": m.endpoint["request"]["body"],
                    "files": list(m.files),
                    "retry": m.retry,
                    "takes_key": m.takes_key,
                    "approval": bool(m.endpoint["sdk"].get("approval")),
                    "secret": bool(m.endpoint["sdk"].get("secret")),
                    "pagination": m.pagination["style"] if m.pagination else None,
                    "errors": [
                        {
                            "code": ACCOUNT_STATUS_CODE[s],
                            "status": s,
                            "role": role_for(
                                ACCOUNT_STATUS_CODE[s].split(":")[0], s, ACCOUNT_STATUS
                            ),
                        }
                        for s in m.endpoint["errors"]
                        if s in ACCOUNT_STATUS_CODE
                    ],
                }
            )
        models = []
        for cls in self.types.classes.values():
            if not cls.fields and cls.base == "TawkedModel":
                continue
            fields = cls.fields or (
                self.types.classes[cls.base].fields if cls.base in self.types.classes else []
            )
            enums = cls.enum_fields or (
                self.types.classes[cls.base].enum_fields if cls.base in self.types.classes else {}
            )
            enum_field = next(iter(enums), None)
            models.append(
                {
                    "name": cls.name,
                    "sample": cls.sample if isinstance(cls.sample, dict) else {},
                    "enum_field": enum_field,
                    "fields": [f.wire for f in fields],
                }
            )
        aliases = []
        for m in [*self.product, *self.account_methods]:
            for p in m.params:
                if p.py != p.wire and m.params_class:
                    aliases.append(
                        {
                            "model": m.params_class,
                            "module": "account" if m.surface == "account" else "types",
                            "py": p.py,
                            "wire": p.wire,
                        }
                    )
        hooks = self.api["webhooks"]
        examples = []
        for ex in hooks["application"].get("examples") or []:
            examples.append({"side": "application", "body": ex})
        for event, spec in hooks["partner"]["events"].items():
            examples.append(
                {
                    "side": "partner",
                    "body": {
                        "event": event,
                        "data": spec.get("example"),
                        "sent_at": "1788265862201",
                    },
                }
            )
        data = {
            "product": product,
            "account": account,
            "models": models,
            "aliases": aliases,
            "events": [{"event": e, "class": c} for e, c in self.event_list],
            "event_examples": examples,
            "webhook_schemes": hooks["schemes"],
            "webhook_cases": hooks["verification"]["cases"],
            "both_headers": self.both_headers,
            "pkce": self.api["oauth"]["pkce"]["worked_example"],
            "oauth_errors": [
                {"code": e["error"], "status": e["http"]}
                for e in self.oauth["oauth-token"]["errors"]
            ],
            "error_status": self.error_status,
        }
        text = (
            HEADER
            + "\n# The contract tests' data: every endpoint, error, retry class, page style, model and webhook case.\n\nfrom typing import Any\n\n"
        )
        for key, value in data.items():
            text += f"{key.upper()}: Any = {py_literal(value)}\n\n"
        self.write(f"{TEST_DIR}/contract_data.py", text)
        self.write(f"{TEST_DIR}/__init__.py", HEADER)
        for name, body in GENERATED_TESTS.items():
            self.write(f"{TEST_DIR}/{name}", HEADER + body)

    # -------------------------------------------------------------- run

    def run(self) -> dict[str, str]:
        self.root_module()
        self.contract_module()
        self.endpoints_module()
        self.types_module()
        self.product_resources()
        self.account_resources()
        self.events_module()
        self.tests_data()
        return self.files


def _ids(cases: list[dict[str, Any]], key: str = "id") -> list[str]:
    return [str(c[key]) for c in cases]


GENERATED_TESTS: dict[str, str] = {
    "test_product.py": """
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


@pytest.mark.parametrize(("case", "error"), ERRORS, ids=[f"{c['id']}-{e['code']}" for c, e in ERRORS])
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
""",
    "test_account.py": """
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


@pytest.mark.parametrize(("case", "error"), ERRORS, ids=[f"{c['id']}-{e['status']}" for c, e in ERRORS])
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
""",
    "test_models.py": """
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
""",
    "test_webhooks.py": """
# Webhooks (item 5): every worked example of both schemes, the Standard Webhooks published vector,
# every verification case of the contract (cross-scheme, rotation, units), and every
# event typed by construct_event. OAuth (item 6): the PKCE worked example.

import json

import pytest

from tawked import webhooks
from tawked._generated import events
from tawked.oauth import code_challenge
from tests.generated.contract_data import BOTH_HEADERS, EVENT_EXAMPLES, EVENTS, PKCE, WEBHOOK_CASES, WEBHOOK_SCHEMES

TAWKED = next(s for s in WEBHOOK_SCHEMES if s["name"] == "tawked")
STANDARD = next(s for s in WEBHOOK_SCHEMES if s["name"] == "standard_webhooks")


@pytest.mark.parametrize("example", TAWKED["worked_examples"], ids=[e["label"] for e in TAWKED["worked_examples"]])
def test_tawked_worked_example(example):
    assert webhooks.sign(example["body"], example["secret"], example["timestamp"]) == example["signature"]
    headers = {"tawked-timestamp": example["timestamp"], "tawked-signature": example["signature"]}
    assert webhooks.verify(example["body"].encode(), headers, example["secret"], now=int(example["timestamp"]) / 1000)
    assert not webhooks.verify(example["body"] + " ", headers, example["secret"], now=int(example["timestamp"]) / 1000)


@pytest.mark.parametrize("example", STANDARD["worked_examples"], ids=[e["label"] for e in STANDARD["worked_examples"]])
def test_standard_worked_example(example):
    signed = webhooks.sign(example["body"], example["secret"], example["timestamp"], id=example["id"])
    assert signed == example["signature"]
    headers = {"webhook-id": example["id"], "webhook-timestamp": str(example["timestamp"]), "webhook-signature": signed}
    assert webhooks.verify(example["body"], headers, example["secret"], now=example["timestamp"])
    assert not webhooks.verify(example["body"] + " ", headers, example["secret"], now=example["timestamp"])


@pytest.mark.parametrize("case", WEBHOOK_CASES, ids=[c["label"] for c in WEBHOOK_CASES])
def test_verification_case(case):
    now = case["now_ms"] / 1000
    assert webhooks.verify(case["body"].encode(), case["headers"], case["secrets"], now=now) is case["valid"]
    if case["valid"]:
        webhooks.assert_valid(case["body"], case["headers"], case["secrets"], now=now)
    else:
        with pytest.raises(webhooks.WebhookVerificationError) as info:
            webhooks.assert_valid(case["body"], case["headers"], case["secrets"], now=now)
        assert info.value.reason == case["reason"]


# one real delivery carrying both header sets. The scheme is chosen by the secrets
# given, never by the headers present, and never falls back from one scheme to the other.
@pytest.mark.parametrize("case", BOTH_HEADERS["cases"], ids=[c["label"] for c in BOTH_HEADERS["cases"]])
def test_both_header_sets(case):
    body, headers, now = BOTH_HEADERS["body"], BOTH_HEADERS["headers"], BOTH_HEADERS["now_seconds"]
    expected = case["expected"]
    assert webhooks.verify(body, headers, case["secrets"], now=now) is expected["valid"]
    assert webhooks.verify(body, headers, case["secrets"], now=now, scheme=expected["scheme"]) is expected["valid"]
    # The chosen scheme alone decides: the other scheme's headers taken away, the answer does not change.
    if expected["scheme"] == "tawked":
        own = {k: v for k, v in headers.items() if not k.startswith("webhook-")}
    else:
        own = {k: v for k, v in headers.items() if k != "tawked-signature"}
    assert webhooks.verify(body, own, case["secrets"], now=now) is expected["valid"]
    if expected["valid"]:
        event = webhooks.construct_event(body, headers, case["secrets"], now=now)
        assert not isinstance(event, events.UnknownEvent) and event.event == "email.delivered"
    else:
        with pytest.raises(webhooks.WebhookVerificationError) as info:
            webhooks.assert_valid(body, headers, case["secrets"], now=now)
        assert info.value.reason == "signature_mismatch"


@pytest.mark.parametrize("example", EVENT_EXAMPLES, ids=[f"{e['side']}-{e['body']['event']}" for e in EVENT_EXAMPLES])
def test_construct_event(example):
    body = json.dumps(example["body"], ensure_ascii=False)
    secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
    event = webhooks.construct_event(body, webhooks.test_headers(body, secret), secret)
    assert type(event) is events.EVENT_TYPES[example["body"]["event"]]
    assert event.event == example["body"]["event"]
    assert event.data is not None and not isinstance(event.data, dict)


def test_every_contract_event_has_a_class():
    assert {e["event"] for e in EVENTS} == set(events.EVENT_TYPES)


def test_unknown_event():
    # A name no contract has (email.opened became a typed event).
    body = json.dumps({"event": "email.teleported", "data": {"id": "x"}, "sent_at": "1788265862201"})
    secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
    event = webhooks.construct_event(body, webhooks.test_headers(body, secret), secret)
    assert isinstance(event, events.UnknownEvent)
    assert event.event == "email.teleported" and event.data == {"id": "x"}


def test_malformed_body():
    secret = "Zm9vYmFyLXRhd2tlZC10ZXN0LXNlY3JldC0wMDAx"
    with pytest.raises(webhooks.WebhookVerificationError) as info:
        webhooks.construct_event("not json", webhooks.test_headers("not json", secret), secret)
    assert info.value.reason == "malformed_body"


def test_pkce_worked_example():
    assert code_challenge(PKCE["code_verifier"]) == PKCE["code_challenge"]
""",
}


ACCOUNT_STATUS = {
    "unauthorized": 401, "forbidden": 403, "not_found": 404, "conflict": 409, "approval_expired": 410,
    "validation_failed": 422, "approval_required": 428, "rate_limited": 429,
}  # fmt: skip
ACCOUNT_STATUS_CODE = {
    401: "unauthorized",
    403: "forbidden",
    404: "not_found",
    409: "conflict:409",
    410: "approval_expired",
    422: "validation_failed",
    428: "approval_required",
    429: "rate_limited",
}


def role_for(code: str, status: int, documented: dict[str, int]) -> str:
    """The role an error answer maps to (the same rule as tawked._errors.error_class_for)."""
    if code == "idempotency_secret_not_replayable":
        return "secret_not_replayable"
    if code.startswith("idempotency_"):
        return "idempotency"
    if code == "insufficient_scope":
        return "scope"
    s = documented.get(code, status)
    return {
        400: "bad_request",
        401: "authentication",
        402: "credits",
        403: "permission",
        404: "not_found",
        409: "conflict",
        410: "gone",
        422: "unprocessable",
        428: "approval",
        429: "rate_limit",
    }.get(s, "server" if s >= 500 else "api")


def expected_path(template: str, values: dict[str, Any]) -> str:
    from urllib.parse import quote

    for name, value in values.items():
        template = template.replace("{" + name + "}", quote(str(value), safe=""))
    return template


def account_example(m: Method) -> tuple[list[Any], dict[str, Any], dict[str, Any]]:
    """Path arguments and the required fields of an Account operation, with values that fit."""
    args = [f"{wire}_1" for _, wire in m.path_params]
    schema = m.endpoint["request"].get("schema") or {}
    kwargs: dict[str, Any] = {}
    wire: dict[str, Any] = {}
    for p in m.params:
        if not p.required and not (p.file and p.wire in m.files):
            continue
        sub = (schema.get("properties") or {}).get(p.wire) or {}
        if p.file:
            kwargs[p.py] = {
                "__file__": {
                    "filename": f"{p.wire}.pdf",
                    "content_type": "application/pdf",
                    "content_base64": base64.b64encode(b"%PDF-1.4 tawked").decode(),
                }
            }
            wire[p.wire] = {"file": f"{p.wire}.pdf"}
            continue
        value = request_value(sub)
        kwargs[p.py] = value
        wire[p.wire] = value
    return args, kwargs, wire


def request_value(schema: dict[str, Any]) -> Any:
    if "enum" in schema:
        return next(v for v in schema["enum"] if v is not None)
    types = schema.get("type")
    kind = next(
        (t for t in (types if isinstance(types, list) else [types]) if t and t != "null"), "string"
    )
    if kind == "integer":
        return (
            max(int(schema.get("minimum", 1)), 1)
            if schema.get("maximum", 2) >= 1
            else int(schema.get("minimum", 0))
        )
    if kind == "number":
        return float(schema.get("minimum", 1))
    if kind == "boolean":
        return True
    if kind == "array":
        item = request_value(schema.get("items") or {})
        return [item] * max(1, int(schema.get("minItems", 1)))
    if kind == "object":
        props = schema.get("properties") or {}
        return {
            k: request_value(v) for k, v in props.items() if k in (schema.get("required") or [])
        } or ({"key": "value"} if not props else {})
    fmt = schema.get("format")
    if fmt == "email":
        return "sara@example.com"
    if fmt in ("uri", "url"):
        return "https://example.com"
    if fmt == "date-time":
        return "2026-10-22T09:00:00+03:00"
    if fmt == "date":
        return "2026-10-22"
    if fmt == "uuid":
        return "c2a10f3e-8b7a-4d2e-9c1a-1a2b3c4d5e6f"
    length = max(int(schema.get("minLength", 1)), 1)
    pattern = schema.get("pattern")
    if pattern:
        return pattern_value(pattern, length)
    return ("abcdefghij" * (length // 10 + 1))[: max(length, 5)][
        : int(schema.get("maxLength", 100))
    ] or "x"


def pattern_value(pattern: str, length: int) -> str:
    """A sample that fits ``pattern`` where Python's ``re`` reads it; the mock checks no pattern."""
    candidates = [
        "abcde",
        "ABCDE",
        "12345",
        "1234",
        "123456",
        "SA",
        "09:30",
        "+966551234567",
        "30000000000003",
        "ABCDEFGHIJK",
        "abc.def",
        "a1b2c",
        "abc_def",
    ]
    for c in candidates:
        try:
            if re.fullmatch(pattern, c):
                return c
        except re.error:
            break
    return "abcde"


def collect(node: Node) -> list[Method]:
    out = list(node.methods)
    for child in node.children.values():
        out += collect(child)
    return out


def namespaces_module(
    modules: list[tuple[str, Node]], prefix: str, base: str, package: str, what: str
) -> str:
    text = HEADER + "\nfrom __future__ import annotations\n\n"
    for seg, node in modules:
        text += f"from tawked._generated.{package}.{seg} import {class_name(prefix, node.path, False)}, {class_name(prefix, node.path, True)}\n"
    for async_ in (False, True):
        name = ("Async" if async_ else "") + base
        text += f'\n\nclass {name}:\n    """The top-level namespaces of {what}{" (async)" if async_ else ""}."""\n\n'
        for seg, node in modules:
            text += f"    {seg}: {class_name(prefix, node.path, async_)}\n"
        text += "\n    def _init_namespaces(self) -> None:\n"
        for seg, node in modules:
            text += f"        self.{seg} = {class_name(prefix, node.path, async_)}(self)  # type: ignore[arg-type]\n"
    return text


def ruff_format(files: dict[str, str]) -> dict[str, str]:
    with tempfile.TemporaryDirectory() as tmp:
        base = Path(tmp)
        shutil.copy(ROOT / "pyproject.toml", base / "pyproject.toml")
        for rel, text in files.items():
            path = base / rel
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(text, encoding="utf-8")
        targets = [str(base / rel) for rel in files if rel.endswith(".py")]
        ruff = shutil.which("ruff") or str(Path(sys.executable).parent / "ruff")
        subprocess.run(
            [
                ruff,
                "check",
                "--fix",
                "--silent",
                "--select",
                "I,F401,UP,RUF022",
                "--exit-zero",
                *targets,
            ],
            check=True,
            cwd=base,
        )
        subprocess.run([ruff, "format", "--quiet", *targets], check=True, cwd=base)
        return {rel: (base / rel).read_text(encoding="utf-8") for rel in files}


def main(argv: Iterable[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "--check", action="store_true", help="write nothing; fail when a generated file is stale"
    )
    args = parser.parse_args(list(argv) if argv is not None else None)
    try:
        files = Generator(CONTRACT_DIR).run()
    except ContractError as error:
        print(f"generate.py: {error}", file=sys.stderr)
        return 1
    files = ruff_format(files)
    files[MANIFEST] = "".join(f"{rel}\n" for rel in sorted(files)) + f"{MANIFEST}\n"
    old = (
        set((ROOT / MANIFEST).read_text(encoding="utf-8").split())
        if (ROOT / MANIFEST).exists()
        else set()
    )
    stale = sorted(old - set(files))
    if args.check:
        problems = [
            rel
            for rel, text in sorted(files.items())
            if not (ROOT / rel).exists() or (ROOT / rel).read_text(encoding="utf-8") != text
        ]
        problems += [f"{rel} (stale)" for rel in stale if (ROOT / rel).exists()]
        if problems:
            print(
                "generate.py --check: out of date, run `uv run python scripts/generate.py`:\n  "
                + "\n  ".join(problems),
                file=sys.stderr,
            )
            return 1
        print(f"generate.py --check: {len(files)} files up to date")
        return 0
    for rel in stale:
        (ROOT / rel).unlink(missing_ok=True)
    for rel, text in files.items():
        path = ROOT / rel
        path.parent.mkdir(parents=True, exist_ok=True)
        if not path.exists() or path.read_text(encoding="utf-8") != text:
            path.write_text(text, encoding="utf-8")
    print(f"generate.py: {len(files)} files written from {CONTRACT_DIR}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
