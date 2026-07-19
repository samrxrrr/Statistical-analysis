import pandas as pd
import numpy as np

from statsmodels.miscmodels.ordinal_model import OrderedModel

# -------------------------------------------------
# Load cleaned data
# -------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

# Encode dose
dose_map = {
    0: 0,
    50: 1,
    100: 2
}

df["Dose"] = df["Concentration"].map(dose_map)

# Response variable
y = df["Ectopic_Vulva"].astype(int)

# Predictor
X = df[["Dose"]]

# -------------------------------------------------
# Fit Ordered Logistic Regression
# -------------------------------------------------

model = OrderedModel(
    endog=y,
    exog=X,
    distr="logit"
)

result = model.fit(
    method="bfgs",
    disp=False
)

# -------------------------------------------------
# Print summary
# -------------------------------------------------

print("=" * 70)
print("ORDINAL LOGISTIC REGRESSION (OrderedModel)")
print("=" * 70)

print(result.summary())

# -------------------------------------------------
# Odds Ratio
# -------------------------------------------------

coef = result.params["Dose"]

OR = np.exp(coef)

ci = result.conf_int()

lower = np.exp(ci.loc["Dose", 0])
upper = np.exp(ci.loc["Dose", 1])

print("\n" + "=" * 70)
print("Odds Ratio")
print("=" * 70)

print(f"Coefficient : {coef:.4f}")
print(f"Odds Ratio  : {OR:.4f}")
print(f"95% CI      : ({lower:.4f}, {upper:.4f})")

# -------------------------------------------------
# Predicted probabilities
# -------------------------------------------------

pred_prob = result.model.predict(result.params)

pred_class = np.argmax(pred_prob, axis=1)

df["Predicted_Severity"] = pred_class

df.to_csv(
    "results/ordinal_predictions_statsmodels.csv",
    index=False
)

# -------------------------------------------------
# Save report
# -------------------------------------------------

with open(
    "reports/ordinal_logistic_statsmodels.txt",
    "w"
) as f:

    f.write(result.summary().as_text())
    f.write("\n\n")
    f.write(f"Coefficient = {coef:.4f}\n")
    f.write(f"Odds Ratio = {OR:.4f}\n")
    f.write(f"95% CI = ({lower:.4f}, {upper:.4f})\n")

print("\nPredictions saved to:")
print("results/ordinal_predictions_statsmodels.csv")

print("Report saved to:")
print("reports/ordinal_logistic_statsmodels.txt")

print("\nDone.")
