import pandas as pd

data = {
    "Name": ["Aarav", "Priya", "Rohan"],
    "Age": [25, 30, 35],
    "Salary": [50000, 60000, 70000]
}
df = pd.DataFrame(data)
df.to_csv("sample.csv", index=False)
print("CSV file created")

df_csv = pd.read_csv("sample.csv")
print("\nDataFrame from CSV:")
print(df_csv)

df.to_excel("sample.xlsx", index=False)
print("\nExcel file created")

df_excel = pd.read_excel("sample.xlsx")
print("\nDataFrame from Excel:")
print(df_excel)
