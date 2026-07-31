import pandas as pd

df = pd.read_csv("students.csv")

print("First 3 Rows:")
print(df.head(3))

print("\nLast 2 Rows:")
print(df.tail(2))

print("\nRandom Student:")
print(df.sample(1))

print("\nDataset Info:")
df.info()

print("\nStatistics:")
print(df.describe())
