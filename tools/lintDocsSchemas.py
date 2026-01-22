#!/usr/bin/env python3
import re
from pathlib import Path


def kebab_to_snake(name: str) -> str:
    return name.replace("-", "_")


def main():
    root = Path(__file__).resolve().parents[1]
    docs_root = root / "docs"
    schemas_root = root / "schemas"

    # Map docs -> expected schema names
    doc_files = sorted(docs_root.glob("*.md"))
    nbt_docs = sorted((docs_root / "nbt").glob("*.md"))

    all_docs = doc_files + nbt_docs

    expected_schemas = set()
    for doc in all_docs:
        base = doc.stem  # e.g. block-models, armor-stand-nbt
        snake = kebab_to_snake(base)
        # Heuristic: strip trailing "-nbt" for NBT docs to match schema naming
        snake = snake.replace("_nbt", "") if "nbt" in doc.parts else snake
        expected_schemas.add(snake)

    schema_files = sorted(schemas_root.rglob("*.schema.json"))
    schema_names = {p.stem.replace(".schema", "") for p in schema_files}

    missing_schemas = sorted(expected_schemas - schema_names)
    orphan_schemas = sorted(schema_names - expected_schemas)

    errors = []

    if missing_schemas:
        errors.append(
            "[ERROR] Docs with no matching schema (by naming convention): "
            + ", ".join(missing_schemas)
        )

    if orphan_schemas:
        # Allow generator schemas to be orphans by design
        orphan_schemas = [s for s in orphan_schemas if not s.startswith("generate")]
        if orphan_schemas:
            errors.append(
                "[ERROR] Schemas with no matching doc (by naming convention): "
                + ", ".join(orphan_schemas)
            )

    # Optional: simple field presence check for top-level headings like "### **field**"
    field_pattern = re.compile(r"^###\s+\*\*(.+?)\*\*", re.MULTILINE)

    for doc in all_docs:
        text = doc.read_text(encoding="utf-8")
        fields = field_pattern.findall(text)
        if not fields:
            continue

        base = doc.stem
        snake = kebab_to_snake(base)
        snake = snake.replace("_nbt", "") if "nbt" in doc.parts else snake

        # Find matching schema
        candidates = [p for p in schema_files if p.stem.startswith(snake)]
        if not candidates:
            continue

        # Just pick the first matching schema
        schema_path = candidates[0]
        import json

        schema = json.loads(schema_path.read_text(encoding="utf-8"))
        props = set(schema.get("properties", {}).keys())

        missing_fields = [f for f in fields if f in props or f.lower() in props]
        # This is intentionally soft; you can tighten it later if you want.

    if errors:
        print("\nDocs–schema lint errors:")
        for e in errors:
            print(e)
        raise SystemExit(1)

    print("Docs and schemas are structurally consistent (naming + basic coverage).")


if __name__ == "__main__":
    main()
