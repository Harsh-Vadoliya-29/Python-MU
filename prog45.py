import pandas as pd

data = {
    "Name": ["Aarav", "Priya", "Rohan", "Sneha", "Vikram"],
    "Age": [25, 30, 35, 28, 22],
    "Salary": [50000, 60000, 70000, 55000, 45000],
    "Department": ["HR", "IT", "IT", "HR", "Finance"]
}

df = pd.DataFrame(data)
print("DataFrame:")
print(df)

print("\nShape:", df.shape)
print("\nColumn types:\n", df.dtypes)
print("\nStatistics:\n", df.describe())

print("\nSalary > 50000:")
print(df[df["Salary"] > 50000])

print("\nAverage salary by department:")
print(df.groupby("Department")["Salary"].mean())

print("\nSorted by Age:")
print(df.sort_values("Age"))
