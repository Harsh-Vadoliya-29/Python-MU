class AgeError(Exception):
    def __init__(self, age, message="Age must be between 18 and 60"):
        self.age = age
        self.message = message
        super().__init__(self.message)

class NegativeValueError(Exception):
    def __init__(self, value):
        self.value = value
        super().__init__(f"Negative value not allowed: {value}")

def check_age(age):
    if age < 18 or age > 60:
        raise AgeError(age)
    print(f"Age {age} is valid")

def check_value(val):
    if val < 0:
        raise NegativeValueError(val)
    print(f"Value {val} is valid")

try:
    check_age(15)
except AgeError as e:
    print(f"AgeError: {e}")

try:
    check_value(-5)
except NegativeValueError as e:
    print(f"NegativeValueError: {e}")

try:
    check_age(25)
    check_value(10)
except (AgeError, NegativeValueError) as e:
    print(f"Error: {e}")
