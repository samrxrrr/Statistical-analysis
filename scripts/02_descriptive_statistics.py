import pandas as pd

# --------------------------------------------------
# Load cleaned dataset
# --------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

print("=" * 70)
print("DESCRIPTIVE STATISTICS")
print("=" * 70)

# --------------------------------------------------
# Overall summary
# --------------------------------------------------

print("\nOverall Dataset Summary")
print(df.describe())

# --------------------------------------------------
# Sample size
# --------------------------------------------------

print("\nSample Size")
print(df.shape[0])

# --------------------------------------------------
# Number of worms per concentration
# --------------------------------------------------

print("\nObservations per Concentration")
group_counts = df["Concentration"].value_counts().sort_index()
print(group_counts)

# --------------------------------------------------
# MUV frequency
# --------------------------------------------------

print("\nMUV Frequency")
muv = pd.crosstab(
    df["Concentration"],
    df["MUV"]
)

print(muv)

# --------------------------------------------------
# Percentage MUV
# --------------------------------------------------

muv_percent = (
    pd.crosstab(
        df["Concentration"],
        df["MUV"],
        normalize="index"
    ) * 100
).round(2)

print("\nPercentage MUV")
print(muv_percent)

# --------------------------------------------------
# Severity statistics
# --------------------------------------------------

severity = (
    df.groupby("Concentration")["Ectopic_Vulva"]
      .agg([
          "count",
          "mean",
          "median",
          "std",
          "min",
          "max"
      ])
)

print("\nSeverity Statistics")
print(severity)

# --------------------------------------------------
# Save publication tables
# --------------------------------------------------

group_counts.to_csv("tables/Table1_GroupCounts.csv")

muv.to_csv("tables/Table2_MUV_Frequency.csv")

muv_percent.to_csv("tables/Table3_MUV_Percentage.csv")

severity.to_csv("tables/Table4_SeverityStatistics.csv")

print("\n✓ Publication tables saved successfully.")
