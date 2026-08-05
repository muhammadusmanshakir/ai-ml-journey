import pandas as pd

students = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Name": ["Ali", "Sara", "Ahmed"]
})

marks = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Marks": [80, 90, 75, 88]
})

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)

right = pd.merge(students, marks, on="StudentID", how="right")

print("\nRight Join Result:")
print(right)
