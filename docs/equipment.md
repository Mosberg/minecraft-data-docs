# Equipment

- [Equipment Schema](../schemas/equipment.schema.json)

Custom equipment models can be defined and referenced by the **equippable item component**.
Equipment definitions are stored in:

```
assets/<namespace>/equipment/
```

Each file defines how an equipment item renders on specific entity slots.

---

## Root Structure

### `layers` (compound)

Defines the layer types for this equipment model.
If a layer type is omitted, the armor piece does **not** render in that slot
(except for the **head** slot, which falls back to the regular item model).

Each layer type contains:

#### Layer Definitions (list)

##### `texture` (string)

A namespaced ID pointing to a texture for this layer.

```
namespace:path
→ assets/<namespace>/textures/entity/equipment/<layer_type>/<path>.png
```

##### `dyeable` (compound, optional)

Controls how the layer behaves when the item is dyed.

- `color_when_undyed` (int, optional)
  RGB integer (decimal).
  If omitted and the item is **not dyed**, the layer is **hidden**.

##### `use_player_texture` (boolean, optional, default: false)

If `true`, the layer texture is overridden by a player‑provided texture.
Currently used only for the `wings` layer type (uses the player’s cape texture).

---

# Equipment Layer Types

Equipment layer types correspond to specific inventory slots:

| Layer Type              | Inventory Slot Description                        |
| ----------------------- | ------------------------------------------------- |
| `wolf_body`             | Wolf armor slot                                   |
| `horse_body`            | Horse armor slot                                  |
| `llama_body`            | Llama carpet slot                                 |
| `humanoid`              | Humanoid head, chest, or feet slot                |
| `humanoid_leggings`     | Humanoid legs slot                                |
| `wings`                 | Humanoid chest slot (requires `glider` component) |
| `pig_saddle`            | Pig saddle slot                                   |
| `strider_saddle`        | Strider saddle slot                               |
| `camel_saddle`          | Camel saddle slot                                 |
| `horse_saddle`          | Horse saddle slot                                 |
| `donkey_saddle`         | Donkey saddle slot                                |
| `mule_saddle`           | Mule saddle slot                                  |
| `skeleton_horse_saddle` | Skeleton Horse saddle slot                        |
| `zombie_horse_saddle`   | Zombie Horse saddle slot                          |
| `happy_ghast_body`      | Happy Ghast body slot                             |
| `nautilus_body`         | Nautilus / Zombie Nautilus body slot              |
| `nautilus_saddle`       | Nautilus / Zombie Nautilus saddle slot            |
| `camel_husk_saddle`     | Camel Husk saddle slot                            |

---

# 📦 Equipment JSON Schema (`equipment.schema.json`)

```json
{
  "$schema": "http://json-schema.org/draft-07/schema#",
  "title": "Minecraft Equipment Definition",
  "type": "object",

  "properties": {
    "layers": {
      "type": "object",
      "description": "Equipment layer types for this model.",
      "additionalProperties": {
        "type": "array",
        "description": "List of layer definitions for this layer type.",
        "items": {
          "type": "object",
          "properties": {
            "texture": {
              "type": "string",
              "description": "Namespaced ID for the layer texture."
            },

            "dyeable": {
              "type": "object",
              "description": "Dye behavior for this layer.",
              "properties": {
                "color_when_undyed": {
                  "type": "integer",
                  "description": "RGB integer used when item is undyed."
                }
              },
              "additionalProperties": false
            },

            "use_player_texture": {
              "type": "boolean",
              "description": "Whether to override the texture with a player-provided one.",
              "default": false
            }
          },
          "required": ["texture"],
          "additionalProperties": false
        }
      }
    }
  },

  "required": ["layers"],
  "additionalProperties": false
}
```

---
