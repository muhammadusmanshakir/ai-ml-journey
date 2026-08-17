import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS",
        "AI",
        "CS",
        "SE",
        "AI",
        "CS",
        "SE",
        "AI"
    ]
}

df = pd.DataFrame(data)

print(df)

sns.countplot(data=df, x="Department")

plt.title("Students by Department")
plt.show()