def calculate_average(marks):
    assert len(marks) > 0, "Marks list cannot be empty"
    assert all(0 <= m <= 100 for m in marks), "Marks must be between 0 and 100"
    return sum(marks) / len(marks)

def set_discount(price, discount):
    assert price > 0, "Price must be positive"
    assert 0 <= discount <= 100, "Discount must be between 0 and 100"
    return price - (price * discount / 100)

print("--- Valid cases ---")
print(f"Average: {calculate_average([80, 90, 70])}")
print(f"Discounted price: {set_discount(1000, 20)}")

print("\n--- Assert failure ---")
try:
    calculate_average([])
except AssertionError as e:
    print(f"AssertionError: {e}")

try:
    set_discount(-500, 10)
except AssertionError as e:
    print(f"AssertionError: {e}")
