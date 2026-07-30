text = "  Hello, Welcome To MU !  "

# --- SLICING ---
print("Original:", repr(text))
print("Slice [2:7]:", text[2:7])       
print("Slice [:5]:", text[:5])         
print("Slice [-6:]:", text[-6:])       
print("Reversed:", text[::-1])         

# --- BUILT-IN STRING FUNCTIONS ---
print("Uppercase:", text.upper())
print("Lowercase:", text.lower())
print("Title Case:", text.title())
print("Stripped:", text.strip())
print("Replace:", text.replace("MU", "MarwadI University"))
print("Count of 'o':", text.count("o"))

# --- FORMATTING ---
name = "Anuj Gupta"
age = 36
print("Formatted (f-string):", f"My name is {name} and I am {age} years old.")
print("Formatted (.format):", "My name is {} and I am {} years old.".format(name, age))
print("Formatted (%):", "My name is %s and I am %d years old." % (name, age))
