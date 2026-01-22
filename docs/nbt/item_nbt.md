# Item NBT tags (overview)

- [Item NBT Schema](../../schemas/nbt/item_nbt.schema.json)

> This section is a high‑level placeholder; the source text was truncated.
> It focuses on **item format**, not the newer **data component format**.

Item NBT is used with:

- `/give`
- `/item`
- `/clear`
- As nested `tag:{...}` inside other commands (e.g. `/summon`, `/setblock`).

Example:

```nbt
{id:"minecraft:stone",Count:3b,tag:{CustomName:'{"text":"Name Here"}'}}
```

Common patterns include:

- `id`: Item ID (`"minecraft:stone"`)
- `Count`: Stack size (byte)
- `tag`: Compound containing:
  - `CustomName`
  - `Lore`
  - `Enchantments`
  - `Unbreakable`
  - And many more

For modern versions (1.20.5+), see the **data component format** instead; many classic item NBT fields have been replaced by components.
