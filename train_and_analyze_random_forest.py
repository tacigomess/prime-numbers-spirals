
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score

# Load dataset
df = pd.read_csv("data/prime_spiral_features_dataset.csv")
#df = pd.read_csv("data/teste_prime_spiral_log_shell_dataset_3D.csv")
#df = pd.read_csv("data/prime_spiral_shell_features_extended.csv")

# Features and target
features = ['x', 'y', 'r', 'theta', 'prime_density', 'avg_prime_dist']
X = df[features]
y = df['is_prime']

# Split into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create and train model
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# --- 1. Evaluation ---
print("Confusion Matrix:")
print(confusion_matrix(y_test, model.predict(X_test)))

print("\nClassification Report:")
print(classification_report(y_test, model.predict(X_test)))

print("Accuracy Score:", accuracy_score(y_test, model.predict(X_test)))

# --- 2. Feature Importance ---
importances = model.feature_importances_
print("\nFeature Importances:")
for feat, score in zip(features, importances):
    print(f"{feat}: {score:.4f}")

# Plotting
plt.figure(figsize=(8, 4))
plt.bar(features, importances, color="steelblue")
plt.title("Feature Importance - Random Forest")
plt.ylabel("Importance Score")
plt.tight_layout()
plt.show()
