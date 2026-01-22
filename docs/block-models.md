# **block-models.md**

- [Block Models](../schemas/block_model.schema.json)

### **Block Models — Specification & Structure**

_Based solely on the raw wiki text, rewritten into clean Markdown._

---

# **1. Introduction**

Block models define the 3D shapes used to render blocks in _Minecraft: Java Edition_.
They determine:

- Geometry (via `elements`)
- Texture assignment (via `textures`)
- Lighting behavior
- Rotation and transformation rules
- How models inherit from parent models

Block models are stored in:

```
assets/<namespace>/models/block/<model_name>.json
```

They are referenced by **blockstate files**, which determine which model is used for each block state variant.

---

# **2. File Path Rules**

Minecraft uses _resource locations_ of the form:

```
namespace:path
```

When used in a model file, this maps to:

```
assets/<namespace>/models/<path>.json
```

Textures referenced in models map to:

```
assets/<namespace>/textures/<path>.png
```

If `namespace` is omitted, it defaults to `minecraft`.

---

# **3. Root Structure of a Block Model**

A block model JSON file contains the following top‑level fields:

| Field              | Type       | Description                                    |
| ------------------ | ---------- | ---------------------------------------------- |
| `parent`           | string     | Path to another model to inherit from.         |
| `ambientocclusion` | boolean    | Enables or disables ambient occlusion shading. |
| `textures`         | object     | Defines texture variables.                     |
| `elements`         | array      | List of cuboid elements composing the model.   |
| `display`          | object     | Transformations for item rendering contexts.   |
| `name`             | string     | _(Blockbench only)_ Element name.              |
| `texture_size`     | integer[2] | _(Blockbench only)_ Texture atlas size.        |

Unknown fields are allowed **only at the root**, per your schema strictness choice.

---

# **4. Parent**

### **parent** _(string)_

Loads another model from a resource location.

Example:

```
"parent": "block/cube_all"
```

Rules:

- If both `parent` and `elements` are present, the child’s `elements` **replace** the parent’s.
- Special parent:
  - `"builtin/generated"` — generates a model from a single texture layer.

---

# **5. Ambient Occlusion**

### **ambientocclusion** _(boolean)_

Controls whether the model uses ambient occlusion shading.

- `true` — default
- `false` — disables AO shading on the model

This does **not** affect light‑level shading.

---

# **6. Textures**

### **textures** _(object)_

Defines texture variables used by faces.

Each entry is:

```
"<variable>": "<namespace>:<path>"
```

### Special texture variables

#### **particle** _(string)_

Texture used for:

- Block breaking particles
- Nether portal overlay
- Water/lava still textures
- General particle effects

Can be referenced as:

```
"#particle"
```

---

# **7. Elements**

### **elements** _(array of objects)_

Each element defines a cuboid in the model.
If omitted, the model may rely entirely on its parent.

Each element contains:

- `from`
- `to`
- `rotation`
- `shade`
- `light_emission`
- `faces`

---

## **7.1 Element Coordinates**

### **from** _(number[3])_

Start corner of the cuboid.

- Range: **−16 to 32**

### **to** _(number[3])_

Opposite corner of the cuboid.

- Range: **−16 to 32**

Coordinates are in 1/16th block units.

---

## **7.2 Element Rotation**

### **rotation** _(object)_

Defines rotation of the cuboid.

Fields:

| Field     | Type                | Description                       |
| --------- | ------------------- | --------------------------------- |
| `origin`  | number[3]           | Rotation pivot point.             |
| `x`       | number              | Rotation around X axis (legacy).  |
| `y`       | number              | Rotation around Y axis (legacy).  |
| `z`       | number              | Rotation around Z axis (legacy).  |
| `axis`    | `"x"`, `"y"`, `"z"` | Axis of rotation.                 |
| `angle`   | number              | Rotation angle.                   |
| `rescale` | boolean             | Scales faces to avoid distortion. |

### Rotation rules:

- If `axis` and `angle` are present, the legacy `x`, `y`, `z` values are ignored.
- As of **1.21.11**, rotations are no longer limited to ±45°.
- As of **1.21.6**, rotations are no longer limited to 22.5° increments.
- Multi‑axis rotation is now supported.

---

## **7.3 Shading**

### **shade** _(boolean)_

Controls whether the element’s faces receive directional shading.

- `true` — default
- `false` — disables directional shading
  - AO still applies
  - Light‑level shading still applies

---

## **7.4 Light Emission**

### **light_emission** _(integer)_

Minimum light level the element receives.

- Range: **0–15**
- Default: **0**

