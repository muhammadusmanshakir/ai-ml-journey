students=[]
n=int(input("How  many students? "))

for i in range(n):
    name=input("Enter student name: ")
    marks=int(input("Enter student marks: "))

    if marks >= 90:
        grade="A"
    elif marks >= 80:
        grade="B"
    elif marks >= 70:
        grade="C"
    elif marks >= 60:
        grade="D"
    else:
        grade="F"
    students.append((name,marks,grade))

students=sorted(students,key=lambda student:student[1],reverse=True)
print("\nStudent Records:")
print("="*30)

for student in students:
    print(f"Name: {student[0]}")
    print(f"Marks: {student[1]}")
    print(f"Grade: {student[2]}")
    print("-"*30)

topper=students[0]
print(f"Top scorer: {topper[0]}  ({topper[1]} marks)")
