import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": ["CS", "AI", "SE"],
    "Marks": [78, 82, 74]
}

df = pd.DataFrame(data)

print(df)

sns.barplot(
    data=df,
    x="Department",
    y="Marks"
)

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Marks")

plt.show()