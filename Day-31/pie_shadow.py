import matplotlib.pyplot as plt
departments=["CS","AI","IT","SE"]
students=[20,10,55,15]
plt.pie(students,labels=departments,autopct="%1.1f%%",startangle=90,shadow=True)
plt.title("Students by departments")
plt.show()

