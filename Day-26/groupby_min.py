import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed","Usman"],
    "Department":["CS","AI","CS","AI"],
    "Marks":[80,90,75,88]
}
df=pd.DataFrame(data)
print("Original Dataset:")
print(df)
print("\nLowest Marks in each department:")
print(df.groupby("Department")["Marks"].min())

