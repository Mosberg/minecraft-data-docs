# Falling block NBT tags

- [Falling Block NBT Schema](../../schemas/nbt/falling_block_nbt.schema.json)

Falling blocks are summoned with `/summon falling_block` and use specific tags to control their behavior.

---

## Falling block tags

| Tag              | Description                                                           | Value type | Example                                                         |
| ---------------- | --------------------------------------------------------------------- | ---------- | --------------------------------------------------------------- |
| `BlockState`     | The block to render and place when landing.                           | Compound   | `{BlockState:{Name:"minecraft:oak_log",Properties:{axis:"y"}}}` |
| `Time`           | Despawn behavior before hitting the ground.                           | Int        | `{Time:1}` (normal), `{Time:0}` (despawn immediately)           |
| `DropItem`       | Whether the block drops its item if it cannot be placed.              | Byte       | `{DropItem:1b}`                                                 |
| `TileEntityData` | Block entity data for the block (e.g. chest contents, command block). | Compound   | `{TileEntityData:{Command:"say hi"}}`                           |
