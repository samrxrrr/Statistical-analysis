import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.graphics.mosaicplot import mosaic

# Load data
df = pd.read_csv("results/cleaned_dataset.csv")

# Convert binary labels
df["MUV"] = df["MUV_Binary"].map({
    1: "Present",
    0: "Absent"
})

# Create figure and axes
fig, ax = plt.subplots(figsize=(8, 6))

# Draw mosaic plot on the existing axes
mosaic(
    df,
    ["Concentration", "MUV"],
    ax=ax
)

# Title
ax.set_title("Treatment vs Multivulva Phenotype")

# Improve layout
fig.tight_layout()

# Save figure
fig.savefig(
    "figures/Figure8_Mosaic.png",
    dpi=600,
    bbox_inches="tight"
)

# Close figure (prevents blank windows)
plt.close(fig)

print("Mosaic plot saved.")
