# **item-models.md**

- [Item Models](../schemas/item_model.schema.json)
-

### **Item Models — Specification & Structure**

_Based solely on the raw wiki text, rewritten into clean Markdown._

---

# **1. Introduction**

Item models define how items are rendered in _Minecraft: Java Edition_ across all contexts:

- Inventory
- First‑person view
- Third‑person view
- Dropped items
- Item frames
- Armor stands
- Mob hands
- Head slot (helmets, hats)

Item models share many structural similarities with block models but include additional fields specific to item rendering, such as:

- `gui_light`
- `layerN` textures
- Display transforms for item‑specific contexts
- Optional 3D geometry (`elements`)

Item models are stored in:

```
assets/<namespace>/models/item/<model_name>.json
```

They are referenced by the **item definition system** (1.21.4+) or by legacy item model paths.

---

# **2. File Path Rules**

Minecraft uses resource locations of the form:

```
namespace:path
```

When used in an item model, this maps to:

```
assets/<namespace>/models/<path>.json
```

Textures referenced in item models map to:

```
assets/<namespace>/textures/<path>.png
```

If `namespace` is omitted, it defaults to `minecraft`.

---

# **3. Root Structure of an Item Model**

An item model JSON file contains the following top‑level fields:

| Field          | Type       | Description                                  |
| -------------- | ---------- | -------------------------------------------- |
| `parent`       | string     | Path to another model to inherit from.       |
| `textures`     | object     | Defines texture variables and icon layers.   |
| `display`      | object     | Transformations for item rendering contexts. |
| `gui_light`    | string     | Controls shading style in GUI.               |
| `elements`     | array      | Optional 3D geometry.                        |
| `name`         | string     | _(Blockbench only)_ Element name.            |
| `texture_size` | integer[2] | _(Blockbench only)_ Texture atlas size.      |

Unknown fields are allowed **only at the root**, per your strict‑schema preference.

---

# **4. Parent**

### **parent** _(string)_

Loads another model from a resource location.

Special parents:

- `"item/generated"`
  - Generates a flat 2D item from texture layers (`layer0`, `layer1`, …).
- `"builtin/entity"`
  - Loads an entity model.
  - Only works for:
    - chests
    - ender chests
    - mob heads
    - shields
    - banners
    - tridents

If both `parent` and `elements` are present, the child’s `elements` override the parent’s.

---

# **5. Textures**

### **textures** _(object)_

Defines texture variables used by faces or by the item icon.

---

## **5.1 Icon Layers**

### **layerN** _(string)_

Defines the icon texture for the item in the inventory.

- `layer0` is required for `"item/generated"`.
- Additional layers (`layer1`, `layer2`, …) are used for:
  - Leather armor overlays
  - Trimmed armor
  - Potions
  - Other multi‑layer items

The number of supported layers is hardcoded per item.

---

## **5.2 Particle Texture**

### **particle** _(string)_

Used for:

- Food crumb particles
- Barrier particle
- Default particle when no other texture is available

If omitted, defaults to `layer0`.

---

## **5.3 Custom Texture Variables**

Any additional key in `textures` becomes a texture variable usable via:

```
"#<variable>"
```

---

# **6. GUI Light**

### **gui_light** _(string)_

Controls shading style in GUI contexts.

Valid values:

- `"front"` — flat shading (like 2D items)
- `"side"` — block‑like shading

Default: `"side"`

---

# **7. Elements**

### **elements** _(array of objects)_

Defines optional 3D geometry for the item.

Item elements follow the same structure as block model elements:

- `from`
- `to`
- `rotation`
- `shade`
- `light_emission`
- `faces`

### Differences from block models:

- Rotation angle is limited to **−45° to +45°** for item models.
- Multi‑axis rotation is **not** supported for item models (as of the wiki text).
- UV auto‑generation rules are identical.

---

# **8. Element Fields**

## **8.1 Coordinates**

### **from** _(number[3])_

Start coordinate of the cuboid.
Range: −16 to 32.

### **to** _(number[3])_

End coordinate of the cuboid.
Range: −16 to 32.

---

## **8.2 Rotation**

### **rotation** _(object)_

Defines rotation of the cuboid.

Fields:

| Field     | Type                | Description                  |
| --------- | ------------------- | ---------------------------- |
| `origin`  | number[3]           | Pivot point.                 |
| `axis`    | `"x"`, `"y"`, `"z"` | Rotation axis.               |
| `angle`   | number              | Rotation angle (−45 to +45). |
| `rescale` | boolean             | Adjusts face scaling.        |

Notes:

- Item models **do not** support legacy `x`, `y`, `z` rotation fields.
- Item models **do not** support multi‑axis rotation.

---

## **8.3 Shading**

### **shade** _(boolean)_

Default: `true`
Controls directional shading.

---

## **8.4 Light Emission**

