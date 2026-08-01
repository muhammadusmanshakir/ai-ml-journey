import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed"],
    "Marks":[80,90,75]
}
df=pd.DataFrame(data)
print("Original df:")
print(df)
df.rename(columns={"Marks":"Score"},inplace=True)
print("\nAfter renaming:")
print(df)
