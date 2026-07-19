#!/usr/bin/env python3
"""
===========================================================
Automatic GitHub README Generator
===========================================================

Project:
    Thymoquinone Statistical Analysis Pipeline

Purpose
-------
Automatically generate a professional GitHub README.md
directly from the repository.

The generated README includes:

• Project overview
• Scientific background
• Objectives
• Repository structure
• Installation
• Usage
• Statistical workflow
• Output description
• Repository statistics
• Reproducibility
• Citation
• License
• Contact information

Author:
    Mohd Sameer

Institution:
    College of Biotechnology
    Sardar Vallabhbhai Patel University of Agriculture &
    Technology
    Meerut, India

===========================================================
"""

from pathlib import Path
import datetime
import os

# ----------------------------------------------------------
# Project Paths
# ----------------------------------------------------------

PROJECT_ROOT = Path(__file__).resolve().parent.parent

README_FILE = PROJECT_ROOT / "README.md"

# ----------------------------------------------------------
# Repository Statistics
# ----------------------------------------------------------

python_scripts = sorted(PROJECT_ROOT.glob("scripts/*.py"))
r_scripts = sorted(PROJECT_ROOT.glob("scripts/*.R"))

figures = sorted(PROJECT_ROOT.glob("figures/*.png"))

csv_tables = sorted(PROJECT_ROOT.glob("tables/*.csv"))
xlsx_tables = sorted(PROJECT_ROOT.glob("tables/*.xlsx"))
markdown_tables = sorted(PROJECT_ROOT.glob("tables/*.md"))

reports = sorted(PROJECT_ROOT.glob("reports/*"))

csv_results = sorted(PROJECT_ROOT.glob("results/*.csv"))

docs = []

for ext in ["*.md", "*.txt"]:
    docs.extend(PROJECT_ROOT.glob(ext))

# ----------------------------------------------------------
# Dynamic Counts
# ----------------------------------------------------------

stats = {
    "python": len(python_scripts),
    "r": len(r_scripts),
    "figures": len(figures),
    "csv_tables": len(csv_tables),
    "xlsx_tables": len(xlsx_tables),
    "markdown_tables": len(markdown_tables),
    "reports": len(reports),
    "results": len(csv_results),
    "documents": len(docs),
}

today = datetime.date.today().strftime("%d %B %Y")

# ----------------------------------------------------------
# README Builder
# ----------------------------------------------------------

lines = []

append = lines.append

append("# Thymoquinone Statistical Analysis Pipeline")
append("")
append("![Python](https://img.shields.io/badge/Python-3.12-blue)")
append("![Platform](https://img.shields.io/badge/Linux-Ubuntu-orange)")
append("![Status](https://img.shields.io/badge/Status-Complete-brightgreen)")
append("![Reproducibility](https://img.shields.io/badge/Reproducible-Yes-success)")
append("")
append("---")
append("")
append("> **Automatically generated README**")
append("")
append(f"Last updated: **{today}**")
append("")
append("---")
append("")
append("# Overview")
append("")
append(
    "This repository contains a fully reproducible statistical "
    "analysis pipeline developed to evaluate the effect of "
    "thymoquinone on the Ras/MAPK-induced Multivulva (MUV) "
    "phenotype in *Caenorhabditis elegans*."
)
append("")
append(
    "The workflow performs automated data cleaning, descriptive "
    "statistics, inferential analyses, regression modelling, "
    "bootstrap validation, risk estimation, publication-quality "
    "figure generation, quality control, reproducibility auditing "
    "and manuscript-ready report generation."
)
append("")
append("---")
append("")
append("# Repository Statistics")
append("")
append("| Item | Count |")
append("|------|------:|")
append(f"| Python scripts | {stats['python']} |")
append(f"| R scripts | {stats['r']} |")
append(f"| Figures | {stats['figures']} |")
append(f"| CSV tables | {stats['csv_tables']} |")
append(f"| Excel tables | {stats['xlsx_tables']} |")
append(f"| Markdown tables | {stats['markdown_tables']} |")
append(f"| Reports | {stats['reports']} |")
append(f"| Result files | {stats['results']} |")
append(f"| Documentation files | {stats['documents']} |")
append("")

# ----------------------------------------------------------
# Project Features
# ----------------------------------------------------------

