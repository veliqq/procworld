TERRAINS = {
    "water": "~",
    "river": "🌊",
    "lake": "💧",
    "forest": "🌲",
    "mountain": "⛰️",
    "plain": "🌾",
    "desert": "🏜️"
}

# Biome probability rules
BIOME_RULES = {
    "default": {"water":0.1, "forest":0.2, "mountain":0.1, "plain":0.5, "desert":0.1},
    "forest": {"water":0.05, "forest":0.6, "mountain":0.1, "plain":0.2, "desert":0.05},
    "desert": {"water":0.05, "forest":0.05, "mountain":0.1, "plain":0.3, "desert":0.5},
    "mountain": {"water":0.05, "forest":0.1, "mountain":0.7, "plain":0.1, "desert":0.05},
    "plains": {"water":0.05, "forest":0.2, "mountain":0.05, "plain":0.7, "desert":0.0},
}
