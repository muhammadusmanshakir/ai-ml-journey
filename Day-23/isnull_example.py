import pandas as pd
import numpy as np
data={
    "Name":["Ali","Sara","Ahmad"],
    "Marks":[80,np.nan,90]
}
df=pd.DataFrame(data)
print(df)
print("\nMissing values:")
print(df.isnull())
