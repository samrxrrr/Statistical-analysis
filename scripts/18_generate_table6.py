import pandas as pd

# -------------------------------------------------
# Pairwise Risk Analysis
# -------------------------------------------------

table = pd.DataFrame({

    "Comparison":[
        "0 vs 50 µM",
        "0 vs 100 µM",
        "50 vs 100 µM"
    ],

    "Relative Risk (RR)":[
        0.517,
        0.241,
        0.467
    ],

    "Odds Ratio (OR)":[
        6.444,
        19.333,
        3.000
    ],

    "95% CI":[
        "2.135–19.456",
        "5.778–64.689",
        "1.034–8.702"
    ],

    "Absolute Risk Reduction (ARR)":[
        0.400,
        0.629,
        0.229
    ],

    "Relative Risk Reduction (RRR)":[
        0.483,
        0.759,
        0.533
    ],

    "Fisher's Exact P-value":[
        "0.001093",
        "<0.000001",
        "0.070287"
    ],

    "Interpretation":[
        "Significant reduction in MUV incidence",
        "Highly significant reduction in MUV incidence",
        "Difference not statistically significant"
    ]

})

# -------------------------------------------------
# Save outputs
# -------------------------------------------------

table.to_csv(
    "tables/Table6_Pairwise_Risk_Analysis.csv",
    index=False
)

table.to_excel(
    "tables/Table6_Pairwise_Risk_Analysis.xlsx",
    index=False
)

try:
    md = table.to_markdown(index=False)
except ImportError:
    md = table.to_string(index=False)

with open(
    "tables/Table6_Pairwise_Risk_Analysis.md",
    "w"
) as f:
    f.write("# Table 6. Pairwise Risk Analysis\n\n")
    f.write(md)

print("="*70)
print("TABLE 6 GENERATED")
print("="*70)
print(table)

print("\nClinical Interpretation")
print("-"*70)
print("Thymoquinone treatment substantially reduced the")
print("risk of the multivulva phenotype. The greatest")
print("protective effect was observed at 100 µM.")
print("The comparison between 50 µM and 100 µM showed")
print("additional reduction, although it was not")
print("statistically significant (Fisher's exact test).")

print("\nSaved:")
print("tables/Table6_Pairwise_Risk_Analysis.csv")
print("tables/Table6_Pairwise_Risk_Analysis.xlsx")
print("tables/Table6_Pairwise_Risk_Analysis.md")
