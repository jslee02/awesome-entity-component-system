#!/usr/bin/env python3
"""Validate all data/*.yaml files against schema/entry.schema.json"""

from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any, cast

import jsonschema
import yaml

Entry = dict[str, Any]


def load_schema(path: Path) -> dict[str, Any]:
    with path.open() as f:
        return cast(dict[str, Any], json.load(f))


def load_yaml(path: Path) -> list[Entry]:
    with path.open() as f:
        data = yaml.safe_load(f)
        if not isinstance(data, list):
            return []
        return cast(list[Entry], data)


def validate() -> bool:
    root = Path(__file__).parent.parent
    schema = load_schema(root / "schema" / "entry.schema.json")
    data_dir = root / "data"
    yaml_files = sorted(data_dir.glob("*.yaml"))
    if not yaml_files:
        print(f"WARNING: No YAML files in {data_dir}")
        return True
    all_valid = True
    total, errors = 0, 0
    for yf in yaml_files:
        try:
            entries = load_yaml(yf)
        except Exception as e:
            print(f"ERROR: Failed to load {yf.name}: {e}", file=sys.stderr)
            all_valid = False
            continue
        for idx, entry in enumerate(entries):
            total += 1
            if not isinstance(entry, dict):
                print(f"ERROR: {yf.name}[{idx}]: not a dict", file=sys.stderr)
                all_valid = False
                errors += 1
                continue
            raw_name = entry.get("name")
            name = raw_name if isinstance(raw_name, str) else f"[entry {idx}]"
            try:
                jsonschema.validate(
                    instance=entry,
                    schema=schema,
                    format_checker=jsonschema.FormatChecker(),
                )
            except jsonschema.ValidationError as e:
                print(f"ERROR: {yf.name}[{name}]: {e.message}", file=sys.stderr)
                all_valid = False
                errors += 1
            except jsonschema.SchemaError as e:
                print(f"ERROR: Schema error in {yf.name}: {e.message}", file=sys.stderr)
                all_valid = False
                errors += 1
    if all_valid:
        print(f"✓ All {total} entries validated successfully")
    else:
        print(
            f"✗ Validation failed: {errors} error(s) in {total} entries",
            file=sys.stderr,
        )
    return all_valid


if __name__ == "__main__":
    sys.exit(0 if validate() else 1)
