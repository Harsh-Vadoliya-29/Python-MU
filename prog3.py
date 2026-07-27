a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

# Arithmetic operations
print("\nArithmetic Operations:")
print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b}")
print(f"{a} % {b} = {a % b}")
print(f"{a} ** {b} = {a ** b}")

# Logical operations
x = bool(int(input("\nEnter 1 or 0 for x (True/False): ")))
y = bool(int(input("Enter 1 or 0 for y (True/False): ")))

print("\nLogical Operations:")
print(f"{x} and {y} : {x and y}")
print(f"{x} or {y}  : {x or y}")
print(f"not {x}     : {not x}")
