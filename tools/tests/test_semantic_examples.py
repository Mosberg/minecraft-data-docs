import json
from pathlib import Path


from tools.generateExampleJsonFiles import (
    generate_block_model_minimal,
    generate_block_model_typical,
    generate_item_model_minimal,
    generate_item_model_typical,
    generate_nbt_minimal,
    generate_nbt_typical,
)

ROOT = Path(__file__).resolve().parents[2]


def load_schema(name: str) -> dict:
    path = next((ROOT / "schemas").rglob(name))
    return json.loads(path.read_text(encoding="utf-8"))


def test_block_model_minimal_semantics():
    schema = load_schema("block_model.schema.json")
    ex = generate_block_model_minimal(schema)
    assert ex["parent"] in ["block/cube_all", "block/cube"]
    assert "textures" in ex
    assert "elements" in ex
    assert len(ex["elements"]) == 1
    elem = ex["elements"][0]
    assert elem["from"] == [0, 0, 0]
    assert elem["to"] == [16, 16, 16]


def test_block_model_typical_semantics():
    schema = load_schema("block_model.schema.json")
    ex = generate_block_model_typical(schema)
    assert ex["textures"]["particle"].startswith("minecraft:block/")
    assert "display" in ex
    assert "gui" in ex["display"]


def test_item_model_minimal_semantics():
    schema = load_schema("item_model.schema.json")
    ex = generate_item_model_minimal(schema)
    assert ex["parent"] in ["item/generated", "item/handheld"]
    assert "textures" in ex
    assert "layer0" in ex["textures"]


def test_item_model_typical_semantics():
    schema = load_schema("item_model.schema.json")
    ex = generate_item_model_typical(schema)
    assert ex["textures"]["layer0"].startswith("minecraft:item/")
    assert "display" in ex


def test_nbt_minimal_semantics_item():
    schema = load_schema("item_nbt.schema.json")
    path = next((ROOT / "schemas/nbt").rglob("item_nbt.schema.json"))
    ex = generate_nbt_minimal(schema, path)
    assert ex["id"].startswith("minecraft:")
    assert "Count" in ex


def test_nbt_typical_semantics_entity():
    schema = load_schema("entity_nbt.schema.json")
    path = next((ROOT / "schemas/nbt").rglob("entity_nbt.schema.json"))
    ex = generate_nbt_typical(schema, path)
    assert ex["id"].startswith("minecraft:")
    assert "Passengers" in ex or "CustomName" in ex
