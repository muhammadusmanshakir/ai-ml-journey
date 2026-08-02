import pandas as pd

df = pd.DataFrame({
    "Name": ["Ali", "Sara", "Ahmed", "Usman"],
    "Marks": [80, 95, 75, 88]
})

# First sort by marks
sorted_df = df.sort_values("Marks")

print("Sorted by Marks:")
print(sorted_df)

print("\nSorted by Index:")
print(sorted_df.sort_index())

