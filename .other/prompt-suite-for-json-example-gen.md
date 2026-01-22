# **Comprehensive Prompt Suite for JSON Example Generation from Schemas and Documentation**

# **0. Primary Prompt for JSON Example Generation**

Generate all possible _.json example files in the examples/ directory by strictly following the documentation in the docs/ folder and the corresponding _.schema.json files in the schemas/ folder. Validate every generated file using the JSON Schema configuration defined in .vscode/settings.json.

---\*\*\*---

# **1. Base Prompt for JSON Example Generation**

Generate every valid `*.json` example file that can be produced under the `examples/` directory by **strictly** following the JSON Schemas in the `schemas/` folder.
Use the Markdown files in the `docs/` folder **only as reference documentation** to understand the meaning, intent, and allowed patterns of each field, but **never** to override or contradict the schemas.

All generated JSON must:

- Conform **exactly** to the corresponding `*.schema.json` file in `schemas/`.
- Include **every valid structural variation** permitted by each schema.
- Use `.vscode/settings.json` for JSON Schema validation.
- Avoid any fields, values, or structures not permitted by the schema.
- Prefer examples that illustrate the full expressive range of each schema, while remaining strictly valid.

Place each generated example in:

```
examples/<schema-name>/<descriptive-example-name>.json
```

Use the Markdown files in `docs/` to guide:

- Naming conventions
- Typical usage patterns
- Semantic meaning of fields
- Recommended best practices
- Version‑specific behaviors

But always treat the schemas as the **single source of truth** for what is allowed.
Ensure that every generated example is validated against the schema before finalizing. If any example fails validation, it must be corrected.

---\*\*\*---

# **2. Version Tailored for a GitHub Action / CI Workflow**

This version is written as if it will be consumed by an automated CI job, a GitHub Action, or a validation bot. It emphasizes determinism, reproducibility, and failure conditions.

---

## **CI‑Optimized Prompt**

Generate the complete set of valid `*.json` example files under the `examples/` directory by strictly validating against every `*.schema.json` file in the `schemas/` folder.

### **Requirements**

- Treat the JSON Schemas in `schemas/` as the **single authoritative specification**.
- Use the Markdown files in `docs/` only as descriptive reference material.
  They may clarify semantics, but they must never override or expand the schemas.
- For each schema, generate a comprehensive suite of examples that:
  - Exercise every field permitted by the schema.
  - Demonstrate all structural variations allowed by the schema.
  - Use realistic, semantically meaningful values when possible.
  - Remain strictly valid according to the schema.

### **Validation Rules**

- All generated files must pass JSON Schema validation using the configuration defined in `.vscode/settings.json`.
- Any example that does not validate must be rejected and regenerated.
- No example may include fields, values, or structures not permitted by the schema.

### **Output Structure**

Place generated examples in:

```
examples/<schema-name>/<example-name>.json
```

Where `<schema-name>` matches the filename in `schemas/` (without extension).

### **CI Behavior Expectations**

- The workflow should fail if:
  - Any generated file is invalid.
  - Any schema is missing corresponding examples.
  - Any example violates formatting or structural rules.

- The workflow should succeed only when:
  - All schemas have complete example coverage.
  - All examples validate cleanly.
  - No extraneous files are produced.

---\*\*\*---

# **3. Version Optimized for Automated Pipelines**

This version is written for a fully automated generator or pipeline component — deterministic, machine‑friendly, and unambiguous. It assumes no human intervention.

---

## **Pipeline‑Optimized Prompt**

Produce a complete, deterministic set of example `*.json` files under the `examples/` directory by exhaustively enumerating all valid structures permitted by the JSON Schemas in the `schemas/` folder.

### **Authoritative Specification**

- The `schemas/` directory defines the full and exclusive set of allowed fields, types, and structures.
- The `docs/` directory provides contextual meaning and recommended usage patterns but must never introduce fields or structures not present in the schemas.

### **Generation Rules**

- For each schema:
  - Generate examples that cover the full combinatorial space of allowed structures.
  - Include minimal, typical, and maximal examples.
  - Include edge‑case examples (e.g., boundary numeric values, optional fields omitted, optional fields present).
  - Use canonical ordering of fields for deterministic output.
  - Use stable, reproducible naming conventions for example files.

- All examples must be strictly valid according to the schema.

### **Validation**

- Validate every generated file using the JSON Schema configuration defined in `.vscode/settings.json`.
- Reject and regenerate any file that fails validation.
- Ensure deterministic output: the same input repository must always produce identical example files.

### **Output Layout**

```
examples/
  <schema-name>/
    minimal.json
    typical.json
    maximal.json
    edge-case-1.json
    edge-case-2.json
    ...
```

### **Pipeline Guarantees**

- No example may include undocumented or schema‑forbidden fields.
- No example may rely on implicit behavior not defined in the schema.
- All examples must be self‑contained and require no external context.

---\*\*\*---

# **3. Machine‑Readable Specification (JSON)**

This is a **formal contract** describing exactly what the generator must do.
It is designed to be parsed by a CLI tool, CI job, or code generator.

