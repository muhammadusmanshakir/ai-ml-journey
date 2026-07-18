with open("student.txt","a") as file:
    name=input("Enter student name: ")
    file.write(name + "\n")

print("Student saved successfuly!")

print("\nStudent List")
print("="*20)

with open("student.txt","r") as file:
    for student in file:
        print(student.strip())
        
