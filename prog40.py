f = open("seektest.txt", "w")
f.write("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
f.close()

f = open("seektest.txt", "r")
print("Current position:", f.tell())
print("Read 5 chars:", f.read(5))
print("Position after read:", f.tell())

f.seek(10)
print("Position after seek(10):", f.tell())
print("Read 5 chars:", f.read(5))

f.seek(0)
print("Position after seek(0):", f.tell())
print("Full content:", f.read())
f.close()
