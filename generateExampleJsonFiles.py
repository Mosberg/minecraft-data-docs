#!/usr/bin/env python3
import json
from pathlib import Path

from jsonschema import Draft202012Validator, RefResolver, validate

# ------------------------------------------------------------
# Utility helpers
# ------------------------------------------------------------


def load_json(path: Path):
    with path.open("r", encoding="utf-8") as f:
        return json.load(f)


def write_json(path: Path, data: dict, pretty=True):
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8") as f:
        if pretty:
            json.dump(data, f, indent=2, ensure_ascii=False)
        else:
            json.dump(data, f)
        f.write("\n")


def list_schema_files(schema_root: Path):
    return sorted(schema_root.rglob("*.schema.json"))


# ------------------------------------------------------------
# Example generation strategies
# ------------------------------------------------------------


def generate_minimal_example(schema: dict):
    """Generate the smallest valid object allowed by the schema."""
    result = {}
    required = schema.get("required", [])
    props = schema.get("properties", {})

    # Special case for items_model: always generate valid 'model' (object, not None)
    if "model" in required and "model" in props:
        val = generate_value_for_schema(props["model"], minimal=True)
        if val is None:
            val = {"type": "minecraft:model", "model": "example_model"}
        result["model"] = val

    for key in required:
        if key == "model":
            continue
        if key in props:
            val = generate_value_for_schema(props[key], minimal=True)
            # entity_nbt.Passengers: always valid object in array
            if key == "Passengers" and isinstance(val, list):
                val = [{"id": "minecraft:stone"}]
            result[key] = val

    # Special case for minecraft_nbt_full: minimal must match only one referenced schema
    if "oneOf" in schema:
        from jsonschema import Draft202012Validator

        for subschema_ref in schema["oneOf"]:
            ref = subschema_ref.get("$ref")
            if ref:
                # Load referenced schema
                import os

                import requests

                # Try local path first
                local_path = None
                if ref.startswith(
                    "https://github.com/Mosberg/minecraft-data-docs/tree/main/"
                ):
                    rel_path = ref.split("projects/minecraft-data-docs/")[-1]
                    local_path = Path(os.path.join("minecraft-data-docs", rel_path))
                if local_path and local_path.exists():
                    ref_schema = load_json(local_path)
                else:
                    try:
                        ref_schema = requests.get(ref).json()
                    except Exception:
                        continue
                candidate = generate_minimal_example(ref_schema)
                # Validate against all schemas in oneOf
                matches = 0
                for other_ref in schema["oneOf"]:
                    other_ref_url = other_ref.get("$ref")
                    if other_ref_url:
                        # Try local path first
                        other_local_path = None
                        if other_ref_url.startswith(
                            "https://github.com/Mosberg/minecraft-data-docs/tree/main/"
                        ):
                            rel_path = other_ref_url.split(
                                "projects/minecraft-data-docs/"
                            )[-1]
                            other_local_path = Path(
                                os.path.join("minecraft-data-docs", rel_path)
                            )
                        if other_local_path and other_local_path.exists():
                            other_schema = load_json(other_local_path)
                        else:
                            try:
                                other_schema = requests.get(other_ref_url).json()
                            except Exception:
                                continue
                        try:
                            Draft202012Validator(other_schema).validate(candidate)
                            matches += 1
                        except Exception:
                            pass
                if matches == 1:
                    return candidate
        # Fallback: just pick first referenced schema
        subschema_ref = schema["oneOf"][0]
        ref = subschema_ref.get("$ref")
        if ref:
            # Try local path first
            rel_path = ref.split("projects/minecraft-data-docs/")[-1]
            local_path = Path(os.path.join("minecraft-data-docs", rel_path))
            if local_path.exists():
                ref_schema = load_json(local_path)
                return generate_minimal_example(ref_schema)
        return {"id": "minecraft:stone"}
    return result


