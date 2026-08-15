import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Study_Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [55, 60, 65, 70, 75, 80, 85, 90],
    "Assignments": [2, 3, 4, 5, 6, 7, 8, 9],
    "Marks": [50, 55, 61, 66, 72, 78, 85, 92]
}

df = pd.DataFrame(data)

print("Student Performance Data:")
print(df)

correlation = df.corr()

print("\nCorrelation Matrix:")
print(correlation)

sns.heatmap(
    correlation,
    annot=True,
    cmap="coolwarm",
    fmt=".2f",
    linewidths=0.5
)

plt.title("Student Performance Correlation Heatmap")
plt.show()