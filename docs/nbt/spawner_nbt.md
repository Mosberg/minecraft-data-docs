# Spawner NBT tags

- [Spawner NBT Schema](../../schemas/nbt/spawner_nbt.schema.json)

These tags are used when creating spawners with:

- `/setblock` (placing a spawner block)
- `/summon` for spawner minecarts

Only include the tags you need to avoid errors.

---

## Main spawner tags

| Tag                   | Description                                                                     | Value type        | Example                                                              |
| --------------------- | ------------------------------------------------------------------------------- | ----------------- | -------------------------------------------------------------------- |
| `SpawnData`           | Entity data for the spawned entity, including its NBT.                          | Compound          | `{SpawnData:{entity:{id:"minecraft:zombie"}}}`                       |
| `SpawnCount`          | Number of entities spawned each time.                                           | Int               | `{SpawnCount:4}`                                                     |
| `SpawnRange`          | Range (radius) around the spawner where entities can appear.                    | Int               | `{SpawnRange:4}`                                                     |
| `RequiredPlayerRange` | Distance within which a player must be for the spawner to activate.             | Int               | `{RequiredPlayerRange:16}`                                           |
| `Delay`               | Initial delay (ticks) before the first spawn after a player is detected.        | Int               | `{Delay:20}`                                                         |
| `MinSpawnDelay`       | Minimum delay (ticks) between spawn cycles after the first spawn.               | Int               | `{MinSpawnDelay:200}`                                                |
| `MaxSpawnDelay`       | Maximum delay (ticks) between spawn cycles after the first spawn.               | Int               | `{MaxSpawnDelay:800}`                                                |
| `MaxNearbyEntities`   | Maximum number of nearby entities before the spawner stops spawning more.       | Int               | `{MaxNearbyEntities:6}`                                              |
| `SpawnPotentials`     | Weighted list of possible entities to spawn, each with its own data and weight. | List of compounds | `SpawnPotentials:[{data:{entity:{id:"minecraft:zombie"}},weight:1}]` |

---

## `SpawnPotentials` sub‑tags

Each entry in `SpawnPotentials` is a compound with fields like:

| Sub‑tag  | Description                                                 | Value type | Example                                     |
| -------- | ----------------------------------------------------------- | ---------- | ------------------------------------------- |
| `data`   | Contains `entity` and its NBT data.                         | Compound   | `{data:{entity:{id:"minecraft:skeleton"}}}` |
| `weight` | Relative weight for this entry when choosing what to spawn. | Int        | `{weight:5}`                                |

Older formats sometimes used `Type`, `Weight`, and `Properties` directly; modern usage wraps entity data under `data:{entity:{...}}`.
