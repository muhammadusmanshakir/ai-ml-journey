import pandas as pd
import numpy as np
data={
    "Name":["Ali","Sara","Ahmed"],
    "Marks":[80,np.nan,90]
}
df=pd.DataFrame(data)
print(df.fillna(0))

