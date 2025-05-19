import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Load the CSV with the distances
df = pd.read_csv("prime_spiral_distances_columns.csv")

# Create a dictionary to store the results
stats = {}

for col in df.columns:
    data = df[col].dropna()  # Remove NaN before calculations
    mean = data.mean()
    std = data.std()
    var = data.var()
    rel_std = (std / mean) * 100

    stats[col] = {
        'Mean': mean,
        'Standard Deviation': std,
        'Relative Std Dev (%)': rel_std,
        'Variance': var
    }

# Show results
for step, values in stats.items():
    print(f"\n{step}:")
    for key, val in values.items():
        print(f"  {key}: {val:.4f}")

# Preparing the data to generate the graphs
# Organizing the data
steps = list(stats.keys())
means = [stats[step]['Mean'] for step in steps]
stds = [stats[step]['Standard Deviation'] for step in steps]
rel_stds = [stats[step]['Relative Std Dev (%)'] for step in steps]
variances = [stats[step]['Variance'] for step in steps]

# Plot: Average of distances
plt.figure(figsize=(8, 5))
plt.bar(steps, means)
plt.title("Mean Distance")
plt.ylabel("Distance")
plt.xlabel("Step")
plt.show()

# Plot: Standard deviation
plt.figure(figsize=(8, 5))
plt.bar(steps, stds)
plt.title("Standard Deviation")
plt.ylabel("Standard Deviation")
plt.xlabel("Step")
plt.show()

# Plot: Relative deviation (%)
plt.figure(figsize=(8, 5))
plt.bar(steps, rel_stds)
plt.title("Relative Standard Deviation (%)")
plt.ylabel("%")
plt.xlabel("Step")
plt.show()

# Plot: Variance
plt.figure(figsize=(8, 5))
plt.bar(steps, variances)
plt.title("Variance")
plt.ylabel("Variance")
plt.xlabel("Step")
plt.show()
