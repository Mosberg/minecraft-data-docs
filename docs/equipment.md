# Minecraft Equipment Model

**Schema:** [schemas/equipment.schema.json](../schemas/equipment.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Armor](https://minecraft.wiki/w/Armor)

## Overview

The equipment model format defines the rendering and layering of wearable items such as armor in Minecraft. It specifies how different equipment layers (helmet, chestplate, leggings, boots, etc.) are rendered, including support for dyeable layers and player textures.

## Structure

| Name   | Type   | Required | Description                              |
| ------ | ------ | -------- | ---------------------------------------- |
| layers | object | Yes      | Equipment layer definitions (see below). |

### layers

A mapping from layer type (e.g., `helmet`, `chestplate`) to an array of layer definitions. Each layer definition can include:

- `texture` (string, required): Namespaced texture ID.
- `dyeable` (object, optional): Dye behavior, with `color_when_undyed` (integer RGB).
- `use_player_texture` (boolean, optional): If true, uses the player's skin texture for this layer.

#### Example

```json
{
  "layers": {
    "helmet": [{ "texture": "minecraft:armor/diamond_layer_1" }],
    "chestplate": [
      { "texture": "minecraft:armor/diamond_layer_1", "dyeable": { "color_when_undyed": 10511680 } }
    ]
  }
}
```

## See Also

- [Item Models](item-models.md)
- [Minecraft Wiki: Armor](https://minecraft.wiki/w/Armor)
