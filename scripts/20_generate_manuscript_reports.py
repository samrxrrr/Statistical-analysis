from pathlib import Path

report_dir = Path("reports")
report_dir.mkdir(exist_ok=True)

# -------------------------------------------------
# Statistical Analysis (Methods)
# -------------------------------------------------

methods = """
STATISTICAL ANALYSIS

Statistical analyses were performed using Python 3 with the pandas, NumPy,
SciPy, statsmodels, scikit-posthocs, and matplotlib libraries.

Differences in MUV incidence among treatment groups were evaluated using the
Pearson chi-square test. The strength of association was quantified using
Cramer's V.

Differences in ectopic vulva severity scores were assessed using the
Kruskal–Wallis test followed by Dunn's multiple-comparison test with
Bonferroni correction.

Binary logistic regression was used to estimate the effect of increasing
thymoquinone concentration on the probability of the MUV phenotype.

Ordinal logistic regression (OrderedModel, statsmodels) was used to evaluate
changes in severity categories.

Bootstrap resampling was performed to evaluate the robustness of the estimated
odds ratios and prevalence estimates.

Pairwise treatment comparisons were evaluated using Fisher's exact test,
relative risk, odds ratio, absolute risk reduction, and relative risk
reduction.

A two-sided P value <0.05 was considered statistically significant.
"""

(report_dir / "Statistical_Analysis_Methods.txt").write_text(methods)

# -------------------------------------------------
# Results
# -------------------------------------------------

results = """
RESULTS

Treatment with thymoquinone produced a marked dose-dependent reduction in the
multivulva phenotype.

MUV incidence declined from 82.9% in untreated worms to 42.9% following
50 µM treatment and to 20.0% following 100 µM treatment.

Pearson chi-square analysis demonstrated a highly significant association
between treatment and phenotype (χ² = 28.366, P < 0.000001).

The severity of ectopic vulva formation differed significantly among groups
(Kruskal–Wallis H = 23.750, P = 0.000007).

Binary logistic regression demonstrated that each 50 µM increase in
thymoquinone concentration reduced the odds of the MUV phenotype by
approximately 77% (OR = 0.228).

Ordinal logistic regression similarly demonstrated a significant reduction
in the probability of higher severity classes (OR = 0.283, P < 0.001).

Bootstrap resampling confirmed the robustness of the estimated odds ratios.

Pairwise risk analysis indicated that the greatest protective effect occurred
at 100 µM thymoquinone.
"""

(report_dir / "Results_Section.txt").write_text(results)

# -------------------------------------------------
# Figure Legends
# -------------------------------------------------

figure_legends = """
Figure 1.
Dose-dependent reduction in multivulva incidence following thymoquinone treatment.

Figure 2.
Distribution of ectopic vulva severity scores across treatment groups.

Figure 3.
Binary logistic regression showing predicted probability of MUV.

Figure 4.
Ordinal logistic regression demonstrating decreasing probability of severe phenotypes.

Figure 5.
Bootstrap validation of odds ratio estimates.

Figure 6.
Pairwise risk analysis among treatment groups.
"""

(report_dir / "Figure_Legends.txt").write_text(figure_legends)

# -------------------------------------------------
# Table Legends
# -------------------------------------------------

table_legends = """
Table 1. Descriptive statistics.

Table 2. Summary of inferential statistical analyses.

Table 3. Binary logistic regression model.

Table 4. Ordered logistic regression model.

Table 5. Bootstrap validation results.

Table 6. Pairwise risk analysis.

Table 7. Overall statistical summary.
"""

(report_dir / "Table_Legends.txt").write_text(table_legends)

# -------------------------------------------------
# Supplementary Report
# -------------------------------------------------

supplementary = """
SUPPLEMENTARY STATISTICAL REPORT

All statistical analyses consistently demonstrated a significant
dose-dependent protective effect of thymoquinone against Ras/MAPK-induced
multivulva formation.

The agreement among non-parametric analyses, regression models,
bootstrap validation, and risk analysis provides strong support
for the robustness of the findings.
"""

(report_dir / "Supplementary_Statistical_Report.txt").write_text(supplementary)

print("=" * 70)
print("PUBLICATION REPORTS GENERATED")
print("=" * 70)

for file in sorted(report_dir.glob("*.txt")):
    print(file)

