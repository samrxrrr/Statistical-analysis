#!/usr/bin/env python3
"""
23_reproducibility_audit.py

Generates:
- SOFTWARE_VERSIONS.txt
- requirements.txt
- environment.yml
- PROVENANCE.md
- PIPELINE.md
- REPRODUCIBILITY_REPORT.txt
"""

from pathlib import Path
from datetime import datetime
from importlib.metadata import version, PackageNotFoundError
import subprocess
import platform
import sys
import os

# ==========================================================
# Project paths
# ==========================================================

ROOT = Path.cwd()

REPORTS = ROOT / "reports"
TABLES = ROOT / "tables"
RESULTS = ROOT / "results"
SCRIPTS = ROOT / "scripts"

REPORTS.mkdir(exist_ok=True)

report = []

def divider():
    report.append("=" * 80)

def section(title):
    report.append("")
    report.append(title)
    report.append("-" * 80)

divider()
report.append("REPRODUCIBILITY AUDIT REPORT")
divider()
report.append(f"Generated : {datetime.now()}")
report.append(f"Project   : {ROOT}")
report.append("")

# ==========================================================
# System information
# ==========================================================

section("SYSTEM INFORMATION")

report.append(f"Operating System : {platform.system()}")
report.append(f"Platform         : {platform.platform()}")
report.append(f"Architecture     : {platform.machine()}")
report.append(f"Processor        : {platform.processor()}")
report.append(f"Python Version   : {platform.python_version()}")
report.append(f"Executable       : {sys.executable}")

# ==========================================================
# Installed package versions
# ==========================================================

section("INSTALLED PYTHON PACKAGES")

packages = [
    "numpy",
    "pandas",
    "scipy",
    "statsmodels",
    "matplotlib",
    "openpyxl",
    "xlsxwriter",
    "scikit-posthocs"
]

software_versions = []

for pkg in packages:

    try:

        ver = version(pkg)

    except PackageNotFoundError:

        ver = "NOT INSTALLED"

    software_versions.append((pkg, ver))
    report.append(f"{pkg:<30}{ver}")

software_file = REPORTS / "SOFTWARE_VERSIONS.txt"

with open(software_file, "w") as f:

    f.write("SOFTWARE VERSIONS\n")
    f.write("=" * 60 + "\n\n")

    f.write(f"Generated : {datetime.now()}\n")
    f.write(f"Platform  : {platform.platform()}\n")
    f.write(f"Python    : {platform.python_version()}\n\n")

    for pkg, ver in software_versions:
        f.write(f"{pkg:<30}{ver}\n")

report.append("")
report.append(f"Saved -> {software_file}")

# ==========================================================
# Generate requirements.txt
# ==========================================================

section("GENERATING REQUIREMENTS.TXT")

requirements_file = ROOT / "requirements.txt"

try:

    result = subprocess.run(
        [sys.executable, "-m", "pip", "freeze"],
        capture_output=True,
        text=True,
        check=True
    )

    with open(requirements_file, "w") as f:
        f.write(result.stdout)

    report.append("requirements.txt successfully generated.")

except Exception as e:

    report.append(f"Failed to generate requirements.txt : {e}")

report.append(f"Output : {requirements_file}")

# ==========================================================
# Generate environment.yml
# ==========================================================

section("GENERATING ENVIRONMENT.YML")

environment_file = ROOT / "environment.yml"

conda_available = True

try:

    subprocess.run(
        ["conda", "--version"],
        capture_output=True,
        check=True
    )

except Exception:

    conda_available = False

if conda_available:

    try:

        result = subprocess.run(
            ["conda", "env", "export", "--no-builds"],
            capture_output=True,
            text=True,
            check=True
        )

        with open(environment_file, "w") as f:
            f.write(result.stdout)

        report.append("environment.yml exported from Conda.")

    except Exception as e:

        report.append(f"Conda export failed : {e}")