def generate_typical_example(schema: dict):
    """Generate a typical example with all common fields."""
    result = {}
    props = schema.get("properties", {})

    # Special case for items_model: always generate valid 'model' (object, not None)
    if "model" in props:
        val = generate_value_for_schema(props["model"], minimal=True)
        if val is None:
            val = {"type": "minecraft:model", "model": "example_model"}
        result["model"] = val

    for key, subschema in props.items():
        if key == "model":
            continue
        val = generate_value_for_schema(subschema, minimal=False)
        # entity_nbt.Passengers: always valid object in array
        if key == "Passengers" and isinstance(val, list):
            val = [{"id": "minecraft:stone"}]
        result[key] = val

    # Special case for minecraft_nbt_full: typical must match only one referenced schema
    if "oneOf" in schema:
        from jsonschema import Draft202012Validator

        for subschema_ref in schema["oneOf"]:
            ref = subschema_ref.get("$ref")
            if ref:
                import os

                import requests

                local_path = None
                if ref.startswith(
                    "https://github.com/Mosberg/minecraft-data-docs/tree/main/"
                ):
                    rel_path = ref.split("projects/minecraft-data-docs/")[-1]
                    local_path = Path(os.path.join("minecraft-data-docs", rel_path))
                if local_path and local_path.exists():
                    ref_schema = load_json(local_path)
                else:
                    try:
                        ref_schema = requests.get(ref).json()
                    except Exception:
                        continue
                candidate = generate_typical_example(ref_schema)
                matches = 0
                for other_ref in schema["oneOf"]:
                    other_ref_url = other_ref.get("$ref")
                    if other_ref_url:
                        other_local_path = None
                        if other_ref_url.startswith(
                            "https://github.com/Mosberg/minecraft-data-docs/tree/main/"
                        ):
                            rel_path = other_ref_url.split(
                                "projects/minecraft-data-docs/"
                            )[-1]
                            other_local_path = Path(
                                os.path.join("minecraft-data-docs", rel_path)
                            )
                        if other_local_path and other_local_path.exists():
                            other_schema = load_json(other_local_path)
                        else:
                            try:
                                other_schema = requests.get(other_ref_url).json()
                            except Exception:
                                continue
                        try:
                            Draft202012Validator(other_schema).validate(candidate)
                            matches += 1
                        except Exception:
                            pass
                if matches == 1:
                    return candidate
        subschema_ref = schema["oneOf"][0]
        ref = subschema_ref.get("$ref")
        if ref:
            rel_path = ref.split("projects/minecraft-data-docs/")[-1]
            local_path = Path(os.path.join("minecraft-data-docs", rel_path))
            if local_path.exists():
                ref_schema = load_json(local_path)
                return generate_typical_example(ref_schema)
        return {"id": "minecraft:stone"}
    return result


