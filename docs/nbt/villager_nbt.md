# Villager NBT tags (legacy overview)

- [Villager NBT Schema](../../schemas/nbt/villager_nbt.schema.json)

> Modern villagers use a more complex data structure; this section reflects older formats and basic tags.

---

## Basic villager tags

| Tag          | Description                           | Value type | Example                    |
| ------------ | ------------------------------------- | ---------- | -------------------------- |
| `Profession` | Villager profession (legacy numeric). | Int        | `{Profession:1}`           |
| `Offers`     | Trades offered by the villager.       | Compound   | `{Offers:{Recipes:[...]}}` |

Example (legacy style):

```nbt
{Offers:{Recipes:[
  {buy:{id:"stone",Count:1},maxUses:9999999,sell:{id:"stone",Count:1}}
]}}
```

> Note: In 1.14+ villager data and trades are significantly reworked; use this only as a legacy reference.
