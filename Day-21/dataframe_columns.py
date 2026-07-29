import pandas as pd
data={
    "Name":["Ahmad","Ali","Usman"],
    "Age":[20,21,22],
    "Marks":[80,75,92]
}

df=pd.DataFrame(data)
print("Names")
print(df["Name"])
print("\nMarks:")
print(df["Marks"])