def generate_maximal_example(schema: dict):
    """Generate an example that includes all fields."""
    result = {}
    props = schema.get("properties", {})

    # Special case for items_model: always generate valid 'model' (object, not None)
    if "model" in props:
        val = generate_value_for_schema(props["model"], minimal=True)
        if val is None:
            val = {"type": "minecraft:model", "model": "example_model"}
        result["model"] = val

    for key, subschema in props.items():
        if key == "model":
            continue
        val = generate_value_for_schema(subschema, minimal=False, maximal=True)
        # entity_nbt.Passengers: always valid object in array
        if key == "Passengers" and isinstance(val, list):
            val = [{"id": "minecraft:stone"}]
        result[key] = val

    # Special case for minecraft_nbt_full: maximal must match only one referenced schema
    if "oneOf" in schema:
        from jsonschema import Draft202012Validator

        for subschema_ref in schema["oneOf"]:
            ref = subschema_ref.get("$ref")
            if ref:
                import os

                import requests

                local_path = None
                if ref.startswith(
                    "https://github.com/Mosberg/minecraft-data-docs/tree/main/"
                ):
                    rel_path = ref.split("projects/minecraft-data-docs/")[-1]
                    local_path = Path(os.path.join("minecraft-data-docs", rel_path))
                if local_path and local_path.exists():
                    ref_schema = load_json(local_path)
                else:
                    try:
                        ref_schema = requests.get(ref).json()
                    except Exception:
                        continue
                candidate = generate_maximal_example(ref_schema)
                matches = 0
                for other_ref in schema["oneOf"]:
                    other_ref_url = other_ref.get("$ref")
                    if other_ref_url:
                        other_local_path = None
                        if other_ref_url.startswith(
                            "https://github.com/Mosberg/minecraft-data-docs/tree/main/"
                        ):
                            rel_path = other_ref_url.split(
                                "projects/minecraft-data-docs/"
                            )[-1]
                            other_local_path = Path(
                                os.path.join("minecraft-data-docs", rel_path)
                            )
                        if other_local_path and other_local_path.exists():
                            other_schema = load_json(other_local_path)
                        else:
                            try:
                                other_schema = requests.get(other_ref_url).json()
                            except Exception:
                                continue
                        try:
                            Draft202012Validator(other_schema).validate(candidate)
                            matches += 1
                        except Exception:
                            pass
                if matches == 1:
                    return candidate
        subschema_ref = schema["oneOf"][0]
        ref = subschema_ref.get("$ref")
        if ref:
            rel_path = ref.split("projects/minecraft-data-docs/")[-1]
            local_path = Path(os.path.join("minecraft-data-docs", rel_path))
            if local_path.exists():
                ref_schema = load_json(local_path)
                return generate_maximal_example(ref_schema)
        return {"id": "minecraft:stone"}
    return result


def generate_edge_case_examples(schema: dict):
    """Generate a list of edge-case examples."""
    examples = []
    props = schema.get("properties", {})
    required = schema.get("required", [])

    for key, subschema in props.items():
        if "type" in subschema:
            if subschema["type"] == "string":
                ex1 = {key: ""}
                ex2 = {key: "x" * 256}
                # Always include required 'id' for item_nbt
                if "id" in required and key != "id":
                    ex1["id"] = "minecraft:stone"
                    ex2["id"] = "minecraft:stone"
                examples.append(ex1)
                examples.append(ex2)
            elif subschema["type"] == "integer":
                ex1 = {key: subschema.get("minimum", -999999)}
                ex2 = {key: subschema.get("maximum", 999999)}
                if "id" in required and key != "id":
                    ex1["id"] = "minecraft:stone"
                    ex2["id"] = "minecraft:stone"
                examples.append(ex1)
                examples.append(ex2)
            elif subschema["type"] == "boolean":
                ex1 = {key: True}
                ex2 = {key: False}
                if "id" in required and key != "id":
                    ex1["id"] = "minecraft:stone"
                    ex2["id"] = "minecraft:stone"
                examples.append(ex1)
                examples.append(ex2)

    # Special case for items_model: always include valid 'model' in edge cases
    if "model" in required and "model" in props:
        for ex in examples:
            ex["model"] = generate_value_for_schema(props["model"], minimal=True)

    return examples


# ------------------------------------------------------------
# Value generator for schema fields
# ------------------------------------------------------------


