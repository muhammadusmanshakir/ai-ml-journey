students=[
    ("Usman",95),
    ("Ali",68),
    ("Umar",82),
    ("Ayesha",91),
    ("Talha",74)
]
top_students=[student for student in students if student[1]>= 80]

print("Top Students")
print("="*25)

for name,marks in top_students:
    print(f"{name} :{marks}")

    