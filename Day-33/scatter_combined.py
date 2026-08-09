import matplotlib.pyplot as plt
cs_hours = [1, 2, 3, 4, 5]
cs_marks = [45, 52, 60, 68, 75]

ai_hours = [2, 3, 4, 5, 6]
ai_marks = [50, 58, 67, 76, 85]
plt.scatter(
    cs_hours,cs_marks,color="blue",s=100,marker="o",alpha=0.7,
    label="CS"
)
plt.scatter(
    ai_hours,ai_marks,color="red",s=100,marker="^",alpha=0.7,
    label="AI"
    )
plt.title("Study Hours vs Marks")
plt.xlabel("Study Hours")
plt.ylabel("Marks")

plt.legend()
plt.grid()

plt.show()
