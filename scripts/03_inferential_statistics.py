import pandas as pd
from scipy.stats import chi2_contingency, kruskal
from scipy.stats.contingency import association
import scikit_posthocs as sp

# --------------------------------------------------
# Load data
# --------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

print("=" * 70)
print("INFERENTIAL STATISTICS")
print("=" * 70)

# --------------------------------------------------
# Chi-square Test
# --------------------------------------------------

table = pd.crosstab(df["Concentration"], df["MUV"])

chi2, p, dof, expected = chi2_contingency(table)

print("\nChi-square Test")
print("----------------------")
print(table)
print(f"\nChi² = {chi2:.4f}")
print(f"Degrees of freedom = {dof}")
print(f"P-value = {p:.6f}")

# --------------------------------------------------
# Cramer's V
# --------------------------------------------------

cramers_v = association(table, method="cramer")

print(f"Cramer's V = {cramers_v:.4f}")

# --------------------------------------------------
# Kruskal-Wallis Test
# --------------------------------------------------

g0 = df[df.Concentration == 0]["Ectopic_Vulva"]
g50 = df[df.Concentration == 50]["Ectopic_Vulva"]
g100 = df[df.Concentration == 100]["Ectopic_Vulva"]

H, p_kw = kruskal(g0, g50, g100)

print("\nKruskal-Wallis Test")
print("----------------------")
print(f"H statistic = {H:.4f}")
print(f"P-value = {p_kw:.6f}")

# --------------------------------------------------
# Dunn's Post Hoc Test
# --------------------------------------------------

print("\nDunn's Post Hoc Test (Bonferroni)")

dunn = sp.posthoc_dunn(
    df,
    val_col="Ectopic_Vulva",
    group_col="Concentration",
    p_adjust="bonferroni"
)

print(dunn)

# --------------------------------------------------
# Save results
# --------------------------------------------------

with open("reports/inferential_statistics.txt", "w") as f:
    f.write("Chi-square Test\n")
    f.write(f"Chi² = {chi2:.4f}\n")
    f.write(f"P = {p:.6f}\n")
    f.write(f"Cramer's V = {cramers_v:.4f}\n\n")

    f.write("Kruskal-Wallis\n")
    f.write(f"H = {H:.4f}\n")
    f.write(f"P = {p_kw:.6f}\n\n")

    f.write("Dunn's Test\n")
    f.write(dunn.to_string())

print("\n✓ Inferential statistics saved.")
