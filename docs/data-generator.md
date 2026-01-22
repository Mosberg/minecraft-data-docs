# Data generator

> **Edition:** Java Edition only

This tutorial shows how to run the **data generator** that is included in the Java Edition client and server distributions since **1.13**.

---

## Purpose

The data generator can:

- **Convert NBT files**
  - Convert GZip-compressed NBT files with `.nbt` extensions (as used in structure files) **to and from** stringified NBT files with `.snbt` extensions.
- **Generate vanilla data pack contents**
  - Generate all contents of the vanilla data pack (except `pack.mcmeta`).
- **Create JSON reports**
  - Generate JSON reports of:
    - All block states
    - All registries
    - The full vanilla command tree

---

## Getting started

It is recommended that you download the **official server distribution** of the Minecraft version you want to target.

1. Place the server JAR in a directory of your choice.
2. Open a **terminal** or **command prompt** in that directory.
3. Make sure you have Java installed.
4. Run:

```bash
java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar
```

If everything is set up correctly, the command line prints a list of options and descriptions for the data generator.

---

## Generating data pack contents

To generate the contents of the vanilla data pack, run:

```bash
java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --server
```

- The contents of the vanilla data pack (except `pack.mcmeta`) are generated into a directory named `generated` in the **current working directory**.

---

## Generating stringified server DAT files

Many server data files in the world directory use the `.dat` extension and are stored in **NBT format**. You can convert them to human‑readable **SNBT** using the data generator.

### Step‑by‑step

1. **Open a terminal or command prompt** in the same directory as your server JAR.

2. **Create an `input` directory** next to the server JAR:

   ```bash
   mkdir input
   ```

3. **Copy a `.dat` file into `input` and rename it to `.nbt`:**
   - Linux:

     ```bash
     cp world/level.dat input/level.nbt
     ```

   - Windows:

     ```batch
     copy world\level.dat input\level.nbt
     ```

4. **Run the data generator with the `--dev` flag** to convert all `.nbt` files in `input` to `.snbt`:

   ```bash
   java -DbundlerMainClass="net.minecraft.data.Main" -jar server.jar --dev --input "input"
   ```

   Example output:

   ```text
   [17:17:17] [main/INFO]: Starting provider: NBT to SNBT
   [17:17:17] [main/INFO]: NBT to SNBT finished after 3 ms
   [17:17:17] [main/INFO]: All providers took: 34 ms
   ```

5. A new directory named `generated` appears in the current directory. It contains the **stringified SNBT** versions of the input files.

6. View them with command‑line tools (e.g. `cat` on Linux) or open them in a text editor.

---

## Stringify all DAT files

You can stringify **every `.dat` file** in your world for inspection or experimentation.

### Linux

1. From the directory containing `input`, run:

   ```bash
   # Replace path/to/world/data with your world data path (often just "world")
   find path/to/world/data -name \*.dat -exec cp {} input \;
   ```

2. Rename all copied `.dat` files to `.nbt`:

   ```bash
   for file in input/*.dat; do mv "$file" "${file/.dat/.nbt}"; done
   ```

3. Re‑run the data generator with `--dev` as described above.

### Windows

1. From the directory containing `input`, run:

   ```batch
   rem Replace path\to\world\data with your world data path (often just "world")
   copy path\to\world\data\*.dat input\*.nbt
   ```

2. Re‑run the data generator with `--dev` as described above.

---

## See also

- Data packs
- Importing a data pack
