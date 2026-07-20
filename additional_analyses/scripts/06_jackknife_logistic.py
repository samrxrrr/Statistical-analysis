#!/usr/bin/env python3
"""
===========================================================
06_jackknife_logistic.py

Leave-One-Out (Jackknife) Sensitivity Analysis
for Binary Logistic Regression

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
import statsmodels.api as sm

# ----------------------------------------------------------
# Directories
# ----------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data" / "AP Research 25-26 - Sheet1.csv"

RESULTS = ROOT / "additional_analyses" / "results"

FIGURES = ROOT / "additional_analyses" / "figures"

RESULTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------
# Read data
# ----------------------------------------------------------

df = pd.read_csv(DATA)

dose_col = "Thymoquinone Concentration"
outcome_col = "Multivulva presence (Yes or No)"

df[dose_col] = (
    df[dose_col]
    .astype(str)
    .str.replace("μ", "u")
    .str.replace("µ", "u")
    .str.extract(r"(\d+)")
    .astype(int)
)

df["Event"] = (
    df[outcome_col]
    .astype(str)
    .str.strip()
    .str.lower()
    .eq("yes")
    .astype(int)
)

# ----------------------------------------------------------
# Full model
# ----------------------------------------------------------

X_full = sm.add_constant(df[[dose_col]])
y_full = df["Event"]

full_model = sm.Logit(y_full, X_full).fit(disp=False)

full_intercept = full_model.params["const"]
full_beta = full_model.params[dose_col]

# ----------------------------------------------------------
# Jackknife
# ----------------------------------------------------------

rows = []

for i in range(len(df)):

    temp = df.drop(index=i)

    X = sm.add_constant(temp[[dose_col]])
    y = temp["Event"]

    model = sm.Logit(y, X).fit(disp=False)

    rows.append({
        "Observation_Removed": i,
        "Intercept": model.params["const"],
        "Dose_Coefficient": model.params[dose_col]
    })

jack = pd.DataFrame(rows)

jack["Intercept_Diff"] = jack["Intercept"] - full_intercept
jack["Dose_Diff"] = jack["Dose_Coefficient"] - full_beta

# ----------------------------------------------------------
# Summary statistics
# ----------------------------------------------------------

summary = pd.DataFrame({
    "Statistic": [
        "Full intercept",
        "Full dose coefficient",
        "Mean dose coefficient",
        "SD dose coefficient",
        "Minimum dose coefficient",
        "Maximum dose coefficient",
        "Maximum absolute change"
    ],
    "Value": [
        full_intercept,
        full_beta,
        jack["Dose_Coefficient"].mean(),
        jack["Dose_Coefficient"].std(),
        jack["Dose_Coefficient"].min(),
        jack["Dose_Coefficient"].max(),
        np.abs(jack["Dose_Diff"]).max()
    ]
})

# ----------------------------------------------------------
# Save outputs
# ----------------------------------------------------------

jack.to_csv(
    RESULTS / "06_jackknife_coefficients.csv",
    index=False
)

summary.to_csv(
    RESULTS / "06_jackknife_summary.csv",
    index=False
)

with open(
    RESULTS / "06_jackknife_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("JACKKNIFE LOGISTIC REGRESSION\n")
    f.write("=" * 60 + "\n\n")

    f.write(summary.to_string(index=False))

# ----------------------------------------------------------
# Figure
# ----------------------------------------------------------

plt.figure(figsize=(8,4))

plt.plot(
    jack["Dose_Coefficient"],
    linewidth=1.5
)

plt.axhline(
    full_beta,
    linestyle="--",
    linewidth=1
)

plt.xlabel("Observation Removed")

plt.ylabel("Dose Coefficient")

plt.title("Jackknife Sensitivity of Logistic Regression")

plt.tight_layout()

plt.savefig(
    FIGURES / "Figure12_Jackknife_Logistic.png",
    dpi=600
)

plt.savefig(
    FIGURES / "Figure12_Jackknife_Logistic.pdf"
)

plt.close()

# ----------------------------------------------------------
# Console
# ----------------------------------------------------------

print()

print("=" * 70)
print("JACKKNIFE LOGISTIC SENSITIVITY")
print("=" * 70)

print(summary.round(6))

print("=" * 70)

print()

print("Outputs")
print("-------")

print(RESULTS / "06_jackknife_coefficients.csv")
print(RESULTS / "06_jackknife_summary.csv")
print(RESULTS / "06_jackknife_summary.txt")
print(FIGURES / "Figure12_Jackknife_Logistic.png")
print(FIGURES / "Figure12_Jackknife_Logistic.pdf")

print()
print("Done.")

