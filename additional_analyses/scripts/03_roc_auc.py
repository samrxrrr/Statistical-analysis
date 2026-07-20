#!/usr/bin/env python3
"""
===========================================================
03_roc_auc.py

Receiver Operating Characteristic (ROC)
Area Under the Curve (AUC)

Project:
Statistical-analysis

Author:
Mohd Sameer
===========================================================
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.metrics import (
    roc_curve,
    roc_auc_score,
    confusion_matrix
)

# ---------------------------------------------------------
# Directories
# ---------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "results" / "logistic_predictions.csv"

RESULTS = ROOT / "additional_analyses" / "results"

FIGURES = ROOT / "additional_analyses" / "figures"

RESULTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# ---------------------------------------------------------
# Read data
# ---------------------------------------------------------

df = pd.read_csv(DATA)

y_true = df["MUV_Binary"].astype(int)

y_prob = df["Predicted"].astype(float)

# ---------------------------------------------------------
# ROC
# ---------------------------------------------------------

fpr, tpr, thresholds = roc_curve(y_true, y_prob)

auc = roc_auc_score(y_true, y_prob)

# ---------------------------------------------------------
# Youden Index
# ---------------------------------------------------------

youden = tpr - fpr

best = np.argmax(youden)

best_threshold = thresholds[best]

# ---------------------------------------------------------
# Classification
# ---------------------------------------------------------

prediction = (y_prob >= best_threshold).astype(int)

tn, fp, fn, tp = confusion_matrix(
    y_true,
    prediction
).ravel()

sensitivity = tp / (tp + fn)

specificity = tn / (tn + fp)

accuracy = (tp + tn) / len(df)

# ---------------------------------------------------------
# Save ROC data
# ---------------------------------------------------------

roc_table = pd.DataFrame({

    "Threshold": thresholds,

    "False_Positive_Rate": fpr,

    "True_Positive_Rate": tpr

})

roc_table.to_csv(

    RESULTS / "03_roc_curve_points.csv",

    index=False

)

# ---------------------------------------------------------
# Summary
# ---------------------------------------------------------

with open(

    RESULTS / "03_roc_auc_summary.txt",

    "w",

    encoding="utf-8"

) as f:

    f.write("ROC CURVE ANALYSIS\n")

    f.write("="*60 + "\n\n")

    f.write(f"AUC                  : {auc:.6f}\n")

    f.write(f"Optimal threshold    : {best_threshold:.6f}\n")

    f.write(f"Sensitivity          : {sensitivity:.6f}\n")

    f.write(f"Specificity          : {specificity:.6f}\n")

    f.write(f"Accuracy             : {accuracy:.6f}\n")

# ---------------------------------------------------------
# Figure
# ---------------------------------------------------------

plt.figure(figsize=(6,6))

plt.plot(

    fpr,

    tpr,

    linewidth=2,

    label=f"AUC = {auc:.3f}"

)

plt.plot(

    [0,1],

    [0,1],

    linestyle="--"

)

plt.scatter(

    fpr[best],

    tpr[best],

    s=80,

    label="Optimal threshold"

)

plt.xlabel("False Positive Rate")

plt.ylabel("True Positive Rate")

plt.title("ROC Curve")

plt.legend()

plt.tight_layout()

plt.savefig(

    FIGURES / "Figure10_ROC_Curve.png",

    dpi=600

)

plt.savefig(

    FIGURES / "Figure10_ROC_Curve.pdf"

)

plt.close()

# ---------------------------------------------------------
# Console
# ---------------------------------------------------------

print()

print("="*60)

print("ROC ANALYSIS")

print("="*60)

print(f"AUC                : {auc:.6f}")

print(f"Threshold          : {best_threshold:.6f}")

print(f"Sensitivity        : {sensitivity:.6f}")

print(f"Specificity        : {specificity:.6f}")

print(f"Accuracy           : {accuracy:.6f}")

print("="*60)

print()

print("Outputs")

print("-------")

print(RESULTS / "03_roc_curve_points.csv")

print(RESULTS / "03_roc_auc_summary.txt")

print(FIGURES / "Figure10_ROC_Curve.png")

print(FIGURES / "Figure10_ROC_Curve.pdf")

print()

print("Done.")

