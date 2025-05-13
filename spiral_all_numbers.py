import matplotlib.pyplot as plt
import math

# Initialize
coordinates = []
angle = 0
radius = 5
delta_angle = 0.1
delta_radius = 0.5

# Function to check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True

# Compute positions once and store number + coordinates
for i in range(2, 1000):
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    coordinates.append((i, x, y))  # Store (number, x, y)
    angle += delta_angle
    radius += delta_radius

# Separate all coordinates
x_natural = [x for _, x, _ in coordinates]
y_natural = [y for _, _, y in coordinates]

# Filter only primes
x_prime = [x for i, x, y in coordinates if is_prime(i)]
y_prime = [y for i, x, y in coordinates if is_prime(i)]

# Plotting
plt.figure(figsize=(8, 8))
plt.scatter(x_natural, y_natural, s=3, color='lightgray', label='All Numbers')
plt.scatter(x_prime, y_prime, s=10, color='red', label='Prime Numbers')
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title("Spiral of Natural Numbers with Prime Highlights")
plt.legend()
plt.show()