append("---")
append("")
append("# Features")
append("")
append("- Automated data cleaning")
append("- Descriptive statistical analysis")
append("- Inferential statistical testing")
append("- Binary logistic regression")
append("- Ordinal logistic regression")
append("- Bootstrap validation")
append("- Pairwise risk analysis")
append("- Publication-quality figures")
append("- Publication-ready tables")
append("- Automated manuscript reports")
append("- Quality control checks")
append("- Reproducibility audit")
append("- Submission package generation")
append("- One-command pipeline execution")
append("")

# ----------------------------------------------------------
# Scientific Background
# ----------------------------------------------------------

append("---")
append("")
append("# Scientific Background")
append("")
append(
    "The Ras/MAPK signalling pathway plays a central role in vulval "
    "development in *Caenorhabditis elegans*. Hyperactivation of this "
    "pathway induces the Multivulva (MUV) phenotype, providing a robust "
    "genetic model for investigating modulators of oncogenic signalling."
)
append("")
append(
    "This project evaluates whether thymoquinone suppresses the MUV "
    "phenotype using a fully reproducible computational workflow."
)
append("")

# ----------------------------------------------------------
# Objectives
# ----------------------------------------------------------

append("---")
append("")
append("# Objectives")
append("")
append("1. Clean and validate raw phenotype data.")
append("2. Perform descriptive statistical analyses.")
append("3. Quantify treatment effects.")
append("4. Estimate odds ratios using logistic regression.")
append("5. Model severity using ordinal regression.")
append("6. Validate estimates using bootstrap analysis.")
append("7. Produce publication-ready tables.")
append("8. Produce publication-quality figures.")
append("9. Perform reproducibility and quality-control audits.")
append("10. Generate a complete manuscript submission package.")
append("")

# ----------------------------------------------------------
# Repository Structure
# ----------------------------------------------------------

append("---")
append("")
append("# Repository Structure")
append("")
append("```text")
append("analysis/")
append("├── data/")
append("├── figures/")
append("├── logs/")
append("├── reports/")
append("├── results/")
append("├── scripts/")
append("├── submission/")
append("├── tables/")
append("├── environment.yml")
append("├── requirements.txt")
append("├── PIPELINE.md")
append("├── PROVENANCE.md")
append("└── README.md")
append("```")
append("")

# ----------------------------------------------------------
# Software Requirements
# ----------------------------------------------------------

append("---")
append("")
append("# Software Requirements")
append("")
append("- Python 3.12+")
append("- pandas")
append("- numpy")
append("- scipy")
append("- statsmodels")
append("- matplotlib")
append("- openpyxl")
append("- xlsxwriter")
append("")
append("Install dependencies using:")
append("")
append("```bash")
append("pip install -r requirements.txt")
append("```")
append("")
append("or")
append("")
append("```bash")
append("conda env create -f environment.yml")
append("conda activate austin_stats")
append("```")
append("")

# ----------------------------------------------------------
# Running the Pipeline
# ----------------------------------------------------------

append("---")
append("")
append("# Running the Complete Pipeline")
append("")
append("```bash")
append("python scripts/24_run_pipeline.py")
append("```")
append("")
append("The pipeline automatically performs:")
append("")
append("- Data cleaning")
append("- Statistical analyses")
append("- Regression modelling")
append("- Bootstrap validation")
append("- Risk analysis")
append("- Figure generation")
append("- Table generation")
append("- Report generation")
append("- Quality control")
append("- Reproducibility audit")
append("- Submission package creation")
append("")

# ----------------------------------------------------------
# Input Data
# ----------------------------------------------------------

append("---")
append("")
append("# Input Data")
append("")
append("The pipeline accepts experimental phenotype data in CSV or Excel format.")
append("")
append("Expected variables include:")
append("")
append("| Variable | Description |")
append("|----------|-------------|")
append("| Concentration | Thymoquinone concentration (µM) |")
append("| Ectopic_Vulva | Number of ectopic vulvae |")
append("| MUV | Severity score |")
append("| MUV_Binary | Binary phenotype (0 = Absent, 1 = Present) |")
append("")

# ----------------------------------------------------------
# Generated Outputs
# ----------------------------------------------------------

append("---")
append("")
append("# Generated Outputs")
append("")
append("## Figures")
append("")

for fig in figures:
    append(f"- `{fig.name}`")

append("")
append("## Tables")
append("")

