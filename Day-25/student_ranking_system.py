import pandas as pd
import pandas as pd

print("=" * 50)
print("      Student Ranking System")
print("=" * 50)

# Create DataFrame
df = pd.DataFrame({
    "Name": ["Ali", "Ahmed", "Sara", "Usman", "Bilal", "Hania"],
    "Marks": [80, 95, 75, 88, 92, 85]
})

print("\nOriginal Dataset:")
print(df)

# Sort Ascending
print("\nSorted by Marks (Ascending):")
print(df.sort_values("Marks"))

# Sort Descending
print("\nSorted by Marks (Descending):")
print(df.sort_values("Marks", ascending=False))

# Top Students
print("\nTop 3 Students:")
print(df.nlargest(3, "Marks"))

# Lowest Students
print("\nLowest 2 Students:")
print(df.nsmallest(2, "Marks"))

# Ranking
df["Rank"] = df["Marks"].rank(ascending=False).astype(int)

print("\nStudent Rankings:")
print(df.sort_values("Rank"))

# Sort Back by Index
print("\nSorted by Original Index:")
print(df.sort_index())

print("\n" + "=" * 50)
print("      Analysis Completed Successfully!")
print("=" * 50)