def generate_value_for_schema(schema: dict, minimal=False, maximal=False):
    t = schema.get("type")

    # Handle oneOf for objects (e.g., items_model)
    if "oneOf" in schema and t == "object":
        subschema_ref = schema["oneOf"][0]
        ref = subschema_ref.get("$ref")
        if ref and ref.startswith("#/definitions/"):
            def_name = ref.split("/")[-1]
            if "definitions" in schema:
                return generate_value_for_schema(
                    schema["definitions"][def_name], minimal=minimal, maximal=maximal
                )
        # Fallback: return a valid modelType object
        return {"type": "minecraft:model", "model": "example_model"}

    if t == "string":
        enum = schema.get("enum")
        if enum:
            return enum[0] if minimal else enum[-1]
        const = schema.get("const")
        if const:
            return const
        return "example" if not minimal else ""

    if t == "integer":
        if minimal:
            return schema.get("minimum", 0)
        if maximal:
            return schema.get("maximum", 42)
        return 1

    if t == "number":
        if minimal:
            return schema.get("minimum", 0.0)
        if maximal:
            return schema.get("maximum", 42.0)
        return 1.5

    if t == "boolean":
        return True

    if t == "array":
        item_schema = schema.get("items", {})
        min_items = schema.get("minItems", 0)
        max_items = schema.get("maxItems")
        if minimal:
            count = min_items if min_items > 0 else 1
        elif maximal and max_items:
            count = max_items
        else:
            count = min_items if min_items > 0 else 1
        arr = []
        for _ in range(count):
            val = generate_value_for_schema(item_schema, minimal=True)
            # Always ensure valid object for entity_nbt.Passengers
            if isinstance(val, dict) and "id" in item_schema.get("properties", {}):
                val["id"] = "minecraft:stone"
            if val is None and "id" in item_schema.get("properties", {}):
                val = {"id": "minecraft:stone"}
            arr.append(val)
        # Always at least one valid object for entity_nbt.Passengers
        if "id" in item_schema.get("properties", {}) and not arr:
            arr = [{"id": "minecraft:stone"}]
        # If all elements are None, replace with valid object
        if "id" in item_schema.get("properties", {}) and all(v is None for v in arr):
            arr = [{"id": "minecraft:stone"}]
        return arr

    if t == "object":
        result = {}
        props = schema.get("properties", {})
        required = schema.get("required", [])

        # Always include required 'id' property if present
        if "id" in props and "id" in required:
            result["id"] = "minecraft:stone"

        # minimal: only required fields
        if minimal:
            for key in required:
                if key in props and key not in result:
                    result[key] = generate_value_for_schema(props[key], minimal=True)
            return result

        # typical: include all fields
        for key, subschema in props.items():
            if key not in result:
                result[key] = generate_value_for_schema(subschema, minimal=False)
        return result

    # Fallback for minecraft_nbt_full: pick first referenced schema
    if "oneOf" in schema:
        subschema_ref = schema["oneOf"][0]
        ref = subschema_ref.get("$ref")
        if ref and "item_nbt" in ref:
            return {"id": "minecraft:stone", "Count": 1}
        if ref and "block_nbt" in ref:
            return {"Name": "minecraft:stone"}
        if ref and "entity_nbt" in ref:
            return {"id": "minecraft:stone", "Passengers": [{"id": "minecraft:stone"}]}
        if ref and "armor_stand_nbt" in ref:
            return {"id": "minecraft:stone", "Rotation": [0.0, 0.0]}
        if ref and "potion_nbt" in ref:
            return {"Potion": "minecraft:water"}
        if ref and "turtle_nbt" in ref:
            return {"id": "minecraft:stone"}
        if ref and "spawner_nbt" in ref:
            return {"id": "minecraft:stone"}
        if ref and "item_frame_nbt" in ref:
            return {"id": "minecraft:stone"}
        if ref and "falling_block_nbt" in ref:
            return {"id": "minecraft:stone"}
        if ref and "villager_nbt" in ref:
            return {"id": "minecraft:stone"}
        return {"id": "minecraft:stone"}

    # fallback
    return None


# ------------------------------------------------------------
# Main generator logic
# ------------------------------------------------------------


import collections


def canonical_order(obj):
    if isinstance(obj, dict):
        return collections.OrderedDict(
            sorted((k, canonical_order(v)) for k, v in obj.items())
        )
    if isinstance(obj, list):
        return [canonical_order(x) for x in obj]
    return obj


def generate_full_example(schema: dict):
    # For now, treat as maximal, but can be refined to include only 'commonly used' fields if doc hints are available
    return generate_maximal_example(schema)


def generate_thematic_example(schema: dict):
    # For now, use a placeholder. In future, use doc hints for themes (e.g., biome, holiday)
    ex = generate_typical_example(schema)
    if "color" in ex:
        ex["color"] = "red-green"
    return ex


