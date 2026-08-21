import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS", "CS", "CS", "CS", "CS",
        "AI", "AI", "AI", "AI", "AI",
        "SE", "SE", "SE", "SE", "SE"
    ],
    "Marks": [
        55, 65, 70, 75, 85,
        60, 68, 72, 80, 90,
        58, 64, 70, 78, 88
    ]
}

df = pd.DataFrame(data)

print("Student Performance Data:")
print(df)

plt.figure(figsize=(8, 5))

sns.violinplot(
    data=df,
    x="Department",
    y="Marks",
    inner="box"
)

plt.title("Student Marks Distribution by Department")
plt.xlabel("Department")
plt.ylabel("Marks")

plt.show()