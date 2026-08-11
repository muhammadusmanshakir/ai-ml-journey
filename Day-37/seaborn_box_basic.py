import seaborn as sns
import matplotlib.pyplot as plt

marks = [55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 95]

sns.boxplot(y=marks)

plt.title("Student Marks Distribution")
plt.ylabel("Marks")

plt.show()