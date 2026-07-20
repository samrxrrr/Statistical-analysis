#!/usr/bin/env python3
"""
===============================================================
Publication Tables Generator

Creates publication-ready Excel workbook
containing all statistical analyses.

Output
------
tables/Publication_Tables.xlsx

===============================================================
"""

from pathlib import Path
import re

import numpy as np
import pandas as pd

from openpyxl import Workbook

from openpyxl.styles import (
    Font,
    PatternFill,
    Border,
    Side,
    Alignment
)

from openpyxl.utils import get_column_letter

# ----------------------------------------------------
# Directories
# ----------------------------------------------------

ROOT = Path(__file__).resolve().parents[2]

DATA = ROOT / "data" / "AP Research 25-26 - Sheet1.csv"

RESULTS = ROOT / "results"

ADD = ROOT / "additional_analyses" / "results"

TABLES = ROOT / "tables"

TABLES.mkdir(exist_ok=True)

OUTFILE = TABLES / "Publication_Tables.xlsx"

# ----------------------------------------------------
# Workbook
# ----------------------------------------------------

wb = Workbook()

wb.remove(wb.active)

# ----------------------------------------------------
# Styles
# ----------------------------------------------------

TITLE_FONT = Font(
    bold=True,
    size=16
)

HEADER_FONT = Font(
    bold=True,
    color="FFFFFF"
)

HEADER_FILL = PatternFill(
    fill_type="solid",
    fgColor="1F4E78"
)

BOLD = Font(
    bold=True
)

CENTER = Alignment(
    horizontal="center",
    vertical="center"
)

SIDE = Side(style="thin")

BORDER = Border(
    left=SIDE,
    right=SIDE,
    top=SIDE,
    bottom=SIDE
)

# ----------------------------------------------------
# Helpers
# ----------------------------------------------------

def title(ws, txt):

    ws["A1"] = txt
    ws["A1"].font = TITLE_FONT

def header(ws, cols, row=3):

    for i, col in enumerate(cols, start=1):

        c = ws.cell(row=row, column=i)

        c.value = col

        c.font = HEADER_FONT

        c.fill = HEADER_FILL

        c.alignment = CENTER

        c.border = BORDER

def finish(ws):

    for row in ws.iter_rows():

        for cell in row:

            cell.border = BORDER

            if cell.row > 1:
                cell.alignment = CENTER

    for column in ws.columns:

        length = 0

        letter = get_column_letter(column[0].column)

        for cell in column:

            try:

                length = max(
                    length,
                    len(str(cell.value))
                )

            except:

                pass

        ws.column_dimensions[
            letter
        ].width = min(max(length + 3, 14), 40)

    ws.freeze_panes = "A4"

# ----------------------------------------------------
# Read data
# ----------------------------------------------------

df = pd.read_csv(DATA)

dose_col = "Thymoquinone Concentration"

severity_col = "Amount of Ectopic Vulva or Extra Pseudovulva"

binary_col = "Multivulva presence (Yes or No)"

df[dose_col] = (
    df[dose_col]
    .astype(str)
    .str.replace("μ","u")
    .str.replace("µ","u")
    .str.extract(r"(\d+)")
    .astype(int)
)

df["Positive"] = (
    df[binary_col]
    .astype(str)
    .str.lower()
    .eq("yes")
)
# ============================================================
# TABLE 1
# ============================================================

ws = wb.create_sheet("Table 1")

title(
    ws,
    "Table 1. Descriptive Statistics"
)

header(
    ws,
    [
        "Dose (µM)",
        "Sample Size",
        "Positive",
        "Negative",
        "Prevalence (%)",
        "Mean Severity",
        "SD Severity"
    ]
)

row = 4

for dose in sorted(df[dose_col].unique()):

    sub = df[df[dose_col] == dose]

    n = len(sub)

    pos = int(sub["Positive"].sum())

    neg = n - pos

    prevalence = pos / n * 100

    mean = sub[severity_col].mean()

    sd = sub[severity_col].std()

    values = [

        dose,

        n,

        pos,

        neg,

        round(prevalence,2),

        round(mean,3),

        round(sd,3)

    ]

    for col, value in enumerate(values, start=1):

        ws.cell(
            row=row,
            column=col
        ).value = value

    row += 1

finish(ws)

# ============================================================
# TABLE 2
# ============================================================

ws = wb.create_sheet("Table 2")

title(
    ws,
    "Table 2. Primary Statistical Tests"
)

header(
    ws,
    [
        "Analysis",
        "Statistic",
        "P-value",
        "Effect Size",
        "Interpretation"
    ]
)

tests = []

# ------------------------------------------------------------
# Kruskal-Wallis
# ------------------------------------------------------------

kw = pd.read_csv(
    ADD / "02_kruskal_epsilon_squared.csv"
)

tests.append([

    "Kruskal-Wallis",

    kw.loc[0,"Statistic"],

    kw.loc[0,"P_value"],

    kw.loc[0,"Epsilon_squared"],

    kw.loc[0,"Interpretation"]

])

# ------------------------------------------------------------
# Cochran-Armitage
# ------------------------------------------------------------

summary = (
    ADD /
    "01_cochran_armitage_summary.txt"
).read_text()

chi = re.search(
    r"Chi-square trend\s+([0-9.eE+-]+)",
    summary
)

p = re.search(
    r"Two-sided p\s+([0-9.eE+-]+)",
    summary
)

if chi and p:

    tests.append([

        "Cochran-Armitage Trend",

        float(chi.group(1)),

        float(p.group(1)),

        "",

        "Significant decreasing trend"

    ])

