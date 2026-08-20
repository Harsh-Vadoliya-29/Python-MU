import re

text = "Python is easy to learn and Python is powerful"
pattern = "Python"

result = re.search(pattern, text)

if result:
    print("Pattern found")
    print("Matched text:", result.group())
    print("Starting position:", result.start())
else:
    print("Pattern not found")
