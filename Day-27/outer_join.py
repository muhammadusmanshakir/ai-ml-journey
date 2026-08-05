import pandas as pd

students = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Ahmed"]
})

marks = pd.DataFrame({
    "StudentID": [2, 3, 4],
    "Marks": [90, 75, 88]
})

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)

outer = pd.merge(students, marks, on="StudentID", how="outer")

print("\nOuter Join Result:")
print(outer)
