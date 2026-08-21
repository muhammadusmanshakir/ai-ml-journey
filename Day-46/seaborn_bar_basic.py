import seaborn as sns
import matplotlib.pyplot as plt

categories = ["CS", "AI", "SE"]
values = [78, 82, 74]

sns.barplot(x=categories, y=values)

plt.title("Average Marks by Department")
plt.xlabel("Department")
plt.ylabel("Average Marks")

plt.show()