import pandas as pd
import numpy as np
data={
    "Marks":[80,np.nan,90,100]
}
df=pd.DataFrame(data)
df["Marks"]=df["Marks"].fillna(df["Marks"].mean())

print(df)
