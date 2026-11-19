class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

print("--- Single Inheritance ---")
d = Dog()
d.speak()
d.bark()

class Puppy(Dog):
    def play(self):
        print("Puppy plays")

print("--- Multilevel Inheritance ---")
p = Puppy()
p.speak()
p.bark()
p.play()

class Flyer:
    def fly(self):
        print("Can fly")

class Swimmer:
    def swim(self):
        print("Can swim")

class Duck(Flyer, Swimmer):
    def quack(self):
        print("Duck quacks")

print("--- Multiple Inheritance ---")
dk = Duck()
dk.fly()
dk.swim()
dk.quack()
