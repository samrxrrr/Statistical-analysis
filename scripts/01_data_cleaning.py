import pandas as pd

# --------------------------------------------------
# Load dataset
# --------------------------------------------------
file_path = "data/AP Research 25-26 - Sheet1.csv"

df = pd.read_csv(file_path)

print("=" * 60)
print("DATA PREVIEW")
print("=" * 60)
print(df.head())

print("\nColumns:")
print(df.columns.tolist())

print("\nShape:")
print(df.shape)

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\nDuplicate Rows:", df.duplicated().sum())

# --------------------------------------------------
# Rename columns
# --------------------------------------------------
df.columns = [
    "Concentration",
    "Ectopic_Vulva",
    "MUV"
]

# --------------------------------------------------
# Clean concentration values
# --------------------------------------------------
df["Concentration"] = (
    df["Concentration"]
    .astype(str)
    .str.extract(r'(\d+)')[0]
    .astype(int)
)

# --------------------------------------------------
# Standardize Yes/No values
# --------------------------------------------------
df["MUV"] = (
    df["MUV"]
    .astype(str)
    .str.strip()
    .str.capitalize()
)

df["MUV_Binary"] = df["MUV"].map({
    "Yes": 1,
    "No": 0
})

# --------------------------------------------------
# Convert severity to numeric
# --------------------------------------------------
df["Ectopic_Vulva"] = pd.to_numeric(
    df["Ectopic_Vulva"],
    errors="coerce"
)

print("\nCleaned Data Preview")
print(df.head())

print("\nSummary Statistics")
print(df.describe(include="all"))

# --------------------------------------------------
# Save cleaned dataset
# --------------------------------------------------
output = "results/cleaned_dataset.csv"

df.to_csv(output, index=False)

print("\n✓ Cleaned dataset saved to:")
print(output)

print("\nAnalysis Step 1 Complete.")
