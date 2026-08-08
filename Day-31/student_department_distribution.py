import matplotlib.pyplot as plt

departments = ["AI", "CS", "SE", "IT"]
students = [30, 40, 20, 10]

colors = ["red", "green", "blue", "orange"]
explode = [0, 0.1, 0, 0]

print("=" * 55)
print("     Student Department Distribution")
print("=" * 55)

print("\nDepartments:")
print(departments)

print("\nNumber of Students:")
print(students)

plt.pie(
    students,
    labels=departments,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Student Distribution by Department")

plt.axis("equal")

plt.show()

print("\n" + "=" * 55)
print("Distribution Chart Generated Successfully!")
print("=" * 55)