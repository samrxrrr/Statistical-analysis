#!/usr/bin/env python3
"""
==========================================================
02_kruskal_epsilon_squared.py

Kruskal–Wallis Test with Epsilon-Squared Effect Size

Project: Statistical-analysis
Author : Mohd Sameer
==========================================================
"""

from pathlib import Path

import pandas as pd
import numpy as np
from scipy.stats import kruskal

# -----------------------------------------------------
# Directories
# -----------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data" / "AP Research 25-26 - Sheet1.csv"

RESULTS = ROOT / "additional_analyses" / "results"

RESULTS.mkdir(parents=True, exist_ok=True)

# -----------------------------------------------------
# Load data
# -----------------------------------------------------

df = pd.read_csv(DATA)

df.columns = df.columns.str.strip()

dose_col = "Thymoquinone Concentration"
severity_col = "Amount of Ectopic Vulva or Extra Pseudovulva"

dose_map = {
    "0 ?M":0,
    "50 ?M":50,
    "100 ?M":100,
    "0 µM":0,
    "50 µM":50,
    "100 µM":100
}

df[dose_col] = df[dose_col].replace(dose_map)

if df[dose_col].isna().any():
    raise ValueError("Dose conversion failed.")

# -----------------------------------------------------
# Split groups
# -----------------------------------------------------

groups = []

for dose in sorted(df[dose_col].unique()):
    groups.append(
        df.loc[df[dose_col] == dose, severity_col]
    )

# -----------------------------------------------------
# Kruskal–Wallis
# -----------------------------------------------------

H, p = kruskal(*groups)

n = len(df)

k = len(groups)

epsilon_squared = (H - k + 1) / (n - k)

epsilon_squared = max(0, epsilon_squared)

# -----------------------------------------------------
# Effect size interpretation
# -----------------------------------------------------

if epsilon_squared < 0.01:
    interpretation = "Negligible"

elif epsilon_squared < 0.08:
    interpretation = "Small"

elif epsilon_squared < 0.26:
    interpretation = "Moderate"

else:
    interpretation = "Large"

# -----------------------------------------------------
# Save CSV
# -----------------------------------------------------

results = pd.DataFrame({
    "Statistic":[H],
    "P_value":[p],
    "Epsilon_squared":[epsilon_squared],
    "Interpretation":[interpretation]
})

results.to_csv(
    RESULTS/"02_kruskal_epsilon_squared.csv",
    index=False
)

# -----------------------------------------------------
# Summary
# -----------------------------------------------------

with open(
    RESULTS/"02_kruskal_epsilon_squared.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write("KRUSKAL–WALLIS EFFECT SIZE\n")
    f.write("="*50+"\n\n")

    f.write(f"Sample size            : {n}\n")
    f.write(f"Groups                 : {k}\n\n")

    f.write(f"H statistic            : {H:.6f}\n")
    f.write(f"P-value                : {p:.8g}\n")
    f.write(f"Epsilon-squared        : {epsilon_squared:.6f}\n")
    f.write(f"Interpretation         : {interpretation}\n")

# -----------------------------------------------------
# Console
# -----------------------------------------------------

print("\n")
print("="*60)
print("KRUSKAL–WALLIS EFFECT SIZE")
print("="*60)
print(f"H statistic      : {H:.6f}")
print(f"P-value          : {p:.8g}")
print(f"Epsilon²         : {epsilon_squared:.6f}")
print(f"Interpretation   : {interpretation}")
print("="*60)

print("\nOutputs")
print("-------")
print(RESULTS/"02_kruskal_epsilon_squared.csv")
print(RESULTS/"02_kruskal_epsilon_squared.txt")

print("\nDone.")

