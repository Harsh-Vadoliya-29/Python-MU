import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS companydb")
cursor.execute("USE companydb")

cursor.execute("DROP TABLE IF EXISTS employees")
cursor.execute("CREATE TABLE employees (id INT PRIMARY KEY, name VARCHAR(50), dept VARCHAR(50), salary INT)")

cursor.executemany("INSERT INTO employees VALUES (%s, %s, %s, %s)", [
    (1, "Aarav", "HR", 50000),
    (2, "Priya", "IT", 60000),
    (3, "Rohan", "IT", 70000),
    (4, "Sneha", "HR", 55000),
    (5, "Vikram", "Finance", 45000)
])
conn.commit()

cursor.execute("SELECT * FROM employees")

print("--- fetchone ---")
print(cursor.fetchone())

print("\n--- fetchmany(2) ---")
print(cursor.fetchmany(2))

print("\n--- fetchall ---")
print(cursor.fetchall())

cursor.close()
conn.close()
