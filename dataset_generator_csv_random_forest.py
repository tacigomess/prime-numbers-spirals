import math
import os

import numpy as np
import pandas as pd
from scipy.spatial import KDTree

# Check primality
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate coordinates
data = []
angle = 0
radius = 5
delta_theta = 0.1
delta_radius = 0.5

for n in range(2, 10001):
    r = radius
    theta = angle
    x = math.cos(theta) * r
    y = math.sin(theta) * r
    data.append({'n': n, 'x': x, 'y': y, 'r': r, 'theta': theta, 'is_prime': int(is_prime(n))})
    angle += delta_theta
    radius += delta_radius

df = pd.DataFrame(data)

# Build KDTree with prime coordinates
prime_coords = df[df["is_prime"] == 1][["x", "y"]].values
prime_tree = KDTree(prime_coords)

# Compute density and avg_prime_dist
densities = []
avg_dists = []

for idx, row in df.iterrows():
    x, y = row["x"], row["y"]
    neighbors = prime_tree.query_ball_point([x, y], r=10)
    densities.append(len(neighbors))

    dists, _ = prime_tree.query([x, y], k=min(4, len(prime_coords)))  # includes self if prime
    if row["is_prime"] == 1:
        dists = dists[1:]  # exclude self
    subset = dists[:3]
    avg_dist = np.mean(subset) if len(subset) > 0 else float('nan')
    #avg_dist = sum(dists[:3]) / len(dists[:3]) if dists[:3] else float('nan')
    avg_dists.append(avg_dist)

df["prime_density"] = densities
df["avg_prime_dist"] = avg_dists

os.makedirs("data", exist_ok=True)

# Salvar o CSV
file_path = "data/prime_spiral_features_dataset.csv"
df.to_csv(file_path, index=False)
file_path
