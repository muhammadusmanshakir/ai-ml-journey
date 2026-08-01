import pandas as pd
data={
    "Name":["Ali","Sara","Ahmed"],
    "Marks":[80,90,75]
}

df=pd.DataFrame(data)
print("Original Dataframe:")
print(df)
df["Grade"]=['B','A','C']
print("\nAfter adding grade column:")
print(df)

