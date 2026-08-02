import pandas as pd
data={
    "Name":["Ali","Ahmed","Sara","Usman","Bilal"],
    "Marks":[80,95,75,88,92]
}
df=pd.DataFrame(data)
print("Original dataframe:")
print(df)
print("\nTop 2 students:")
print(df.nlargest(2,"Marks"))
print("\nLowest 2 students:")
print(df.nsmallest(2,"Marks"))

