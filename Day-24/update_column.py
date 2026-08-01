import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed"],
    "Marks":[80,90,75]
}

df=pd.DataFrame(data)
print("Original df:")
print(df)
df["Marks"]=df["Marks"]+5
print("\nAfter adding bonus marks:")
print(df)
