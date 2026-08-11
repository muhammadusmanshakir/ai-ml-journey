import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["Ali", "Ahmed", "Usman", "Hassan", "Bilal", "Hamza"],
    "Subject": ["Math", "Math", "Physics", "Physics", "Computer", "Computer"],
    "Marks": [78, 85, 72, 88, 91, 84]
}

df = pd.DataFrame(data)

print(df)

sns.barplot(
    data=df,
    x="Subject",
    y="Marks"
)

plt.title("Student Performance by Subject")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()