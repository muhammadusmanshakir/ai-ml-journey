import seaborn as sns
import matplotlib.pyplot as plt

marks = [55, 60, 62, 65, 68, 70, 72, 75, 78, 80, 85, 90, 92, 95]

sns.histplot(marks)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()