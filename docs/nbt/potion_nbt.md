# Potion NBT tags

- [Potion NBT Schema](../../schemas/nbt/potion_nbt.schema.json)

These tags customize potions and potion‑like items.

---

## Base potion type

| Tag      | Description                    | Value type | Example                        |
| -------- | ------------------------------ | ---------- | ------------------------------ |
| `Potion` | The base potion type (effect). | String     | `{Potion:"minecraft:healing"}` |

---

## Custom potion effects

| Tag                   | Description                                   | Value type | Example                                                   |
| --------------------- | --------------------------------------------- | ---------- | --------------------------------------------------------- |
| `CustomPotionEffects` | List of custom effects applied by the potion. | List       | `{CustomPotionEffects:[{Id:1,Amplifier:1,Duration:600}]}` |

Each entry in `CustomPotionEffects`:

- `Id`: Effect ID (int)
- `Amplifier`: Effect level (int)
- `Duration`: Duration in ticks (int)

---

## Custom potion color

| Tag                 | Description                               | Value type      | Example                        |
| ------------------- | ----------------------------------------- | --------------- | ------------------------------ |
| `CustomPotionColor` | Color of the potion bottle (since 1.11+). | Decimal RGB int | `{CustomPotionColor:16711680}` |

The color is a packed RGB integer (e.g. `0xRRGGBB` in decimal).
