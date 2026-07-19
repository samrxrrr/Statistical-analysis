import pandas as pd

summary = pd.DataFrame({

    "Analysis":[
        "Descriptive Statistics",
        "Chi-square Test",
        "Cramer's V",
        "Kruskal-Wallis Test",
        "Dunn's Post Hoc",
        "Binary Logistic Regression",
        "Ordinal Logistic Regression",
        "Bootstrap Validation",
        "Fisher Exact (0 vs 50)",
        "Fisher Exact (0 vs 100)",
        "Fisher Exact (50 vs 100)"
    ],

    "Statistic":[
        "105 worms (35/group)",
        "χ² = 28.366",
        "V = 0.520",
        "H = 23.750",
        "0–50, 0–100 significant",
        "β = -1.480",
        "β = -1.081",
        "Bootstrap OR = 0.226",
        "OR = 6.444",
        "OR = 19.333",
        "OR = 3.000"
    ],

    "Effect Size":[
        "-",
        "Large",
        "Large",
        "-",
        "-",
        "OR = 0.228",
        "OR = 0.339",
        "95% CI: 0.106–0.377",
        "ARR = 0.400",
        "ARR = 0.629",
        "ARR = 0.229"
    ],

    "P-value":[
        "-",
        "<0.000001",
        "-",
        "0.000007",
        "0.0046 / 0.000005",
        "<0.001",
        "-",
        "-",
        "0.001093",
        "<0.000001",
        "0.070287"
    ],

    "Interpretation":[
        "Balanced experimental design",
        "Strong association between dose and phenotype",
        "Large association",
        "Severity differs across groups",
        "Control differs from treated groups",
        "Dose lowers odds of MUV",
        "Dose lowers severity",
        "Model is robust",
        "50 µM significantly reduces risk",
        "100 µM strongly reduces risk",
        "Trend only; not statistically significant"
    ]

})

summary.to_csv(
    "tables/Table5_Statistical_Summary.csv",
    index=False
)

summary.to_excel(
    "tables/Table5_Statistical_Summary.xlsx",
    index=False
)

print(summary)

print("\nDone.")
