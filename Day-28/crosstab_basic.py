import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Usman", "Hania"],
    "Department": ["CS", "AI", "CS", "AI", "CS"],
    "Gender": ["Male", "Female", "Male", "Male", "Female"]
})

print("Original Dataset:")
print(df)
table=pd.crosstab(
    df["Department"],
    df["Gender"]
)
print("\nDepartment vs Gender:")
print(table)
