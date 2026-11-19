import mysql.connector

conn = mysql.connector.connect(host="localhost", user="root", password="")

cursor = conn.cursor()
cursor.execute("CREATE DATABASE IF NOT EXISTS studentdb")
cursor.execute("USE studentdb")

cursor.execute("DROP TABLE IF EXISTS students")
cursor.execute("CREATE TABLE students (id INT PRIMARY KEY, name VARCHAR(50), marks INT)")

cursor.execute("INSERT INTO students VALUES (1, 'Aarav', 85)")
cursor.execute("INSERT INTO students VALUES (2, 'Priya', 90)")
cursor.execute("INSERT INTO students VALUES (3, 'Rohan', 78)")
conn.commit()
print("Records inserted")

cursor.execute("SELECT * FROM students")
print("\nAll records:")
for row in cursor.fetchall():
    print(row)

cursor.execute("UPDATE students SET marks = 95 WHERE name = 'Priya'")
conn.commit()
print("\nAfter update:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.execute("DELETE FROM students WHERE name = 'Rohan'")
conn.commit()
print("\nAfter delete:")
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
