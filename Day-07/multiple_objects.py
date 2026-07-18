class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        
    def introduce(self):
        print(f"My name is {self.name} and I am {self.age} years old! ")


student1=Student("usman",21)
student2=Student("ali",22)
student3=Student("Talha",25)

student1.introduce()
student2.introduce()
student3.introduce()

