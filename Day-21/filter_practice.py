import pandas as pd
students={
    "Name":["Ali","Ahmad","Usman","Sara","Ayesha"],
    "Age":[21,22,20,23,19],
    "Marks":[88,75,91,85,65]

}
df=pd.DataFrame(students)
print("Original Data:")
print(df)
print("\nStudents Scoring above 80:")
print(df[df["Marks"]>80])
print("\nStudents older than 20:")
print(df[df["Age"]>20])
print("\nName and Marks:")
print(df[["Name","Marks"]])
