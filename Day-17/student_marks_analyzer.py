import numpy as np
marks = []
for i in range(5):
    mark=int(input(f"Enetr marks of student {i+1}: "))
    marks.append(mark)

marks=np.array(marks)


print("=" * 50)
print("      Student Marks Analyzer")
print("=" * 50)

print("\nMarks:")
print(marks)
print("\nNumber of Students:", marks.size)
print("Highest Marks:", np.max(marks))
print("Lowest Marks:", np.min(marks))
print("Average Marks:", np.mean(marks))
print("Total Marks:", np.sum(marks))

print("\nMarks after adding 5 bonus marks:")
print(marks + 5)

print("\nMarks greater than or equal to 80:")
print(marks[marks>=80])
