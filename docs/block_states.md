# Block States

- [Block States Schema](../schemas/block_states.schema.json)

Block states define how a block selects its model based on its properties.
Some blocks (e.g., doors) have multiple variants, while others use multiple models simultaneously through the **multipart** system.

Blockstate files are stored in:

```
assets/<namespace>/blockstates/
```

The filename determines which block the file applies to.

---

## Blockstate File Structure

A blockstate file may contain:

- **`variants`** — maps specific state combinations to one or more models
- **`multipart`** — applies multiple models conditionally, allowing complex compositions

---

# Examples

## Wall Torch

**File:** `assets/minecraft/blockstates/wall_torch.json`

```json
{
  "variants": {
    "facing=east": { "model": "block/wall_torch" },
    "facing=south": { "model": "block/wall_torch", "y": 90 },
    "facing=west": { "model": "block/wall_torch", "y": 180 },
    "facing=north": { "model": "block/wall_torch", "y": 270 }
  }
}
```

A wall torch can face four directions.
Each variant rotates the same model around the **Y axis**.

---

## Grass Block

**File:** `assets/minecraft/blockstates/grass_block.json`

```json
{
  "variants": {
    "snowy=false": [
      { "model": "block/grass_block" },
      { "model": "block/grass_block", "y": 90 },
      { "model": "block/grass_block", "y": 180 },
      { "model": "block/grass_block", "y": 270 }
    ],
    "snowy=true": { "model": "block/grass_block_snow" }
  }
}
```

The non‑snowy variant randomly selects one of four rotated models (25% each).
The snowy variant uses a single model.

---

## Oak Fence

**File:** `assets/minecraft/blockstates/oak_fence.json`

```json
{
  "multipart": [
    { "apply": { "model": "block/oak_fence_post" } },

    { "when": { "north": "true" }, "apply": { "model": "block/oak_fence_side", "uvlock": true } },

    {
      "when": { "east": "true" },
      "apply": { "model": "block/oak_fence_side", "y": 90, "uvlock": true }
    },

    {
      "when": { "south": "true" },
      "apply": { "model": "block/oak_fence_side", "y": 180, "uvlock": true }
    },

    {
      "when": { "west": "true" },
      "apply": { "model": "block/oak_fence_side", "y": 270, "uvlock": true }
    }
  ]
}
```

The post model is always applied.
Side models appear only when connected to adjacent blocks.

---

## Redstone Wire

**File:** `assets/minecraft/blockstates/redstone_wire.json`

```json
{
  "multipart": [
    {
      "when": {
        "OR": [
          { "north": "none", "east": "none", "south": "none", "west": "none" },
          { "north": "side|up", "east": "side|up" },
          { "east": "side|up", "south": "side|up" },
          { "south": "side|up", "west": "side|up" },
          { "west": "side|up", "north": "side|up" }
        ]
      },
      "apply": { "model": "block/redstone_dust_dot" }
    },

    {
      "when": {
        "OR": [
          { "north": "side|up" },
          { "north": "none", "east": "none", "south": "side|up", "west": "none" }
        ]
      },
      "apply": { "model": "block/redstone_dust_side0" }
    },

    {
      "when": {
        "OR": [
          { "south": "side|up" },
          { "north": "side|up", "east": "none", "south": "none", "west": "none" }
        ]
      },
      "apply": { "model": "block/redstone_dust_side_alt0" }
    },

    {
      "when": {
        "OR": [
          { "east": "side|up" },
          { "north": "none", "east": "none", "south": "none", "west": "side|up" }
        ]
      },
      "apply": { "model": "block/redstone_dust_side_alt1", "y": 270 }
    },

    {
      "when": {
        "OR": [
          { "west": "side|up" },
          { "north": "none", "east": "side|up", "south": "none", "west": "none" }
        ]
      },
      "apply": { "model": "block/redstone_dust_side1", "y": 270 }
    },

    { "when": { "north": "up" }, "apply": { "model": "block/redstone_dust_up" } },
    { "when": { "east": "up" }, "apply": { "model": "block/redstone_dust_up", "y": 90 } },
    { "when": { "south": "up" }, "apply": { "model": "block/redstone_dust_up", "y": 180 } },
    { "when": { "west": "up" }, "apply": { "model": "block/redstone_dust_up", "y": 270 } }
  ]
}
```

This multipart file dynamically assembles the redstone wire model based on its connections.

````

---

# 📦 Block States — JSON Schema‑Style Representation (`block_states.schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Minecraft Blockstate File",
  "type": "object",

  "properties": {
    "variants": {
      "type": "object",
      "additionalProperties": {
        "oneOf": [
          {
            "type": "object",
            "properties": {
              "model": { "type": "string" },
              "x": { "type": "number" },
              "y": { "type": "number" },
              "z": { "type": "number" },
              "uvlock": { "type": "boolean" },
              "weight": { "type": "integer" }
            }
          },
          {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "model": { "type": "string" },
                "x": { "type": "number" },
                "y": { "type": "number" },
                "z": { "type": "number" },
                "uvlock": { "type": "boolean" },
                "weight": { "type": "integer" }
              }
            }
          }
        ]
      }
    },

    "multipart": {
      "type": "array",
      "items": {
        "type": "object",

        "properties": {
          "when": {
            "type": "object",
            "additionalProperties": true
          },

          "apply": {
            "type": "object",
            "properties": {
              "model": { "type": "string" },
              "x": { "type": "number" },
              "y": { "type": "number" },
              "z": { "type": "number" },
              "uvlock": { "type": "boolean" },
              "weight": { "type": "integer" }
            }
          }
        }
      }
    }
  }
}
````
