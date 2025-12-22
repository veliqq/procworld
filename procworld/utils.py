import random

def weighted_choice(weights):
    total = sum(weights.values())
    # Normalize weights
    for k in weights:
        weights[k] /= total
    r = random.random()
    cumulative = 0
    for k, w in weights.items():
        cumulative += w
        if r < cumulative:
            return k
    return list(weights.keys())[0]
