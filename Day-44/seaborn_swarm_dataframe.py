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
        65, 70, 72, 78, 80,
        60, 68, 75, 82, 88,
        55, 62, 70, 76, 85
    ]
}

df = pd.DataFrame(data)

print(df)

sns.swarmplot(
    data=df,
    x="Department",
    y="Marks"
)

plt.title("Student Marks by Department")
plt.xlabel("Department")
plt.ylabel("Marks")

plt.show()