# Minecraft Items Model

**Schema:** [schemas/items_model.schema.json](../schemas/items_model.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Item Model](https://minecraft.wiki/w/Item_model)

## Overview

The items model format is used to define complex item rendering logic, including conditional, composite, and special-case models for items in Minecraft. This format is primarily used for advanced resource packs and modding scenarios, supporting features like custom tints, model selection, and property-based dispatch.

## Structure

| Name                   | Type    | Required | Description                                        |
| ---------------------- | ------- | -------- | -------------------------------------------------- |
| hand_animation_on_swap | boolean | No       | If true, plays hand animation when swapping items. |
| oversized_in_gui       | boolean | No       | If true, item is rendered oversized in GUI.        |
| swap_animation_scale   | number  | No       | Scale factor for swap animation.                   |
| model                  | object  | Yes      | The root model definition (see below).             |

### model (itemsModel)

The `model` property is a polymorphic object. Its `type` field determines its structure. Supported types:

- `minecraft:model`: Direct model reference with optional tints.
- `minecraft:composite`: Array of models rendered together.
- `minecraft:condition`: Conditional model selection based on item properties.
- `minecraft:select`: Selects a model from cases based on a property value.
- `minecraft:range_dispatch`: Selects a model based on a numeric property range.
- `minecraft:empty`: No model.
- `minecraft:bundle/selected_item`: Special bundle item rendering.
- `minecraft:special`: Special-case models (e.g., banners, beds, heads).

#### Example: Direct Model

```json
{
  "model": {
    "type": "minecraft:model",
    "model": "item/diamond_sword"
  }
}
```

#### Example: Conditional Model

```json
{
  "model": {
    "type": "minecraft:condition",
    "property": "minecraft:damaged",
    "on_true": { "type": "minecraft:model", "model": "item/used_sword" },
    "on_false": { "type": "minecraft:model", "model": "item/diamond_sword" }
  }
}
```

#### Example: Composite Model

```json
{
  "model": {
    "type": "minecraft:composite",
    "models": [
      { "type": "minecraft:model", "model": "item/diamond_sword" },
      { "type": "minecraft:model", "model": "item/enchantment_glint" }
    ]
  }
}
```

## See Also

- [Item Models](item-models.md)
- [Block Models](block-models.md)
- [Minecraft Wiki: Item Model](https://minecraft.wiki/w/Item_model)
