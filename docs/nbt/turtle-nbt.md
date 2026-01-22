# Turtle NBT tags

- [Turtle NBT Schema](../../schemas/nbt/turtle_nbt.schema.json)

These tags are used when summoning turtles.

---

## Turtle tags

| Tag          | Description                                     | Value type | Example            |
| ------------ | ----------------------------------------------- | ---------- | ------------------ |
| `HomePosX`   | X coordinate of the turtle’s home beach.        | Int        | `{HomePosX:100}`   |
| `HomePosY`   | Y coordinate of the turtle’s home beach.        | Int        | `{HomePosY:63}`    |
| `HomePosZ`   | Z coordinate of the turtle’s home beach.        | Int        | `{HomePosZ:-20}`   |
| `TravelPosX` | X coordinate of allowed egg‑laying area.        | Int        | `{TravelPosX:120}` |
| `TravelPosY` | Y coordinate of allowed egg‑laying area.        | Int        | `{TravelPosY:63}`  |
| `TravelPosZ` | Z coordinate of allowed egg‑laying area.        | Int        | `{TravelPosZ:-10}` |
| `HasEgg`     | Whether the turtle currently has an egg to lay. | Byte       | `{HasEgg:1b}`      |
