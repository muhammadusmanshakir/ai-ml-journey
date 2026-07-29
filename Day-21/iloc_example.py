import pandas as pd
data={
    "Name":["Ali","Ahmad","Usman"],
    "Age":[20,21,22],
    "Marks":[80,75,92]
}
df=pd.DataFrame(data)

print(df.iloc[0])
print()
print(df.iloc[2])
