#!/usr/bin/env python3
"""Check the built package against sdks/contract/surface.txt and surface-account.txt.

Two independent halves, neither read from the generator's input:

1. **Shape**, from the built artifact: the wheel is built, installed into a clean virtual
   environment, and ``inspect.signature`` plus ``typing.get_type_hints`` walk ``Tawked``,
   ``TawkedAccount`` and ``tawked.apps`` (and their async twins, which must print the same lines).
2. **Behaviour**, observed: the generated contract tests record, from the mock's request log, how
   many requests followed a mock 500 and a 429, whether an Idempotency-Key was sent, and whether
   ``iterate()`` followed pages (``build/behaviour/*.jsonl``; the tests run first when it is missing).

The two are joined into one line per method, type spellings normalised through
``surface-types.json``, and compared with the contract's lines. ``iterate*`` and
``approvals.wait_and_retry`` are helpers on top of the contract's methods and are not lines of it.
"""

from __future__ import annotations

import json
import os
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any

ROOT = Path(__file__).resolve().parent.parent
CONTRACT_DIR = Path(os.environ.get("TAWKED_CONTRACT") or (ROOT.parent / "contract"))
BUILD = ROOT / "build" / "surface"
BEHAVIOUR = ROOT / "build" / "behaviour"

INSPECT = r"""
import inspect, json, sys, typing
import tawked
from tawked import apps

OPTIONS = {"idempotency_key", "timeout", "max_retries", "extra_headers"}
HELPERS = {"wait_and_retry"}


def spell(tp):
    origin = typing.get_origin(tp)
    if origin is not None:
        args = ", ".join(spell(a) for a in typing.get_args(tp))
        name = getattr(origin, "__name__", str(origin))
        return f"{name}[{args}]"
    if tp is type(None):
        return "None"
    return getattr(tp, "__name__", str(tp))


def shape(fn, call, surface, positional_skip=1):
    sig = inspect.signature(fn)
    hints = typing.get_type_hints(fn)
    params = list(sig.parameters.values())[positional_skip:]
    positional = [p.name for p in params if p.kind in (p.POSITIONAL_ONLY, p.POSITIONAL_OR_KEYWORD)]
    keywords = [p for p in params if p.kind == p.KEYWORD_ONLY and p.name not in OPTIONS]
    word = None
    if keywords:
        word = "params" if any(p.default is p.empty for p in keywords) else "params?"
    return {
        "surface": surface,
        "call": call,
        "positional": positional,
        "params": word,
        "returns": spell(hints.get("return")),
        "stability": getattr(fn, "__tawked_stability__", None),
        "coroutine": inspect.iscoroutinefunction(fn),
    }


def walk(obj, prefix, surface, out):
    for name in sorted(vars(obj)):
        if name.startswith("_"):
            continue
        value = getattr(obj, name)
        if type(value).__module__.startswith(("tawked._generated", "tawked.account")):
            walk(value, prefix + [name], surface, out)
    for name, member in inspect.getmembers(type(obj), inspect.isfunction):
        if name.startswith("_") or name.startswith("iterate") or name in HELPERS or name in ("close",):
            continue
        if not type(obj).__module__.startswith(("tawked._generated", "tawked.account")):
            continue
        out.append(shape(member, prefix + [name], surface))


result = {}
for label, client, surface in (
    ("sync", tawked.Tawked(api_key="tk_live_surface"), "product"),
    ("async", tawked.AsyncTawked(api_key="tk_live_surface"), "product"),
    ("sync", tawked.TawkedAccount(token="tk_acct_surfacecheck"), "account"),
    ("async", tawked.AsyncTawkedAccount(token="tk_acct_surfacecheck"), "account"),
):
    rows = result.setdefault(f"{surface}:{label}", [])
    walk(client, [], surface, rows)
result["oauth:sync"] = [
    shape(apps.authorize_url, ["apps", "authorize_url"], "oauth", 0),
    shape(apps.exchange_code, ["apps", "exchange_code"], "oauth", 0),
]
result["oauth:async"] = [
    shape(apps.authorize_url, ["apps", "authorize_url"], "oauth", 0),
    shape(apps.exchange_code_async, ["apps", "exchange_code"], "oauth", 0),
]
result["version"] = tawked.__version__
json.dump(result, sys.stdout)
"""


def run(cmd: list[str], **kwargs: Any) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, check=True, text=True, **kwargs)


