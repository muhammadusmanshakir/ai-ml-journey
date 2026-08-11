import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": [
        "Ali", "Ahmed", "Usman", "Hassan",
        "Bilal", "Hamza", "Umar", "Zain"
    ],
    "Subject": [
        "Math", "Math", "Physics", "Physics",
        "Computer", "Computer", "English", "English"
    ],
    "Marks": [
        65, 85, 72, 88,
        91, 84, 70, 78
    ]
}

df = pd.DataFrame(data)

print(df)

sns.boxplot(
    data=df,
    x="Subject",
    y="Marks"
)

plt.title("Student Marks Distribution by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()