import matplotlib.pyplot as plt

departments = ["AI", "CS", "SE", "IT"]
students = [30, 40, 20, 10]

colors = ["red", "green", "blue", "orange"]
explode = [0, 0.1, 0, 0]

plt.pie(
    students,
    labels=departments,
    colors=colors,
    explode=explode,
    autopct="%1.1f%%",
    startangle=90,
    shadow=True
)

plt.title("Students by Department")

plt.axis("equal")

plt.show()