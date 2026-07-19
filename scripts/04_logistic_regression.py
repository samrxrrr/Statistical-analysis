import pandas as pd
import numpy as np

import statsmodels.api as sm
from statsmodels.stats.contingency_tables import Table2x2

# -------------------------------------------------
# Load
# -------------------------------------------------

df = pd.read_csv("results/cleaned_dataset.csv")

# Scale dose
dose_map = {0:0,50:1,100:2}

df["Dose"] = df["Concentration"].map(dose_map)

# -------------------------------------------------
# Logistic Regression
# -------------------------------------------------

X = sm.add_constant(df["Dose"])

y = df["MUV_Binary"]

model = sm.Logit(y,X)

result = model.fit()

print(result.summary())

# Odds ratios

params = result.params

conf = result.conf_int()

OR = np.exp(params)

CI = np.exp(conf)

print("\nOdds Ratios")

print(pd.DataFrame({

"OR":OR,

"CI Lower":CI[0],

"CI Upper":CI[1]

}))

# Predicted probability

df["Predicted"] = result.predict(X)

df.to_csv("results/logistic_predictions.csv",index=False)

with open("reports/logistic_regression.txt","w") as f:

    f.write(result.summary().as_text())

print("\nDone.")
