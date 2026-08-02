import pandas as pd
data={
    "Name":["Ali","Ahmed","Sara","Usman","Bilal"],
    "Marks":[80,95,75,88,92]
}
df=pd.DataFrame(data)
print("Original df:")
print(df)
df["Rank"]=df["Marks"].rank(ascending=False).astype(int)
print("\nStudents Ranking:")
print(df)
