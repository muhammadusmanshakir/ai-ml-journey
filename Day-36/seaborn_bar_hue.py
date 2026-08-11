import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Subject": ["Math", "Math", "Physics", "Physics",
                "Computer", "Computer"],
    "Gender": ["Male", "Female", "Male", "Female",
               "Male", "Female"],
    "Marks": [75, 82, 80, 85, 90, 88]
}

df = pd.DataFrame(data)

print(df)
sns.barplot(data=df,x="Subject",y="Marks",hue="Gender")
plt.title("Subject Marks by Gender")
plt.xlabel("Subject")
plt.ylabel("Marks")

plt.show()