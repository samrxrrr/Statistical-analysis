import pandas as pd

# -------------------------------------------------
# Binary Logistic Regression Results
# -------------------------------------------------

coef = 1.4024
coef_dose = -1.4800

se_const = 0.376
se_dose = 0.308

z_const = 3.729
z_dose = -4.810

p_const = "<0.001"
p_dose = "<0.001"

or_const = 4.065
or_dose = 0.228

ci_const = "1.945–8.495"
ci_dose = "0.125–0.416"

table = pd.DataFrame({

    "Parameter":[
        "Intercept",
        "Dose (per 50 µM increase)"
    ],

    "Coefficient (β)":[
        coef,
        coef_dose
    ],

    "Std. Error":[
        se_const,
        se_dose
    ],

    "z":[
        z_const,
        z_dose
    ],

    "P-value":[
        p_const,
        p_dose
    ],

    "Odds Ratio":[
        or_const,
        or_dose
    ],

    "95% CI":[
        ci_const,
        ci_dose
    ]

})

table.to_csv(
    "tables/Table3_Binary_Logistic_Regression.csv",
    index=False
)

table.to_excel(
    "tables/Table3_Binary_Logistic_Regression.xlsx",
    index=False
)

try:
    md = table.to_markdown(index=False)
except ImportError:
    md = table.to_string(index=False)

with open(
    "tables/Table3_Binary_Logistic_Regression.md",
    "w"
) as f:

    f.write("# Table 3. Binary Logistic Regression\n\n")
    f.write(md)

print("="*70)
print("TABLE 3 GENERATED")
print("="*70)

print(table)

print("\nModel Statistics")
print("----------------------------")
print("Pseudo R²      : 0.205")
print("Log-Likelihood : -57.798")
print("LLR p-value    : 4.60e-08")

print("\nSaved:")
print("tables/Table3_Binary_Logistic_Regression.csv")
print("tables/Table3_Binary_Logistic_Regression.xlsx")
print("tables/Table3_Binary_Logistic_Regression.md")
