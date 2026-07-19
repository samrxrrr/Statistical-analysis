import pandas as pd
import numpy as np
from mord import LogisticAT
from sklearn.metrics import accuracy_score

# -----------------------------
# Load data
# -----------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

dose_map = {0:0, 50:1, 100:2}
df["Dose"] = df["Concentration"].map(dose_map)

X = df[["Dose"]].values
y = df["Ectopic_Vulva"].values

# -----------------------------
# Fit ordinal logistic model
# -----------------------------

model = LogisticAT(alpha=1.0)

model.fit(X, y)

pred = model.predict(X)

acc = accuracy_score(y, pred)

print("="*60)
print("ORDINAL LOGISTIC REGRESSION")
print("="*60)

print("\nCoefficient:")
print(model.coef_)

print("\nThresholds:")
print(model.theta_)

print(f"\nTraining Accuracy: {acc:.3f}")

# Odds ratio
OR = np.exp(model.coef_[0])

print(f"\nOdds Ratio per 50 µM increase: {OR:.3f}")

# Save predictions
df["Predicted_Severity"] = pred

df.to_csv(
    "results/ordinal_predictions.csv",
    index=False
)

print("\nPredictions saved.")
