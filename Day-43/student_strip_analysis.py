import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS", "CS", "CS", "CS", "CS",
        "AI", "AI", "AI", "AI", "AI",
        "SE", "SE", "SE", "SE", "SE"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female", "Male",
        "Female", "Male", "Female", "Male", "Female",
        "Male", "Female", "Male", "Female", "Male"
    ],
    "Marks": [
        55, 65, 70, 78, 85,
        60, 68, 74, 82, 90,
        58, 64, 72, 80, 88
    ]
}

df = pd.DataFrame(data)

print("Student Performance Data:")
print(df)

plt.figure(figsize=(8, 5))

sns.stripplot(
    data=df,
    x="Department",
    y="Marks",
    hue="Gender",
    jitter=True,
    dodge=True
)

plt.title("Student Performance by Department and Gender")
plt.xlabel("Department")
plt.ylabel("Marks")

plt.show()