#Write a program to create a class and object in Python.

class register:
    
    def add_details(self,rollno,name,stream):
        self.rollno=rollno;
        self.name=name;
        self.stream=stream;
        print("\n Student Details Added Sucessfully")
        self.display(self.rollno,name,stream)
        
    def display(self,rollno,name,stream):
        print("\n Displaying Records...................")
        print("Student Roll no is ",rollno)
        print("Student Name is ",name)
        print("Student Stream is ",stream)

reg=register();
rollno=int(input("Enter Student Roll no : "))
name=input("Enter Student Name : ")
stream=input("Enter Stream : ")
reg.add_details(rollno,name,stream)
