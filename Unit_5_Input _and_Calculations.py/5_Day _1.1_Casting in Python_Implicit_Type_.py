
# Implicit Casting

# Implicit type casting happens automatically by the Python interpreter.
# When you perform an operation involving different data types, 
# Python automatically converts one type to another to prevent data loss or type mismatch errors
# (usually promoting the "smaller" or less precise type to the "larger" one).

#1. Implicit Type Casting (Coercion)

num_int = 10        # Integer
num_float = 5.5     # Float

result = num_int + num_float
print(result)       # Output: 15.5
print(type(result)) # Output: <class 'float'>

# If it dinot detect data type and manage it in same type output wiil be 15 and Data loss will be 0.5 