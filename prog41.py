print("--- SyntaxError ---")
try:
    eval("x ==")
except SyntaxError as e:
    print(f"SyntaxError: {e}")

print("\n--- TypeError ---")
try:
    result = "hello" + 5
except TypeError as e:
    print(f"TypeError: {e}")

print("\n--- ValueError ---")
try:
    num = int("abc")
except ValueError as e:
    print(f"ValueError: {e}")

print("\n--- ZeroDivisionError ---")
try:
    result = 10 / 0
except ZeroDivisionError as e:
    print(f"ZeroDivisionError: {e}")

print("\n--- IndexError ---")
try:
    lst = [1, 2, 3]
    print(lst[5])
except IndexError as e:
    print(f"IndexError: {e}")

print("\n--- KeyError ---")
try:
    d = {"a": 1}
    print(d["b"])
except KeyError as e:
    print(f"KeyError: {e}")

print("\n--- FileNotFoundError ---")
try:
    f = open("nonexistent.txt", "r")
except FileNotFoundError as e:
    print(f"FileNotFoundError: {e}")
