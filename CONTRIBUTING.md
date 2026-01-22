# Contributing to minecraft-data-docs

Thanks for contributing to this project.
This repository is a **spec‑driven reference** for Minecraft data formats, with tight coupling between:

- Markdown documentation (`docs/`)
- JSON Schemas (`schemas/`)
- Auto‑generated examples (`examples/`)

The goal is to keep all three in sync.

---

## Before you start

- Read `README.md` to understand the layout.
- Skim `remote-indexes.md` for quick links to docs and schemas.
- Familiarize yourself with the **Copilot Instructions** in `.github/copilot-instructions.md` (if present).

---

## Adding a new format

1. **Create the schema**
   - Add a new file under `schemas/` (or `schemas/nbt/`).
   - Use `snake_case` + `.schema.json`:
     - Example: `block_model.schema.json`, `armor_stand_nbt.schema.json`.
   - Follow existing patterns:
     - Use `$defs` for shared structures.
     - Use `$ref` to avoid duplication.
     - Add `title` and `description` where helpful.

2. **Create the documentation**
   - Add a new Markdown file under `docs/` (or `docs/nbt/`).
   - Use `kebab-case`:
     - Example: `block-models.md`, `armor-stand-nbt.md`.
   - Mirror the schema structure with headings.
   - Include:
     - A short introduction.
     - A field reference (tables recommended).
     - At least one minimal valid JSON example.

3. **Wire it into navigation**
   - Add links to:
     - `README.md`
     - `remote-indexes.md` (doc + schema)

4. **Generate and validate examples**

   From the repo root:

   ```bash
   cd projects/minecraft-data-docs
   python tools/generateExampleJsonFiles.py
   python tools/validateExamples.py
   python tools/lintDocsSchemas.py
   python tools/schemaCoverageReport.py
   ```

   Fix any reported issues before opening a PR.

---

## Editing an existing format

- Update the schema and doc **together**.
- Keep naming and structure consistent.
- Regenerate and validate examples as above.
- If you rename files, update:
  - `README.md`
  - `remote-indexes.md`
  - Any other inbound links.

---

## Style and quality expectations

- **Correctness over creativity.**
  Do not invent fields or semantics.

- **Explicit constraints when known.**
  Use `enum`, `minimum`, `pattern`, etc., when behavior is well understood.

- **Avoid over‑constraining.**
  If the game is permissive or unclear, allow the structure but document the ambiguity in the Markdown.

- **Small, focused changes.**
  Prefer PRs that tackle one concept at a time.

---

## Running CI locally

To approximate the CI pipeline:

```bash
cd projects/minecraft-data-docs

python tools/generateExampleJsonFiles.py
python tools/validateExamples.py
python tools/lintDocsSchemas.py
python tools/schemaCoverageReport.py > schema-coverage-report.txt
cat schema-coverage-report.txt
```

If all commands succeed and `git status` is clean, your changes are likely CI‑ready.

---

## Questions / unclear behavior

If you’re unsure about:

- How the game interprets a field.
- Whether a constraint is too strict.
- How to model a new structure.

Document the uncertainty in the Markdown file and keep the schema permissive.
Open a PR or issue describing the ambiguity so it can be refined later.
