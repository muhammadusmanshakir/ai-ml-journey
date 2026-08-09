import matplotlib.pyplot as plt

tests = [1, 2, 3, 4, 5]

cs_marks = [55, 62, 68, 75, 82]
ai_marks = [60, 65, 70, 78, 88]

plt.plot(
    tests,
    cs_marks,
    color="blue",
    linewidth=3,
    linestyle="--",
    marker="o",
    label="CS"
)

plt.plot(
    tests,
    ai_marks,
    color="red",
    linewidth=3,
    linestyle="-",
    marker="^",
    label="AI"
)

plt.title("CS vs AI Student Performance")
plt.xlabel("Test Number")
plt.ylabel("Marks")

plt.legend()
plt.grid()

plt.show()