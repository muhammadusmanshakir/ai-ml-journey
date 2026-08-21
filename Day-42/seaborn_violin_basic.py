import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Marks": [
        55, 60, 62, 65, 68,
        70, 72, 75, 78, 80,
        82, 85, 88, 90, 92
    ]
}

df = pd.DataFrame(data)

print(df)

sns.violinplot(data=df, y="Marks")

plt.title("Student Marks Distribution")
plt.ylabel("Marks")

plt.show()