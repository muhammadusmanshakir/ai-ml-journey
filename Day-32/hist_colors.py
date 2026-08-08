import matplotlib.pyplot as plt

marks = [45, 52, 55, 61, 63, 67, 70, 72, 75, 78,
         81, 83, 85, 88, 90, 92, 95]

plt.hist(
    marks,
    bins=5,
    color="skyblue"
)

plt.title("Student Marks Distribution")
plt.xlabel("Marks")
plt.ylabel("Number of Students")

plt.show()