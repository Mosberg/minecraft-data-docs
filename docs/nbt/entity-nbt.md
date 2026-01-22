# Entity NBT tags

- [Entity NBT Schema](../../schemas/nbt/entity_nbt.schema.json)

These tags are used when:

- Summoning entities with `/summon`
- Editing entity data with `/data`

The entire entity NBT is a **compound tag**:

```nbt
/summon zombie ~ ~ ~ {CustomName:'"Bob"',NoAI:1b}
```

---

## General entity tags

| Tag                   | Description                                                                                                    | Allowed tagnames / notes                                                           | Required | Syntax example                                                                      |
| --------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------- | -------- | ----------------------------------------------------------------------------------- |
| `TileEntityData`      | Stores block entity data inside an entity (e.g. falling blocks with data).                                     | Various block entity tags (e.g. `Command`, `Items`, etc.).                         | None     | `{TileEntityData:{<block entity NBT here>}}`                                        |
| `Motion`              | Initial velocity of most entities.                                                                             | 3 doubles: X, Y, Z. Range roughly `-10` to `10`.                                   | All      | `{Motion:[0.0,1.0,0.0]}`                                                            |
| `direction`           | Initial velocity for dragon fireballs, fireballs, small fireballs, wither skulls. Required for these entities. | 3 doubles: X, Y, Z.                                                                | All      | `{direction:[0.0,1.0,0.0]}`                                                         |
| `power`               | Constant acceleration for dragon/fireballs/wither skulls.                                                      | 3 doubles: X, Y, Z.                                                                | All      | `{power:[0.0,1.0,0.0]}`                                                             |
| `ActiveEffects`       | List of status effects applied to a mob.                                                                       | Each entry: `Id`, `Duration`, `Amplifier`, `Ambient`, `ShowParticles`, `ShowIcon`. | All      | `{ActiveEffects:[{Id:1,Duration:999999,Amplifier:1b,Ambient:0b,ShowParticles:1b}]}` |
| `rewardExp`           | Whether villagers give XP for trading.                                                                         | Byte: `0b` or `1b`.                                                                | Optional | `{rewardExp:1b}`                                                                    |
| `Passengers`          | Entities riding on top of this entity.                                                                         | List of entity compounds, each with `id` and other tags.                           | Optional | `{Passengers:[{id:"minecraft:zombie"}, {id:"minecraft:skeleton"}]}`                 |
| `ArmorItems`          | Items worn by the entity (feet, legs, chest, head).                                                            | List of 4 item compounds.                                                          | Optional | `{ArmorItems:[{id:"minecraft:diamond_boots",Count:1b},... ]}`                       |
| `HandItems`           | Items held in main hand and offhand.                                                                           | List of 2 item compounds.                                                          | Optional | `{HandItems:[{id:"minecraft:diamond_sword",Count:1b},{}]}`                          |
| `HandDropChances`     | Drop chances for held items.                                                                                   | 2 floats: main hand, offhand. `0.0–1.0` or `>1.0` for guaranteed full durability.  | Optional | `{HandDropChances:[0.5f,2.0f]}`                                                     |
| `ArmorDropChances`    | Drop chances for armor items.                                                                                  | 4 floats: feet, legs, chest, head. Same semantics as above.                        | Optional | `{ArmorDropChances:[0.0f,0.0f,0.0f,1.0f]}`                                          |
| `NoAI`                | Disables AI (no movement, but still reacts to environment).                                                    | Byte: `0b` or `1b`.                                                                | Optional | `{NoAI:1b}`                                                                         |
| `NoGravity`           | Disables gravity.                                                                                              | Byte: `0b` or `1b`.                                                                | Optional | `{NoGravity:1b}`                                                                    |
| `Silent`              | Mutes most sounds from the entity.                                                                             | Byte: `0b` or `1b`.                                                                | Optional | `{Silent:1b}`                                                                       |
| `Fire`                | Remaining fire ticks.                                                                                          | Short `0–32767`.                                                                   | Optional | `{Fire:200s}`                                                                       |
| `Invulnerable`        | Makes entity invulnerable (except void and Creative players).                                                  | Byte: `0b` or `1b`.                                                                | Optional | `{Invulnerable:1b}`                                                                 |
| `Attributes`          | Custom attributes for the entity.                                                                              | List of attribute compounds.                                                       | Optional | `{Attributes:[{Name:"generic.max_health",Base:40.0d}]}`                             |
| `Health`              | Current health in half‑hearts.                                                                                 | Float.                                                                             | Optional | `{Health:40.0f}`                                                                    |
| `AngerTime`           | Duration of anger for neutral mobs.                                                                            | Int (ticks).                                                                       | Optional | `{AngerTime:200}`                                                                   |
| `AngryAt`             | UUID of target entity.                                                                                         | Int array `[I;INT,INT,INT,INT]`.                                                   | Optional | `{AngryAt:[I;1,2,3,4]}`                                                             |
| `CustomName`          | Custom name displayed above the entity.                                                                        | JSON text component as a string.                                                   | Optional | `{CustomName:'{"text":"Bob","color":"blue"}'}`                                      |
| `CustomNameVisible`   | Whether the custom name is always visible.                                                                     | Byte: `0b` (default) or `1b`.                                                      | Optional | `{CustomNameVisible:1b}`                                                            |
| `PersistenceRequired` | Prevents despawning.                                                                                           | Byte: `0b` or `1b`.                                                                | Optional | `{PersistenceRequired:1b}`                                                          |

