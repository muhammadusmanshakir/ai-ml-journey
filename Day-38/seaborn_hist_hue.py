import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": [
        "Math", "Math", "Math", "Math",
        "Physics", "Physics", "Physics", "Physics"
    ],
    "Marks": [
        60, 68, 75, 82,
        55, 65, 72, 88
    ]
}

df = pd.DataFrame(data)

print(df)

sns.histplot(
    data=df,
    x="Marks",
    hue="Subject",
    bins=5,
    kde=True
)

plt.title("Marks Distribution by Subject")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()