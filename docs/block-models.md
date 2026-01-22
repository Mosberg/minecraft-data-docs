# Minecraft Block Models

**Schema:** [schemas/block_model.schema.json](../schemas/block_model.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Model](https://minecraft.wiki/w/Model)

## Overview

Block models define the 3D geometry, textures, and rendering properties for blocks in Minecraft. They are used in resource packs and data packs to control how blocks appear in the game.

## Structure

| Name             | Type    | Required | Description                                                         |
| ---------------- | ------- | -------- | ------------------------------------------------------------------- |
| parent           | string  | No       | Parent model to inherit from.                                       |
| ambientocclusion | boolean | No       | Enables/disables ambient occlusion.                                 |
| textures         | object  | No       | Texture variables for the model.                                    |
| elements         | array   | No       | List of cuboid elements that make up the model.                     |
| display          | object  | No       | Display transforms for different contexts (GUI, hand, ground, etc). |
| name             | string  | No       | Optional name for the model.                                        |
| texture_size     | array   | No       | [width, height] of the texture atlas.                               |

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
  "parent": "block/cube_all",
  "textures": { "all": "minecraft:block/stone" }
}
```

## Common Real-World Example

```json
{
  "parent": "block/cube_bottom_top",
  "textures": {
    "top": "minecraft:block/grass_block_top",
    "bottom": "minecraft:block/dirt",
    "side": "minecraft:block/grass_block_side"
  },
  "elements": [
    {
      "from": [0, 0, 0],
      "to": [16, 16, 16],
      "faces": {
        "north": { "texture": "#side" },
        "south": { "texture": "#side" },
        "east": { "texture": "#side" },
        "west": { "texture": "#side" },
        "up": { "texture": "#top" },
        "down": { "texture": "#bottom" }
      }
    }
  ]
}
```

## See Also

- [Block States](block-states.md)
- [Minecraft Wiki: Model](https://minecraft.wiki/w/Model)
