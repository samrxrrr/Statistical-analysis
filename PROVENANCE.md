# PROVENANCE DOCUMENT

This file documents the provenance of all major outputs.

| Step | Script | Input | Output |
|-----:|--------|-------|--------|
| 1 | `01_data_cleaning.py` | Raw experimental data | results/cleaned_dataset.csv |
| 2 | `02_descriptive_statistics.py` | results/cleaned_dataset.csv | tables/Table1_Descriptive_Statistics.* |
| 3 | `03_inferential_statistics.py` | results/cleaned_dataset.csv | reports/inferential_statistics.txt |
| 4 | `04_logistic_regression.py` | results/cleaned_dataset.csv | reports/logistic_regression.txt |
| 5 | `05_ordinal_logistic_statsmodels.py` | results/cleaned_dataset.csv | reports/ordinal_logistic_statsmodels.txt |
| 6 | `06_bootstrap_analysis.py` | results/cleaned_dataset.csv | tables/Table5_Bootstrap_Validation.* |
| 7 | `07_pairwise_risk_analysis.py` | results/cleaned_dataset.csv | tables/Table6_Pairwise_Risk_Analysis.* |
| 8 | `13_generate_table1.py` | Analysis outputs | Table1_Descriptive_Statistics |
| 9 | `14_generate_table2.py` | Analysis outputs | Table2_Inferential_Statistics |
| 10 | `15_generate_table3.py` | Analysis outputs | Table3_Binary_Logistic_Regression |
| 11 | `16_generate_table4.py` | Analysis outputs | Table4_Ordered_Logistic_Regression |
| 12 | `17_generate_table5.py` | Analysis outputs | Table5_Bootstrap_Validation |
| 13 | `18_generate_table6.py` | Analysis outputs | Table6_Pairwise_Risk_Analysis |
| 14 | `19_generate_table7.py` | Analysis outputs | Table7_Statistical_Summary |
| 15 | `20_generate_manuscript_reports.py` | Statistical outputs | reports/ |
| 16 | `21_package_submission.py` | Complete project | submission/ |
