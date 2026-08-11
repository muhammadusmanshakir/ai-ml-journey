import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": [
        "Math", "Math", "Math", "Math",
        "Physics", "Physics", "Physics", "Physics"
    ],
    "Marks": [
        65, 70, 75, 80,
        60, 68, 72, 85
    ]
}

df = pd.DataFrame(data)

print(df)

sns.boxplot(
    data=df,
    x="Subject",
    y="Marks"
)

plt.title("Marks Distribution by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()