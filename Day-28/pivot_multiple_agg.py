import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Usman", "Bilal"],
    "Department": ["CS", "AI", "CS", "AI", "CS"],
    "Marks": [80, 90, 75, 88, 92]
})

print("Original Dataset:")
print(df)
pivot=pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    aggfunc=["mean","sum","max","min"]
)
print("\nDepartment Statistics:")
print(pivot)