---

## Summon‑specific tags

These tags are especially relevant when using `/summon` for certain entities.

### Generic summon tags

| Tag       | Description                             | Used in          | Value type | Allowed values / notes                        |
| --------- | --------------------------------------- | ---------------- | ---------- | --------------------------------------------- |
| `Type`    | Changes mob type (e.g. horse variants). | Summon           | Int        | Depends on entity; e.g. horse type `1–…`.     |
| `Saddle`  | Spawns saddled horses or pigs.          | Summon           | Boolean    | `true/false` or `1/0`.                        |
| `Tame`    | Spawns tamed horses.                    | Summon           | Boolean    | `true/false` or `1/0`.                        |
| `Variant` | Horse/axolotl variant.                  | Summoning horses | Int        | `1–1030` (see variant tables).                |
| `Size`    | Size of slimes, magma cubes, phantoms.  | Slimes, etc.     | Int        | `0–255` (large values can cause lag/crashes). |

### Falling block tags

| Tag          | Description                                              | Used in                 | Value type | Example                                                         |
| ------------ | -------------------------------------------------------- | ----------------------- | ---------- | --------------------------------------------------------------- |
| `BlockState` | Which block is being summoned as a falling block.        | `/summon falling_block` | Compound   | `{BlockState:{Name:"minecraft:oak_log",Properties:{axis:"y"}}}` |
| `Time`       | Despawn behavior before hitting ground.                  | Falling block           | Int        | `0` despawns immediately, `1` normal behavior.                  |
| `DropItem`   | Whether the block drops its item if it cannot be placed. | Falling block           | Byte       | `{DropItem:1b}`                                                 |

### Creeper / explosion tags

| Tag               | Description                                    | Used in | Type  | Notes / values                     |
| ----------------- | ---------------------------------------------- | ------- | ----- | ---------------------------------- |
| `Fuse`            | Ticks until explosion for TNT or creepers.     | Summon  | Short | `0–32767`.                         |
| `ExplosionPower`  | Explosion power for fireballs, wither, ghasts. | Summon  | Int   | `0–127` (above 127: no explosion). |
| `ExplosionRadius` | Explosion radius for creepers.                 | Summon  | Byte  | `0–127`.                           |
| `powered`         | Whether a creeper is charged.                  | Summon  | Byte  | `0` or `1`.                        |

### Shulker‑specific tags

| Tag          | Description                            | Value type | Allowed values / notes |
| ------------ | -------------------------------------- | ---------- | ---------------------- |
| `AttachFace` | Which face the shulker is attached to. | Byte       | `0b–5b`.               |
| `Peek`       | How far the shulker opens.             | Byte       | `-127b–127b`.          |
| `APX`        | Approximate X position (internal).     | Int        | Any integer.           |
| `APY`        | Approximate Y position.                | Int        | Any integer.           |
| `APZ`        | Approximate Z position.                | Int        | Any integer.           |

---

## Villager‑specific tags (basic)

See `villager-nbt.md` for more details; older formats used tags like `Profession` and `Offers`.
