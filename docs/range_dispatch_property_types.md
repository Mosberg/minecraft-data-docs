# Range Dispatch Property Types (for `minecraft:range_dispatch`)

- [Items Models Schema (Hybrid JSON Schema)](../schemas/items_model.schema.json#rangeDispatchType)

Common structure:

```jsonc
{
  "type": "minecraft:range_dispatch",
  "property": "minecraft:damage",
  "scale": 1.0,
  "entries": [
    { "threshold": 0.5, "model": { ... } }
  ],
  "fallback": { ... }
}
```

Supported numeric property types:

- `minecraft:bundle/fullness`
- `minecraft:compass`
- `minecraft:cooldown`
- `minecraft:count`
- `minecraft:crossbow/pull`
- `minecraft:damage`
- `minecraft:time`
- `minecraft:use_cycle`
- `minecraft:use_duration`
- `minecraft:custom_model_data`

---

## `minecraft:bundle/fullness`

Returns weight of `minecraft:bundle_contents` or `0`.

No extra fields.

---

## `minecraft:compass`

```jsonc
{
  "property": "minecraft:compass",
  "target": "spawn",
  "wobble": true,
}
```

- `target` (string) — one of:
  - `spawn`
  - `lodestone`
  - `recovery`
  - `none`
- `wobble` (boolean, optional, default `true`)

---

## `minecraft:cooldown`

Remaining cooldown (0.0–1.0). No extra fields.

---

## `minecraft:count`

```jsonc
{
  "property": "minecraft:count",
  "normalize": true,
}
```

- `normalize` (boolean, optional, default `true`)

---

## `minecraft:crossbow/pull`

Crossbow use time. No extra fields.

---

## `minecraft:damage`

```jsonc
{
  "property": "minecraft:damage",
  "normalize": true,
}
```

- `normalize` (boolean, optional, default `true`)

---

## `minecraft:time`

```jsonc
{
  "property": "minecraft:time",
  "source": "daytime",
  "wobble": true,
}
```

- `source` (string) — `daytime`, `moon_phase`, or `random`.
- `wobble` (boolean, optional, default `true`)

---

## `minecraft:use_cycle`

```jsonc
{
  "property": "minecraft:use_cycle",
  "period": 1.0,
}
```

- `period` (float, optional, > 0, default `1.0`)

---

## `minecraft:use_duration`

```jsonc
{
  "property": "minecraft:use_duration",
  "remaining": false,
}
```

- `remaining` (boolean, optional, default `false`)

---

## `minecraft:custom_model_data` (float)

```jsonc
{
  "property": "minecraft:custom_model_data",
  "index": 0,
}
```

- `index` (int, optional, default `0`) — index in `floats` list.
