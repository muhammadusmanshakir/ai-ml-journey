import pandas as pd
import numpy as np

data = {
    "Name": ["Ali", "Sara", "Ahmed", "Usman"],
    "Age": [20, np.nan, 21, 22],
    "Marks": [80, 90, np.nan, 88]
}

df = pd.DataFrame(data)

print("Original Dataset")

print(df)

print("\nMissing Values")

print(df.isnull())

print("\nMissing Count")

print(df.isnull().sum())

print("\nFilled with Zero")

print(df.fillna(0))
