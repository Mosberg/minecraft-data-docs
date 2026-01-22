#!/usr/bin/env python3
from pathlib import Path


def main():
    root = Path(__file__).resolve().parents[1]
    examples_root = root / "examples"

    domains = {
        "block_model": ["minimal", "typical", "maximal"],
        "item_model": ["minimal", "typical", "maximal"],
        "nbt/item_nbt": ["minimal", "typical", "maximal"],
        "nbt/entity_nbt": ["minimal", "typical", "maximal"],
    }

    print("# Semantic Schema Coverage Report\n")

    for key, types in domains.items():
        if "/" in key:
            folder, name = key.split("/")
            schema_name = name
            ex_dir = examples_root / schema_name
        else:
            schema_name = key
            ex_dir = examples_root / schema_name

        print(f"## {schema_name}")

        if not ex_dir.exists():
            print("- Status: ❌ No examples directory found")
            print()
            continue

        present = []
        missing = []

        for t in types:
            path = ex_dir / f"{t}.json"
            if path.exists():
                present.append(t)
            else:
                missing.append(t)

        print(f"- Present semantic types: {', '.join(present) if present else 'none'}")
        print(f"- Missing semantic types: {', '.join(missing) if missing else 'none'}")
        print()


if __name__ == "__main__":
    main()
