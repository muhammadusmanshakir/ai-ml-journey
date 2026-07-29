import pandas as pd
data={
    "Name":["Ali","Ahmad","Usman","Sara"],
    "Age":[20,21,22,19],
    "Marks":[80,75,92,88]
}

df=pd.DataFrame(data)
result=df[(df["Marks"]>80)&(df["Age"]>20)]
print(result)
