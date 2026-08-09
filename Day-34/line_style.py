import matplotlib.pyplot as plt

tests = [1, 2, 3, 4, 5]
marks = [55, 62, 68, 75, 82]

plt.plot(
    tests,
    marks,
    color="blue",
    linewidth=3,
    linestyle="--"
)

plt.title("Student Marks Trend")
plt.xlabel("Test Number")
plt.ylabel("Marks")

plt.show()
