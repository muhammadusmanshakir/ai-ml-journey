import pandas as pd

students = pd.DataFrame({
    "StudentID": [1, 2, 3, 4],
    "Name": ["Ali", "Sara", "Ahmed", "Usman"]
})

marks = pd.DataFrame({
    "StudentID": [1, 2, 3],
    "Marks": [80, 90, 75]
})

print("Students DataFrame:")
print(students)

print("\nMarks DataFrame:")
print(marks)

left=pd.merge(students,marks,on="StudentID",how="left")
print("\nLeft Join result:")
print(left)
