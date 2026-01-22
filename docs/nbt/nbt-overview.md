# NBT tags overview

> **Edition:** Java Edition only
> **Context:** Commands such as `/summon`, `/data`, `/setblock`, `/fill`, `/give`, `/item`, etc.

NBT (Named Binary Tag) is the structured data format used by Minecraft to store information about entities, blocks, items, and more.

- NBT data is written as **compound tags** enclosed in `{}`.
- Lists are enclosed in `[]`.
- Tag names are **case‑sensitive**.
- Whitespace is ignored.
- Boolean‑like flags are often stored as **byte tags** (`0b` or `1b`).

Examples:

```nbt
{CustomName:'"Bob"', Invulnerable:1b}
{Motion:[0.0,1.0,0.0]}
```

You can inspect live NBT data using the `/data` command.

This reference is split into multiple files:

- `entity-nbt.md` — tags for entities (used with `/summon` and `/data`).
- `block-nbt.md` — tags for blocks and block entities (used with `/setblock` and `/fill`).
- `item-nbt.md` — tags for items (used with `/give`, `/item`, `/clear`).
- `potion-nbt.md` — potion‑specific tags.
- `armor-stand-nbt.md` — armor stand‑specific tags.
- `turtle-nbt.md` — turtle‑specific tags.
- `spawner-nbt.md` — monster spawner tags.
- `item-frame-nbt.md` — item frame tags.
- `falling-block-nbt.md` — falling block tags.
- `villager-nbt.md` — villager‑specific tags.
