import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": [
        "Ali", "Ahmed", "Usman", "Hassan",
        "Bilal", "Hamza", "Umar", "Zain",
        "Ahsan", "Talha", "Saad", "Owais"
    ],
    "Subject": [
        "Math", "Math", "Math", "Math",
        "Physics", "Physics", "Physics", "Physics",
        "Computer", "Computer", "Computer", "Computer"
    ],
    "Marks": [
        55, 62, 70, 78,
        60, 68, 75, 85,
        65, 72, 82, 90
    ]
}

df = pd.DataFrame(data)

print(df)

sns.histplot(
    data=df,
    x="Marks",
    hue="Subject",
    bins=6,
    kde=True
)

plt.title("Student Marks Distribution by Subject")
plt.xlabel("Marks")
plt.ylabel("Frequency")

plt.show()