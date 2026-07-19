import pandas as pd
import matplotlib.pyplot as plt

# Load data
df = pd.read_csv("results/cleaned_dataset.csv")

# Frequency table
table = pd.crosstab(
    df["Ectopic_Vulva"],
    df["Concentration"]
)

plt.figure(figsize=(6,4))

plt.imshow(
    table,
    aspect="auto",
    interpolation="nearest"
)

plt.colorbar(label="Number of Worms")

plt.xticks(
    range(len(table.columns)),
    table.columns
)

plt.yticks(
    range(len(table.index)),
    table.index
)

plt.xlabel("Thymoquinone (µM)")
plt.ylabel("Severity Score")
plt.title("Severity Distribution Across Treatment Groups")

plt.tight_layout()

plt.savefig(
    "figures/Figure7_Heatmap.png",
    dpi=600
)

plt.show()

print("Heatmap saved.")
