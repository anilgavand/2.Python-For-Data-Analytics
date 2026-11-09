# Assignment

# Example 1. printing output in same line.

#print(" My name is",sep="",end="\n")  y default sep= Space and \n New Line
 # Sample:

# print ("My name is")
# print("Lakhan")

# print("My name is", end=" ")
# print("Lakhan")

# Sample 1.

# i=1
# while i<4:
#     print(f"My name is lakhan {i}")
#     i+=1
#     # Here we get ans in diffferent line.

#Final Ans:

# i=1
# while i<4:
#     print(f"My name is lakhan {i}",end=" ")
#     i+=1   

# i=1
# while i<4:
#     print(f"My name is{i}", "lakhan",sep="-",end=" ")
#     i+=1   

# Example 2. Nested loop Star Triangle Pattern

# Method 1.

# n=5  # No of rows

# for i in range(1,n+1):
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# # Method 2.

# n=5

# for i in range(1,n+1):
#     print("*"*i)

# Example 3.Nested loop Star inverted Triangle Pattern

# n=5  # No of rows

# for i in range(n,0,-1):    # started from 5 and end with 1 by educing 1
#     for j in range(1,i+1):
#         print("*",end="")
#     print()

# Method 2.

# n=5

# for i in range(n,0,-1):

#     print("* "*i)

# Example 3.Nested loop Pyramid / Equilateral Triangle Pattern

