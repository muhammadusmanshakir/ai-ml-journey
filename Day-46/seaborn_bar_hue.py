import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS", "CS", "CS", "CS",
        "AI", "AI", "AI", "AI",
        "SE", "SE", "SE", "SE"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female"
    ],
    "Marks": [
        65, 72, 78, 80,
        60, 70, 82, 88,
        55, 68, 76, 85
    ]
}

df = pd.DataFrame(data)

print(df)

sns.barplot(
    data=df,
    x="Department",
    y="Marks",
    hue="Gender"
)

plt.title("Average Marks by Department and Gender")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.show()