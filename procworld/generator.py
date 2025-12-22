import random
import json
from PIL import Image, ImageDraw
from .biomes import TERRAINS, BIOME_RULES
from .utils import weighted_choice

class WorldGenerator:
    def __init__(self, width=50, height=20, seed=None):
        self.width = width
        self.height = height
        self.seed = seed or random.randint(0, 999999)
        random.seed(self.seed)
        self.map = [["" for _ in range(width)] for _ in range(height)]
        self.elevation = [[0 for _ in range(width)] for _ in range(height)]

    def generate(self):
        # Step 1: terrain and elevation
        for y in range(self.height):
            for x in range(self.width):
                biome = self._determine_biome(x, y)
                terrain = weighted_choice(BIOME_RULES[biome])
                self.map[y][x] = terrain
                self.elevation[y][x] = self._calculate_elevation(x, y)

        # Step 2: rivers & lakes
        self._generate_rivers()
        self._generate_lakes()

    def _determine_biome(self, x, y):
        if y < self.height * 0.2 or y > self.height * 0.8:
            return "default"
        choice = random.random()
        if choice < 0.3:
            return "forest"
        elif choice < 0.5:
            return "plains"
        elif choice < 0.7:
            return "mountain"
        else:
            return "desert"

    def _calculate_elevation(self, x, y):
        return random.randint(0, 100)

    def _generate_rivers(self, count=2):
        for _ in range(count):
            x = random.randint(0, self.width - 1)
            for y in range(self.height):
                self.map[y][x] = "river"
                # Slight meander
                if random.random() < 0.5 and x > 0:
                    x -= 1
                elif random.random() < 0.5 and x < self.width - 1:
                    x += 1

    def _generate_lakes(self, count=3):
        for _ in range(count):
            lx = random.randint(0, self.width - 1)
            ly = random.randint(0, self.height - 1)
            size = random.randint(2, 5)
            for y in range(max(0, ly-size), min(self.height, ly+size)):
                for x in range(max(0, lx-size), min(self.width, lx+size)):
                    self.map[y][x] = "lake"

    def display(self):
        return "\n".join("".join(TERRAINS[cell] for cell in row) for row in self.map)

    def get_map(self):
        return self.map

    def get_elevation(self):
        return self.elevation

    def export_json(self, filename="world.json"):
        data = {
            "seed": self.seed,
            "width": self.width,
            "height": self.height,
            "map": self.map,
            "elevation": self.elevation
        }
        with open(filename, "w") as f:
            json.dump(data, f, indent=4)
        print(f"World exported as JSON: {filename}")

    def export_png(self, filename="world.png", cell_size=20):
        color_map = {
            "water": (64, 164, 223),
            "river": (0, 102, 204),
            "lake": (0, 153, 204),
            "forest": (34, 139, 34),
            "mountain": (139, 137, 137),
            "plain": (144, 238, 144),
            "desert": (237, 201, 175)
        }

        img_width = self.width * cell_size
        img_height = self.height * cell_size
        img = Image.new("RGB", (img_width, img_height))
        draw = ImageDraw.Draw(img)

        for y in range(self.height):
            for x in range(self.width):
                color = color_map.get(self.map[y][x], (0, 0, 0))
                draw.rectangle(
                    [x*cell_size, y*cell_size, (x+1)*cell_size, (y+1)*cell_size],
                    fill=color
                )

        img.save(filename)
        print(f"World exported as PNG: {filename}")
