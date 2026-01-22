# Armor stand NBT tags

- [Armor Stand NBT Schema](../../schemas/nbt/armor_stand_nbt.schema.json)

These tags are used when summoning armor stands.

```nbt
/summon armor_stand ~ ~ ~ {NoGravity:1b,ShowArms:1b,Small:1b}
```

---

## Armor stand tags

| Tag           | Description                            | Value type | Example                                         |
| ------------- | -------------------------------------- | ---------- | ----------------------------------------------- |
| `NoGravity`   | Toggles gravity.                       | Byte       | `{NoGravity:1b}`                                |
| `ShowArms`    | Shows or hides the armor stand’s arms. | Byte       | `{ShowArms:1b}`                                 |
| `NoBasePlate` | Hides the base plate.                  | Byte       | `{NoBasePlate:1b}`                              |
| `Small`       | Makes the armor stand small.           | Byte       | `{Small:1b}`                                    |
| `Rotation`    | Yaw rotation of the armor stand.       | List/float | `{Rotation:[90f,0f]}`                           |
| `Marker`      | Makes hitbox very small (marker mode). | Byte       | `{Marker:1b}`                                   |
| `Pose`        | Rotations of individual body parts.    | Compound   | `{Pose:{Head:[0f,0f,0f],LeftArm:[-10f,0f,0f]}}` |
| `Invisible`   | Makes the armor stand invisible.       | Byte       | `{Invisible:1b}`                                |

### `Pose` sub‑tags

Each pose sub‑tag is a list of three floats `[xRot,yRot,zRot]`:

- `Head`
- `Body`
- `LeftArm`
- `RightArm`
- `LeftLeg`
- `RightLeg`

Example:

```nbt
{Pose:{Head:[0f,30f,0f],RightArm:[-45f,0f,0f]}}
```

> Note: The `Equipment` tag (items worn/held) also works for armor stands.
