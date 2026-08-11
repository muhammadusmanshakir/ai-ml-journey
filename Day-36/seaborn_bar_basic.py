import seaborn as sns
import matplotlib.pyplot as plt
subjects=["Math","Physics","Computer","English"]
marks=[75,82,90,78]
sns.barplot(x=subjects,y=marks)
plt.title("Student Subject Marks")
plt.xlabel("Subjects")
plt.ylabel("Marks")

plt.show()
