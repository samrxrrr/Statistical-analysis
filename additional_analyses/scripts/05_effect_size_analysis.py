#!/usr/bin/env python3
"""
===========================================================
05_effect_size_analysis.py

Effect Size Analysis
- Relative Risk (RR)
- Odds Ratio (OR)
- Absolute Risk Reduction (ARR)
- Relative Risk Reduction (RRR)
- Number Needed to Treat (NNT)
- 95% Confidence Intervals
- Fisher's Exact Test
- Pearson Chi-square Test

===========================================================
"""

from pathlib import Path

import numpy as np
import pandas as pd

from scipy.stats import fisher_exact
from scipy.stats import chi2_contingency
from scipy.stats import norm

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data" / "AP Research 25-26 - Sheet1.csv"

RESULTS = ROOT / "additional_analyses" / "results"

RESULTS.mkdir(parents=True, exist_ok=True)

# ----------------------------------------------------------

df = pd.read_csv(DATA)

dose_col = "Thymoquinone Concentration"
outcome_col = "Multivulva presence (Yes or No)"

df[dose_col] = (
    df[dose_col]
    .astype(str)
    .str.replace("μ","u")
    .str.replace("µ","u")
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

control = df[df[dose_col] == 0]

z = norm.ppf(0.975)

rows = []

for treatment in [50,100]:

    treat = df[df[dose_col] == treatment]

    a = int(treat["Event"].sum())
    b = len(treat) - a

    c = int(control["Event"].sum())
    d = len(control) - c

    risk_t = a/(a+b)
    risk_c = c/(c+d)

    RR = risk_t/risk_c

    ARR = risk_c-risk_t

    RRR = ARR/risk_c

    OR = (a*d)/(b*c)

    NNT = np.inf if ARR==0 else 1/ARR

    se_log_rr = np.sqrt(
        (1/a)-(1/(a+b))+
        (1/c)-(1/(c+d))
    )

    rr_low = np.exp(np.log(RR)-z*se_log_rr)
    rr_high = np.exp(np.log(RR)+z*se_log_rr)

    se_log_or = np.sqrt(
        1/a+1/b+1/c+1/d
    )

    or_low = np.exp(np.log(OR)-z*se_log_or)
    or_high = np.exp(np.log(OR)+z*se_log_or)

    table = [[a,b],[c,d]]

    fisher_p = fisher_exact(table)[1]

    chi2,pchi,_,_ = chi2_contingency(table)

    rows.append({

        "Comparison":f"{treatment} uM vs 0 uM",

        "RR":RR,

        "RR_95CI_Lower":rr_low,

        "RR_95CI_Upper":rr_high,

        "OR":OR,

        "OR_95CI_Lower":or_low,

        "OR_95CI_Upper":or_high,

        "ARR":ARR,

        "RRR":RRR,

        "NNT":NNT,

        "Fisher_p":fisher_p,

        "ChiSquare_p":pchi

    })

results = pd.DataFrame(rows)

outfile = RESULTS/"05_effect_size_analysis.csv"

results.to_csv(outfile,index=False)

with open(
RESULTS/"05_effect_size_summary.txt",
"w",
encoding="utf-8"
) as f:

    f.write("EFFECT SIZE ANALYSIS\n")
    f.write("="*80+"\n\n")
    f.write(results.round(6).to_string(index=False))

print()

print("="*70)
print("EFFECT SIZE ANALYSIS")
print("="*70)

print(results.round(6))

print("="*70)

print()

print(outfile)
print(RESULTS/"05_effect_size_summary.txt")

print()
print("Done.")

