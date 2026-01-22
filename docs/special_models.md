# Special Models (`minecraft:special`)

- [Items Models Schema (Hybrid JSON Schema)](../schemas/items_model.schema.json#specialType)

Common structure:

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

`model.type` can be:

- `minecraft:banner`
- `minecraft:bed`
- `minecraft:chest`
- `minecraft:conduit`
- `minecraft:copper_golem_statue`
- `minecraft:decorated_pot`
- `minecraft:head`
- `minecraft:player_head`
- `minecraft:shield`
- `minecraft:shulker_box`
- `minecraft:standing_sign`
- `minecraft:hanging_sign`
- `minecraft:trident`

---

## `minecraft:banner`

```jsonc
{
  "type": "minecraft:banner",
  "color": "red",
}
```

- `color` — one of the 16 dye colors.

---

## `minecraft:bed`

```jsonc
{
  "type": "minecraft:bed",
  "texture": "minecraft:red_bed",
}
```

- `texture` — namespaced ID in bed texture atlas (no `.png`).

---

## `minecraft:chest`

```jsonc
{
  "type": "minecraft:chest",
  "texture": "minecraft:single",
  "openness": 0.0,
}
```

- `texture` — namespaced ID in chest texture atlas (no `.png`).
- `openness` (float, optional, 0.0–1.0, default `0.0`).

---

## `minecraft:conduit`

No extra fields.

---

## `minecraft:copper_golem_statue`

```jsonc
{
  "type": "minecraft:copper_golem_statue",
  "pose": "standing",
  "texture": "namespace:path.png",
}
```

- `pose` — `sitting`, `running`, `star`, or `standing`.
- `texture` — namespaced ID including `.png`.

---

## `minecraft:decorated_pot`

No extra fields (uses `minecraft:pot_decorations`).

---

## `minecraft:head`

```jsonc
{
  "type": "minecraft:head",
  "kind": "zombie",
  "texture": "minecraft:entity/zombie",
  "animation": 0.0,
}
```

- `kind` — `skeleton`, `wither_skeleton`, `player`, `zombie`, `creeper`, `piglin`, `dragon`.
- `texture` (optional) — namespaced ID without `textures/entity/` prefix and `.png` suffix.
- `animation` (float, optional) — controls head animation.

---

## `minecraft:player_head`

No extra fields; uses `minecraft:profile` component.

---

## `minecraft:shield`

No extra fields; uses `minecraft:banner_patterns` and `minecraft:base_color`.

---

## `minecraft:shulker_box`

```jsonc
{
  "type": "minecraft:shulker_box",
  "texture": "minecraft:white",
  "openness": 0.0,
  "orientation": "up",
}
```

- `texture` — namespaced ID in shulker texture atlas (no `.png`).
- `openness` (float, optional, 0.0–1.0, default `0.0`).
- `orientation` (string, optional, default `up`).

---

## `minecraft:standing_sign`

```jsonc
{
  "type": "minecraft:standing_sign",
  "wood_type": "oak",
  "texture": "minecraft:entity/signs/oak",
}
```

- `wood_type` — one of:
  - `oak`, `spruce`, `birch`, `acacia`, `cherry`, `jungle`,
    `dark_oak`, `pale_oak`, `mangrove`, `bamboo`, `crimson`, `warped`
- `texture` (optional) — overrides atlas texture; if present, `wood_type` is ignored.

---

## `minecraft:hanging_sign`

Same fields as `standing_sign`.

---

## `minecraft:trident`

No extra fields.
