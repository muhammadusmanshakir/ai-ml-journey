import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Usamn"]
marks=[80,95,75,88]
bars=plt.bar(students,marks,color="green")
for bar in bars:
    height=bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )

plt.title("Student Marks")
plt.xlabel("Students")
plt.ylabel("Marks")

plt.show()