def build_and_inspect() -> dict[str, Any]:
    uv = shutil.which("uv")
    if uv is None:
        raise SystemExit("surface.py needs uv")
    shutil.rmtree(BUILD, ignore_errors=True)
    BUILD.mkdir(parents=True)
    run(
        [uv, "build", "--wheel", "--out-dir", str(BUILD / "dist"), str(ROOT)],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
    wheel = next((BUILD / "dist").glob("tawked-*.whl"))
    run([uv, "venv", "--quiet", "--python", sys.executable, str(BUILD / "venv")])
    python = BUILD / "venv" / ("Scripts" if os.name == "nt" else "bin") / "python"
    run([uv, "pip", "install", "--quiet", "--python", str(python), str(wheel)])
    out = run([str(python), "-I", "-c", INSPECT], capture_output=True, cwd=BUILD)
    return dict(json.loads(out.stdout))


def behaviour() -> dict[tuple[str, str], dict[str, Any]]:
    files = sorted(BEHAVIOUR.glob("*.jsonl")) if BEHAVIOUR.exists() else []
    if not files:
        print(
            "surface.py: no recorded behaviour yet; running the contract tests first",
            file=sys.stderr,
        )
        run(
            [
                sys.executable,
                "-m",
                "pytest",
                "-q",
                "tests/generated",
                "tests/test_oauth_and_approvals.py",
            ],
            cwd=ROOT,
        )
        files = sorted(BEHAVIOUR.glob("*.jsonl"))
    seen: dict[tuple[str, str], dict[str, Any]] = {}
    for path in files:
        for line in path.read_text(encoding="utf-8").splitlines():
            row = json.loads(line)
            seen.setdefault((row["surface"], row["call"]), {})[row["probe"]] = row["value"]
    return seen


def camel(words: list[str]) -> str:
    parts = [p for w in words for p in w.split("_") if p]
    return parts[0] + "".join(p[:1].upper() + p[1:] for p in parts[1:])


class Normaliser:
    def __init__(self, table: dict[str, str]) -> None:
        self.exact = {k: v for k, v in table.items() if "T" not in re.findall(r"\bT\b", k)}
        self.generic = []
        for pattern, neutral in table.items():
            if re.search(r"\bT\b", pattern):
                prefix = pattern.split("[", 1)[0]
                self.generic.append((prefix, pattern[len(prefix) :], neutral))
        self.generic.sort(key=lambda g: -len(g[0]))

    def __call__(self, spelling: str) -> str:
        spelling = spelling.strip()
        if spelling in self.exact:
            return self.exact[spelling]
        match = re.match(r"^([\w.]+)\[(.*)\]$", spelling)
        if match:
            name, inner = match.group(1), match.group(2)
            for prefix, rest, neutral in self.generic:
                if name == prefix and rest.count("T") == 1 and "," not in rest:
                    return neutral.replace("T", self(inner))
        return spelling


def flags(
    surface: str, call: str, row: dict[str, Any], seen: dict[tuple[str, str], dict[str, Any]]
) -> list[str]:
    if surface == "oauth" and not row["coroutine"] and call == "apps.authorizeUrl":
        return ["local"]
    observed = seen.get((surface, ".".join(row["call"])), {})
    after_500 = observed.get("after_500")
    after_429 = observed.get("after_429")
    out: list[str] = []
    if after_500 is None or after_429 is None:
        out.append("unobserved")
    elif after_500["requests"] > 1:
        out.append("idempotent" if after_500.get("key") and after_500.get("same_key") else "safe")
    elif after_429["requests"] > 1:
        out.append("write_once")
    else:
        out.append("never")
    pages = observed.get("pages")
    if pages and pages.get("requests", 0) > 1:
        out.append(str(pages.get("style")))
    if row.get("stability") == "early_access":
        out.append("early_access")
    return out


def line(
    row: dict[str, Any], seen: dict[tuple[str, str], dict[str, Any]], normalise: Normaliser
) -> str:
    call = ".".join(camel([w]) for w in row["call"][:-1]) + "." + camel([row["call"][-1]])
    args = [p[:-1] if p.endswith("_") else p for p in row["positional"]]
    if row["params"]:
        args.append(row["params"])
    returns = normalise(row["returns"])
    marks = flags(row["surface"], call, row, seen)
    return f"{row['surface']:<8} {call}({', '.join(args)}) -> {returns}  " + " ".join(
        f"[{m}]" for m in marks
    )


def contract_lines(name: str) -> list[str]:
    text = (CONTRACT_DIR / name).read_text(encoding="utf-8")
    return sorted(line for line in text.splitlines() if line and not line.startswith("#"))


def main() -> int:
    shapes = build_and_inspect()
    seen = behaviour()
    table = json.loads((CONTRACT_DIR / "surface-types.json").read_text(encoding="utf-8"))["python"]
    normalise = Normaliser({k: v for k, v in table.items() if not k.startswith("$")})
    problems = 0
    for surface_file, keys in (
        ("surface.txt", ("product", "oauth")),
        ("surface-account.txt", ("account",)),
    ):
        expected = contract_lines(surface_file)
        mine: dict[str, list[str]] = {}
        for label in ("sync", "async"):
            lines: list[str] = []
            for key in keys:
                lines += [line(r, seen, normalise) for r in shapes[f"{key}:{label}"]]
            mine[label] = sorted(lines)
        if mine["sync"] != mine["async"]:
            problems += 1
            for got in sorted(set(mine["sync"]) ^ set(mine["async"])):
                print(f"  sync and async differ: {got}")
        missing = sorted(set(expected) - set(mine["sync"]))
        extra = sorted(set(mine["sync"]) - set(expected))
        for got in missing:
            print(f"- {got}   (in {surface_file}, not in the package)")
        for got in extra:
            print(f"+ {got}   (in the package, not in {surface_file})")
        problems += len(missing) + len(extra)
        print(
            f"surface.py: {surface_file}: {len(expected)} lines, {len(expected) - len(missing)} match"
        )
    print(
        f"surface.py: tawked {shapes['version']} "
        + ("matches the contract" if problems == 0 else f"differs in {problems} places")
    )
    return 0 if problems == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
