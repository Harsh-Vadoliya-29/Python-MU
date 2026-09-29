class Demo:
    count = 0

    def __init__(self, name):
        self.name = name  
        Demo.count += 1  

    def show_name(self):
        print(f"My name is {self.name}")

    @classmethod
    def show_count(cls):
        print(f"Total objects created: {cls.count}")

    @staticmethod
    def greet():
        print("Hello! This is a static method.")

obj1 = Demo("xyz")
obj2 = Demo("abc")

obj1.show_name()
obj2.show_name()

Demo.show_count()
Demo.greet()
