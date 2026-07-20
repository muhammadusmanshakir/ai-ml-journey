students=[
    ("Usman",85),
    ("Ali",92),
    ("Talha",78)
]

sorted_students=sorted(
    students,
    key=lambda student:student[1],
    reverse=True)


print(sorted_students)
