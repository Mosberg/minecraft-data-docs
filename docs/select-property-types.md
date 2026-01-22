# Select Property Types (for `minecraft:select`)

- [Items Models Schema (Hybrid JSON Schema)](../schemas/items_model.schema.json#selectType)

Used in `property` for `minecraft:select` models.

Common structure:

```jsonc
{
  "type": "minecraft:select",
  "property": "minecraft:display_context",
  "cases": [
    { "when": "gui", "model": { ... } }
  ],
  "fallback": { ... }
}
```

Supported property types:

- `minecraft:block_state`
- `minecraft:charge_type`
- `minecraft:component`
- `minecraft:context_dimension`
- `minecraft:context_entity_type`
- `minecraft:display_context`
- `minecraft:local_time`
- `minecraft:main_hand`
- `minecraft:trim_material`
- `minecraft:custom_model_data`

---

## `minecraft:block_state`

```jsonc
{
  "property": "minecraft:block_state",
  "block_state_property": "some_property",
}
```

- `block_state_property` (string) — key in `minecraft:block_state` component.
  `when` values are strings.

---

## `minecraft:charge_type`

Values for `when`:

- `"none"`
- `"rocket"`
- `"arrow"`

---

## `minecraft:component`

```jsonc
{
  "property": "minecraft:component",
  "component": "minecraft:some_component",
}
```

- `component` (string) — namespaced component ID.
  `when` values depend on the component.

---

## `minecraft:context_dimension`

`when` values: namespaced dimension IDs.

---

## `minecraft:context_entity_type`

`when` values: namespaced entity type IDs.

---

## `minecraft:display_context`

`when` values:

- `none`
- `thirdperson_lefthand`
- `thirdperson_righthand`
- `firstperson_lefthand`
- `firstperson_righthand`
- `head`
- `gui`
- `ground`
- `fixed`
- `on_shelf`

---

## `minecraft:local_time`

```jsonc
{
  "property": "minecraft:local_time",
  "locale": "en_US",
  "time_zone": "Europe/Stockholm",
  "pattern": "HH:mm:ss",
}
```

- `locale` (string, optional)
- `time_zone` (string, optional)
- `pattern` (string, required)

`when` values: formatted strings.

---

## `minecraft:main_hand`

`when` values: `"left"` or `"right"`.

---

## `minecraft:trim_material`

`when` values: namespaced trim material IDs.

---

## `minecraft:custom_model_data` (string)

```jsonc
{
  "property": "minecraft:custom_model_data",
  "index": 0,
}
```

- `index` (int, optional, default `0`) — index in `strings` list.
  `when` values: strings.
