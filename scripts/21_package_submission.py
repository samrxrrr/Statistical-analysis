from pathlib import Path
import shutil
from datetime import datetime

# -------------------------------------------------
# Directories
# -------------------------------------------------

submission = Path("submission")
submission.mkdir(exist_ok=True)

tables_dir = submission / "Tables"
reports_dir = submission / "Reports"
figures_dir = submission / "Figures"
supp_dir = submission / "Supplementary"

for d in [tables_dir, reports_dir, figures_dir, supp_dir]:
    d.mkdir(exist_ok=True)

# -------------------------------------------------
# Copy Tables
# -------------------------------------------------

for file in Path("tables").iterdir():

    if file.is_file():

        shutil.copy(file, tables_dir / file.name)

# -------------------------------------------------
# Copy Reports
# -------------------------------------------------

for file in Path("reports").iterdir():

    if file.is_file():

        shutil.copy(file, reports_dir / file.name)

# -------------------------------------------------
# Copy Figures (if present)
# -------------------------------------------------

fig_path = Path("figures")

if fig_path.exists():
    for file in fig_path.glob("*"):
        shutil.copy(file, figures_dir / file.name)

# -------------------------------------------------
# Copy Supplementary Material
# -------------------------------------------------

supp_files = [
    "cleaned_dataset.csv"
]

results = Path("results")

for f in supp_files:
    p = results / f
    if p.exists():
        shutil.copy(p, supp_dir / p.name)

# -------------------------------------------------
# README
# -------------------------------------------------

readme = f"""
=========================================================
Submission Package
=========================================================

Generated:
{datetime.now().strftime('%Y-%m-%d %H:%M:%S')}

Contents

Tables/
    Publication-ready statistical tables

Reports/
    Methods
    Results
    Figure legends
    Table legends
    Supplementary report
    Statistical outputs

Figures/
    Publication figures (if available)

Supplementary/
    Cleaned dataset

=========================================================

Statistical analyses included

✓ Descriptive Statistics
✓ Pearson Chi-square
✓ Cramer's V
✓ Kruskal-Wallis
✓ Dunn's Test
✓ Binary Logistic Regression
✓ Ordered Logistic Regression
✓ Bootstrap Validation
✓ Pairwise Risk Analysis

=========================================================
"""

with open(submission / "README.txt", "w") as f:
    f.write(readme)

# -------------------------------------------------
# Manifest
# -------------------------------------------------

manifest = submission / "MANIFEST.txt"

with open(manifest, "w") as f:

    for folder in sorted(submission.iterdir()):

        if folder.is_dir():

            f.write(folder.name + "\n")

            for file in sorted(folder.iterdir()):
                f.write(f"   {file.name}\n")

            f.write("\n")

print("=" * 70)
print("SUBMISSION PACKAGE CREATED")
print("=" * 70)

print("Location:")
print(submission.resolve())

print("\nContents:")

for folder in sorted(submission.iterdir()):

    if folder.is_dir():

        count = len(list(folder.iterdir()))
        print(f"{folder.name:<15} {count:>3} files")

print("\nREADME.txt created")
print("MANIFEST.txt created")
print("\nReady for manuscript preparation.")
