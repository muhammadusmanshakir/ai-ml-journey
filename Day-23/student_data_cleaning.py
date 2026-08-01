import pandas as pd
import numpy as np

print("=" * 50)
print("      Student Data Cleaning System")
print("=" * 50)

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Usman", "Ayesha"],
    "Age": [20, np.nan, 21, 22, np.nan],
    "Marks": [80, 90, np.nan, 88, 95]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")

print(df)

print("\nMissing Values:")

print(df.isnull())

print("\nMissing Values Count:")

print(df.isnull().sum())

print("\nFill Missing Ages with Mean")

df["Age"] = df["Age"].fillna(df["Age"].mean())

print(df)

print("\nFill Missing Marks with Mean")

df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)

print("\nDataset after Cleaning")

print(df)