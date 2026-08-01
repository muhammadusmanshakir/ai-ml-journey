import pandas as pd

print("=" * 50)
print("      Student Grade Management System")
print("=" * 50)

# Create DataFrame
data = {
    "Name": ["Ali", "Sara", "Ahmed", "Usman"],
    "Age": [20, 21, 22, 23],
    "Marks": [80, 90, 75, 88]
}

df = pd.DataFrame(data)

print("\nOriginal Dataset:")
print(df)

#Add grade column
df["Grade"]=['B','A','C','A']
print("\nAfter Adding Grade Column:")
print(df)

# Add bonus marks
df["Marks"] = df["Marks"] + 5

print("\nAfter Adding Bonus Marks:")
print(df)

# Rename Marks column
df.rename(columns={"Marks": "Score"}, inplace=True)

print("\nAfter Renaming Marks to Score:")
print(df)

# Drop Age column
df = df.drop(columns=["Age"])

print("\nAfter Dropping Age Column:")
print(df)

# Drop second row (Sara)
df = df.drop(index=1)

print("\nAfter Dropping Sara:")
print(df)