# ------------------------------------------------------------
# Write table
# ------------------------------------------------------------

row = 4

for result in tests:

    for col, value in enumerate(result, start=1):

        ws.cell(
            row=row,
            column=col
        ).value = value

    row += 1

finish(ws)

# ============================================================
# TABLE 3
# ============================================================

ws = wb.create_sheet("Table 3")

title(
    ws,
    "Table 3. Logistic Regression Summary"
)

header(
    ws,
    [
        "Metric",
        "Value"
    ]
)

jack = pd.read_csv(
    ADD / "06_jackknife_summary.csv"
)

row = 4

for _, r in jack.iterrows():

    ws.cell(row=row, column=1).value = r["Statistic"]
    ws.cell(row=row, column=2).value = float(r["Value"])

    row += 1

finish(ws)

# ============================================================
# TABLE 4
# ============================================================

ws = wb.create_sheet("Table 4")

title(
    ws,
    "Table 4. Model Performance"
)

header(
    ws,
    [
        "Metric",
        "Value"
    ]
)

roc_text = (
    ADD /
    "03_roc_auc_summary.txt"
).read_text()

hl_text = (
    ADD /
    "04_hosmer_lemeshow_summary.txt"
).read_text()

patterns = [

    ("AUC", r"AUC\s*:\s*([0-9.eE+-]+)"),
    ("Optimal Threshold", r"Optimal threshold\s*:\s*([0-9.eE+-]+)"),
    ("Sensitivity", r"Sensitivity\s*:\s*([0-9.eE+-]+)"),
    ("Specificity", r"Specificity\s*:\s*([0-9.eE+-]+)"),
    ("Accuracy", r"Accuracy\s*:\s*([0-9.eE+-]+)"),
    ("Hosmer-Lemeshow χ²", r"HL statistic\s*:\s*([0-9.eE+-]+)"),
    ("Hosmer-Lemeshow P", r"P-value\s*:\s*([0-9.eE+-]+)")
]

row = 4

for label, pattern in patterns:

    source = roc_text if "Hosmer" not in label else hl_text

    match = re.search(pattern, source)

    if match:

        ws.cell(row=row, column=1).value = label
        ws.cell(row=row, column=2).value = float(match.group(1))

        row += 1

finish(ws)

# ============================================================
# TABLE 5
# ============================================================

ws = wb.create_sheet("Table 5")

title(
    ws,
    "Table 5. Treatment Effect Size Analysis"
)

header(
    ws,
    [
        "Comparison",
        "Relative Risk",
        "RR 95% CI",
        "Odds Ratio",
        "OR 95% CI",
        "ARR",
        "RRR",
        "NNT",
        "Fisher P",
        "Chi-square P"
    ]
)

effect = pd.read_csv(
    ADD / "05_effect_size_analysis.csv"
)

row = 4

for _, r in effect.iterrows():

    rr_ci = (
        f"{r['RR_95CI_Lower']:.3f} – "
        f"{r['RR_95CI_Upper']:.3f}"
    )

    or_ci = (
        f"{r['OR_95CI_Lower']:.3f} – "
        f"{r['OR_95CI_Upper']:.3f}"
    )

    values = [

        r["Comparison"],

        round(r["RR"],3),

        rr_ci,

        round(r["OR"],3),

        or_ci,

        round(r["ARR"],3),

        round(r["RRR"],3),

        round(r["NNT"],2),

        r["Fisher_p"],

        r["ChiSquare_p"]

    ]

    for c, value in enumerate(values, start=1):

        ws.cell(
            row=row,
            column=c
        ).value = value

    row += 1

finish(ws)

# ============================================================
# TABLE 6
# ============================================================

ws = wb.create_sheet("Table 6")

title(
    ws,
    "Table 6. Jackknife Robustness Analysis"
)

header(
    ws,
    [
        "Statistic",
        "Value"
    ]
)

summary = pd.read_csv(
    ADD / "06_jackknife_summary.csv"
)

row = 4

for _, r in summary.iterrows():

    ws.cell(
        row=row,
        column=1
    ).value = r["Statistic"]

    ws.cell(
        row=row,
        column=2
    ).value = float(r["Value"])

    row += 1

finish(ws)

# ============================================================
# SUMMARY
# ============================================================

ws = wb.create_sheet("Summary")

title(
    ws,
    "Statistical Analysis Summary"
)

ws["A3"] = "Dataset"

ws["B3"] = "105 C. elegans observations"

ws["A4"] = "Treatment Groups"

ws["B4"] = "0, 50, 100 µM"

ws["A5"] = "Primary Endpoint"

ws["B5"] = "Multivulva phenotype"

ws["A6"] = "Regression"

ws["B6"] = "Binary Logistic Regression"

ws["A7"] = "Additional Analyses"

ws["B7"] = (
    "Trend, Effect Size, ROC, "
    "Calibration, Jackknife"
)

ws["A9"] = "Workbook Generated"

from datetime import datetime

ws["B9"] = datetime.now().strftime(
    "%Y-%m-%d %H:%M:%S"
)

finish(ws)

# ============================================================
# SAVE
# ============================================================

wb.save(OUTFILE)

print()

print("=" * 70)
print("PUBLICATION TABLES GENERATED")
print("=" * 70)

print()
print(f"Workbook : {OUTFILE}")
print()

print("Sheets")
print("------")

for sheet in wb.sheetnames:
    print(f"• {sheet}")

print()
print("Done.")
