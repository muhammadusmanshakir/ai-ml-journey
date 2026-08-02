import pandas as pd
data={
    "Name":["Ali","Ahmed","Sara","Hooria","Hania"],
    "Department":["CS","AI","CS","AI","CS"],
    "Marks":[80,95,75,88,92]  
}
df=pd.DataFrame(data)
print("Original dataframe:")
print(df)
print("\nSorted by department and marks:")
print(df.sort_values(by=["Department","Marks"]))
