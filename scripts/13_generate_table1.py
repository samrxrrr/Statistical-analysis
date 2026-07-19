import pandas as pd
import numpy as np

# -------------------------------------------------
# Load cleaned dataset
# -------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

# -------------------------------------------------
# Group summary
# -------------------------------------------------

summary = (
    df
    .groupby("Concentration")
    .agg(
        Sample_Size=("MUV_Binary", "count"),
        MUV_Positive=("MUV_Binary", "sum"),
        Mean_Severity=("Ectopic_Vulva", "mean"),
        SD_Severity=("Ectopic_Vulva", "std"),
        Median_Severity=("Ectopic_Vulva", "median"),
        Min_Severity=("Ectopic_Vulva", "min"),
        Max_Severity=("Ectopic_Vulva", "max")
    )
    .reset_index()
)

summary["MUV_Negative"] = (
    summary["Sample_Size"] -
    summary["MUV_Positive"]
)

summary["MUV_Percentage"] = (
    summary["MUV_Positive"] /
    summary["Sample_Size"] * 100
).round(2)

summary = summary[
    [
        "Concentration",
        "Sample_Size",
        "MUV_Positive",
        "MUV_Negative",
        "MUV_Percentage",
        "Mean_Severity",
        "SD_Severity",
        "Median_Severity",
        "Min_Severity",
        "Max_Severity"
    ]
]

summary.rename(
    columns={
        "Concentration":"Thymoquinone (µM)",
        "Sample_Size":"n",
        "MUV_Positive":"MUV Present",
        "MUV_Negative":"MUV Absent",
        "MUV_Percentage":"MUV (%)",
        "Mean_Severity":"Mean Severity",
        "SD_Severity":"SD",
        "Median_Severity":"Median",
        "Min_Severity":"Minimum",
        "Max_Severity":"Maximum"
    },
    inplace=True
)

# Round numeric columns
for col in ["Mean Severity","SD","Median"]:
    summary[col] = summary[col].round(3)

# -------------------------------------------------
# Save outputs
# -------------------------------------------------

summary.to_csv(
    "tables/Table1_Descriptive_Statistics.csv",
    index=False
)

summary.to_excel(
    "tables/Table1_Descriptive_Statistics.xlsx",
    index=False
)

# Markdown version for manuscript
with open(
    "tables/Table1_Descriptive_Statistics.md",
    "w"
) as f:

    f.write("# Table 1. Descriptive Statistics\n\n")
    f.write(summary.to_markdown(index=False))

print("\n")
print("="*70)
print("TABLE 1 GENERATED")
print("="*70)
print(summary)
print("\nSaved:")
print("tables/Table1_Descriptive_Statistics.csv")
print("tables/Table1_Descriptive_Statistics.xlsx")
print("tables/Table1_Descriptive_Statistics.md")
