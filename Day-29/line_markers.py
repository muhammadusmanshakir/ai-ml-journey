import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Usman"]
marks=[80,90,75,88]
plt.plot(students,marks,color="red",marker="o")
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

