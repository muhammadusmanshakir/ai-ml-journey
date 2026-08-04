import pandas as pd

print("=" * 50)
print("     Department Performance Analyzer")
print("=" * 50)

# Create dataset
df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Usman", "Bilal", "Hania"],
    "Department": ["CS", "AI", "CS", "AI", "CS", "AI"],
    "Marks": [80, 90, 75, 88, 92, 85]
})

print("\nOriginal Dataset:")
print(df)

print("\nTotal Marks by Department:")
print(df.groupby("Department")["Marks"].sum())

print("\nAverage Marks by Department:")
print(df.groupby("Department")["Marks"].mean())

print("\nNumber of Students in Each Department:")
print(df.groupby("Department")["Name"].count())

print("\nHighest Marks in Each Department:")
print(df.groupby("Department")["Marks"].max())

print("\nLowest Marks in Each Department:")
print(df.groupby("Department")["Marks"].min())

print("\n" + "=" * 50)
print("Analysis Completed Successfully!")
print("=" * 50) 