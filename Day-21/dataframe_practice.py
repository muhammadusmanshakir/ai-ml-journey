import pandas as pd

student = {
    "Name": ["Usman", "Ali", "Ahmed", "Sara"],
    "Age": [21, 22, 20, 23],
    "Marks": [88, 75, 91, 85]
}

df = pd.DataFrame(student)

print(df)

print("\nShape:")
print(df.shape)

print("\nNames:")
print(df["Name"])

print("\nThird Student:")
print(df.loc[2])

