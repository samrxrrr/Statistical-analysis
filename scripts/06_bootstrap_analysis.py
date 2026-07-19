import pandas as pd
import numpy as np
from scipy.stats import bootstrap
from sklearn.utils import resample
import statsmodels.api as sm

# -----------------------------
# Load data
# -----------------------------
df = pd.read_csv("results/cleaned_dataset.csv")

# -----------------------------
# Bootstrap CI for MUV proportion
# -----------------------------
def muv_prop(x):
    return np.mean(x)

res = bootstrap(
    (df["MUV_Binary"].values,),
    statistic=muv_prop,
    n_resamples=10000,
    confidence_level=0.95,
    random_state=42,
    method="BCa"
)

print("="*60)
print("BOOTSTRAP ANALYSIS")
print("="*60)

print(f"\nObserved MUV proportion: {df['MUV_Binary'].mean():.4f}")
print(f"95% BCa CI: ({res.confidence_interval.low:.4f}, "
      f"{res.confidence_interval.high:.4f})")

# -----------------------------
# Bootstrap logistic OR
# -----------------------------
boot_or = []

dose_map = {0:0, 50:1, 100:2}
df["Dose"] = df["Concentration"].map(dose_map)

for _ in range(1000):
    sample = resample(df, replace=True)

    X = sm.add_constant(sample["Dose"])
    y = sample["MUV_Binary"]

    try:
        model = sm.Logit(y, X).fit(disp=False)
        boot_or.append(np.exp(model.params["Dose"]))
    except:
        continue

boot_or = np.array(boot_or)

print(f"\nObserved OR: {np.exp(sm.Logit(df['MUV_Binary'], sm.add_constant(df['Dose'])).fit(disp=False).params['Dose']):.3f}")
print(f"Bootstrap OR mean: {boot_or.mean():.3f}")
print(f"95% CI: ({np.percentile(boot_or,2.5):.3f}, "
      f"{np.percentile(boot_or,97.5):.3f})")

pd.DataFrame({"Bootstrap_OR": boot_or}).to_csv(
    "results/bootstrap_OR.csv",
    index=False
)

print("\nBootstrap complete.")
