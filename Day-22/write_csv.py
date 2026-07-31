import pandas as pd
data={
    "Name":["Ali","Sara","Usman"],
    "Marks":[80,90,95]
}

df=pd.DataFrame(data)
df.to_csv("students_output.csv",index=False)
print("CSV file saved successfully")

