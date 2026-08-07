import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Usman"]
marks=[80,95,70,50]
plt.bar(students,marks,color="green",width=0.4)
plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")
plt.show()

