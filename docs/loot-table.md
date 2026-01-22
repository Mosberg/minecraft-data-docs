# Minecraft Loot Table

**Schema:** [schemas/loot_table.schema.json](../schemas/loot_table.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Loot Table](https://minecraft.wiki/w/Loot_table)

## Overview

Loot tables define the items, experience, and other rewards that can be generated in Minecraft from blocks, entities, chests, and more. They are a core part of the game's data-driven loot system.

## Structure

| Name      | Type   | Required | Description                                                    |
| --------- | ------ | -------- | -------------------------------------------------------------- |
| type      | string | No       | Loot table type (e.g., `minecraft:block`, `minecraft:entity`). |
| pools     | array  | No       | List of loot pools, each defining possible drops.              |
| functions | array  | No       | List of functions to apply to the loot.                        |

> **Note:** Additional properties are allowed for extensibility and custom loot table features.

## Smallest Valid Example

```json
{
  "type": "minecraft:block"
}
```

## Common Real-World Example

```json
{
  "type": "minecraft:block",
  "pools": [
    {
      "rolls": 1,
      "entries": [{ "type": "item", "name": "minecraft:diamond" }]
    }
  ]
}
```

## See Also

- [Minecraft Wiki: Loot Table](https://minecraft.wiki/w/Loot_table)
