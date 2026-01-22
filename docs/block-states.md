# Minecraft Block States

**Schema:** [schemas/block_states.schema.json](../schemas/block_states.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Block states](https://minecraft.wiki/w/Block_states)

## Overview

Block state files define how a block's state properties (such as orientation, power, or other metadata) map to different block models. They are a core part of Minecraft's resource pack and data pack system, allowing blocks to have multiple visual or functional variants.

## Structure

| Name      | Type   | Required | Description                                                     |
| --------- | ------ | -------- | --------------------------------------------------------------- |
| variants  | object | No       | Maps property combinations to model definitions.                |
| multipart | array  | No       | List of conditional model applications for complex block logic. |

### variants

A mapping from property strings (e.g., `facing=north`) to either a single model object or an array of model objects. Each model object can include:

- `model` (string): Model resource location.
- `x`, `y`, `z` (number, optional): Rotation angles.
- `uvlock` (boolean, optional): Locks UV mapping.
- `weight` (integer, optional): Weight for random selection.

### multipart

An array of objects, each with:

- `when` (object): Conditions for applying the model (property-based logic).
- `apply` (object): Model definition to apply (same structure as above).

## Smallest Valid Example

```json
{
  "variants": {
    "": { "model": "block/stone" }
  }
}
```

## Common Real-World Example

```json
{
  "variants": {
    "facing=north": { "model": "block/stone" },
    "facing=south": { "model": "block/stone" }
  },
  "multipart": [
    {
      "when": { "powered": true },
      "apply": { "model": "block/lever_on" }
    }
  ]
}
```

## See Also

- [Block Models](block-models.md)
- [Minecraft Wiki: Block states](https://minecraft.wiki/w/Block_states)