---

## **7.5 Faces**

### **faces** _(object)_

Defines the six possible faces of the cuboid:

- `down`
- `up`
- `north`
- `south`
- `west`
- `east`

Each face is optional; omitted faces do not render.

---

# **7.5.1 Face Properties**

Each face contains:

| Field       | Type      | Description                              |
| ----------- | --------- | ---------------------------------------- |
| `uv`        | number[4] | Texture coordinates `[x1, y1, x2, y2]`.  |
| `texture`   | string    | Texture variable reference (`"#side"`).  |
| `cullface`  | string    | Face to cull when adjacent block exists. |
| `rotation`  | integer   | Texture rotation (0, 90, 180, 270).      |
| `tintindex` | integer   | Tint index (−1 = no tint).               |

### UV rules:

- If omitted, UV is auto‑generated from element geometry.
- UV outside 0–16 behaves inconsistently.
- Swapping x1/x2 flips the texture.

### Cullface rules:

- Values: `down`, `up`, `north`, `south`, `west`, `east`
- Determines:
  - Whether the face is culled
  - Which side’s light level is used

### Tint index:

- `-1` — no tint
- Any other value — passed to BlockColors
- Vanilla blocks do not use multiple tint indices

---

# **8. Display Transforms**

Although primarily used by **item models**, block models may also define a `display` section.
This controls how the block model appears when rendered as an item (e.g., in inventory, in hand, in item frames).

### **display** _(object)_

Contains transformations for different rendering contexts.

Valid transform keys:

- `thirdperson_righthand`
- `thirdperson_lefthand`
- `firstperson_righthand`
- `firstperson_lefthand`
- `gui`
- `head`
- `ground`
- `fixed`

Each transform contains:

| Field         | Type      | Description                                     |
| ------------- | --------- | ----------------------------------------------- |
| `rotation`    | number[3] | Rotation in degrees `[x, y, z]`.                |
| `translation` | number[3] | Position offset `[x, y, z]`. Clamped to −80…80. |
| `scale`       | number[3] | Scale factor. Clamped to max 4.                 |

### Notes:

- Translations are applied **before** rotations.
- If a transform is defined but missing one of the fields (`rotation`, `translation`, `scale`), the missing fields **are not inherited** from the parent.

---

# **9. Blockbench‑Only Fields**

These fields are ignored by Minecraft but used by Blockbench for editing.

### **name** _(string)_

Human‑readable name for an element.

### **texture_size** _(integer[2])_

Specifies the texture atlas size used by Blockbench.

Example:

```
"texture_size": [64, 32]
```

---

# **10. Use Cases for Block Models**

Block models are used in the following contexts:

| Use Case            | Applies To                       | Respects `shade=false`? |
| ------------------- | -------------------------------- | ----------------------- |
| Placed blocks       | All blocks except hardcoded ones | Yes                     |
| Falling blocks      | All blocks except hardcoded ones | Yes                     |
| Piston‑moved blocks | All blocks except hardcoded ones | Yes                     |
| Lit TNT             | TNT                              | No                      |

Hardcoded blocks and fluids (e.g., water, lava, fire, some plants) do **not** use block models.

---

# **11. Display Contexts (Item Rendering)**

When a block is rendered as an item, the following display transforms apply:

| Use Case                                | Display Type            |
| --------------------------------------- | ----------------------- |
| Inventory items                         | `gui`                   |
| Items on mob/player heads               | `head`                  |
| Dropped items                           | `ground`                |
| Items in item frames                    | `fixed`                 |
| Items held in right hand (third person) | `thirdperson_righthand` |
| Items held in left hand (third person)  | `thirdperson_lefthand`  |
| Items held in right hand (first person) | `firstperson_righthand` |
| Items held in left hand (first person)  | `firstperson_lefthand`  |
| Item display entities                   | As specified            |

---

# **12. Limitations**

### **12.1 Non‑Remodelable Blocks**

Some blocks cannot have their visual models changed via resource packs, including:

- Fluids (water, lava)
- Fire
- Portals
- Enchanting table book
- Certain particle‑based or animated sub‑elements

These blocks still have **particle textures**, but not editable models.

### **12.2 Entity Models**

Block models cannot modify:

- Entity geometry
- Mob models
- Armor models
- Held item transforms for non‑humanoid mobs (hardcoded)

### **12.3 Hardcoded Exceptions**

Some blocks ignore model shading or lighting rules:

- Lit TNT ignores `shade=false`
- Some blocks ignore `cullface`
- Some blocks ignore `light_emission`

---

# **13. Summary of Block Model Structure**

