import pandas as pd

print("=" * 50)
print("    Employee & Department Management System")
print("=" * 50)

employees = pd.DataFrame({
    "EmpID": [101, 102, 103, 104],
    "Name": ["Ali", "Sara", "Ahmed", "Usman"]
})

departments = pd.DataFrame({
    "EmpID": [102, 103, 104, 105],
    "Department": ["AI", "CS", "IT", "HR"]
})

print("\nEmployees DataFrame:")
print(employees)

print("\nDepartments DataFrame:")
print(departments)

# Inner Join
print("\nInner Join:")
inner = pd.merge(employees, departments, on="EmpID", how="inner")
print(inner)

# Left Join
print("\nLeft Join:")
left = pd.merge(employees, departments, on="EmpID", how="left")
print(left)

# Right Join
print("\nRight Join:")
right = pd.merge(employees, departments, on="EmpID", how="right")
print(right)

# Outer Join
print("\nOuter Join:")
outer = pd.merge(employees, departments, on="EmpID", how="outer")
print(outer)

print("\n" + "=" * 50)
print("Analysis Completed Successfully!")
print("=" * 50)
