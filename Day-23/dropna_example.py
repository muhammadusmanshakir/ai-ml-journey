import pandas as pd
import numpy as np
data={
    "Name":["Ali","Sara","Ahmad"],
    "Marks":[80,np.nan,90]
}
df=pd.DataFrame(data)
print("Original df:")
print(df)
print("\nAfter dropna():")
print(df.dropna())
