# Thymoquinone Statistical Analysis Pipeline

![Python](https://img.shields.io/badge/Python-3.12-blue)
![Platform](https://img.shields.io/badge/Linux-Ubuntu-orange)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)
![Reproducibility](https://img.shields.io/badge/Reproducible-Yes-success)

---

> **Automatically generated README**

Last updated: **19 July 2026**

---

# Overview

This repository contains a fully reproducible statistical analysis pipeline developed to evaluate the effect of thymoquinone on the Ras/MAPK-induced Multivulva (MUV) phenotype in *Caenorhabditis elegans*.

The workflow performs automated data cleaning, descriptive statistics, inferential analyses, regression modelling, bootstrap validation, risk estimation, publication-quality figure generation, quality control, reproducibility auditing and manuscript-ready report generation.

---

# Repository Statistics

| Item | Count |
|------|------:|
| Python scripts | 33 |
| R scripts | 6 |
| Figures | 8 |
| CSV tables | 12 |
| Excel tables | 8 |
| Markdown tables | 7 |
| Reports | 13 |
| Result files | 5 |
| Documentation files | 3 |

---

# Features

- Automated data cleaning
- Descriptive statistical analysis
- Inferential statistical testing
- Binary logistic regression
- Ordinal logistic regression
- Bootstrap validation
- Pairwise risk analysis
- Publication-quality figures
- Publication-ready tables
- Automated manuscript reports
- Quality control checks
- Reproducibility audit
- Submission package generation
- One-command pipeline execution

---

# Scientific Background

The Ras/MAPK signalling pathway plays a central role in vulval development in *Caenorhabditis elegans*. Hyperactivation of this pathway induces the Multivulva (MUV) phenotype, providing a robust genetic model for investigating modulators of oncogenic signalling.

This project evaluates whether thymoquinone suppresses the MUV phenotype using a fully reproducible computational workflow.

---

# Objectives

1. Clean and validate raw phenotype data.
2. Perform descriptive statistical analyses.
3. Quantify treatment effects.
4. Estimate odds ratios using logistic regression.
5. Model severity using ordinal regression.
6. Validate estimates using bootstrap analysis.
7. Produce publication-ready tables.
8. Produce publication-quality figures.
9. Perform reproducibility and quality-control audits.
10. Generate a complete manuscript submission package.

---

# Repository Structure

```text
analysis/
├── data/
├── figures/
├── logs/
├── reports/
├── results/
├── scripts/
├── submission/
├── tables/
├── environment.yml
├── requirements.txt
├── PIPELINE.md
├── PROVENANCE.md
└── README.md
```

---

# Software Requirements

- Python 3.12+
- pandas
- numpy
- scipy
- statsmodels
- matplotlib
- openpyxl
- xlsxwriter

Install dependencies using:

```bash
pip install -r requirements.txt
```

or

```bash
conda env create -f environment.yml
conda activate austin_stats
```

---

# Running the Complete Pipeline

```bash
python scripts/24_run_pipeline.py
```

The pipeline automatically performs:

- Data cleaning
- Statistical analyses
- Regression modelling
- Bootstrap validation
- Risk analysis
- Figure generation
- Table generation
- Report generation
- Quality control
- Reproducibility audit
- Submission package creation

---

# Input Data

The pipeline accepts experimental phenotype data in CSV or Excel format.

Expected variables include:

| Variable | Description |
|----------|-------------|
| Concentration | Thymoquinone concentration (µM) |
| Ectopic_Vulva | Number of ectopic vulvae |
| MUV | Severity score |
| MUV_Binary | Binary phenotype (0 = Absent, 1 = Present) |

---

# Generated Outputs

## Figures

- `Figure1_MUV_Percentage.png`
- `Figure2_Boxplot.png`
- `Figure3_MeanSeverity.png`
- `Figure4_DoseResponse.png`
- `Figure5_Logistic_Dose_Response.png`
- `Figure6_ForestPlot_OR.png`
- `Figure7_Heatmap.png`
- `Figure8_Mosaic.png`

## Tables

- `Table1_Descriptive_Statistics.csv`
- `Table1_GroupCounts.csv`
- `Table2_Inferential_Statistics.csv`
- `Table2_MUV_Frequency.csv`
- `Table3_Binary_Logistic_Regression.csv`
- `Table3_MUV_Percentage.csv`
- `Table4_Ordered_Logistic_Regression.csv`
- `Table4_SeverityStatistics.csv`
- `Table5_Bootstrap_Validation.csv`
- `Table5_Statistical_Summary.csv`
- `Table6_Pairwise_Risk_Analysis.csv`
- `Table7_Statistical_Summary.csv`

## Reports

- `Figure_Legends.txt`
- `PIPELINE_EXECUTION_LOG.txt`
- `QUALITY_CONTROL_REPORT.txt`
- `REPRODUCIBILITY_REPORT.txt`
- `Results_Section.txt`
- `SOFTWARE_VERSIONS.txt`
- `Statistical_Analysis_Methods.txt`
- `Statistical_Report.md`
- `Supplementary_Statistical_Report.txt`
- `Table_Legends.txt`
- `inferential_statistics.txt`
- `logistic_regression.txt`
- `ordinal_logistic_statsmodels.txt`

---

# Statistical Workflow

1. Import raw dataset
2. Data cleaning and validation
3. Descriptive statistics
4. Inferential statistical testing
5. Binary logistic regression
6. Ordinal logistic regression
7. Bootstrap validation
8. Pairwise risk analysis
9. Publication figure generation
10. Publication table generation
11. Manuscript report generation
12. Quality control
13. Reproducibility audit
14. Submission package creation

---

# Reproducibility

The repository includes:

- requirements.txt
- environment.yml
- PROVENANCE.md
- PIPELINE.md
- SOFTWARE_VERSIONS.txt
- REPRODUCIBILITY_REPORT.txt

All analyses can be reproduced using a single command.

---

# Quality Assurance

Automated checks include:

- Dataset validation
- Missing value detection
- Duplicate record assessment
- Output verification
- Pipeline execution logging
- Reproducibility auditing

---

# Repository Highlights

- 33 Python scripts
- 6 R scripts
- 8 publication-quality figures
- 12 CSV tables
- 8 Excel tables
- 13 reports

---

# Citation

If you use this repository, please cite the associated research article once published.

Example:

```text
Sameer M. et al. Thymoquinone Attenuates the Ras/MAPK-Induced Multivulva Phenotype in Caenorhabditis elegans.
```

---

# License

This repository is intended for academic research and educational purposes. Add an appropriate open-source license (e.g., MIT, BSD-3, or GPL-3.0) before public release.

---

# Contact

**Author:** Mohd Sameer

College of Biotechnology  
Sardar Vallabhbhai Patel University of Agriculture & Technology  
Meerut, Uttar Pradesh, India

GitHub: *(add repository URL after publication)*

Email: *(add your preferred contact email)*

---

# Acknowledgements

The statistical workflow implemented in this repository was developed to provide a transparent, reproducible, and publication-ready analysis pipeline for experimental studies in Caenorhabditis elegans.

---

# Publication-Grade Statistical Framework (Version 2.0)

The statistical framework has been expanded beyond conventional hypothesis testing to include advanced analyses commonly expected in peer-reviewed biomedical research.

## Additional Statistical Analyses

### Trend Analysis

- Cochran–Armitage Trend Test

### Effect Size Estimation

- Relative Risk (RR)
- Odds Ratio (OR)
- Absolute Risk Reduction (ARR)
- Relative Risk Reduction (RRR)
- Number Needed to Treat (NNT)
- 95% Confidence Intervals
- Kruskal ε² Effect Size

### Predictive Performance

- Receiver Operating Characteristic (ROC) Curve
- Area Under the ROC Curve (AUC)
- Optimal Threshold Determination
- Sensitivity
- Specificity
- Classification Accuracy

### Model Calibration

- Grouped Hosmer–Lemeshow Goodness-of-Fit Test

### Robustness Assessment

- Jackknife Leave-One-Out Sensitivity Analysis
- Bootstrap Validation

---

# Additional Analysis Module

The `additional_analyses/` directory contains independent scripts that extend the core statistical workflow.

```text
additional_analyses/

├── scripts/
│   ├── 01_cochran_armitage.py
│   ├── 02_kruskal_epsilon_squared.py
│   ├── 03_roc_auc.py
│   ├── 04_hosmer_lemeshow.py
│   ├── 05_effect_size_analysis.py
│   ├── 06_jackknife_logistic.py
│   └── 07_publication_tables.py
│
├── results/
├── figures/
└── tables/
```

---

# Publication Outputs

The repository now automatically generates:

- Publication_Tables.xlsx
- Supplementary_Tables.xlsx
- Statistical_Report.md
- Reproducibility_Report.md

These outputs are intended for direct use during manuscript preparation and journal submission.

---

# Current Statistical Coverage

The repository currently includes:

- Descriptive Statistics
- Pearson Chi-square Test
- Fisher's Exact Test
- Kruskal–Wallis Test
- Cochran–Armitage Trend Test
- Binary Logistic Regression
- Ordered Logistic Regression
- ROC/AUC Analysis
- Hosmer–Lemeshow Calibration Test
- Relative Risk Analysis
- Odds Ratio Analysis
- Bootstrap Validation
- Jackknife Sensitivity Analysis
- Publication-Ready Tables
- Publication-Quality Figures
- Reproducibility Auditing

---

**Current Repository Status:** Publication-grade statistical analysis framework completed.
