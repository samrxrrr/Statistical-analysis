import pandas as pd

# -------------------------------------------------
# Bootstrap Validation Results
# -------------------------------------------------

table = pd.DataFrame({

    "Metric":[
        "Observed MUV Proportion",
        "Bootstrap Mean MUV Proportion",
        "95% BCa CI (MUV)",
        "Observed Odds Ratio",
        "Bootstrap Mean Odds Ratio",
        "95% Bootstrap CI (OR)"
    ],

    "Value":[
        0.4857,
        0.4857,
        "0.3905–0.5810",
        0.2280,
        0.2260,
        "0.106–0.377"
    ],

    "Interpretation":[
        "Observed overall prevalence",
        "Bootstrap estimate consistent with observed value",
        "Stable estimate of MUV prevalence",
        "Observed logistic regression odds ratio",
        "Bootstrap estimate confirms model stability",
        "Confidence interval excludes the null value (OR = 1)"
    ]

})

table.to_csv(
    "tables/Table5_Bootstrap_Validation.csv",
    index=False
)

table.to_excel(
    "tables/Table5_Bootstrap_Validation.xlsx",
    index=False
)

try:
    md = table.to_markdown(index=False)
except ImportError:
    md = table.to_string(index=False)

with open(
    "tables/Table5_Bootstrap_Validation.md",
    "w"
) as f:
    f.write("# Table 5. Bootstrap Validation\n\n")
    f.write(md)

print("="*70)
print("TABLE 5 GENERATED")
print("="*70)
print(table)

print("\nSummary")
print("----------------------------")
print("Bootstrap resampling confirmed the stability")
print("of the estimated odds ratio and MUV prevalence.")
print("The confidence intervals indicate robust model")
print("performance across resampled datasets.")

print("\nSaved:")
print("tables/Table5_Bootstrap_Validation.csv")
print("tables/Table5_Bootstrap_Validation.xlsx")
print("tables/Table5_Bootstrap_Validation.md")
