import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90],
    "Assignments": [3, 4, 5, 6, 7, 8, 9],
    "Marks": [55, 60, 65, 72, 78, 85, 90]
}

df = pd.DataFrame(data)

correlation = df.corr()

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Student Performance Correlation")

plt.show()