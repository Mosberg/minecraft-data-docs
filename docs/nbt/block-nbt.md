# Block and block entity NBT tags

- [Block NBT Schema](../../schemas/nbt/block_nbt.schema.json)

These tags are used with:

- `/setblock`
- `/fill`
- `/data` on block entities

The NBT is attached to the block as a **block entity** where applicable.

---

## Generic block entity tags

These tags apply to many tile entities (chests, furnaces, etc.).

| Tag          | Description                                               | Value type          | Example                          |
| ------------ | --------------------------------------------------------- | ------------------- | -------------------------------- |
| `CustomName` | Custom name shown in the GUI instead of the default name. | JSON text component | `{CustomName:"\"Custom Name\""}` |
| `Lock`       | Name of an item required to open the inventory.           | String              | `{Lock:"Key's Name"}`            |

---

## Command block tags

Used with command blocks and command block minecarts.

| Tag       | Description                                                       | Value type     | Example                 |
| --------- | ----------------------------------------------------------------- | -------------- | ----------------------- |
| `Command` | The command stored in the command block.                          | String         | `{Command:"say Hello"}` |
| `auto`    | Whether the block is “Always Active” instead of “Needs Redstone”. | Byte (`0b/1b`) | `{auto:1b}`             |

---

## Beacon tags

| Tag         | Description                                                                  | Value type | Example         |
| ----------- | ---------------------------------------------------------------------------- | ---------- | --------------- |
| `Primary`   | First status effect the beacon provides (level 1 by default).                | Effect ID  | `{Primary:1}`   |
| `Secondary` | Second status effect. If same as `Primary`, upgrades to level 2.             | Effect ID  | `{Secondary:1}` |
| `Levels`    | Number of valid layers below the beacon. Auto‑updates and overrides `/data`. | Int        | `{Levels:4}`    |

---

## Spawner tags (overview)

See `spawner-nbt.md` for a full breakdown.

Spawner NBT controls what entities are spawned, how often, and under which conditions.

Key tags include:

- `SpawnData`
- `SpawnCount`
- `SpawnRange`
- `RequiredPlayerRange`
- `Delay`
- `MinSpawnDelay`
- `MaxSpawnDelay`
- `MaxNearbyEntities`
- `SpawnPotentials`
