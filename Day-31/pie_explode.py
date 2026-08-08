import matplotlib.pyplot as plt
departments=["CS","AI","IT","SE"]
students=[10,20,40,30]
explode=[0,0.1,0,0]
plt.pie(students,labels=departments,explode=explode,autopct="%1.1f%%")
plt.title("Students by department")
plt.show()

