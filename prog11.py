java = int(input("Enter your Java Marks: "))
py = int(input("Enter your Python Marks: "))
c = int(input("Enter your C Marks: "))

total_marks = java + py + c
percentage = (total_marks / 3)

if percentage < 35:
 print("Better Luck Next Time")
elif 35 <= percentage <= 50:
 print("Pass")
elif 51 <= percentage <= 60:
 print("Second Class")
elif 61 <= percentage <= 70:
 print("First Class")
else:
 print("First Distinction Class")
