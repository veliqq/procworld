from procworld import WorldGenerator

# Create world
world = WorldGenerator(width=40, height=20)
world.generate()

# Display in terminal
print(world.display())

# Export to JSON and PNG
world.export_json("example_world.json")
world.export_png("example_world.png")

# Access raw data
terrain_map = world.get_map()
elevation_map = world.get_elevation()
print(f"Seed used: {world.seed}")
