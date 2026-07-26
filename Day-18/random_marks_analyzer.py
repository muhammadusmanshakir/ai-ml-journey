import numpy as np
np.random.seed(25)
marks=np.random.randint(40,101,size=10)
print("="*50)
print("     Random Students Marks Analyzer")
print("="*50)

print("\nMarks")
print(marks)

print("Highest marks:",np.max(marks))
print("Lowest marks:",np.min(marks))
print("Average marks:",np.mean(marks))
print("Total marks:",np.sum(marks))
print("\nStudents Scoring above 80:")
print(marks[marks>80])
