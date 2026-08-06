import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Hania"],
    "Department": ["CS", "AI", "CS"],
    "Gender": ["Male", "Female", "Female"],
    "Marks": [80, 90, 92]
})

print("Original Dataset:")
print(df)
pivot=pd.pivot_table(
    df,
    values="Marks",
    index=["Department","Gender"]
   # columns="Gender",
    aggfunc="mean",
    fill_value=0
)
print("\nPivot Table with fill_value:")
print(pivot)
