import matplotlib.pyplot as plt
departments=["CS","AI","IT","SE"]
students=[20,50,10,30]
colors=["red","green","blue","orange"]
plt.pie(students,labels=departments,colors=colors,autopct="%1.1f%%")
plt.title("Students by departments")
plt.show()
