import matplotlib.pyplot as plt
departments=["CS","AI","SE","IT"]
students=[30,40,20,10]
plt.pie(students,labels=departments,autopct="%1.1f%%")
plt.title("Students by departmnets")
plt.show()