```json
{
  "version": "1.0.0",
  "description": "Specification for generating example JSON files from schemas and documentation.",
  "input": {
    "schema_root": "schemas/",
    "docs_root": "docs/",
    "validation_settings": ".vscode/settings.json"
  },
  "rules": {
    "authority": {
      "schemas_are_source_of_truth": true,
      "docs_are_reference_only": true
    },
    "generation": {
      "examples_per_schema": "comprehensive",
      "example_types": ["minimal", "typical", "maximal", "edge_cases"],
      "field_ordering": "canonical",
      "naming_convention": "kebab-case",
      "deterministic_output": true,
      "allow_additional_properties": false
    },
    "validation": {
      "strict_schema_validation": true,
      "use_vscode_settings": true,
      "reject_invalid_examples": true
    }
  },
  "output": {
    "root": "examples/",
    "structure": "examples/<schema-name>/<example-name>.json",
    "overwrite_existing": true,
    "pretty_print": true,
    "newline_at_end_of_file": true
  },
  "ci_requirements": {
    "fail_on_missing_examples": true,
    "fail_on_invalid_examples": true,
    "fail_on_unexpected_files": true
  }
}
```

This JSON spec is intentionally rigid so that:

- Any generator can read it.
- CI can enforce it.
- Output is deterministic and reproducible.

If you want, I can also generate a **JSON Schema** for this spec itself.

---\*\*\*---

# **4. GitHub Action Workflow YAML**

This workflow:

- Checks out your repo
- Installs your generator (placeholder command)
- Runs the generator using the machine‑readable spec
- Validates all generated examples
- Fails CI if anything is invalid or missing

```yaml
name: Generate and Validate JSON Examples

on:
  workflow_dispatch:
  push:
    branches: [main]
  pull_request:

jobs:
  generate-examples:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout repository
        uses: actions/checkout@v4

      - name: Set up Node.js
        uses: actions/setup-node@v4
        with:
          node-version: 20

      - name: Install generator dependencies
        run: |
          npm ci

      - name: Run example generator
        run: |
          node tools/generate-examples.js \
            --spec machine-readable-spec.json

      - name: Validate generated examples
        run: |
          node tools/validate-examples.js \
            --schemas schemas \
            --examples examples \
            --settings .vscode/settings.json

      - name: Fail if uncommitted changes exist
        run: |
          if [[ -n "$(git status --porcelain)" ]]; then
            echo "Generated files differ from expected output."
            git status --porcelain
            exit 1
          fi

      - name: Success
        run: echo "All examples generated and validated successfully."
```

### Notes

- The workflow assumes you have:
  - `tools/generate-examples.js`
  - `tools/validate-examples.js`
  - `machine-readable-spec.json` (the spec above)

- If you prefer Python, Rust, Bun, Deno, or Go, I can rewrite the workflow accordingly.

---\*\*\*---

Improve, optimize and implement more features, functions, methods, logics, settings, options, configs, etc.

Make sure it can generate all example_types:

```json
{
  "example_types": {
    "type": "array",
    "items": {
      "type": "string",
      "enum": [
        "minimal", // least number of fields to be valid
        "typical", // commonly used fields
        "full", // all commonly used fields
        "maximal", // all possible fields
        "thematic", // e.g., "holiday-themed", "biome-themed"
        "performance", // e.g., large arrays, high numerical values
        "experimental", // using newer or less common features
        "vanilla", // reflects standard vanilla usage
        "modded", // reflects common modded usage
        "edge_cases" // e.g., empty arrays, zero values
      ]
    },
    "minItems": 1,
    "uniqueItems": true
  }
}
```

Produce a complete, deterministic set of example `*.json` files under the `examples/` directory by exhaustively enumerating all valid structures permitted by the JSON Schemas in the `schemas/` folder.

### **Authoritative Specification**

- The `schemas/` directory defines the full and exclusive set of allowed fields, types, and structures.
- The `docs/` directory provides contextual meaning and recommended usage patterns but must never introduce fields or structures not present in the schemas.

### **Generation Rules**

- For each schema:
  - Generate examples that cover the full combinatorial space of allowed structures.
  - Include minimal, typical, and maximal examples.
  - Include edge‑case examples (e.g., boundary numeric values, optional fields omitted, optional fields present).
  - Use canonical ordering of fields for deterministic output.
  - Use stable, reproducible naming conventions for example files.

- All examples must be strictly valid according to the schema.

### **Validation**

- Validate every generated file using the JSON Schema configuration defined in `.vscode/settings.json`.
- Reject and regenerate any file that fails validation.
- Ensure deterministic output: the same input repository must always produce identical example files.

### **Output Layout**

```
examples/
  <schema-name>/
    minimal.json        // least number of fields to be valid
    typical.json        // commonly used fields
    full.json           // all commonly used fields
    maximal.json        // all possible fields
    thematic.json       // e.g., "holiday-themed", "biome-themed"
    performance.json    // e.g., large arrays, high numerical values
    experimental.json   // using newer or less common features
    vanilla.json        // reflects standard vanilla usage
    modded.json         // reflects common modded usage
    edge_cases/         // directory for multiple edge case examples
      edge-case-1.json  // e.g., empty arrays, zero values
      edge-case-2.json  // e.g., boundary numeric values
      ...
```

### **Pipeline Guarantees**

- No example may include undocumented or schema‑forbidden fields.
- No example may rely on implicit behavior not defined in the schema.
- All examples must be self‑contained and require no external context.

---\*\*\*---
