import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

data = {
    "Department": [
        "CS", "AI", "SE", "CS", "AI",
        "CS", "SE", "AI", "CS", "SE",
        "AI", "CS"
    ],
    "Gender": [
        "Male", "Female", "Male", "Female",
        "Male", "Male", "Female", "Female",
        "Male", "Male", "Female", "Female"
    ],
    "Status": [
        "Pass", "Pass", "Fail", "Pass",
        "Pass", "Fail", "Pass", "Pass",
        "Pass", "Fail", "Pass", "Pass"
    ]
}

df = pd.DataFrame(data)

print("Student Data:")
print(df)

plt.figure(figsize=(8, 5))

sns.countplot(
    data=df,
    x="Department",
    hue="Gender"
)

plt.title("Student Distribution by Department and Gender")
plt.xlabel("Department")
plt.ylabel("Number of Students")

plt.show()