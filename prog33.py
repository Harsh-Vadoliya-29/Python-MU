class Demo:
    class_var = "I am a class variable"

    def __init__(self, value):
        self.instance_var = value

obj1 = Demo("Instance value for obj1")
obj2 = Demo("Instance value for obj2")

print(obj1.instance_var)  
print(obj2.instance_var)  

print(obj1.class_var)    
print(obj2.class_var)
