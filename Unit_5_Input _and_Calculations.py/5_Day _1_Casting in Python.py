# Casting in Python-(Type Casting)

# Example 1. Changing data type

 # Rule 1. Only integer value changed into int().

# a=5
# print(type(a))
# b="19"
# print(type(b))
# c=int(b)
# print(a+c)
# print(a+int(b))

 # Rule 2. Sting Value Cannot convert into Integer.

# Name= "Sneha"
# New_Name=int(Name) #ValueError: invalid literal for int() with base 10: 'Sneha'

# Rule 3. Number (Integer) can convert to String but string cannot convert in Integer.

# Name1= 26
# New_Name=str(Name1)
# print(type(New_Name))

# Rule 4. All Integer can convert to Float by adding .00 or removing .xx during int Conversion

a=22.55
b=int(a)
print(b)
print(type(b))
