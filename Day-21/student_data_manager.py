import pandas as pd

students = {
    "Name": ["Ali", "Ahmed", "Usman", "Sara", "Ayesha"],
    "Age": [20, 21, 22, 20, 23],
    "Marks": [80, 75, 92, 88, 95]
}

df = pd.DataFrame(students)

print("=" * 50)
print("      Student Data Manager")
print("=" * 50)

print("\nStudent Data:")
print(df)

print("\nShape:")
print(df.shape)

print("\nStudent Names:")
print(df["Name"])

print("\nMarks:")
print(df["Marks"])

print("\nFirst Student:")
print(df.loc[0])

print("\nLast Student:")
print(df.loc[4])
