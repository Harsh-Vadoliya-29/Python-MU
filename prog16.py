list1=["A","B",3,"D","E"]
string="ABCD"
dics={"Name " : " Tom ", "age" : 29 , "country" : "england"}

print("YOUR LIST AS FOLLOWS :- ")
for i in list1:
    print(i)

print(" ")
print("YOUR STRING AS FOLLOWS :- ")
for i in string:
    print(i)

print(" ")

print("YOUR dictionary AS FOLLOWS :- ")
for key,value in dics.items():
    print(f"{key} : {value}")
