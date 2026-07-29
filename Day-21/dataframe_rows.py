import pandas as pd
data={
    "Name":["Ali","Ahmad","Usman"],
    "Age":[20,21,22],
    "Marks":[80,75,92]
}

df=pd.DataFrame(data)
print("First Row:")
print(df.loc[0])
print("\nSecond Row:")
print(df.loc[1])
print("\nThird Row:")
print(df.loc[2])

