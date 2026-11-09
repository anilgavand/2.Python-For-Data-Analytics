# Identity Operators

# They are used to compare the objects, not if they are equal, but if they are actually the same object with the same memory location.

# 1. IS Operator (is) : Returns True if both variables are the same object, otherwise returns False.
# 2. IS NOT Operator (is not) : Returns True if both variables are not the same object, otherwise returns False.

# Example No: 1

a = 5
b = 5
c = 10

print("IS Operator (is) :", a is b)
print("IS NOT Operator (is not) :", a is not c)


# Example No: 1

x=[1,2,3,4]
y= x
z=[1,2,3,4]
print(x is y)  #is operator
print(x is z)  # False because memory location doesent matches 
