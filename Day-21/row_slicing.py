import pandas as pd
data={
    "Name":["Ali","Ahmad","Usman","Ayesha","Sara"],
    "Marks":[80,75,92,88,95]
}

df=pd.DataFrame(data)
print(df[1:4])