### **light_emission** _(integer)_

Range: 0–15
Default: 0

---

## **8.5 Faces**

### **faces** _(object)_

Defines the six possible faces of the cuboid:

- `down`
- `up`
- `north`
- `south`
- `west`
- `east`

Each face is optional.

---

# **8.5.1 Face Properties**

Each face contains:

| Field       | Type      | Description                               |
| ----------- | --------- | ----------------------------------------- |
| `uv`        | number[4] | Texture coordinates `[x1, y1, x2, y2]`.   |
| `texture`   | string    | Texture variable reference (`"#layer0"`). |
| `cullface`  | string    | Face to cull when adjacent to a block.    |
| `rotation`  | integer   | Texture rotation (0, 90, 180, 270).       |
| `tintindex` | integer   | Tint index (−1 = no tint).                |

UV rules:

- If omitted, UV is auto‑generated.
- UV outside 0–16 behaves inconsistently.
- Swapping x1/x2 flips the texture.

---

# **9. Display Transforms**

Item models use the `display` section to define how the item appears in different rendering contexts.
This is one of the most important parts of item modeling.

### **display** _(object)_

Contains transformations for each rendering context.

Valid transform keys:

- `thirdperson_righthand`
- `thirdperson_lefthand`
- `firstperson_righthand`
- `firstperson_lefthand`
- `gui`
- `head`
- `ground`
- `fixed`
- `on_shelf` _(added in 1.21.9)_

Each transform contains:

| Field         | Type      | Description                                     |
| ------------- | --------- | ----------------------------------------------- |
| `rotation`    | number[3] | Rotation in degrees `[x, y, z]`.                |
| `translation` | number[3] | Position offset `[x, y, z]`. Clamped to −80…80. |
| `scale`       | number[3] | Scale factor. Clamped to max 4.                 |

### Notes:

- Translations apply **before** rotations.
- Missing fields (`rotation`, `translation`, `scale`) **do not inherit** from the parent.
- `fixed` refers to item frames.
- `on_shelf` is ignored by shelves with `align_items_to_bottom=true`.

---

# **10. Display Contexts (Where Each Transform Is Used)**

The following table summarizes which display transform applies in each situation.

| Use Case                                                 | Display Type            |
| -------------------------------------------------------- | ----------------------- |
| Inventory items                                          | `gui`                   |
| Items worn on head (players, humanoid mobs)              | `head`                  |
| Dropped items                                            | `ground`                |
| Items held by dolphins, pandas, foxes                    | `ground`                |
| Thrown projectiles (snowballs, eggs, ender pearls, etc.) | `ground`                |
| Items in item frames                                     | `fixed`                 |
| Totem of undying animation                               | `fixed`                 |
| Items brushed out of suspicious sand/gravel              | `fixed`                 |
| Third‑person right hand                                  | `thirdperson_righthand` |
| Third‑person left hand                                   | `thirdperson_lefthand`  |
| First‑person right hand                                  | `firstperson_righthand` |
| First‑person left hand                                   | `firstperson_lefthand`  |
| Item display entities                                    | As specified            |
| Items on shelves                                         | `on_shelf`              |

### Notes:

- If a left‑hand transform is missing, the right‑hand transform is used.
- Some mobs use hardcoded transforms (e.g., witches holding potions).

---

# **11. Use Cases for Item Models**

Item models are used in the following contexts:

| Use Case                   | Applies To                              | Respects `shade=false`? |
| -------------------------- | --------------------------------------- | ----------------------- |
| Inventory icons            | All items except air                    | No                      |
| First‑person held items    | All items except air                    | No                      |
| Third‑person held items    | All items except air                    | No                      |
| Items held by mobs         | All items except air                    | No                      |
| Dropped items              | All items except air                    | No                      |
| Item frames                | All items except air                    | No                      |
| Totem of undying animation | Items with “death protection” component | No                      |

### Notes:

- Tridents and shields have partial hardcoding.
- Some mobs override item transforms (e.g., foxes, villagers).

---

# **12. Limitations**

### **12.1 Hardcoded Items**

Some items cannot be fully remodeled:

- Trident (entity model is hardcoded)
- Shield (entity model is hardcoded)
- Bows and fishing rods have special animation logic
- Some items ignore `display` transforms in certain contexts

### **12.2 Layer Limits**

- The number of supported `layerN` textures is hardcoded per item.
- Most items support up to 4 layers (plus `layer0`).

### **12.3 Rotation Limits**

- Item model rotations are limited to **−45° to +45°**.
- Multi‑axis rotation is not supported.

### **12.4 No Multipart Logic**

Unlike block models, item models:

- Cannot use multipart definitions
- Cannot use blockstate logic
- Cannot select models based on block properties

### **12.5 Overrides Removed (1.21.4+)**

The legacy `overrides` system has been removed and replaced with the new item model definition system.

