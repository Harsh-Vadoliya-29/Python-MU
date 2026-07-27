students = {"name" : "Aman" , "age" : 21 , "city" : "Rakot"}

print("Key And Values Are : - ",students)

students["Pincode"] = 360006

print("Name :- ",students.get("name"))

print("Remove Pincode :- ",students.pop("Pincode"),students)

print("Check age In Students :- ","age" in students)

print("KEYs :- ")
for stud in students:
    print(stud)

print("VALUEs :- ")
for stud1 in students:
      print(stud1)

print("KEYs And VALUEs :- ")
for key,values in students.items():
    print(f"{key} = {values}")
