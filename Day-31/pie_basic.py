import matplotlib.pyplot as plt
departments=["AI","CS","SE","IT"]
students=[30,40,20,10]
plt.pie(students,labels=departments)
plt.title("Students by department")
plt.show()
