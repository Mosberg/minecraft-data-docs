# Minecraft Language File

**Schema:** [schemas/language.schema.json](../schemas/language.schema.json)
**Authoritative Reference:** [Minecraft Wiki: Language](https://minecraft.wiki/w/Language)

## Overview

Language files (`.lang` or `.json`) provide translations for in-game text, such as item names, tooltips, and UI elements. Each key maps to a localized string value.

## Structure

| Name              | Type   | Required | Description                             |
| ----------------- | ------ | -------- | --------------------------------------- |
| <translation key> | string | Yes      | The localized string for the given key. |

- The file is a flat object with arbitrary string keys and string values.
- No required keys; all are user-defined.

## Smallest Valid Example

```json
{
  "item.minecraft.diamond_sword": "Diamond Sword"
}
```

## Common Real-World Example

```json
{
  "item.minecraft.diamond_sword": "Diamond Sword",
  "block.minecraft.stone": "Stone",
  "menu.quit": "Quit Game"
}
```

## See Also

- [Minecraft Wiki: Language](https://minecraft.wiki/w/Language)
