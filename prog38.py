from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

class BankAccount:
    def __init__(self, owner, balance):
        self.__owner = owner
        self.__balance = balance

    def deposit(self, amount):
        self.__balance += amount
        print(f"Deposited {amount}. Balance: {self.__balance}")

    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance")
        else:
            self.__balance -= amount
            print(f"Withdrawn {amount}. Balance: {self.__balance}")

    def get_balance(self):
        return self.__balance

print("--- Encapsulation ---")
acc = BankAccount("Aarav", 1000)
acc.deposit(500)
acc.withdraw(200)
print(f"Balance: {acc.get_balance()}")

class Rectangle(Shape):
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

print("\n--- Abstraction ---")
r = Rectangle(5, 3)
print(f"Area: {r.area()}")
