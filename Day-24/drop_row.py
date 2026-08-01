import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed"],
    "Age":[20,21,22],
    "Marks":[80,90,75]
}
df=pd.DataFrame(data)
print("Original df:")
print(df)
df=df.drop(index=1)
print("After dropping row:")
print(df)
