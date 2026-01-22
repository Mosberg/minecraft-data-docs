# Copilot Instructions — minecraft-data-docs

These instructions define the quality bar and contribution rules for this repository.
Follow them by default; only deviate when explicitly asked.

## What this repo is

This repository documents Minecraft data formats and provides JSON Schemas for validating those formats (block models, item models, block states, NBT, etc.).

Primary goal: accurate, maintainable reference documentation + validation schemas that stay in sync.

## Where things live

- `docs/`: Human-readable Markdown documentation.
- `schemas/`: JSON Schema files (including `schemas/nbt/`).
- `README.md`: Navigation hub and entrypoint.
- `remote-indexes.md`: Curated link index for internal files and external references.

## High-level rules (always)

- Prefer correctness over creativity; do not invent fields, tags, or semantics.
- Keep documentation and schemas paired: if one changes, update the other.
- Maintain cross-links (README ↔ docs ↔ schemas) so readers can navigate quickly.
- Be consistent with existing style and file layout; avoid “new patterns” unless clearly better and applied consistently.

## Naming & file conventions

- Markdown docs: kebab-case (example: `block-models.md`, `armor-stand-nbt.md`).
- Schemas: snake_case + `.schema.json` (example: `block_model.schema.json`, `armor_stand_nbt.schema.json`).
- Keep names aligned between doc and schema (same concept, predictable mapping).

## Documentation authoring standards (`docs/`)

- Write for technical readers: concise definitions, then structured details.
- Use headings to mirror the data structure (top-level → nested).
- Use Markdown tables for field/property definitions where practical:
  - Column suggestions: Name, Type, Required, Description.
- Provide minimal, valid JSON examples:
  - One “smallest valid” example.
  - One “common real-world” example (only if it adds clarity).
- Prefer stable internal links (relative paths). Avoid linking to moving targets when possible.

## JSON Schema standards (`schemas/`)

- Follow existing schema patterns in this repo for consistency.
- Use `$ref` to reuse definitions rather than duplicating structures.
- Keep schemas readable:
  - Group related definitions under `$defs` (or the repo’s existing pattern).
  - Use `title`/`description` meaningfully for editor/tooling UX.
- Be explicit about constraints when known:
  - Use `enum` for closed sets.
  - Use `minimum`/`maximum`, `pattern`, `minItems`, etc., where appropriate.
- Avoid over-constraining when the game format is permissive/unknown:
  - Prefer “allow but document” when unsure.
  - If uncertain, add a short note in the doc describing the ambiguity.

## Change workflow (what to update when)

When adding a new format/type:

1. Add the Markdown doc in the appropriate folder under `docs/` (use kebab-case).
2. Add the matching schema in `schemas/` (use snake_case + `.schema.json`).
3. Link both from `README.md` (and from any relevant overview docs).
4. Update `remote-indexes.md` with quick links to the new doc + schema.

When editing an existing format/type:

- Update the doc and schema together unless the change is strictly editorial (spelling/formatting).
- If you rename/move files, fix all inbound links (README and other docs).

## Safety / review mindset

- Do not make sweeping “cleanup” changes across many files unless requested.
- Prefer small, reviewable commits: one concept per change set.
- If requirements are unclear, ask a clarifying question before restructuring schemas or rewriting large documentation sections.
