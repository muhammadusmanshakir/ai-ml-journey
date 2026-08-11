import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
data={
    "Subject":["Math","English","Physics","Computer"],
    "Marks":[20,75,85,90]
}
df=pd.DataFrame(data)
print(df)
sns.barplot(data=df,x="Subject",y="Marks")
plt.title("Subject-wise Marks")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()
