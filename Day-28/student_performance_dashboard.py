import pandas as pd

print("=" * 55)
print("      Student Performance Dashboard")
print("=" * 55)

# Student dataset
df = pd.DataFrame({
    "Name": [
        "Ali", "Sara", "Ahmed",
        "Usman", "Hania", "Bilal"
    ],
    "Department": [
        "CS", "AI", "CS",
        "AI", "CS", "AI"
    ],
    "Gender": [
        "Male", "Female", "Male",
        "Male", "Female", "Male"
    ],
    "Marks": [
        80, 90, 75,
        88, 92, 85
    ]
})

print("\nOriginal Dataset:")
print(df)

# Average Marks
print("\nAverage Marks by Department:")
average = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    aggfunc="mean"
)
print(average)

# Multiple statistics
print("\nDepartment Statistics:")
stats = pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    aggfunc=["mean", "sum", "max", "min"]
)
print(stats)

# Crosstab
print("\nDepartment vs Gender:")
table = pd.crosstab(
    df["Department"],
    df["Gender"]
)
print(table)

print("\n" + "=" * 55)
print("Dashboard Generated Successfully!")
print("=" * 55)
