import matplotlib.pyplot as plt

marks = [
    45, 52, 55, 61, 63, 67, 70, 72, 75, 78,
    81, 83, 85, 88, 90, 92, 95,
    56, 64, 69, 73, 77, 82, 86, 91
]

print("=" * 55)
print("       Student Marks Distribution")
print("=" * 55)

print("\nTotal Students:", len(marks))
print("Marks:", marks)

plt.hist(
    marks,
    bins=6,
    color="skyblue",
    edgecolor="black",
    alpha=0.7
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.grid(axis="y")

plt.show()

print("\n" + "=" * 55)
print("       Histogram Generated Successfully!")
print("=" * 55)