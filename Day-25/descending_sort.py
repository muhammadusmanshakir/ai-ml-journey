import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed","Usman"],
    "Marks":[80,95,75,88]
}
df=pd.DataFrame(data)
print("Original df:")
print(df)

print("\nSorted marks(descending):")
print(df.sort_values("Marks",ascending=False))

