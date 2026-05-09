import pandas as pd
import matplotlib.pyplot as plt

# Read cleaned dataset
df = pd.read_excel(
    "cleaned_ecommerce_dataset.xlsx",
    engine="openpyxl"
)

# Different colors
colors = [
    "skyblue",
    "lightgreen",
    "orange",
    "violet",
    "gold",
    "pink",
    "cyan",
    "salmon",
    "turquoise",
    "plum"
]

# Figure size
plt.figure(figsize=(12,7))

# Horizontal bar chart
plt.barh(
    df["Product"],
    df["Sales"],
    color=colors
)

# Labels and title
plt.xlabel("Sales")
plt.ylabel("Products")
plt.title("E-Commerce Product Sales Analysis")

# Grid
plt.grid(axis='x', linestyle='--', alpha=0.5)

# Save graph
plt.savefig("ecommerce_bar_chart.png")

# Show graph
plt.show()