A block model consists of:

- Optional inheritance (`parent`)
- Optional AO toggle (`ambientocclusion`)
- Texture variable definitions (`textures`)
- Zero or more cuboid elements (`elements`)
- Optional item display transforms (`display`)
- Optional Blockbench metadata (`name`, `texture_size`)

The core of the model is the **elements**, each defining:

- Geometry (`from`, `to`)
- Rotation (`rotation`)
- Lighting (`shade`, `light_emission`)
- Per‑face texture mapping (`faces`)

---

# **14. Detailed Field Reference**

This section provides a concise, structured reference for every field used in block models.

---

## **14.1 Root-Level Fields**

### **parent**

**Type:** `string`
**Description:**
Specifies a parent model to inherit from.
If both `parent` and `elements` are present, the child’s `elements` override the parent’s.

---

### **ambientocclusion**

**Type:** `boolean`
**Default:** `true`
**Description:**
Enables or disables ambient occlusion shading.

---

### **textures**

**Type:** `object<string, string>`
**Description:**
Defines texture variables used by faces.
Values must be valid resource locations.

Special variable:

- **particle** — used for block breaking particles, portal overlay, and fluid still textures.

---

### **elements**

**Type:** `array<object>`
**Description:**
Defines the cuboids that make up the model.
If omitted, the model may rely entirely on its parent.

---

### **display**

**Type:** `object`
**Description:**
Defines item rendering transforms for various contexts.

---

### **name** _(Blockbench only)_

**Type:** `string`
**Description:**
Human-readable name for an element.

---

### **texture_size** _(Blockbench only)_

**Type:** `integer[2]`
**Description:**
Specifies the texture atlas size used by Blockbench.

---

## **14.2 Element Fields**

Each element in `elements[]` contains:

---

### **from**

**Type:** `number[3]`
**Range:** −16 to 32
**Description:**
Start coordinate of the cuboid.

---

### **to**

**Type:** `number[3]`
**Range:** −16 to 32
**Description:**
End coordinate of the cuboid.

---

### **rotation**

**Type:** `object`
**Description:**
Defines rotation of the cuboid.

Fields:

| Field     | Type                | Description                               |
| --------- | ------------------- | ----------------------------------------- |
| `origin`  | number[3]           | Pivot point for rotation.                 |
| `x`       | number              | Legacy X rotation.                        |
| `y`       | number              | Legacy Y rotation.                        |
| `z`       | number              | Legacy Z rotation.                        |
| `axis`    | `"x"`, `"y"`, `"z"` | Rotation axis.                            |
| `angle`   | number              | Rotation angle.                           |
| `rescale` | boolean             | Adjusts face scaling to avoid distortion. |

Notes:

- If `axis` and `angle` are present, legacy `x`, `y`, `z` are ignored.
- As of 1.21.11, multi-axis rotation is supported.
- As of 1.21.6, rotations are no longer limited to 22.5° increments.

---

### **shade**

**Type:** `boolean`
**Default:** `true`
**Description:**
Controls whether directional shading is applied.

---

### **light_emission**

**Type:** `integer`
**Range:** 0–15
**Default:** 0
**Description:**
Minimum light level the element receives.

---

### **faces**

**Type:** `object`
**Description:**
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

## **14.3 Face Fields**

Each face contains:

---

### **uv**

**Type:** `number[4]`
**Format:** `[x1, y1, x2, y2]`
**Description:**
Defines the texture region to use.

Rules:

- If omitted, UV is auto-generated.
- UV outside 0–16 behaves inconsistently.
- Swapping x1/x2 flips the texture.

---

### **texture**

**Type:** `string`
**Format:** `"#<variable>"`
**Description:**
References a texture variable defined in `textures`.

---

### **cullface**

**Type:** `string`
**Enum:** `down`, `up`, `north`, `south`, `west`, `east`
**Description:**
Determines whether the face is hidden when touching another block.

Also determines which side’s light level is used.

---

### **rotation**

**Type:** `integer`
**Enum:** `0`, `90`, `180`, `270`
**Description:**
Rotates the texture clockwise (counterclockwise for `down`).

---

### **tintindex**

**Type:** `integer`
**Default:** `-1`
**Description:**
Applies a tint from BlockColors.

- `-1` = no tint
- Any other value = tint index

Vanilla blocks do not use multiple tint indices.

---

# **15. Rendering Behavior**

This section summarizes how block models behave in the game engine.

---

## **15.1 Shading Behavior**

- `shade=false` disables directional shading but not:
  - ambient occlusion
  - light-level shading

