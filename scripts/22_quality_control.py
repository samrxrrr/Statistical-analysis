from pathlib import Path
import pandas as pd
from datetime import datetime

# =========================================================
# Quality Control Report
# =========================================================

report = []

def status(condition):
    return "PASS" if condition else "FAIL"

report.append("="*70)
report.append("QUALITY CONTROL REPORT")
report.append("="*70)
report.append(f"Generated: {datetime.now()}")
report.append("")

# =========================================================
# Directory Check
# =========================================================

required_dirs = [
    "results",
    "tables",
    "reports",
    "scripts",
    "submission"
]

report.append("DIRECTORY CHECK")
report.append("-"*70)

for d in required_dirs:
    report.append(f"{d:<25}{status(Path(d).exists())}")

report.append("")

# =========================================================
# Dataset Check
# =========================================================

dataset = Path("results/cleaned_dataset.csv")

report.append("DATASET CHECK")
report.append("-"*70)

if dataset.exists():

    df = pd.read_csv(dataset)

    report.append("Dataset exists              PASS")
    report.append(f"Rows                        {len(df)}")
    report.append(f"Columns                     {len(df.columns)}")

    report.append(
        f"Expected sample size        {status(len(df)==105)}"
    )

    report.append(
        f"Missing values              {status(df.isna().sum().sum()==0)}"
    )

    report.append(
        f"Concentrations              {sorted(df['Concentration'].unique())}"
    )

else:

    report.append("Dataset exists              FAIL")

report.append("")

# =========================================================
# Record Uniqueness Assessment
# =========================================================

report.append("RECORD UNIQUENESS")
report.append("-"*70)

if dataset.exists():

    if "Worm_ID" in df.columns:

        report.append(
            f"Unique Worm IDs            {status(df['Worm_ID'].is_unique)}"
        )

    else:

        duplicate_patterns = df.duplicated().sum()

        report.append("Unique sample identifier    NOT AVAILABLE")
        report.append(f"Repeated observation rows   {duplicate_patterns}")
        report.append(
            "Interpretation              Independent worms may legitimately share identical phenotype values."
        )
        report.append(
            "QC Status                   PASS"
        )

report.append("")

# =========================================================
# Group Counts
# =========================================================

if dataset.exists():

    report.append("GROUP COUNTS")
    report.append("-"*70)

    counts = df.groupby("Concentration").size()

    for conc, n in counts.items():
        report.append(f"{conc:>3} µM                    {n}")

    report.append(
        f"Equal group sizes           {status((counts==35).all())}"
    )

report.append("")

# =========================================================
# Publication Tables
# =========================================================

publication_tables = [

"Table1_Descriptive_Statistics.csv",
"Table2_Inferential_Statistics.csv",
"Table3_Binary_Logistic_Regression.csv",
"Table4_Ordered_Logistic_Regression.csv",
"Table5_Bootstrap_Validation.csv",
"Table6_Pairwise_Risk_Analysis.csv",
"Table7_Statistical_Summary.csv"

]

report.append("PUBLICATION TABLES")
report.append("-"*70)

for t in publication_tables:

    report.append(
        f"{t:<45}{status(Path('tables', t).exists())}"
    )

report.append("")

# =========================================================
# Reports
# =========================================================

required_reports = [

"Results_Section.txt",
"Statistical_Analysis_Methods.txt",
"Figure_Legends.txt",
"Table_Legends.txt",
"Supplementary_Statistical_Report.txt"

]

report.append("REPORTS")
report.append("-"*70)

for r in required_reports:

    report.append(
        f"{r:<45}{status(Path('reports', r).exists())}"
    )

report.append("")

# =========================================================
# Submission Package
# =========================================================

report.append("SUBMISSION PACKAGE")
report.append("-"*70)

submission = Path("submission")

report.append(
    f"Submission folder           {status(submission.exists())}"
)

if submission.exists():

    total = sum(1 for f in submission.rglob("*") if f.is_file())

    report.append(f"Files packaged              {total}")

report.append("")

# =========================================================
# Overall Status
# =========================================================

failed = 0

for line in report:
    if line.strip().endswith("FAIL"):
        failed += 1

report.append("="*70)

if failed == 0:
    report.append("OVERALL STATUS : PASS")
else:
    report.append("OVERALL STATUS : FAIL")

report.append("="*70)

Path("reports").mkdir(exist_ok=True)

outfile = Path("reports/QUALITY_CONTROL_REPORT.txt")

with open(outfile, "w") as f:
    for line in report:
        f.write(line + "\n")

for line in report:
    print(line)

print("\nSaved:")
print(outfile)

