# ProcWorld

Advanced **Procedural World Generator** library for Python. Generate maps with biomes, rivers, lakes, mountains, and elevation. Export maps to **JSON** or **PNG** for games, simulations, or visualizations.

---

## Features

* Procedural terrain generation with multiple **biomes**:

  * Forests, plains, mountains, deserts, water
* **Rivers** and **lakes** placement
* **Elevation map** generation
* **Terminal display** with emojis
* **Export to JSON** for programmatic use
* **Export to PNG** for visual representation
* Fully **modular and library-ready**
* **Seeded randomness** for reproducible worlds

---

## Installation

```bash
pip install procworld
```

Optional dependency for PNG export:

```bash
pip install Pillow
```

---

## Usage

```python
from procworld import WorldGenerator

# Create a world
world = WorldGenerator(width=40, height=20)
world.generate()

# Display in terminal
print(world.display())

# Export to JSON
world.export_json("example_world.json")

# Export to PNG
world.export_png("example_world.png")

# Access raw data
terrain_map = world.get_map()
elevation_map = world.get_elevation()
print(f"Seed used: {world.seed}")
```

---

## Parameters

* `width` (int): Width of the world map (default 50)
* `height` (int): Height of the world map (default 20)
* `seed` (int, optional): Seed for reproducible worlds. Random if None

---

## Export Functions

* `export_json(filename="world.json")`: Save map and elevation data as JSON
* `export_png(filename="world.png", cell_size=20)`: Save map as PNG image

---

## Contributing

* Fork the repository
* Create a new branch for your feature
* Submit a pull request with improvements or new biomes

---

## License

MIT License © veliqq

---

## Example Output (Terminal)

```
🌾🌾🌲🌲🌾🌾🌊🌾🌾🌲
🌲🌲🌾🌾🌾🌊🌊🌲🌾🌾
🌾🌾🌾🌲🌲🌲🌾🌾🌾🌲
⛰️⛰️🌾🌾🌾🌾🌾🌲🌲🌾
🌾🌾🌾🌾💧💧💧🌾🌲🌲
```

---

**ProcWorld** makes generating and visualizing procedural worlds simple, fast, and fun!
