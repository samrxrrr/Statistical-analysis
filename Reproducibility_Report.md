# Reproducibility Report

**Project:** Thymoquinone Statistical Analysis Pipeline

**Version:** 2.0.0-publication-framework

**Date:** 19 July 2026

---

# Purpose

This document describes the computational environment, software dependencies, workflow execution, and reproducibility measures implemented for the statistical analysis of the thymoquinone dose-response study in *Caenorhabditis elegans*.

The objective is to ensure that every reported statistical result can be independently reproduced from the raw dataset using the supplied scripts.

---

# Operating Environment

| Item | Value |
|------|-------|
| Operating System | Ubuntu (WSL) |
| Python | 3.12 |
| Environment | conda |
| Environment Name | austin_stats |

---

# Primary Python Packages

- pandas
- numpy
- scipy
- statsmodels
- matplotlib
- openpyxl
- xlsxwriter

---

# Input Dataset

Input file:

```
data/AP Research 25-26 - Sheet1.csv
```

Primary variables:

- Thymoquinone Concentration
- Amount of Ectopic Vulva or Extra Pseudovulva
- Multivulva presence (Yes or No)

---

# Statistical Analyses

The pipeline performs the following analyses:

- Descriptive statistics
- Pearson Chi-square Test
- Fisher's Exact Test
- Kruskal–Wallis Test
- Binary Logistic Regression
- Ordered Logistic Regression
- Bootstrap Validation
- Cochran–Armitage Trend Test
- ROC Curve Analysis
- Area Under the Curve (AUC)
- Hosmer–Lemeshow Calibration Test
- Relative Risk Analysis
- Odds Ratio Analysis
- Absolute Risk Reduction
- Relative Risk Reduction
- Number Needed to Treat
- Jackknife Sensitivity Analysis

---

# Generated Outputs

Major outputs include:

- Publication_Tables.xlsx
- Supplementary_Tables.xlsx
- Figures
- Statistical reports
- CSV result tables
- Markdown reports
---

# Pipeline Execution Order

The recommended execution order is shown below.

| Step | Analysis |
|------|----------|
| 1 | Data import and validation |
| 2 | Data cleaning |
| 3 | Descriptive statistics |
| 4 | Pearson Chi-square test |
| 5 | Fisher's Exact test |
| 6 | Kruskal–Wallis test |
| 7 | Binary logistic regression |
| 8 | Ordered logistic regression |
| 9 | Bootstrap validation |
| 10 | Cochran–Armitage trend test |
| 11 | ROC/AUC analysis |
| 12 | Hosmer–Lemeshow calibration |
| 13 | Effect size analysis |
| 14 | Jackknife sensitivity analysis |
| 15 | Publication table generation |
| 16 | Figure generation |
| 17 | Report generation |

---

# Repository Structure

```text
analysis/
│
├── data/
├── scripts/
├── figures/
├── results/
├── tables/
├── reports/
├── submission/
│
├── additional_analyses/
│   ├── scripts/
│   ├── results/
│   ├── figures/
│   └── tables/
│
├── README.md
├── Reproducibility_Report.md
├── environment.yml
├── requirements.txt
└── LICENSE
```

---

# Quality Assurance

The framework incorporates multiple quality-control measures to improve the reliability and reproducibility of statistical results.

Implemented checks include:

- Input dataset validation
- Missing-value assessment
- Variable consistency checks
- Statistical assumption verification where applicable
- Confidence interval estimation
- Bootstrap validation
- Jackknife sensitivity analysis
- Automated report generation
- Publication table generation

---

# Version Control

Repository version:

```
v2.0.0-publication-framework
```

The repository should be version-controlled using Git, with all analysis scripts, generated outputs, and documentation tracked to ensure transparency and reproducibility.

---

# Reproducibility Checklist

The following items should be verified before reproducing the analysis:

- Python environment created successfully
- Required packages installed
- Input dataset available in the `data/` directory
- Analysis scripts executed in the recommended order (or via the master pipeline)
- Output directories writable
- Generated tables and figures reviewed for completeness

---

# Expected Deliverables

Successful execution of the workflow should produce:

- Publication-ready Excel tables
- Supplementary statistical tables
- Publication-quality figures
- Statistical summary reports
- Logistic regression outputs
- ROC analysis outputs
- Calibration analysis outputs
- Effect-size analysis outputs
- Sensitivity analysis outputs

---

# Citation

If this workflow contributes to published research, please cite the associated manuscript describing the statistical framework and its application to thymoquinone dose-response analysis in *Caenorhabditis elegans*.

---

# Conclusion

This repository provides a transparent, reproducible, and publication-oriented statistical analysis framework for biomedical dose-response studies. All analyses are designed to be regenerated directly from the original dataset using the supplied scripts, ensuring computational reproducibility and facilitating peer review.
