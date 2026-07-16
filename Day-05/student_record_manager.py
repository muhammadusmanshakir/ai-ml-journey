num_students = int(input("How many students? "))
students={}
for student in range(num_students):
    name=input("Enter student name: ")
    marks=int(input("Enter student marks: "))
    students[name]=marks

print("\nStudent Records")
print("-" * 20)   
for name,marks in students.items():
    print(f"{name}:{marks}")
