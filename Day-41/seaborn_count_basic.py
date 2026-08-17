import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Class": [
        "First",
        "Second",
        "Third",
        "First",
        "Third",
        "Second",
        "Third",
        "First",
        "Third",
        "Second"
    ]
}

df = pd.DataFrame(data)

print(df)

sns.countplot(data=df, x="Class")

plt.title("Passenger Count by Class")
plt.xlabel("Class")
plt.ylabel("Number of Passengers")

plt.show()