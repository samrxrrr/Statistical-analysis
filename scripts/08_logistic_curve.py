import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import statsmodels.api as sm

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("results/cleaned_dataset.csv")

dose_map = {0: 0, 50: 1, 100: 2}
df["Dose"] = df["Concentration"].map(dose_map)

X = sm.add_constant(df["Dose"])
y = df["MUV_Binary"]

model = sm.Logit(y, X).fit(disp=False)

# Prediction grid
dose_numeric = np.linspace(0, 2, 200)
X_pred = sm.add_constant(dose_numeric)

# Predicted probabilities
prob = model.predict(X_pred)

# Approximate 95% CI using parameter covariance
cov = model.cov_params().values
beta = model.params.values

lower = []
upper = []

for row in X_pred:
    eta = row @ beta
    se = np.sqrt(row @ cov @ row.T)

    eta_low = eta - 1.96 * se
    eta_high = eta + 1.96 * se

    lower.append(1 / (1 + np.exp(-eta_low)))
    upper.append(1 / (1 + np.exp(-eta_high)))

lower = np.array(lower)
upper = np.array(upper)

dose_um = dose_numeric * 50

# Observed proportions
obs = df.groupby("Concentration")["MUV_Binary"].mean()

plt.figure(figsize=(8,6))

plt.plot(
    dose_um,
    prob,
    linewidth=3,
    label="Logistic fit"
)

plt.fill_between(
    dose_um,
    lower,
    upper,
    alpha=0.25,
    label="95% CI"
)

plt.scatter(
    obs.index,
    obs.values,
    s=90,
    zorder=5,
    label="Observed"
)

plt.xticks([0,50,100])
plt.ylim(0,1.05)

plt.xlabel("Thymoquinone concentration (µM)")
plt.ylabel("Probability of Multivulva phenotype")
plt.title("Dose–response logistic regression")

plt.grid(alpha=0.3)
plt.legend()

plt.tight_layout()

plt.savefig(
    "figures/Figure5_Logistic_Dose_Response.png",
    dpi=600
)

plt.show()

print("Figure saved successfully.")
