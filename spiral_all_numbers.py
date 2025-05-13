import matplotlib.pyplot as plt
import math

# Generate all natural numbers up to 1000x_natural = []
x_natural = []
y_natural = []
angle = 0
radius = 5
delta_angle = 0.1
delta_radius = 0.5

# All numbers (not just primes)
for i in range(2, 1000):
    x = math.cos(angle) * radius
    y = math.sin(angle) * radius
    x_natural.append(x)
    y_natural.append(y)
    angle += delta_angle
    radius += delta_radius

# Apenas os primos recebem marcações maiores
x_prime = []
y_prime = []

# Reset ângulo e raio para sincronizar com valores
angle = 0
radius = 5

def is_prime(n):
    if n < 2:
        return False
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True

for i in range(2, 1000):
    if is_prime(i):
        x = math.cos(angle) * radius
        y = math.sin(angle) * radius
        x_prime.append(x)
        y_prime.append(y)
    angle += delta_angle
    radius += delta_radius

# Plotando todos os números e destacando os primos
plt.figure(figsize=(8, 8))
plt.scatter(x_natural, y_natural, s=3, color='lightgray', label='All numbers')
plt.scatter(x_prime, y_prime, s=10, color='red', label='Primes')
plt.gca().set_aspect('equal')
plt.axis('off')
plt.title("Spiral of All Numbers with Primes Highlighted")
plt.legend()
plt.show()
