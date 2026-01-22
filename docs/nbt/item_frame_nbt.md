# Item frame NBT tags

- [Item Frame NBT Schema](../../schemas/nbt/item_frame_nbt.schema.json)

These tags are used when summoning item frames.

```nbt
/summon item_frame ~ ~ ~ {Facing:2,ItemRotation:4,Invisible:1b}
```

---

## Item frame tags

| Tag            | Description                                             | Value type | Allowed values / notes                                             | Example                                          |
| -------------- | ------------------------------------------------------- | ---------- | ------------------------------------------------------------------ | ------------------------------------------------ |
| `Facing`       | Direction the item frame is attached to.                | Int        | `0–5` (`0` up, `1` down, `2` south, `3` north, `4` east, `5` west) | `{Facing:2}`                                     |
| `ItemRotation` | Rotation of the item inside the frame.                  | Int        | `0–7` (clockwise steps)                                            | `{ItemRotation:4}`                               |
| `Item`         | The item displayed in the frame.                        | Compound   | Standard item NBT (`id`, `Count`, `tag`, etc.).                    | `{Item:{id:"minecraft:diamond_sword",Count:1b}}` |
| `Invisible`    | Whether the frame itself is invisible.                  | Byte       | `0b` or `1b`.                                                      | `{Invisible:1b}`                                 |
| `Fixed`        | Whether the frame cannot be broken or rotated normally. | Byte       | `0b` or `1b`.                                                      | `{Fixed:1b}`                                     |
