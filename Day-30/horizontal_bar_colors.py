import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Usman"]
marks=[80,95,75,30]
colors=["red","green","blue","orange"]
plt.barh(students,marks,color=colors)
plt.title("Student Marks")
plt.xlabel("Marks")
plt.ylabel("Students")

plt.show()
