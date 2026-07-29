import pandas as pd

print("=" * 50)
print("      Student Performance Filter")
print("=" * 50)

students = {
    "Name": ["Ali", "Ahmed", "Usman", "Sara", "Ayesha", "Bilal"],
    "Age": [20, 21, 22, 20, 23, 21],
    "Marks": [80, 75, 92, 88, 95, 67]
}

df = pd.DataFrame(students)

print("\nComplete Student Data:")
print(df)

print("\nTop Scorers (Marks > 85):")
print(df[df["Marks"] > 85])

print("\nStudents Age > 20:")
print(df[df["Age"] > 20])

print("\nSelected Columns:")
print(df[["Name", "Marks"]])

print("\nFirst Three Students:")
print(df.iloc[:3])

print("\nLast Two Students:")
print(df.iloc[-2:])