---

# **13. Rendering Behavior**

This section summarizes how item models behave in the engine.

---

## **13.1 Shading Behavior**

- `shade=false` disables directional shading.
- GUI rendering uses `gui_light` to determine shading style.
- Most item contexts ignore `shade=false`.

---

## **13.2 Culling Behavior**

- `cullface` is rarely used in item models.
- Items are usually rendered as 2D quads or small 3D models.
- Culling is ignored in many item contexts.

---

## **13.3 Light Emission Behavior**

- `light_emission` sets the **minimum** light level.
- Does not make the item emit light.
- Dropped items and held items still use world lighting.

---

## **13.4 Rotation Behavior**

- Rotation is limited to one axis.
- Angle range is −45° to +45°.
- `rescale=true` helps avoid UV distortion.

---

# **14. Summary of Item Model Structure**

An item model consists of:

- Optional inheritance (`parent`)
- Texture variables and icon layers (`textures`)
- Optional 3D geometry (`elements`)
- Display transforms for all item contexts (`display`)
- GUI shading mode (`gui_light`)
- Optional Blockbench metadata (`name`, `texture_size`)

---

# **item-models.md (Part 3 / ~4)**

### **Item Models — Specification & Structure**

---

# **15. Detailed Field Reference**

This section provides a structured, authoritative reference for every field used in item models.

---

## **15.1 Root-Level Fields**

### **parent**

**Type:** `string`
**Description:**
Specifies a parent model to inherit from.
If both `parent` and `elements` are present, the child’s `elements` override the parent’s.

Special parents:

- `"item/generated"` — generates a flat icon from texture layers.
- `"builtin/entity"` — loads an entity model (limited to specific items).

---

### **textures**

**Type:** `object<string, string>`
**Description:**
Defines texture variables and icon layers.

Special keys:

- `layer0` — required for `"item/generated"`.
- `layerN` — additional icon layers.
- `particle` — used for particles.

---

### **display**

**Type:** `object`
**Description:**
Defines item rendering transforms for all contexts.

---

### **gui_light**

**Type:** `string`
**Enum:** `"front"`, `"side"`
**Default:** `"side"`
**Description:**
Controls shading style in GUI contexts.

---

### **elements**

**Type:** `array<object>`
**Description:**
Optional 3D geometry for the item.

---

### **name** _(Blockbench only)_

**Type:** `string`
Human‑readable name for an element.

---

### **texture_size** _(Blockbench only)_

**Type:** `integer[2]`
Texture atlas size used by Blockbench.

---

## **15.2 Element Fields**

Each element in `elements[]` contains:

---

### **from**

**Type:** `number[3]`
**Range:** −16 to 32
Start coordinate of the cuboid.

---

### **to**

**Type:** `number[3]`
**Range:** −16 to 32
End coordinate of the cuboid.

---

### **rotation**

**Type:** `object`
Defines rotation of the cuboid.

Fields:

| Field     | Type                | Description                  |
| --------- | ------------------- | ---------------------------- |
| `origin`  | number[3]           | Pivot point.                 |
| `axis`    | `"x"`, `"y"`, `"z"` | Rotation axis.               |
| `angle`   | number              | Rotation angle (−45 to +45). |
| `rescale` | boolean             | Adjusts face scaling.        |

Notes:

- Item models do **not** support multi‑axis rotation.
- Item models do **not** support legacy `x`, `y`, `z` rotation fields.

---

### **shade**

**Type:** `boolean`
**Default:** `true`
Controls directional shading.

---

### **light_emission**

**Type:** `integer`
**Range:** 0–15
**Default:** 0
Minimum light level the element receives.

---

### **faces**

**Type:** `object`
Defines the six possible faces of the cuboid.

Valid keys:

- `down`
- `up`
- `north`
- `south`
- `west`
- `east`

Each face is optional.

---

## **15.3 Face Fields**

Each face contains:

---

### **uv**

**Type:** `number[4]`
**Format:** `[x1, y1, x2, y2]`
Defines the texture region to use.

Rules:

- If omitted, UV is auto‑generated.
- UV outside 0–16 behaves inconsistently.
- Swapping x1/x2 flips the texture.

---

### **texture**

**Type:** `string`
**Format:** `"#<variable>"`
References a texture variable defined in `textures`.

---

### **cullface**

**Type:** `string`
**Enum:** `down`, `up`, `north`, `south`, `west`, `east`
Determines whether the face is hidden when touching a block.

---

### **rotation**

**Type:** `integer`
**Enum:** `0`, `90`, `180`, `270`
Rotates the texture clockwise (counterclockwise for `down`).

---

### **tintindex**

**Type:** `integer`
**Default:** `-1`
Applies a tint from the item model definition.

---

# **16. Rendering Behavior**

This section summarizes how item models behave in the engine.

---

