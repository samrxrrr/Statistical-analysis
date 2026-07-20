#!/usr/bin/env python3
"""
===========================================================
04_hosmer_lemeshow.py

Grouped Hosmer-Lemeshow Goodness-of-Fit Test

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

from scipy.stats import chi2

# ----------------------------------------------------------
# Directories
# ----------------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "results" / "logistic_predictions.csv"

RESULTS = ROOT / "additional_analyses" / "results"

FIGURES = ROOT / "additional_analyses" / "figures"

RESULTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------
# Read data
# ----------------------------------------------------------

df = pd.read_csv(DATA)

required = ["Dose", "MUV_Binary", "Predicted"]

missing = [c for c in required if c not in df.columns]

if missing:
    raise ValueError(f"Missing columns: {missing}")

# ----------------------------------------------------------
# Group by predicted probability
# ----------------------------------------------------------

summary = (
    df
    .groupby("Predicted")
    .agg(
        Observations=("MUV_Binary", "count"),
        Observed=("MUV_Binary", "sum")
    )
    .reset_index()
    .rename(columns={"Predicted": "Predicted_Probability"})
)

summary["Expected"] = (
    summary["Predicted_Probability"] *
    summary["Observations"]
)

summary["Observed_No"] = (
    summary["Observed"] * 0 +
    summary["Observations"] -
    summary["Observed"]
)

summary["Expected_No"] = (
    summary["Observations"] -
    summary["Expected"]
)

# ----------------------------------------------------------
# Hosmer-Lemeshow statistic
# ----------------------------------------------------------

eps = 1e-10

hl = np.sum(
    (
        (summary["Observed"] - summary["Expected"]) ** 2
    ) /
    (summary["Expected"] + eps)
    +
    (
        (summary["Observed_No"] - summary["Expected_No"]) ** 2
    ) /
    (summary["Expected_No"] + eps)
)

groups = len(summary)

# degrees of freedom = groups - 2
df_hl = max(groups - 2, 1)

p_value = 1 - chi2.cdf(hl, df_hl)

# ----------------------------------------------------------
# Save table
# ----------------------------------------------------------

summary.to_csv(
    RESULTS / "04_hosmer_lemeshow_table.csv",
    index=False
)

# ----------------------------------------------------------
# Summary report
# ----------------------------------------------------------

with open(
    RESULTS / "04_hosmer_lemeshow_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("HOSMER-LEMESHOW GOODNESS OF FIT\n")
    f.write("=" * 60 + "\n\n")

    f.write(summary.to_string(index=False))

    f.write("\n\n")

    f.write(f"Groups                 : {groups}\n")
    f.write(f"Degrees of freedom     : {df_hl}\n")
    f.write(f"HL statistic           : {hl:.6f}\n")
    f.write(f"P-value                : {p_value:.8f}\n\n")

    if p_value > 0.05:
        f.write(
            "Interpretation:\n"
            "No evidence of lack of fit.\n"
            "Model calibration appears acceptable.\n"
        )
    else:
        f.write(
            "Interpretation:\n"
            "Evidence of poor calibration.\n"
        )

# ----------------------------------------------------------
# Calibration plot
# ----------------------------------------------------------

plt.figure(figsize=(6,6))

plt.plot(
    [0,1],
    [0,1],
    "--",
    linewidth=1
)

plt.scatter(
    summary["Predicted_Probability"],
    summary["Observed"] / summary["Observations"],
    s=90
)

plt.plot(
    summary["Predicted_Probability"],
    summary["Observed"] / summary["Observations"],
    linewidth=2
)

plt.xlabel("Predicted probability")

plt.ylabel("Observed proportion")

plt.title("Calibration Plot")

plt.tight_layout()

plt.savefig(
    FIGURES / "Figure11_Calibration.png",
    dpi=600
)

plt.savefig(
    FIGURES / "Figure11_Calibration.pdf"
)

plt.close()

# ----------------------------------------------------------
# Console
# ----------------------------------------------------------

print()
print("=" * 65)
print("GROUPED HOSMER-LEMESHOW TEST")
print("=" * 65)

print(summary)

print()

print(f"Groups               : {groups}")
print(f"Degrees of freedom   : {df_hl}")
print(f"HL statistic         : {hl:.6f}")
print(f"P-value              : {p_value:.8f}")

print("=" * 65)

print()
print("Outputs")
print("-------")

print(RESULTS / "04_hosmer_lemeshow_table.csv")
print(RESULTS / "04_hosmer_lemeshow_summary.txt")
print(FIGURES / "Figure11_Calibration.png")
print(FIGURES / "Figure11_Calibration.pdf")

print()
print("Done.")

