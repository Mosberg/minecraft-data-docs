# Copilot Instructions — minecraft-data-docs

These instructions define the quality bar and contribution rules for this repository.
Follow them unless explicitly instructed otherwise.

## Purpose of this repository

This project documents Minecraft data formats and provides JSON Schemas that validate those formats (block models, item models, block states, NBT structures, etc.).

The primary goals are:

- **Accuracy** — documentation and schemas must reflect real game behavior.
- **Maintainability** — changes must be easy to track, review, and update.
- **Consistency** — documentation, schemas, and examples must stay in sync.

## Repository layout

- `docs/` — Human‑readable Markdown documentation.
- `schemas/` — JSON Schemas (including `schemas/nbt/`).
- `examples/` — Auto‑generated example JSON files.
- `remote-indexes.md` — Curated internal + external reference index.
- `README.md` — Navigation hub and entrypoint.

## Core rules (always apply)

- **Never invent fields, tags, or semantics.**
  If it’s not in the game or not documented, do not add it.

- **Documentation and schemas must match.**
  If one changes, update the other in the same PR.

- **Maintain cross‑links.**
  README ↔ docs ↔ schemas must always be navigable.

- **Follow existing patterns.**
  Do not introduce new structural patterns unless clearly superior and applied consistently across the repo.

## Naming conventions

- Markdown docs: **kebab-case**
  Example: `block-models.md`, `armor-stand-nbt.md`

- Schemas: **snake_case + `.schema.json`**
  Example: `block_model.schema.json`, `armor_stand_nbt.schema.json`

- Names must align between doc and schema.

## Documentation standards (`docs/`)

- Write for technical readers.
- Use headings that mirror the data structure.
- Use Markdown tables for field definitions:
  - Name, Type, Required, Description
- Provide:
  - One **smallest valid** JSON example.
  - One **common real‑world** example (optional).
- Prefer stable internal links.

## JSON Schema standards (`schemas/`)

- Follow existing schema structure.
- Use `$ref` to avoid duplication.
- Use `$defs` for shared structures.
- Use constraints (`enum`, `minimum`, `pattern`, etc.) when known.
- Avoid over‑constraining when the game is permissive.
- If uncertain, document the ambiguity in the Markdown file.

## Change workflow

When adding a new format:

1. Add Markdown doc in `docs/` (kebab-case).
2. Add matching schema in `schemas/` (snake_case + `.schema.json`).
3. Link both from `README.md`.
4. Add links to `remote-indexes.md`.

When modifying an existing format:

- Update doc + schema together.
- Fix all inbound links if renaming/moving files.

## Review mindset

- Avoid sweeping changes unless requested.
- Prefer small, reviewable commits.
- Ask clarifying questions when requirements are unclear.
- Prioritize accuracy and maintainability over cleverness.