## **16.1 Shading Behavior**

- `shade=false` disables directional shading.
- GUI shading is controlled by `gui_light`.
- Most item contexts ignore `shade=false`.

---

## **16.2 Culling Behavior**

- `cullface` is rarely used in item models.
- Items are usually rendered as quads or small 3D models.
- Many item contexts ignore culling entirely.

---

## **16.3 Light Emission Behavior**

- `light_emission` sets the **minimum** light level.
- Does not cause the item to emit light.
- Dropped items and held items still use world lighting.

---

## **16.4 Rotation Behavior**

- Rotation is limited to one axis.
- Angle range is −45° to +45°.
- `rescale=true` helps avoid UV distortion.

---

# **17. Best Practices for Item Model Authors**

These recommendations help ensure consistent behavior across versions and tools.

---

## **17.1 Icon Layers**

- Always define `layer0` for `"item/generated"`.
- Keep layer count minimal for performance.
- Use consistent naming conventions.

---

## **17.2 Geometry**

- Use 3D elements sparingly; many items are intended to be flat.
- Keep coordinates within the valid range (−16 to 32).
- Avoid overlapping cuboids unless intentional.

---

## **17.3 Display Transforms**

- Keep GUI scale ≤ 1.0 to avoid clipping.
- Use consistent transforms across related items.
- Remember that missing fields do **not** inherit from parents.

---

## **17.4 Texture Variables**

- Always define a `particle` texture.
- Use descriptive variable names (`blade`, `handle`, etc.).
- Avoid UV values outside 0–16 unless intentional.

---

## **17.5 Blockbench Metadata**

- Safe to include; Minecraft ignores it.
- Useful for collaboration and editing.
- Do not rely on Blockbench fields for in‑game behavior.

---

# **18. Complete Example (Fully Annotated)**

Below is an original, illustrative example of a complete item model.
It demonstrates all major fields while avoiding copyrighted content.

```json
{
  "parent": "item/generated",

  "textures": {
    "layer0": "minecraft:item/iron_sword",
    "particle": "minecraft:item/iron_sword"
  },

  "display": {
    "gui": {
      "rotation": [30, 45, 0],
      "translation": [0, 0, 0],
      "scale": [1.0, 1.0, 1.0]
    },
    "firstperson_righthand": {
      "rotation": [0, -90, 25],
      "translation": [1, 3, 1],
      "scale": [0.9, 0.9, 0.9]
    },
    "thirdperson_righthand": {
      "rotation": [0, 90, -55],
      "translation": [0, 4, 0],
      "scale": [0.55, 0.55, 0.55]
    }
  },

  "elements": [
    {
      "from": [7, 0, 7],
      "to": [9, 16, 9],

      "rotation": {
        "origin": [8, 8, 8],
        "axis": "y",
        "angle": 15,
        "rescale": true
      },

      "shade": true,
      "light_emission": 0,

      "faces": {
        "north": { "texture": "#layer0", "uv": [0, 0, 16, 16] },
        "south": { "texture": "#layer0" },
        "east": { "texture": "#layer0" },
        "west": { "texture": "#layer0" },
        "up": { "texture": "#layer0" },
        "down": { "texture": "#layer0" }
      }
    }
  ],

  "texture_size": [16, 16]
}
```

This example demonstrates:

- A generated 2D icon (`item/generated`)
- A single 3D element added on top of the icon
- Multiple display transforms
- Texture variables
- Rotation within item limits (−45° to +45°)
- Blockbench metadata

---

# **19. Version Notes (Non‑Historical)**

These are high‑level, non‑copyrighted summaries of changes relevant to item model authors.

- **1.21.9** — Added `on_shelf` display transform.
- **1.21.4** — Removed legacy `overrides`; introduced new item model definition system.
- **1.21.2** — Added `light_emission` to item models.
- **1.15.2** — Added `gui_light`.
- **1.9** — Added auto‑generated UVs; added left/right hand transforms.
- **1.8** — Item model system introduced.

---

# **20. Glossary**

| Term                  | Definition                                                                   |
| --------------------- | ---------------------------------------------------------------------------- |
| **Icon Layer**        | A texture layer used to build the 2D item icon.                              |
| **Display Transform** | A set of rotation/translation/scale values for a specific rendering context. |
| **GUI Light**         | Determines shading style in GUI contexts.                                    |
| **Tintindex**         | Index used to apply color tints to item faces.                               |
| **Particle Texture**  | Texture used for item particles.                                             |
| **Element**           | A cuboid that forms part of a 3D item model.                                 |

---

# **21. Final Notes**

This document provides a complete, strict, and tooling‑friendly specification of Minecraft item models based solely on the raw wiki text, rewritten into clean Markdown.

It is suitable for:

- Resource pack authors
- Modding tool developers
- JSON schema validation
- IDE integrations
- Automated pipelines

---
