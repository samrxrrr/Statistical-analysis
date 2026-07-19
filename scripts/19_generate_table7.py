import pandas as pd

# -------------------------------------------------
# Complete Statistical Summary
# -------------------------------------------------

summary = pd.DataFrame({

    "Analysis":[
        "MUV Incidence",
        "Severity Analysis",
        "Pearson Chi-square",
        "Kruskal-Wallis",
        "Binary Logistic Regression",
        "Ordered Logistic Regression",
        "Bootstrap Validation",
        "Pairwise Risk Analysis"
    ],

    "Primary Result":[
        "82.9% → 42.9% → 20.0%",
        "Mean: 1.000 → 0.514 → 0.286",
        "χ² = 28.366",
        "H = 23.750",
        "OR = 0.228",
        "OR = 0.283",
        "Bootstrap OR = 0.226",
        "Maximum protection at 100 µM"
    ],

    "P-value":[
        "-",
        "-",
        "<0.000001",
        "0.000007",
        "<0.001",
        "<0.001",
        "-",
        "See pairwise tests"
    ],

    "Conclusion":[
        "Dose-dependent reduction in MUV frequency",
        "Severity decreases with treatment",
        "Strong association between treatment and phenotype",
        "Severity differs significantly among groups",
        "Each 50 µM increase markedly reduces odds of MUV",
        "Higher doses reduce odds of severe phenotype",
        "Model estimates are robust",
        "100 µM provides the greatest protective effect"
    ]

})

summary.to_csv(
    "tables/Table7_Statistical_Summary.csv",
    index=False
)

summary.to_excel(
    "tables/Table7_Statistical_Summary.xlsx",
    index=False
)

try:
    md = summary.to_markdown(index=False)
except ImportError:
    md = summary.to_string(index=False)

with open(
    "tables/Table7_Statistical_Summary.md",
    "w"
) as f:
    f.write("# Table 7. Complete Statistical Summary\n\n")
    f.write(md)

print("="*70)
print("TABLE 7 GENERATED")
print("="*70)
print(summary)

print("\nOverall Conclusion")
print("-"*70)
print("Across all statistical analyses, thymoquinone")
print("demonstrated a significant dose-dependent")
print("reduction in both the incidence and severity")
print("of the multivulva phenotype.")
print("The findings were consistent across")
print("non-parametric tests, regression models,")
print("bootstrap validation, and pairwise risk analyses.")

print("\nSaved:")
print("tables/Table7_Statistical_Summary.csv")
print("tables/Table7_Statistical_Summary.xlsx")
print("tables/Table7_Statistical_Summary.md")
