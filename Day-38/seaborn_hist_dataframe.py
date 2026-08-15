import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Student": ["Ali", "Ahmed", "Usman", "Hassan", "Bilal",
                "Hamza", "Umar", "Zain", "Ahsan", "Talha"],
    "Marks": [55, 60, 65, 68, 70, 72, 75, 80, 88, 92]
}

df = pd.DataFrame(data)

print(df)

sns.histplot(
    data=df,
    x="Marks"
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()