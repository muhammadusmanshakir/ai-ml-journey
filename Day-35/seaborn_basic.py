import seaborn as sns
import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[10,15,12,20,18]
sns.lineplot(x=x,y=y)
plt.title("My First Seaborn Line Plot")
plt.xlabel("Days")
plt.ylabel("Values")

plt.show()
