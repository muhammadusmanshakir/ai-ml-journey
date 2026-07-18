class Student:
    def __init__(self,name,marks):
        self.name=name
        self.marks=marks
        
    def display(self):
        print(f"Student: {self.name}")
        print(f"Marks: {self.marks}")
        print("-"*20)


students=[]
count=int(input("How many Students: "))
for i in range(count):
    name=input("Enter Student name: ")
    marks=int(input("Enter marks: "))
    students.append(Student(name,marks))

print("\nStudent Records")
print("="*20)

for student in students:
    student.display()

    
