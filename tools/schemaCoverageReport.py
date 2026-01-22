#!/usr/bin/env python3
import json
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    schemas_root = root / "schemas"
    examples_root = root / "examples"
    spec_path = root / "generate-example-json-files.json"

    spec = json.loads(spec_path.read_text(encoding="utf-8"))
    expected_types = spec["rules"]["generation"]["example_types"]

    schema_files = sorted(schemas_root.rglob("*.schema.json"))
    schema_names = [p.stem.replace(".schema", "") for p in schema_files]

    print("# Schema Coverage Report\n")

    for schema_name in schema_names:
        schema_examples_dir = examples_root / schema_name
        print(f"## {schema_name}")

        if not schema_examples_dir.exists():
            print("- Status: ❌ No examples directory found")
            print()
            continue

        # Collect example files
        existing_types = set()
        for path in schema_examples_dir.rglob("*.json"):
            rel = path.relative_to(schema_examples_dir)
            if rel.parts[0] == "edge_cases":
                existing_types.add("edge_cases")
            else:
                existing_types.add(path.stem)

        missing = [t for t in expected_types if t not in existing_types]
        present = [t for t in expected_types if t in existing_types]

        print(f"- Present types: {', '.join(present) if present else 'none'}")
        print(f"- Missing types: {', '.join(missing) if missing else 'none'}")
        print()
