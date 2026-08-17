import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS", "AI", "CS", "SE",
        "AI", "CS", "SE", "AI",
        "CS", "SE"
    ],
    "Gender": [
        "Male", "Female", "Female", "Male",
        "Male", "Male", "Female", "Female",
        "Male", "Male"
    ]
}

df = pd.DataFrame(data)

print(df)

sns.countplot(
    data=df,
    x="Department",
    hue="Gender"
)

plt.title("Students by Department and Gender")
plt.show()