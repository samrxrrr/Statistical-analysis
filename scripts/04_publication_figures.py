import pandas as pd
import matplotlib.pyplot as plt

# --------------------------------------------------
# Load data
# --------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

# --------------------------------------------------
# Figure 1: MUV Percentage
# --------------------------------------------------

muv_percent = (
    pd.crosstab(df["Concentration"], df["MUV"], normalize="index") * 100
)

plt.figure(figsize=(7,5))
muv_percent.plot(kind="bar", stacked=True)

plt.title("Multivulva Phenotype by Thymoquinone Concentration")
plt.xlabel("Thymoquinone Concentration (µM)")
plt.ylabel("Percentage of Worms")
plt.legend(title="Phenotype")
plt.tight_layout()

plt.savefig(
    "figures/Figure1_MUV_Percentage.png",
    dpi=600,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Figure 2: Severity Boxplot
# --------------------------------------------------

plt.figure(figsize=(7,5))

df.boxplot(
    column="Ectopic_Vulva",
    by="Concentration",
    grid=False
)

plt.title("Severity of Ectopic Vulvae")
plt.suptitle("")
plt.xlabel("Thymoquinone Concentration (µM)")
plt.ylabel("Severity Score")

plt.tight_layout()

plt.savefig(
    "figures/Figure2_Boxplot.png",
    dpi=600,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Figure 3: Mean Severity
# --------------------------------------------------

summary = (
    df.groupby("Concentration")["Ectopic_Vulva"]
      .agg(["mean","std"])
)

plt.figure(figsize=(7,5))

plt.bar(
    summary.index.astype(str),
    summary["mean"],
    yerr=summary["std"],
    capsize=6
)

plt.xlabel("Thymoquinone Concentration (µM)")
plt.ylabel("Mean Severity Score")
plt.title("Dose-dependent Reduction in Vulval Severity")

plt.tight_layout()

plt.savefig(
    "figures/Figure3_MeanSeverity.png",
    dpi=600,
    bbox_inches="tight"
)

plt.close()

# --------------------------------------------------
# Figure 4: Dose-response
# --------------------------------------------------

dose = (
    df.groupby("Concentration")["MUV_Binary"]
      .mean() * 100
)

plt.figure(figsize=(7,5))

plt.plot(
    dose.index,
    dose.values,
    marker="o",
    linewidth=2
)

plt.xticks([0,50,100])

plt.xlabel("Thymoquinone Concentration (µM)")
plt.ylabel("MUV Positive (%)")
plt.title("Dose-response Relationship")

plt.grid(True)

plt.tight_layout()

plt.savefig(
    "figures/Figure4_DoseResponse.png",
    dpi=600,
    bbox_inches="tight"
)

plt.close()

print("\nPublication-quality figures generated successfully.")
