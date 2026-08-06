import matplotlib.pyplot as plt

# Student Data
students = ["Ali", "Sara", "Ahmed", "Usman", "Bilal", "Hania"]
marks = [80, 95, 75, 88, 92, 85]

print("=" * 55)
print("     Student Performance Visualization")
print("=" * 55)

print("\nStudents:")
print(students)

print("\nMarks:")
print(marks)

# Create Line Graph
plt.plot(
    students,
    marks,
    color="blue",
    marker="o",
    linestyle="--"
)

# Title
plt.title("Student Performance")

# Axis Labels
plt.xlabel("Students")
plt.ylabel("Marks")

# Grid
plt.grid(True)

# Show Graph
plt.show()

print("\n" + "=" * 55)
print("Graph Generated Successfully!")
print("=" * 55)