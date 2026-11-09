# Nested While Loop


'''
A loop inside another loop is called a Nested Loop.

This means that every time the outer loop runs once, the inner loop completes all of its iterations.


outer_loop:
    
    inner_loop:
        
        # Code block to execute - inner loop

# Code block to execute - outer loop



for outer in range(3):
    for inner in range(2):
        print("Outer:", outer, "Inner:", inner)


Why Use Nested Loops?

Handling Multi-Dimensional Data

1.Matrices
2.Tables
3.Grids
4.Lists inside lists


'''

# Example 1. Nested Looop: While - for loop

# i=1
# while i<4:
#     print(" Outer iteration Number",i)
#     for j in range(1,5):
#         print(j)
#     print("----")
#     i+=1

# Example 1. Nested Looop:printing prime numbers for loop

for num in range(2,10):
    for i in range(2,num):
        if num% i==0:
            break
    else:
        print(num)
