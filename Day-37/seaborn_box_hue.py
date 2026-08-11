import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": [
        "Math", "Math", "Math", "Math",
        "Physics", "Physics", "Physics", "Physics"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female"
    ],
    "Marks": [
        65, 72, 75, 80,
        60, 70, 74, 85
    ]
}

df = pd.DataFrame(data)

print(df)

sns.boxplot(
    data=df,
    x="Subject",
    y="Marks",
    hue="Gender"
)

plt.title("Marks Distribution by Subject and Gender")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()