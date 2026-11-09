
# Explicit Type Casting (Type Conversion)

#Explicit type casting is performed manually by the programmer using Python’s built-in functions. 
# You explicitly tell Python to transform a value into a specific data type.

# 2. Explicit Type Casting (Type Conversion)

# 2.A. Numeric Conversions (int(), float())

# Float to Int (truncates decimal)
print(int(9.87))       # Output: 9

# String to Int
print(int("100") + 5)  # Output: 105

# Boolean to Int (True becomes 1, False becomes 0)
print(int(True))       # Output: 1

# Int to Float
print(float(42))       # Output: 42.0

# String to Float
print(float("3.14159"))# Output: 3.14159

#2.B. String Conversion (str())

# The str() function converts any data type (integers, floats, lists, booleans)
# into its string representation.
# This is crucial when concatenating strings and numbers.

score = 95
# print("Your score is: " + score)  # TypeError! Cannot concatenate str and int

# Correct way using explicit casting:
print("Your score is: " + str(score))  # Output: Your score is: 95

# 2.C. Boolean Conversion (bool())

print(bool(0))        # Output: False (0)
print(bool(42))       # Output: True (1)
print(bool(""))       # Output: False (0)
print(bool("Python")) # Output: True(1)


# 2.D. Collection Conversions (list(), tuple(), set(), dict())

# Tuple to List
my_tuple = (1, 2, 3)
my_list = list(my_tuple)
print(my_list)        # Output: [1, 2, 3]

# String to List (splits into individual characters)
print(list("Code"))   # Output: ['C', 'o', 'd', 'e']

# Removing duplicates from a list using a Set conversion
numbers = [1, 2, 2, 3, 4, 4]
unique_numbers = list(set(numbers))
print(unique_numbers) # Output: [1, 2, 3, 4] (order may vary)