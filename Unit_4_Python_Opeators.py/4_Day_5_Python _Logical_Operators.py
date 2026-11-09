# Logical Operators

# They are used to combine multiple conditions.

# 1. AND Operator (and) : Returns True if both conditions are True, otherwise returns False.
# 2. OR Operator (or) : Returns True if at least one condition is True, otherwise returns False.
# 3. NOT Operator (not) : Returns True if the condition is False, otherwise returns False.

# Rules for 'AND' Operators


# True + True = True
# True + False = False
# False + False = False

# Example No: 1

a=5
b=10    
print(a>5 and b<5)
print(a==10 and b==10)
print(a==5 or b<10)


# Rules for 'OR' Operators

# True + False = true

print(not(a==5 and b==10))
