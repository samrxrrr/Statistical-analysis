import matplotlib.pyplot as plt
import numpy as np

# Pairwise comparison labels
labels = [
    "0 vs 50 µM",
    "0 vs 100 µM",
    "50 vs 100 µM"
]

# Odds ratios from your analysis
OR = np.array([6.444, 19.333, 3.000])

# 95% confidence intervals
lower = np.array([2.135, 5.778, 1.034])
upper = np.array([19.456, 64.689, 8.702])

# Error bars
xerr = np.vstack([OR - lower, upper - OR])

plt.figure(figsize=(8,5))

plt.errorbar(
    OR,
    labels,
    xerr=xerr,
    fmt='o',
    capsize=5,
    linewidth=2
)

# Null effect line
plt.axvline(
    1,
    linestyle='--',
    linewidth=1.5,
    color='red'
)

plt.xscale("log")

plt.xlabel("Odds Ratio (log scale)", fontsize=12)
plt.title("Pairwise Odds Ratios with 95% Confidence Intervals")

plt.tight_layout()

plt.savefig(
    "figures/Figure6_ForestPlot_OR.png",
    dpi=600
)

plt.show()

print("Forest plot saved.")
