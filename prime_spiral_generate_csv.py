# (Prime spiral generate .CSV).py
# than after ->
# (Prime spiral calculate metrics from the .CSV).py

import math
import csv

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Generate prime-based polar spiral points
angle = 0
radius = 5
delta_angle = 0.1
delta_radius = 0.5

x_coords = []
y_coords = []

for i in range(2, 10000):
    if is_prime(i):
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        x_coords.append(x)
        y_coords.append(y)
        angle += delta_angle
        radius += delta_radius

# Function to calculate distances between points with a given step
def calculate_distances(step):
    distances = []
    for i in range(len(x_coords) - step):
        x1, y1 = x_coords[i], y_coords[i]
        x2, y2 = x_coords[i + step], y_coords[i + step]
        dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        distances.append(dist)
    return distances

# Calculate distances for each step
distances_63 = calculate_distances(63)
distances_126 = calculate_distances(126)
distances_189 = calculate_distances(189)

# Determine the max length
max_len = max(len(distances_63), len(distances_126), len(distances_189))

# Pad each list with NaN to match the longest one
def pad_with_nan(lst, target_len):
    return lst + [float('nan')] * (target_len - len(lst))

distances_63 = pad_with_nan(distances_63, max_len)
distances_126 = pad_with_nan(distances_126, max_len)
distances_189 = pad_with_nan(distances_189, max_len)

# Save to CSV
with open('prime_spiral_distances_columns.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Distance (63 steps)', 'Distance (126 steps)', 'Distance (189 steps)'])
    for i in range(max_len):
        writer.writerow([distances_63[i], distances_126[i], distances_189[i]])

print("File 'prime_spiral_distances_columns.csv' successfully saved!")
