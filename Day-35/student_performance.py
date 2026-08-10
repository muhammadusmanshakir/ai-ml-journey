import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Create student performance data
data = {
    "Days": [1, 2, 3, 4, 5, 6, 7],
    "Marks": [55, 60, 65, 72, 68, 80, 88]
}

# Create DataFrame
df = pd.DataFrame(data)

# Display the data
print(df)
sns.set_theme()
sns.lineplot(data=df,x="Days",y="Marks",marker="o")
plt.title("Student Performance Over 7 Days")
plt.xlabel("Days")
plt.ylabel("Marks")

# Display graph
plt.show()
