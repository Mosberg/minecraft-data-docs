# Boolean Property Types (for `minecraft:condition`)

- [Items Models Schema (Hybrid JSON Schema)](../schemas/items_model.schema.json#conditionType)

Used in `property` for `minecraft:condition` models.

Common structure:

```jsonc
{
  "type": "minecraft:condition",
  "property": "minecraft:damaged",
  "on_true": { ... },
  "on_false": { ... }
}
```

Supported boolean properties:

- `minecraft:broken`
- `minecraft:bundle/has_selected_item`
- `minecraft:carried`
- `minecraft:component`
- `minecraft:damaged`
- `minecraft:extended_view`
- `minecraft:fishing_rod/cast`
- `minecraft:has_component`
- `minecraft:keybind_down`
- `minecraft:selected`
- `minecraft:using_item`
- `minecraft:view_entity`
- `minecraft:custom_model_data`

Only some require extra fields:

---

## `minecraft:component`

```jsonc
{
  "type": "minecraft:condition",
  "property": "minecraft:component",
  "predicate": "minecraft:some_predicate",
  "value": "...",
}
```

- `predicate` (string) — ID in `minecraft:data_component_predicate_type`.
- `value` (string) — value to match.

---

## `minecraft:has_component`

```jsonc
{
  "type": "minecraft:condition",
  "property": "minecraft:has_component",
  "component": "minecraft:some_component",
  "ignore_default": false,
}
```

- `component` (string) — component name.
- `ignore_default` (boolean, optional, default `false`).

---

## `minecraft:keybind_down`

```jsonc
{
  "type": "minecraft:condition",
  "property": "minecraft:keybind_down",
  "keybind": "key.jump",
}
```

- `keybind` (string) — keybind ID.

---

## `minecraft:custom_model_data` (boolean)

```jsonc
{
  "type": "minecraft:condition",
  "property": "minecraft:custom_model_data",
  "index": 0,
}
```

- `index` (int, optional, default `0`) — index in `flags` list.

Other boolean properties (`broken`, `damaged`, `carried`, `extended_view`, `fishing_rod/cast`, `selected`, `using_item`, `view_entity`, `bundle/has_selected_item`) have no extra fields.
