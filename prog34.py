class MyClass:
    count = 0

    def __init__(self, name):
        self.name = name
        MyClass.count += 1

    def instance_method(self):
        print(f"Instance method called by {self.name}")

    @classmethod
    def class_method(cls):
        print(f"Class method called. Total objects: {cls.count}")

    @staticmethod
    def static_method():
        print("Static method called. No access to class or instance.")

obj = MyClass("Aarav")
obj.instance_method()
MyClass.class_method()
MyClass.static_method()
