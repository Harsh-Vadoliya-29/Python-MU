class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C):
    pass

print("--- Method Resolution Order ---")
print(D.mro())
d = D()
d.show()

class Book:
    def __init__(self, title, pages):
        self.title = title
        self.pages = pages

    def __str__(self):
        return f"'{self.title}' ({self.pages} pages)"

    def __len__(self):
        return self.pages

    def __add__(self, other):
        return Book(self.title + " & " + other.title, self.pages + other.pages)

print("\n--- Magic Methods ---")
b1 = Book("Python", 300)
b2 = Book("Java", 400)
print(b1)
print(f"Length: {len(b1)}")
b3 = b1 + b2
print(f"Combined: {b3}")
