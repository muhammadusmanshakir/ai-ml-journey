import pandas as pd
import numpy as np
data={
    "City":["Lahore",np.nan,"Lahore","Karachi"]
}
df=pd.DataFrame(data)
df["City"]=df["City"].fillna(df["City"].mode()[0])
print(df)
