import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed"],
    "Age":[20,21,22],
    "Marks":[80,90,75]
}
df=pd.DataFrame(data)
print("Original dataframe:")
print(df)
df=df.drop(columns=["Age"])
print("\nAfter dropping Age column:")
print(df)
