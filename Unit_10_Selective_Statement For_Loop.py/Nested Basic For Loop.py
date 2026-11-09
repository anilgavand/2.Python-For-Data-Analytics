# Nested Loop


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


# Example 1. Basic Example

for num in range(5):
    print(num)

    # Ans : 0,1,2,3,4,

# Example 2. Basic Example

for i in range(3):
    print(" Outer iteration Number",i)
    for num in range(1,5):
        print(num)
    print("-----") 