- Some blocks ignore `shade=false` (e.g., lit TNT).

---

## **15.2 Culling Behavior**

- `cullface` hides faces adjacent to opaque blocks.
- If omitted, the face is always rendered.
- Some blocks ignore culling rules (e.g., leaves with fancy graphics).

---

## **15.3 Light Emission Behavior**

- `light_emission` sets the **minimum** light level.
- Does not make the block emit light; that is controlled by block properties, not models.

---

## **15.4 Rotation Behavior**

- Rotations apply to the entire cuboid.
- Multi-axis rotation is now supported.
- Rotations may distort UV unless `rescale=true`.

---

# **16. Complete Example (Fully Annotated)**

Below is a minimal but representative block model demonstrating all major fields.
This example is **not** from the wiki text (to avoid copyright issues) — it is an original illustrative model consistent with the documented rules.

```json
{
  "parent": "block/cube",
  "ambientocclusion": true,

  "textures": {
    "particle": "minecraft:block/stone",
    "side": "minecraft:block/stone",
    "top": "minecraft:block/stone"
  },

  "elements": [
    {
      "from": [0, 0, 0],
      "to": [16, 16, 16],

      "rotation": {
        "origin": [8, 8, 8],
        "axis": "y",
        "angle": 45,
        "rescale": true
      },

      "shade": true,
      "light_emission": 0,

      "faces": {
        "north": { "texture": "#side", "uv": [0, 0, 16, 16] },
        "south": { "texture": "#side" },
        "east": { "texture": "#side", "cullface": "east" },
        "west": { "texture": "#side", "cullface": "west" },
        "up": { "texture": "#top", "rotation": 90 },
        "down": { "texture": "#side" }
      }
    }
  ],

  "display": {
    "gui": {
      "rotation": [30, 45, 0],
      "translation": [0, 0, 0],
      "scale": [0.8, 0.8, 0.8]
    }
  },

  "texture_size": [16, 16]
}
```

This example demonstrates:

- Parent inheritance
- Texture variable definitions
- A single cuboid element
- Rotation around the Y axis
- Per‑face texture mapping
- Display transforms for GUI rendering
- Blockbench metadata

---

# **17. Best Practices for Model Authors**

These recommendations help ensure models behave consistently across versions and tools.

---

## **17.1 Geometry**

- Keep coordinates within the valid range (−16 to 32).
- Avoid overlapping cuboids unless intentional.
- Use `rescale: true` when rotating elements to avoid UV distortion.

---

## **17.2 Textures**

- Always define a `particle` texture.
- Use consistent naming for texture variables (`side`, `top`, `bottom`, etc.).
- Avoid UV values outside 0–16 unless you understand the quirks.

---

## **17.3 Faces**

- Omit faces that will never be visible (e.g., internal geometry).
- Use `cullface` to improve performance on opaque blocks.
- Use `tintindex` only when the block is designed to be tinted.

---

## **17.4 Display Transforms**

- Keep GUI scale ≤ 1.0 to avoid clipping.
- Use consistent transforms across related items (e.g., slabs, stairs).
- Remember that missing fields do **not** inherit from parents.

---

## **17.5 Blockbench Metadata**

- Safe to include; Minecraft ignores it.
- Useful for collaboration and editing.
- Do not rely on Blockbench fields for in‑game behavior.

---

# **18. Version Notes (Non‑Historical)**

These are **non‑copyrighted**, high‑level summaries of changes relevant to model authors.

- **1.21.6** — Block model rotations are no longer restricted to 22.5° increments.
- **1.21.11** — Elements can now rotate around multiple axes; angle limits removed.
- **1.21.4** — Overrides removed from block models; item model system reworked.
- **1.9** — UV became optional; auto‑generation introduced.
- **1.8** — Block model system introduced.

---

# **19. Glossary**

| Term                       | Definition                                      |
| -------------------------- | ----------------------------------------------- |
| **AO (Ambient Occlusion)** | Soft shadowing based on geometry.               |
| **Cullface**               | Face hidden when adjacent to another block.     |
| **Tintindex**              | Index used to apply biome or block color tints. |
| **Element**                | A cuboid that forms part of a model.            |
| **Parent Model**           | A model that another model inherits from.       |
| **Resource Location**      | Namespaced identifier for assets.               |

---

# **20. Final Notes**

This document provides a complete, strict, and tooling‑friendly specification of Minecraft block models based solely on the raw wiki text, rewritten into clean Markdown.

It is suitable for:

- Resource pack authors
- Modding tool developers
- JSON schema validation
- IDE integrations
- Automated pipelines

---
