# Items Models Overview

- [Items Models Schema (Hybrid JSON Schema)](../schemas/items_model.schema.json)

Items models are JSON files that define how items are rendered and which model is selected based on components, context, and in‑game values.

They are stored in:

```text
assets/<namespace>/items/
```

The item’s model is chosen via the `minecraft:item_model` component, which references the items model at:

```text
assets/<namespace>/items/<id>.json
```

---

## Top‑Level JSON Format

```jsonc
{
  "hand_animation_on_swap": true,
  "oversized_in_gui": false,
  "swap_animation_scale": 1.0,
  "model": {
    // Items model object
  },
}
```

### `hand_animation_on_swap` (boolean, optional)

Whether a down‑and‑up animation plays in first‑person when the item slot changes.
Default: `true`.

### `oversized_in_gui` (boolean, optional)

Whether the item is allowed to render outside its slot in GUIs.
If `false`, rendering is clipped to the slot.
Default: `false`.

> Rendering outside slots is considered backward‑compatibility, not a fully supported feature.

### `swap_animation_scale` (float, optional)

Controls how fast the item moves up and down when swapping items in the hotbar.
Default: `1.0`.

### `model` (object, required)

The root **Items model** object. See `items_model_types.md`.

````

---

### `items_model_types.md`

```markdown
# Items Model Types

The `model` field is an **Items model object**:

```jsonc
{
  "type": "minecraft:model" // or other types
  // additional fields depending on type
}
````

## Common Structure

- `type` (string, required)
  One of:
  - `minecraft:model`
  - `minecraft:composite`
  - `minecraft:condition`
  - `minecraft:select`
  - `minecraft:range_dispatch`
  - `minecraft:empty`
  - `minecraft:bundle/selected_item`
  - `minecraft:special`

Additional fields depend on the chosen type.

---

## `minecraft:model`

Renders a plain model from the `models` directory.

```jsonc
{
  "type": "minecraft:model",
  "model": "namespace:path",
  "tints": [
    {
      "type": "minecraft:constant",
      // additional fields per tint source type
    },
  ],
}
```

- `model` (string, required) — namespaced ID of the model.
- `tints` (array, optional) — list of tint sources.
  First entry applies to `tintindex = 0`, second to `1`, etc.
  See `tint_sources.md`.

---

## `minecraft:composite`

Renders multiple sub‑models in the same space.

```jsonc
{
  "type": "minecraft:composite",
  "models": [
    { "type": "minecraft:model", "model": "..." },
    { "type": "minecraft:condition", ... }
  ]
}
```

- `models` (array, required) — list of Items model objects.

---

## `minecraft:condition`

Chooses between two models based on a boolean property.

```jsonc
{
  "type": "minecraft:condition",
  "property": "minecraft:damaged",
  // additional fields depending on property
  "on_true":  { "type": "minecraft:model", ... },
  "on_false": { "type": "minecraft:model", ... }
}
```

- `property` (string, required) — boolean property type.
  See `boolean_properties.md`.
- `on_true` (object, required) — Items model when property is `true`.
- `on_false` (object, required) — Items model when property is `false`.

---

## `minecraft:select`

Selects a model based on a discrete property.

```jsonc
{
  "type": "minecraft:select",
  "property": "minecraft:display_context",
  // additional fields depending on property
  "cases": [
    {
      "when": "gui",
      "model": { "type": "minecraft:model", ... }
    }
  ],
  "fallback": { "type": "minecraft:model", ... }
}
```

- `property` (string, required) — property type.
  See `select_properties.md`.
- `cases` (array, required) — list of cases:
  - `when` — value or list of values to match.
  - `model` — Items model for this case.
- `fallback` (object, optional) — Items model if no case matches.

---

## `minecraft:range_dispatch`

Selects a model based on a numeric property.

```jsonc
{
  "type": "minecraft:range_dispatch",
  "property": "minecraft:damage",
  "scale": 1.0,
  "entries": [
    {
      "threshold": 0.5,
      "model": { "type": "minecraft:model", ... }
    }
  ],
  "fallback": { "type": "minecraft:model", ... }
}
```

- `property` (string, required) — numeric property type.
  See `range_dispatch.md`.
- `scale` (float, optional) — multiplier for the property value. Default: `1.0`.
- `entries` (array, required) — list of:
  - `threshold` (float) — entry applies if property ≥ threshold.
  - `model` — Items model.
- `fallback` (object, optional) — Items model if no entry matches.

---

## `minecraft:empty`

```jsonc
{
  "type": "minecraft:empty",
}
```

Renders nothing.

---

## `minecraft:bundle/selected_item`

```jsonc
{
  "type": "minecraft:bundle/selected_item",
}
```

Renders the selected stack in `minecraft:bundle_contents`, if present.

---

## `minecraft:special`

Renders a special built‑in model.

```jsonc
{
  "type": "minecraft:special",
  "model": {
    "type": "minecraft:banner",
    // additional fields per special type
  },
  "base": "namespace:path",
}
```

- `model` (object, required) — special model object.
  See `special_models.md`.
- `base` (string, required) — namespaced ID of a base model in `models` directory, providing transforms, particle texture, and GUI light.

````

---

### `tint_sources.md`

```markdown
# Tint Sources

Tint sources are used in `tints` arrays of `minecraft:model` items models.

```jsonc
{
  "tints": [
    { "type": "minecraft:constant", "value": -1 }
  ]
}
````

## Common Structure

- `type` (string, required) — one of:
  - `minecraft:constant`
  - `minecraft:dye`
  - `minecraft:firework`
  - `minecraft:grass`
  - `minecraft:map_color`
  - `minecraft:potion`
  - `minecraft:team`
  - `minecraft:custom_model_data`

Additional fields depend on the type.

---

## `minecraft:constant`

```jsonc
{
  "type": "minecraft:constant",
  "value": -1,
}
```

- `value` — either:
  - integer packed RGB (e.g. `-1`), or
  - array `[r, g, b]` with floats 0.0–1.0.

---

## `minecraft:dye`

```jsonc
{
  "type": "minecraft:dye",
  "default": 0xffffff,
}
```

- `default` — RGB value used if `minecraft:dyed_color` is absent.

---

## `minecraft:firework`

```jsonc
{
  "type": "minecraft:firework",
  "default": 0xffffff,
}
```

- `default` — RGB value used if no explosion colors exist.

---

## `minecraft:grass`

```jsonc
{
  "type": "minecraft:grass",
  "temperature": 0.5,
  "downfall": 0.5,
}
```

- `temperature` (float 0.0–1.0)
- `downfall` (float 0.0–1.0)

---

## `minecraft:map_color`

```jsonc
{
  "type": "minecraft:map_color",
  "default": 0xffffff,
}
```

- `default` — RGB value if `minecraft:map_color` is absent.

---

## `minecraft:potion`

```jsonc
{
  "type": "minecraft:potion",
  "default": 0xffffff,
}
```

- `default` — RGB value used when potion has no effects or component is absent.

---

## `minecraft:team`

```jsonc
{
  "type": "minecraft:team",
  "default": 0xffffff,
}
```

- `default` — RGB value if no team color is available.

---

## `minecraft:custom_model_data`

```jsonc
{
  "type": "minecraft:custom_model_data",
  "index": 0,
  "default": 0xffffff,
}
```

- `index` (int, optional, default `0`) — index in `colors` list.
- `default` — RGB value if no color is present.
