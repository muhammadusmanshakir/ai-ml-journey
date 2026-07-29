import pandas as pd
data={
    "Name":["Ali","Ahmad","Usman"],
    "Age":[20,21,22],
    "Marks":[80,75,92]
}
df=pd.DataFrame(data)
print(df)

print("\nShape:")
print(df.shape)
print("\nColumns:")
print(df.columns)
print("\nIndex:")
print(df.index)
print("\nData Types:")
print(df.dtypes)
