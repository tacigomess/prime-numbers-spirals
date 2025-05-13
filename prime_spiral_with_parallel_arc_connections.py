import math
import matplotlib.pyplot as plt

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

# Spiral parameters
angle = 0
radius = 5
delta_angle = 0.1
delta_radius = 0.5

x_coords = []
y_coords = []

# Generate coordinates for prime numbers in the spiral
for i in range(2, 1000):
    if is_prime(i):
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        x_coords.append(x)
        y_coords.append(y)
        angle += delta_angle
        radius += delta_radius

# Plotting the spiral and connections
fig, ax = plt.subplots(figsize=(8, 8))
ax.set_aspect('equal')
ax.set_facecolor('white')
plt.axis('off')

# Plot the prime number points
ax.scatter(x_coords, y_coords, s=10, color='black')

# Connect primes that are "step" positions apart
step = 63
for i in range(len(x_coords) - step):
    x1, y1 = x_coords[i], y_coords[i]
    x2, y2 = x_coords[i + step], y_coords[i + step]
    ax.plot([x1, x2], [y1, y2], color='blue', linewidth=0.5, alpha=0.6)

plt.title("Connections Between Primes in Parallel Arcs (step = 63)", fontsize=10)
plt.show()
