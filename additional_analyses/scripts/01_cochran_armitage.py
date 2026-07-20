#!/usr/bin/env python3

"""
==========================================================
01_cochran_armitage.py

Cochran–Armitage Trend Test
Publication-grade implementation

Author: Mohd Sameer
Project: Statistical-analysis
==========================================================
"""

from pathlib import Path

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import norm

# ----------------------------------------------------
# Directories
# ----------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data" / "AP Research 25-26 - Sheet1.csv"

RESULTS = ROOT / "additional_analyses" / "results"
FIGURES = ROOT / "additional_analyses" / "figures"

RESULTS.mkdir(parents=True, exist_ok=True)
FIGURES.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------
# Read dataset
# ----------------------------------------------------

df = pd.read_csv(DATA)

df.columns = df.columns.str.strip()

DOSE = "Thymoquinone Concentration"
OUTCOME = "Multivulva presence (Yes or No)"

dose_map = {
    "0 ?M":0,
    "50 ?M":50,
    "100 ?M":100,
    "0 µM":0,
    "50 µM":50,
    "100 µM":100
}

df[DOSE] = df[DOSE].replace(dose_map)

df[OUTCOME] = (
    df[OUTCOME]
    .astype(str)
    .str.strip()
    .str.lower()
    .map({"yes":1,"no":0})
)

if df[DOSE].isna().any():
    raise ValueError("Dose mapping failed.")

if df[OUTCOME].isna().any():
    raise ValueError("Outcome mapping failed.")

# ----------------------------------------------------
# Build contingency table
# ----------------------------------------------------

summary = (
    df
    .groupby(DOSE)[OUTCOME]
    .agg(
        Positive="sum",
        Total="count"
    )
    .sort_index()
)

summary["Negative"] = summary["Total"] - summary["Positive"]
summary["Prevalence"] = summary["Positive"] / summary["Total"]

scores = summary.index.to_numpy(dtype=float)
x = summary["Positive"].to_numpy(dtype=float)
n = summary["Total"].to_numpy(dtype=float)

N = n.sum()
A = x.sum()

p_bar = A / N

score_bar = np.sum(scores * n) / N

numerator = np.sum(
    x * (scores - score_bar)
)

variance = (
    p_bar
    * (1 - p_bar)
    * np.sum(
        n * (scores - score_bar)**2
    )
)

z = numerator / np.sqrt(variance)

p_two = 2 * norm.sf(abs(z))

chi_trend = z**2

# ----------------------------------------------------
# Console
# ----------------------------------------------------

print("\n")
print("="*70)
print("COCHRAN–ARMITAGE TREND TEST")
print("="*70)
print(summary)
print()
print(f"Z statistic              : {z:.6f}")
print(f"Chi-square for trend     : {chi_trend:.6f}")
print(f"Two-sided p-value        : {p_two:.8f}")
print("="*70)

# ----------------------------------------------------
# Save table
# ----------------------------------------------------

table = summary.reset_index()

table.rename(
    columns={
        DOSE:"Dose_uM"
    },
    inplace=True
)

table.to_csv(
    RESULTS/"01_cochran_armitage_results.csv",
    index=False
)

# ----------------------------------------------------
# Summary
# ----------------------------------------------------

with open(
    RESULTS/"01_cochran_armitage_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("COCHRAN–ARMITAGE TREND TEST\n")
    f.write("="*50+"\n\n")

    f.write(table.to_string(index=False))

    f.write("\n\n")

    f.write(f"Total observations : {int(N)}\n")
    f.write(f"Total MUV          : {int(A)}\n\n")

    f.write(f"Z statistic        : {z:.6f}\n")
    f.write(f"Chi-square trend   : {chi_trend:.6f}\n")
    f.write(f"Two-sided p-value  : {p_two:.8f}\n\n")

    if p_two < 0.05:
        f.write(
            "Interpretation:\n"
            "There is a statistically significant monotonic "
            "dose-response trend in multivulva prevalence.\n"
        )
    else:
        f.write(
            "Interpretation:\n"
            "No statistically significant monotonic trend detected.\n"
        )

# ----------------------------------------------------
# Figure
# ----------------------------------------------------

plt.figure(figsize=(6,5))

plt.plot(
    table["Dose_uM"],
    table["Prevalence"]*100,
    marker="o",
    linewidth=2
)

for x0,y0 in zip(
    table["Dose_uM"],
    table["Prevalence"]*100
):
    plt.text(
        x0,
        y0+2,
        f"{y0:.1f}%",
        ha="center",
        fontsize=10
    )

plt.xlabel("Thymoquinone concentration (µM)")
plt.ylabel("MUV prevalence (%)")
plt.title("Cochran–Armitage Dose–Response Trend")
plt.grid(alpha=0.3)

plt.tight_layout()

plt.savefig(
    FIGURES/"Figure9_Cochran_Armitage_Trend.png",
    dpi=600
)

plt.savefig(
    FIGURES/"Figure9_Cochran_Armitage_Trend.pdf"
)

plt.close()

print("\nOutputs")
print("-------")
print(RESULTS/"01_cochran_armitage_results.csv")
print(RESULTS/"01_cochran_armitage_summary.txt")
print(FIGURES/"Figure9_Cochran_Armitage_Trend.png")
print(FIGURES/"Figure9_Cochran_Armitage_Trend.pdf")
print("\nDone.")
