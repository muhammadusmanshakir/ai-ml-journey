import pandas as pd
import numpy as np
data={
    "Name":["Ali","Sara","Ahmad"],
    "Age":[20,np.nan,22],
    "Marks":[80,np.nan,90]
}
df=pd.DataFrame(data)
print(df)
print("\nMissing values count:")
print(df.isnull().sum())
