import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Usman"]
marks=[80,90,70,65]
plt.plot(students,marks,color="green",marker="o",linestyle="--")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.grid(True)
plt.show()