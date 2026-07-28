import numpy as np

marks = np.array([
    [85, 78, 92],
    [67, 88, 75],
    [90, 81, 95],
    [72, 69, 80]
])

print("=" * 50)
print("      Student Performance Analyzer")
print("=" * 50)

print("\nMarks:")
print(marks)

print("\nTotal Marks of Each Student:")
print(np.sum(marks, axis=1))

print("\nAverage Marks of Each Student:")
print(np.mean(marks, axis=1))

print("\nHighest Marks in Each Subject:")
print(np.max(marks, axis=0))

print("\nLowest Marks in Each Subject:")
print(np.min(marks, axis=0))

print("\nStudents Scoring Above 80:")
print(marks[marks > 80])

print("\nBonus Marks (+5):")
print(marks + 5)

print("\nUnique Marks:")
print(np.unique(marks))
