import pandas as pd

# -------------------------------------------------
# Final inferential statistics
# (Update these only if analyses are rerun)
# -------------------------------------------------

table = pd.DataFrame({

    "Analysis": [
        "Pearson Chi-square",
        "Cramer's V",
        "Kruskal-Wallis",
        "Dunn Post Hoc",
        "Binary Logistic Regression",
        "Ordered Logistic Regression",
        "Bootstrap Validation"
    ],

    "Statistic": [
        "χ² = 28.366",
        "V = 0.520",
        "H = 23.750",
        "0 vs 50, 0 vs 100",
        "β = -1.480",
        "β = -1.264",
        "Bootstrap OR = 0.226"
    ],

    "Effect Size": [
        "Large",
        "Large",
        "-",
        "-",
        "OR = 0.228",
        "OR = 0.283",
        "95% CI = 0.106–0.377"
    ],

    "95% Confidence Interval": [
        "-",
        "-",
        "-",
        "-",
        "0.125–0.416",
        "0.165–0.485",
        "0.106–0.377"
    ],

    "P-value": [
        "<0.000001",
        "-",
        "0.000007",
        "0.0046 / 0.000005",
        "<0.001",
        "<0.001",
        "-"
    ],

    "Interpretation": [
        "Strong association between treatment and MUV phenotype",
        "Large effect size",
        "Severity differs significantly among groups",
        "Control differs significantly from both treatment groups",
        "Dose significantly decreases odds of MUV",
        "Dose significantly decreases severity",
        "Bootstrap confirms model stability"
    ]

})

# -------------------------------------------------
# Save files
# -------------------------------------------------

table.to_csv(
    "tables/Table2_Inferential_Statistics.csv",
    index=False
)

table.to_excel(
    "tables/Table2_Inferential_Statistics.xlsx",
    index=False
)

try:
    markdown = table.to_markdown(index=False)
except ImportError:
    markdown = table.to_string(index=False)

with open(
    "tables/Table2_Inferential_Statistics.md",
    "w"
) as f:
    f.write("# Table 2. Inferential Statistics\n\n")
    f.write(markdown)

# -------------------------------------------------
# Display
# -------------------------------------------------

print("=" * 70)
print("TABLE 2 - INFERENTIAL STATISTICS")
print("=" * 70)
print(table)

print("\nSaved:")
print("tables/Table2_Inferential_Statistics.csv")
print("tables/Table2_Inferential_Statistics.xlsx")
print("tables/Table2_Inferential_Statistics.md")
