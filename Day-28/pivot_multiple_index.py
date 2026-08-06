import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Usman", "Hania"],
    "Department": ["CS", "AI", "CS", "AI", "CS"],
    "Gender": ["Male", "Female", "Male", "Male", "Female"],
    "Marks": [80, 90, 75, 88, 92]
})

print("Original Dataset:")
print(df)

pivot = pd.pivot_table(
    df,
    values="Marks",
    index=["Department", "Gender"],
    aggfunc="mean"
)

print("\nAverage Marks by Department and Gender:")
print(pivot)