for tbl in csv_tables:
    append(f"- `{tbl.name}`")

append("")
append("## Reports")
append("")

for rep in reports:
    append(f"- `{rep.name}`")

append("")

# ----------------------------------------------------------
# Statistical Workflow
# ----------------------------------------------------------

append("---")
append("")
append("# Statistical Workflow")
append("")
append("1. Import raw dataset")
append("2. Data cleaning and validation")
append("3. Descriptive statistics")
append("4. Inferential statistical testing")
append("5. Binary logistic regression")
append("6. Ordinal logistic regression")
append("7. Bootstrap validation")
append("8. Pairwise risk analysis")
append("9. Publication figure generation")
append("10. Publication table generation")
append("11. Manuscript report generation")
append("12. Quality control")
append("13. Reproducibility audit")
append("14. Submission package creation")
append("")

# ----------------------------------------------------------
# Reproducibility
# ----------------------------------------------------------

append("---")
append("")
append("# Reproducibility")
append("")
append("The repository includes:")
append("")
append("- requirements.txt")
append("- environment.yml")
append("- PROVENANCE.md")
append("- PIPELINE.md")
append("- SOFTWARE_VERSIONS.txt")
append("- REPRODUCIBILITY_REPORT.txt")
append("")
append("All analyses can be reproduced using a single command.")
append("")

# ----------------------------------------------------------
# Quality Assurance
# ----------------------------------------------------------

append("---")
append("")
append("# Quality Assurance")
append("")
append("Automated checks include:")
append("")
append("- Dataset validation")
append("- Missing value detection")
append("- Duplicate record assessment")
append("- Output verification")
append("- Pipeline execution logging")
append("- Reproducibility auditing")
append("")

# ----------------------------------------------------------
# Repository Highlights
# ----------------------------------------------------------

append("---")
append("")
append("# Repository Highlights")
append("")
append(f"- {stats['python']} Python scripts")
append(f"- {stats['r']} R scripts")
append(f"- {stats['figures']} publication-quality figures")
append(f"- {stats['csv_tables']} CSV tables")
append(f"- {stats['xlsx_tables']} Excel tables")
append(f"- {stats['reports']} reports")
append("")

# ----------------------------------------------------------
# Citation
# ----------------------------------------------------------

append("---")
append("")
append("# Citation")
append("")
append(
    "If you use this repository, please cite the associated "
    "research article once published."
)
append("")
append("Example:")
append("")
append("```text")
append(
    "Sameer M. et al. Thymoquinone Attenuates the Ras/MAPK-Induced "
    "Multivulva Phenotype in Caenorhabditis elegans."
)
append("```")
append("")

# ----------------------------------------------------------
# License
# ----------------------------------------------------------

append("---")
append("")
append("# License")
append("")
append(
    "This repository is intended for academic research and educational "
    "purposes. Add an appropriate open-source license (e.g., MIT, BSD-3, "
    "or GPL-3.0) before public release."
)
append("")

# ----------------------------------------------------------
# Contact
# ----------------------------------------------------------

append("---")
append("")
append("# Contact")
append("")
append("**Author:** Mohd Sameer")
append("")
append(
    "College of Biotechnology  \n"
    "Sardar Vallabhbhai Patel University of Agriculture & Technology  \n"
    "Meerut, Uttar Pradesh, India"
)
append("")

append("GitHub: *(add repository URL after publication)*")
append("")
append("Email: *(add your preferred contact email)*")
append("")

# ----------------------------------------------------------
# Acknowledgements
# ----------------------------------------------------------

append("---")
append("")
append("# Acknowledgements")
append("")
append(
    "The statistical workflow implemented in this repository was "
    "developed to provide a transparent, reproducible, and publication-"
    "ready analysis pipeline for experimental studies in "
    "Caenorhabditis elegans."
)
append("")

# ----------------------------------------------------------
# Write README
# ----------------------------------------------------------

README_FILE.write_text("\n".join(lines), encoding="utf-8")

print("=" * 60)
print("GitHub README generated successfully.")
print("=" * 60)
print(f"Output file : {README_FILE}")
print(f"Python scripts : {stats['python']}")
print(f"R scripts      : {stats['r']}")
print(f"Figures        : {stats['figures']}")
print(f"CSV tables     : {stats['csv_tables']}")
print(f"Reports        : {stats['reports']}")
print("=" * 60)
