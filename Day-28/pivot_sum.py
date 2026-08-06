import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Usman"],
    "Department": ["CS", "AI", "CS", "AI"],
    "Marks": [80, 90, 75, 88]
})

print("Original Dataset:")
print(df)
pivot=pd.pivot_table(
    df,
    values="Marks",
    index="Department",
    aggfunc="sum"
)
print("\nTotal marks of each department:")
print(pivot)
