import matplotlib.pyplot as plt

tests = [1, 2, 3, 4, 5, 6]

cs_marks = [55, 62, 68, 75, 82, 88]
ai_marks = [60, 65, 70, 78, 85, 92]

print("=" * 55)
print("       Student Performance Trend")
print("=" * 55)

print("\nCS Marks:")
for test, marks in zip(tests, cs_marks):
    print(f"Test {test}: {marks}")

print("\nAI Marks:")
for test, marks in zip(tests, ai_marks):
    print(f"Test {test}: {marks}")

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

print("\n" + "=" * 55)
print("       Line Plot Generated Successfully!")
print("=" * 55)