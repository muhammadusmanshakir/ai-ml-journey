import pandas as pd
data={
    "Name":["Ali","Ahmad","Usman","Sara"],
    "Marks":[80,75,92,88]
}
df=pd.DataFrame(data)
print(df[df["Marks"]>80])

