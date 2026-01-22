# Minecraft Item Models

**Schema:** [schemas/item_model.schema.json](../schemas/item_model.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Item Model](https://minecraft.wiki/w/Item_model)

## Overview

Item models define the 3D geometry, textures, and rendering properties for items in Minecraft. They are used in resource packs and data packs to control how items appear in the game, both in the inventory and in the world.

## Structure

| Name         | Type   | Required | Description                                                         |
| ------------ | ------ | -------- | ------------------------------------------------------------------- |
| parent       | string | No       | Parent model to inherit from.                                       |
| textures     | object | No       | Texture variables for the model.                                    |
| gui_light    | string | No       | Lighting mode: `front` or `side`.                                   |
| elements     | array  | No       | List of cuboid elements that make up the model.                     |
| display      | object | No       | Display transforms for different contexts (GUI, hand, ground, etc). |
| name         | string | No       | Optional name for the model.                                        |
| texture_size | array  | No       | [width, height] of the texture atlas.                               |

### elements[]

Each element is a cuboid with properties:

- `from`, `to`: 3D coordinates (min/max corners)
- `rotation`: (optional) rotation origin, axis, angle, rescale
- `shade`: (optional) whether to shade the element
- `light_emission`: (optional) min light level
- `faces`: (optional) face definitions for each side

### faces

Each face can define:

- `uv`: [x1, y1, x2, y2] texture coordinates
- `texture`: texture variable name
- `cullface`: which face to cull
- `rotation`: rotation of the face
- `tintindex`: tint index for coloring

### display

Display transforms for different contexts (e.g., `thirdperson_righthand`, `gui`). Each transform can specify `rotation`, `translation`, and `scale` arrays.

## Smallest Valid Example

```json
{
  "parent": "item/generated",
  "textures": { "layer0": "minecraft:item/diamond_sword" }
}
```

## Common Real-World Example

```json
{
  "parent": "item/handheld",
  "textures": {
    "layer0": "minecraft:item/iron_pickaxe"
  },
  "display": {
    "thirdperson_righthand": {
      "rotation": [-80, 260, -40],
      "translation": [-1, 2, 2.5],
      "scale": [0.9, 0.9, 0.9]
    }
  }
}
```

## See Also

- [Block Models](block-models.md)
- [Minecraft Wiki: Item Model](https://minecraft.wiki/w/Item_model)
