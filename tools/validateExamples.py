#!/usr/bin/env python3
import json
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def list_schema_files(schema_root: Path):
    return sorted(schema_root.rglob("*.schema.json"))


def list_example_files(examples_root: Path):
    return sorted(examples_root.rglob("*.json"))


def main():
    root = Path(__file__).resolve().parents[1]

    schema_root = root / "schemas"
    examples_root = root / "examples"

    schema_files = list_schema_files(schema_root)
    schema_by_name = {p.stem.replace(".schema", ""): p for p in schema_files}

    example_files = list_example_files(examples_root)

    errors = []

    for ex_path in example_files:
        # examples/<schema-name>/<example-name>.json
        try:
            schema_name = ex_path.relative_to(examples_root).parts[0]
        except Exception:
            errors.append(f"[ERROR] Example outside expected structure: {ex_path}")
            continue

        schema_path = schema_by_name.get(schema_name)
        if not schema_path:
            errors.append(
                f"[ERROR] No schema found for example '{ex_path}' (expected schema name '{schema_name}')"
            )
            continue

        schema = load_json(schema_path)
        instance = load_json(ex_path)

        resolver = RefResolver(base_uri=schema_path.as_uri(), referrer=schema)
        validator = Draft202012Validator(schema, resolver=resolver)

        try:
            validator.validate(instance)
            print(f"[OK] {ex_path} validates against {schema_path.name}")
        except Exception as e:
            errors.append(
                f"[ERROR] Validation failed for {ex_path} against {schema_path.name}: {e}"
            )

    if errors:
        print("\nValidation errors:")
        for e in errors:
            print(e)
        raise SystemExit(1)

    print("All examples validate against their schemas.")


if __name__ == "__main__":
    main()