def generate_performance_example(schema: dict):
    ex = generate_typical_example(schema)
    for k, v in ex.items():
        if isinstance(v, list):
            ex[k] = v * 10
        if isinstance(v, int):
            ex[k] = 9999999
        if isinstance(v, float):
            ex[k] = 1e10
    return ex


def generate_experimental_example(schema: dict):
    ex = generate_maximal_example(schema)
    return ex


def generate_vanilla_example(schema: dict):
    return generate_typical_example(schema)


def generate_modded_example(schema: dict):
    ex = generate_maximal_example(schema)
    for k in ex:
        if "mod" in k:
            ex[k] = True
    return ex


def generate_examples_for_schema(
    schema_path: Path, spec: dict, output_root: Path, example_types=None
):
    schema = load_json(schema_path)
    schema_name = schema_path.stem.replace(".schema", "")
    schema_output_dir = output_root / schema_name

    resolver = RefResolver(base_uri=schema_path.as_uri(), referrer=schema)
    validator = Draft202012Validator(schema, resolver=resolver)

    def validate_example(name, data):
        try:
            validator.validate(data)
        except Exception as e:
            print(
                f"[ERROR] Example '{name}' failed validation for schema {schema_name}: {e}"
            )
            return False
        return True

    if example_types is None:
        example_types = [
            "minimal",
            "typical",
            "full",
            "maximal",
            "thematic",
            "performance",
            "experimental",
            "vanilla",
            "modded",
            "edge_cases",
        ]

    generators = {
        "minimal": generate_minimal_example,
        "typical": generate_typical_example,
        "full": generate_full_example,
        "maximal": generate_maximal_example,
        "thematic": generate_thematic_example,
        "performance": generate_performance_example,
        "experimental": generate_experimental_example,
        "vanilla": generate_vanilla_example,
        "modded": generate_modded_example,
    }

    for ex_type in example_types:
        if ex_type == "edge_cases":
            edge_dir = schema_output_dir / "edge_cases"
            edge_dir.mkdir(parents=True, exist_ok=True)
            edge_cases = generate_edge_case_examples(schema)
            for idx, ex in enumerate(edge_cases):
                ex = canonical_order(ex)
                if validate_example(f"edge-case-{idx+1}", ex):
                    out_path = edge_dir / f"edge-case-{idx+1}.json"
                    write_json(out_path, ex, pretty=True)
                    print(f"[OK] Wrote {out_path}")
        else:
            gen = generators.get(ex_type)
            if gen:
                ex = canonical_order(gen(schema))
                if validate_example(ex_type, ex):
                    out_path = schema_output_dir / f"{ex_type}.json"
                    write_json(out_path, ex, pretty=True)
                    print(f"[OK] Wrote {out_path}")


# ------------------------------------------------------------
# Entry point
# ------------------------------------------------------------


def main():
    root = Path(__file__).resolve().parent.parent
    spec_path = root / "minecraft-data-docs/generate-example-json-files.json"
    spec_schema_path = (
        root
        / "minecraft-data-docs/schemas/generator/generate-example-json-files.schema.json"
    )

    # Load and validate spec
    spec = load_json(spec_path)
    spec_schema = load_json(spec_schema_path)

    validate(instance=spec, schema=spec_schema)

    schema_root = root / spec["input"]["schema_root"]
    output_root = root / spec["output"]["root"]

    schema_files = list_schema_files(schema_root)

    print(f"Found {len(schema_files)} schema files")

    example_types = None
    if (
        "rules" in spec
        and "generation" in spec["rules"]
        and "example_types" in spec["rules"]["generation"]
    ):
        example_types = spec["rules"]["generation"]["example_types"]

    for schema_path in schema_files:
        print(f"Generating examples for {schema_path}")
        generate_examples_for_schema(
            schema_path, spec, output_root, example_types=example_types
        )

    print("Done.")


if __name__ == "__main__":
    main()
