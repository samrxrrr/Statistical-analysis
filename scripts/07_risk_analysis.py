import pandas as pd
import numpy as np
from scipy.stats import fisher_exact
from statsmodels.stats.contingency_tables import Table2x2

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("results/cleaned_dataset.csv")

groups = [0, 50, 100]

print("=" * 70)
print("PAIRWISE RISK ANALYSIS")
print("=" * 70)

for i in range(len(groups)):
    for j in range(i + 1, len(groups)):

        g1 = groups[i]
        g2 = groups[j]

        d1 = df[df["Concentration"] == g1]
        d2 = df[df["Concentration"] == g2]

        # Event = MUV present
        a = d1["MUV_Binary"].sum()
        b = len(d1) - a

        c = d2["MUV_Binary"].sum()
        d = len(d2) - c

        table = np.array([[a, b],
                          [c, d]])

        t = Table2x2(table)

        risk1 = a / (a + b)
        risk2 = c / (c + d)

        rr = risk2 / risk1
        rd = risk2 - risk1
        arr = risk1 - risk2
        rrr = arr / risk1

        _, fisher_p = fisher_exact(table)

        print("\n")
        print("=" * 70)
        print(f"{g1} µM  vs  {g2} µM")
        print("=" * 70)

        print(table)

        print(f"\nRisk {g1} µM : {risk1:.3f}")
        print(f"Risk {g2} µM : {risk2:.3f}")

        print(f"\nRelative Risk (RR): {rr:.3f}")

        print(f"Odds Ratio: {t.oddsratio:.3f}")
        print(f"OR 95% CI: ({t.oddsratio_confint()[0]:.3f}, "
              f"{t.oddsratio_confint()[1]:.3f})")

        print(f"\nRisk Difference: {rd:.3f}")
        print(f"Absolute Risk Reduction: {arr:.3f}")
        print(f"Relative Risk Reduction: {rrr:.3f}")

        print(f"\nFisher Exact p-value: {fisher_p:.6f}")
