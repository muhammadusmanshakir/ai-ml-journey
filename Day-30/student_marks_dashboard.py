import matplotlib.pyplot as plt
students=["Ali","Sara","Ahmed","Usman","Bilal","Hania"]
marks=[80,95,75,88,12,100]
colors=["red","green","blue","orange","purple","cyan"]
print("=" * 55)
print("      Student Marks Dashboard")
print("=" * 55)

print("\nStudents:")
print(students)

print("\nMarks:")
print(marks)
bars=plt.bar(students,marks,color=colors,width=0.4)
for bar in bars:
    height=bar.get_height()
    plt.text(
        bar.get_x()+bar.get_width()/2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )


plt.title("Student Marks Comparison")
plt.xlabel("Students")
plt.ylabel("Marks")

#plt.grid(axis="y")

plt.show()

print("\n" + "=" * 55)
print("Dashboard Generated Successfully!")
print("=" * 55)
