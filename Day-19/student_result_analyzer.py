import numpy as np

print("=" * 50)
print("        Student Result Analyzer")
print("=" * 50)

marks = np.array([75, 92, 68, 84, 59, 90, 77, 45, 88, 95])

print("\nStudent Marks:")
print(marks)

print("\nSorted Marks:")
print(np.sort(marks))

print("\nHighest Marks:")
print(np.max(marks))

print("\nLowest Marks:")
print(np.min(marks))

print("\nAverage Marks:")
print(np.mean(marks))

print("\nStudents scoring above 80:")
print(marks[marks > 80])

print("\nIndexes of students scoring above 80:")
print(np.where(marks > 80))

print("\nInsert position for mark 85:")
print(np.searchsorted(np.sort(marks), 85))
