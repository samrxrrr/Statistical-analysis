import pandas as pd

# -------------------------------------------------
# Ordered Logistic Regression (statsmodels OrderedModel)
# -------------------------------------------------

table = pd.DataFrame({

    "Parameter": [
        "Dose (per 50 µM increase)"
    ],

    "Coefficient (β)": [
        -1.2640
    ],

    "Std. Error": [
        0.276
    ],

    "z-value": [
        -4.588
    ],

    "P-value": [
        "<0.001"
    ],

    "Odds Ratio": [
        0.2825
    ],

    "95% CI": [
        "0.1646–0.4848"
    ]

})

# Save outputs
table.to_csv(
    "tables/Table4_Ordered_Logistic_Regression.csv",
    index=False
)

table.to_excel(
    "tables/Table4_Ordered_Logistic_Regression.xlsx",
    index=False
)

try:
    md = table.to_markdown(index=False)
except ImportError:
    md = table.to_string(index=False)

with open(
    "tables/Table4_Ordered_Logistic_Regression.md",
    "w"
) as f:
    f.write("# Table 4. Ordered Logistic Regression (OrderedModel)\n\n")
    f.write(md)

print("=" * 70)
print("TABLE 4 GENERATED")
print("=" * 70)
print(table)

print("\nModel Statistics")
print("----------------------------")
print("Log-Likelihood : -88.064")
print("AIC            : 182.128")
print("BIC            : 190.091")

print("\nInterpretation")
print("----------------------------")
print("Each 50 µM increase in thymoquinone concentration")
print("reduced the odds of belonging to a higher ectopic")
print("vulva severity category by approximately 72%.")

print("\nSaved:")
print("tables/Table4_Ordered_Logistic_Regression.csv")
print("tables/Table4_Ordered_Logistic_Regression.xlsx")
print("tables/Table4_Ordered_Logistic_Regression.md")