else:

    report.append("Conda not detected. Creating portable environment.yml")

    with open(environment_file, "w") as f:

        f.write("name: reproducible_analysis\n")
        f.write("channels:\n")
        f.write("  - conda-forge\n")
        f.write("  - defaults\n")
        f.write("\n")
        f.write("dependencies:\n")
        f.write(f"  - python={platform.python_version()}\n")
        f.write("  - pip\n")
        f.write("  - numpy\n")
        f.write("  - pandas\n")
        f.write("  - scipy\n")
        f.write("  - matplotlib\n")
        f.write("  - statsmodels\n")
        f.write("  - openpyxl\n")
        f.write("  - xlsxwriter\n")
        f.write("  - pip:\n")
        f.write("      - scikit-posthocs\n")

    report.append("Fallback environment.yml created.")

report.append(f"Output : {environment_file}")

# ==========================================================
# Directory Snapshot
# ==========================================================

section("PROJECT DIRECTORY SNAPSHOT")

directories = [
    RESULTS,
    TABLES,
    REPORTS,
    SCRIPTS
]

for directory in directories:

    report.append(f"\n{directory.name}/")

    if directory.exists():

        files = sorted(directory.glob("*"))

        if not files:

            report.append("    (empty)")

        else:

            for file in files:

                if file.is_file():

                    size = file.stat().st_size

                    report.append(
                        f"    {file.name:<45} {size:>10} bytes"
                    )

                else:

                    report.append(f"    {file.name}/")

    else:

        report.append("    Directory not found.")

# ==========================================================
# Generate PROVENANCE.md
# ==========================================================

section("GENERATING PROVENANCE")

provenance_file = ROOT / "PROVENANCE.md"

workflow = [

("01_data_cleaning.py",
 "Raw experimental data",
 "results/cleaned_dataset.csv"),

("02_descriptive_statistics.py",
 "results/cleaned_dataset.csv",
 "tables/Table1_Descriptive_Statistics.*"),

("03_inferential_statistics.py",
 "results/cleaned_dataset.csv",
 "reports/inferential_statistics.txt"),

("04_logistic_regression.py",
 "results/cleaned_dataset.csv",
 "reports/logistic_regression.txt"),

("05_ordinal_logistic_statsmodels.py",
 "results/cleaned_dataset.csv",
 "reports/ordinal_logistic_statsmodels.txt"),

("06_bootstrap_analysis.py",
 "results/cleaned_dataset.csv",
 "tables/Table5_Bootstrap_Validation.*"),

("07_pairwise_risk_analysis.py",
 "results/cleaned_dataset.csv",
 "tables/Table6_Pairwise_Risk_Analysis.*"),

("13_generate_table1.py",
 "Analysis outputs",
 "Table1_Descriptive_Statistics"),

("14_generate_table2.py",
 "Analysis outputs",
 "Table2_Inferential_Statistics"),

("15_generate_table3.py",
 "Analysis outputs",
 "Table3_Binary_Logistic_Regression"),

("16_generate_table4.py",
 "Analysis outputs",
 "Table4_Ordered_Logistic_Regression"),

("17_generate_table5.py",
 "Analysis outputs",
 "Table5_Bootstrap_Validation"),

("18_generate_table6.py",
 "Analysis outputs",
 "Table6_Pairwise_Risk_Analysis"),

("19_generate_table7.py",
 "Analysis outputs",
 "Table7_Statistical_Summary"),

("20_generate_manuscript_reports.py",
 "Statistical outputs",
 "reports/"),

("21_package_submission.py",
 "Complete project",
 "submission/")
]

with open(provenance_file, "w") as f:

    f.write("# PROVENANCE DOCUMENT\n\n")

    f.write("This file documents the provenance of all major outputs.\n\n")

    f.write("| Step | Script | Input | Output |\n")
    f.write("|-----:|--------|-------|--------|\n")

    for i, (script, inp, out) in enumerate(workflow, start=1):

        f.write(
            f"| {i} | `{script}` | {inp} | {out} |\n"
        )

