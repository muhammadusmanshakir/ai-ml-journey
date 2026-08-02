import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed","Usman"],
    "Marks":[80,95,75,88]
}
df=pd.DataFrame(data)
print("Original data:")
print(df)
print("\nSorted by marks(ascending):")
print(df.sort_values("Marks"))
