# Relationals / Comparison Operators

# They are used to compare two values. 

# 1. Equal to (==) : Returns True if both values are equal, otherwise returns False.
# 2. Not equal to (!=) : Returns True if both values are not equal, otherwise returns False.
# 3. Greater than (>) : Returns True if the left value is greater than the right value, otherwise returns False.
# 4. Less than (<) : Returns True if the left value is less than the right value, otherwise returns False.
# 5. Greater than or equal to (>=) : Returns True if the left value is greater than or equal to the right value, otherwise returns False.
# 6. Less than or equal to (<=) : Returns True if the left value is less than or equal to the right value, otherwise returns False. 

# #Example No: 1

print("----------------------------------------------------------------------------------")
print("Relational or comparision operators As per following")
print("----------------------------------------------------------------------------------")
a=int(input("Enter the First Value :"))
b=int(input("Enter the Second Value :"))  
a==b
print("Equal to (==) :",a==b)
a!=b    
print("Not equal to (!=) :",a!=b)
a>b
print("Greater than (>) :",a>b)
a<b
print("Less than (<) :",a<b)
a>=b
print("Greater than or equal to (>=) :",a>=b)
a<=b
print("Less than or equal to (<=) :",a<=b)
print("----------------------------------------------------------------------------------")

# example No: 2

a=int(input("Enter the First Value :"))
b=int(input("Enter the second Value :"))
if a<b:
    print("a is less than b")
else:
    print("a is greater than b")

