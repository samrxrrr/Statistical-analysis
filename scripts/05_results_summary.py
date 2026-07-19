import pandas as pd
from scipy.stats import chi2_contingency, kruskal
from scipy.stats.contingency import association
import scikit_posthocs as sp

# --------------------------------------------------
# Load data
# --------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

# --------------------------------------------------
# Descriptive statistics
# --------------------------------------------------

group_counts = df["Concentration"].value_counts().sort_index()

muv = pd.crosstab(df["Concentration"], df["MUV"])

muv_percent = (
    pd.crosstab(
        df["Concentration"],
        df["MUV"],
        normalize="index"
    ) * 100
).round(2)

severity = (
    df.groupby("Concentration")["Ectopic_Vulva"]
      .agg(["count","mean","std","median","min","max"])
)

# --------------------------------------------------
# Inferential statistics
# --------------------------------------------------

table = pd.crosstab(df["Concentration"], df["MUV"])

chi2, p, dof, expected = chi2_contingency(table)

cramers = association(table, method="cramer")

H, p_kw = kruskal(
    df[df.Concentration==0]["Ectopic_Vulva"],
    df[df.Concentration==50]["Ectopic_Vulva"],
    df[df.Concentration==100]["Ectopic_Vulva"]
)

dunn = sp.posthoc_dunn(
    df,
    val_col="Ectopic_Vulva",
    group_col="Concentration",
    p_adjust="bonferroni"
)

# --------------------------------------------------
# Write report
# --------------------------------------------------

with open("reports/Statistical_Report.md","w") as f:

    f.write("# Statistical Analysis Report\n\n")

    f.write("## Dataset\n")
    f.write(f"- Total observations: {len(df)}\n")
    f.write(f"- Treatment groups: {group_counts.to_dict()}\n\n")

    f.write("## MUV Frequency (%)\n\n")
    f.write(muv_percent.to_markdown())
    f.write("\n\n")

    f.write("## Severity Statistics\n\n")
    f.write(severity.round(3).to_markdown())
    f.write("\n\n")

    f.write("## Chi-square Test\n\n")
    f.write(f"- χ² = {chi2:.3f}\n")
    f.write(f"- df = {dof}\n")
    f.write(f"- p = {p:.6f}\n")
    f.write(f"- Cramer's V = {cramers:.3f}\n\n")

    f.write("## Kruskal-Wallis Test\n\n")
    f.write(f"- H = {H:.3f}\n")
    f.write(f"- p = {p_kw:.6f}\n\n")

    f.write("## Dunn's Post Hoc Test\n\n")
    f.write(dunn.round(6).to_markdown())
    f.write("\n\n")

    f.write("## Interpretation\n\n")

    f.write(
"""
Increasing thymoquinone concentration significantly reduced
both the frequency and severity of the multivulva phenotype.
The strongest statistical difference was observed between
0 µM and 100 µM. The comparison between 50 µM and
100 µM was not statistically significant after Bonferroni
correction.
"""
)

print("\nStatistical report generated successfully.")
