class MyClass:
    def __init__(self, name):
        self.name = name
        print(f"Constructor called for {self.name}")

    def __del__(self):
        print(f"Destructor called for {self.name}")

obj1 = MyClass("Object1")
obj2 = MyClass("Object2")
print("Program running...")
del obj1
del obj2
print("Program ended")
