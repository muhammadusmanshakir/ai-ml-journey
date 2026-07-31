import pandas as pd

print("=" * 50)
print("      Student CSV Analyzer")
print("=" * 50)

df = pd.read_csv("students.csv")

print("\nComplete Dataset:")
print(df)

print("\nFirst Five Students:")
print(df.head())

print("\nLast Three Students:")
print(df.tail(3))

print("\nRandom Two Students:")
print(df.sample(2))

print("\nDataset Information:")
df.info()

print("\nStatistical Summary:")
print(df.describe())