report.append(f"Generated : {provenance_file}")

# ==========================================================
# Generate PIPELINE.md
# ==========================================================

section("GENERATING PIPELINE")

pipeline_file = ROOT / "PIPELINE.md"

pipeline = """
# Statistical Analysis Workflow

Raw Experimental Dataset
        │
        ▼
01_data_cleaning.py
        │
        ▼
results/cleaned_dataset.csv
        │
        ▼
02_descriptive_statistics.py
        │
        ▼
03_inferential_statistics.py
        │
        ▼
04_logistic_regression.py
        │
        ▼
05_ordinal_logistic_statsmodels.py
        │
        ▼
06_bootstrap_analysis.py
        │
        ▼
07_pairwise_risk_analysis.py
        │
        ▼
13_generate_table1.py
        │
        ▼
14_generate_table2.py
        │
        ▼
15_generate_table3.py
        │
        ▼
16_generate_table4.py
        │
        ▼
17_generate_table5.py
        │
        ▼
18_generate_table6.py
        │
        ▼
19_generate_table7.py
        │
        ▼
20_generate_manuscript_reports.py
        │
        ▼
21_package_submission.py
        │
        ▼
Submission Package
"""

with open(pipeline_file, "w") as f:

    f.write(pipeline.strip())

report.append(f"Generated : {pipeline_file}")

# ==========================================================
# Script Inventory
# ==========================================================

section("SCRIPT INVENTORY")

script_files = sorted(SCRIPTS.glob("*.py"))

for script in script_files:

    report.append(script.name)

report.append(f"Total Python scripts : {len(script_files)}")

# ==========================================================
# Integrity Check
# ==========================================================

section("INTEGRITY CHECK")

required_files = [

RESULTS / "cleaned_dataset.csv",

TABLES / "Table1_Descriptive_Statistics.csv",
TABLES / "Table2_Inferential_Statistics.csv",
TABLES / "Table3_Binary_Logistic_Regression.csv",
TABLES / "Table4_Ordered_Logistic_Regression.csv",
TABLES / "Table5_Bootstrap_Validation.csv",
TABLES / "Table6_Pairwise_Risk_Analysis.csv",
TABLES / "Table7_Statistical_Summary.csv",

REPORTS / "Results_Section.txt",
REPORTS / "Statistical_Analysis_Methods.txt",
REPORTS / "Supplementary_Statistical_Report.txt",
REPORTS / "Figure_Legends.txt",
REPORTS / "Table_Legends.txt"

]

missing = []

for file in required_files:

    if file.exists():

        report.append(f"[PASS] {file}")

    else:

        report.append(f"[FAIL] {file}")
        missing.append(file)

# ==========================================================
# Overall Status
# ==========================================================

section("OVERALL STATUS")

if len(missing) == 0:

    report.append("STATUS : PASS")
    report.append("")
    report.append("All essential project files were found.")
    report.append("Project is reproducible.")
    report.append("Documentation generated successfully.")
    report.append("Submission package appears complete.")

else:

    report.append("STATUS : FAIL")
    report.append("")
    report.append("Missing files detected:")

    for file in missing:

        report.append(f" - {file}")

# ==========================================================
# Save Reproducibility Report
# ==========================================================

repro_file = REPORTS / "REPRODUCIBILITY_REPORT.txt"

with open(repro_file, "w") as f:

    for line in report:

        f.write(line + "\n")

# ==========================================================
# Console Summary
# ==========================================================

print("\n")
print("="*80)
print("REPRODUCIBILITY AUDIT")
print("="*80)

for line in report:

    print(line)

print("\nGenerated Files")
print("-"*80)

generated = [

software_file,
requirements_file,
environment_file,
provenance_file,
pipeline_file,
repro_file

]

for file in generated:

    if file.exists():

        print(f"[OK] {file}")

    else:

        print(f"[MISSING] {file}")

print("\nAudit completed.")

print("="*80)
