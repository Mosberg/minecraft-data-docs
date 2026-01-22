# Copilot Instructions for minecraft-data-docs

## Project Overview

This repository documents Minecraft data formats and provides JSON schemas for block models, item models, block states, and NBT data. It is a reference for developers and modders working with Minecraft data.

## Structure & Key Directories

- **docs/**: Markdown documentation for each data format. Subfolder `docs/nbt/` covers NBT data types.
- **schemas/**: JSON Schema files for validating Minecraft data. Subfolder `schemas/nbt/` contains NBT-related schemas.
- **README.md**: Entry point for navigation and project context.

## Authoring & Contribution Patterns

- Documentation and schemas are organized by data type (block, item, NBT, etc.).
- Each schema in `schemas/` is paired with a corresponding documentation file in `docs/`.
- When adding a new data type, create both a markdown doc and a schema file, and update the README with links.
- Use clear, descriptive file names matching the data type (e.g., `block_model.schema.json`, `block-models.md`).

## References

- See `remote-indexes.md` [Remote Indexes](remote-indexes.md) for quick access to important project resources.

- See `README.md` [README](../README.md) for a full directory and file listing.

- See `docs/` [docs](../docs/) and `schemas/` [schemas](../schemas/) for examples of documentation and schema structure.

## Conventions

- **Naming**: Use kebab-case for markdown files, snake_case for schema files.
- **Schema Design**: Follow existing schema structure for consistency. Reference other schemas using `$ref` where possible.
- **Documentation**: Use markdown tables and code blocks to illustrate data structures and examples.
- **Links**: Keep README and docs cross-linked for easy navigation.

## Workflows

- No build or test scripts; this is a documentation and schema repository.
- Validate JSON schemas using your preferred JSON Schema validator.
- Preview documentation using a markdown viewer or GitHub Pages.

## Examples

- To add a new NBT type:
  1. Add `docs/nbt/new-type-nbt.md`.
  2. Add `schemas/nbt/new_type_nbt.schema.json`.
  3. Update `README.md` with links to both files.

## Integration

- No external dependencies or code execution. All content is static.
- GitHub Pages is used for documentation hosting.

---

For questions about conventions or structure, review the README or existing files for patterns to follow.
