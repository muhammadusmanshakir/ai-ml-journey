students =[]
for i in range(1,4):
    student=input(f"Enter student {i}: ")
    students.append(student)
print("Students List: ")
for student in students:
    print(student)

print(f"Total students: {len(students)}")
