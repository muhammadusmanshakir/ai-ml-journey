import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS", "CS", "CS", "CS", "CS", "CS",
        "AI", "AI", "AI", "AI", "AI", "AI",
        "SE", "SE", "SE", "SE", "SE", "SE"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male", "Female"
    ],
    "Marks": [
        55, 65, 70, 78, 80, 95,
        60, 68, 75, 82, 88, 92,
        50, 62, 70, 76, 85, 98
    ]
}

df = pd.DataFrame(data)

print("Student Performance Data:")
print(df)

plt.figure(figsize=(8, 5))

sns.boxplot(
    data=df,
    x="Department",
    y="Marks",
    hue="Gender"
)

plt.title("Student Performance Distribution")
plt.xlabel("Department")
plt.ylabel("Marks")

plt.show()