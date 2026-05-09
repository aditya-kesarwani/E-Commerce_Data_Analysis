import pandas as pd
import numpy as np

# Read Excel file
df = pd.read_excel("ecommerce_dataset.xlsx", engine="openpyxl")

# Print original dataset
print("Original Dataset:\n")
print(df)

# Check missing values
print("\nMissing Values:\n")
print(df.isnull().sum())

# Fill missing values with average
df["Price"].fillna(df["Price"].mean(), inplace=True)
df["Quantity"].fillna(df["Quantity"].mean(), inplace=True)
df["Rating"].fillna(df["Rating"].mean(), inplace=True)
df["Sales"].fillna(df["Sales"].mean(), inplace=True)

# Print cleaned dataset
print("\nCleaned Dataset:\n")
print(df)

# NumPy calculations
average_sales = np.mean(df["Sales"])
maximum_sales = np.max(df["Sales"])
minimum_sales = np.min(df["Sales"])

print("\nAverage Sales:", average_sales)
print("Maximum Sales:", maximum_sales)
print("Minimum Sales:", minimum_sales)

# Save cleaned dataset
df.to_excel("cleaned_ecommerce_dataset.xlsx", index=False)

print("\nCleaned Excel dataset saved successfully!")