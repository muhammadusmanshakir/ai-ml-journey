import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
data={
    "Days":[1,2,3,4,5],
    "Marks":[60,65,70,75,80]
}

df=pd.DataFrame(data)
print(df)
sns.lineplot(data=df,x="Days",y="Marks")
plt.title("Student Performance")
plt.xlabel("Day")
plt.ylabel("Marks")

plt.show()