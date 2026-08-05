import pandas as pd
students=pd.DataFrame({
    "StudentId":[1,2,3],
    "Name":["Ali","Sara","Ahmed"]
})
marks=pd.DataFrame({
    "StudentId":[1,2,3],
    "Marks":[80,90,75]
})
print("Students data frame:")
print(students)
print("\nMarks data frame:")
print(marks)
merged=pd.merge(students,marks,on="StudentId")
print("\nMerged data frame:")
print(merged)
