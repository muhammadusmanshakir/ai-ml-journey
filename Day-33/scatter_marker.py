import matplotlib.pyplot as plt

study_hours = [1, 2, 3, 4, 5, 6, 7]
marks = [45, 50, 58, 65, 72, 80, 85]

plt.scatter(
    study_hours,
    marks,
    color="blue",
    s=100,
    marker="s"
)

plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.show()