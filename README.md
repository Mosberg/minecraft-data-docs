# minecraft-data-docs

Structured, schema‑driven documentation of Minecraft data formats, with:

- JSON Schemas for validation.
- Markdown docs for humans.
- Auto‑generated example JSON files.
- CI‑enforced consistency between docs, schemas, and examples.

## Repository structure

- `docs/` — Human‑readable documentation for each data domain:
  - Block models, item models, block states, NBT, etc.
- `schemas/` — JSON Schemas that define and validate each format.
- `examples/` — Auto‑generated example JSON files per schema.
- `tools/` — Python utilities:
  - `generateExampleJsonFiles.py` — Generate examples from schemas.
  - `validateExamples.py` — Validate examples against schemas.
  - `lintDocsSchemas.py` — Check docs ↔ schema consistency.
  - `schemaCoverageReport.py` — Report example coverage per schema.
- `remote-indexes.md` — Curated internal + external reference links.
- `generate-example-json-files.json` — Spec for the example generator.
- `schemas/generator/` — JSON Schema for the generator spec itself.

## Design principles

- **Schemas are the source of truth.**
  Docs explain; schemas define what is valid.

- **Docs and schemas stay in sync.**
  Every format has both a doc and a schema, linked and named consistently.

- **Examples are generated, not hand‑written.**
  Examples live under `examples/` and are produced by the generator spec.

- **CI enforces correctness.**
  The GitHub Action regenerates examples, validates them, lints docs/schemas, and checks coverage.

## Example generation pipeline

1. `generateExampleJsonFiles.py`:
   - Reads `generate-example-json-files.json`.
   - Validates it against `schemas/generator/generate-example-json-files.schema.json`.
   - Enumerates all `*.schema.json` under `schemas/`.
   - Generates multiple example types per schema:
     - `minimal`, `typical`, `full`, `maximal`, `thematic`, `performance`, `experimental`, `vanilla`, `modded`, `edge_cases`.
   - Writes examples to:
     - `examples/<schema-name>/<example-type>.json`
     - `examples/<schema-name>/edge_cases/*.json`

2. `validateExamples.py`:
   - Validates every example against its corresponding schema.

3. `lintDocsSchemas.py`:
   - Ensures docs and schemas are aligned by naming and basic coverage.

4. `schemaCoverageReport.py`:
   - Summarizes which example types exist per schema.

## CI workflow

The GitHub Action:

- Runs on pushes, PRs, and manual triggers.
- Regenerates examples.
- Validates examples.
- Lints docs and schemas.
- Generates a coverage report.
- Fails if:
  - Examples are invalid.
  - Expected examples are missing.
  - Unexpected changes are introduced.

## Contributing

See `CONTRIBUTING.md` (or the onboarding section below) for detailed guidelines.
