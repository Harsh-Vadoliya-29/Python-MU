# Create a list
nums = [1,2,3,4,5,6,7,8,9,10]
print("Original list:", nums)

# Indexing
print("First element:", nums[0])
print("Last element:", nums[-1])

# Slicing
print("First 5 elements:", nums[:5])
print("Every 2nd element:", nums[::2])
print("Reversed list:", nums[::-1])

# List comprehension: squares of even numbers
squares_even = [x**2 for x in nums if x % 2 == 0]
print("Squares of even numbers:", squares_even)

# Modify using indexing
nums[0] = 100
print("After modification:", nums)

# Modify using slicing
nums[1:4] = [200, 300, 400]
print("After slicing modification:", nums)
