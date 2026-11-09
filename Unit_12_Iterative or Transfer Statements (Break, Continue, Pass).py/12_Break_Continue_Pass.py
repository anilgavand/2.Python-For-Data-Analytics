
#3. Iterative / Transfer Statements (Break, Continue, Pass)
'''
Loop Control Statements

Loop control statements allow you to alter the normal flow of a loop.

Python supports 3 clauses within loops:

1. Pass Statement : Doing nothing

The pass statement is a null operation.
It does nothing when executed and is used as a placeholder
where code is required syntactically but no action is needed.

2. Break Statement : Exiting the loop

The break statement immediately terminates the loop and transfers 
control to the statement following the loop.

3. Continue Statement : Skipping an iteration

The continue statement skips the remaining code in 
the current iteration and moves to the next iteration of the loop.

'''

#Example .01 Pass Statement : Doing nothing

# count = 5

# while count > 0:
#     if count == 3:
#         pass
#     else:
#         print(count)
#     count -= 1
   
# for i in range(1,11):
#     if i==5:
#         continue
#     print(i)

# for i in range(1,11):
#     if i==5:
#         pass
#     print(i)

#Example .02 Break Statement : Exiting the loop

# for i in range(1,11):
#     if i==5:
#         break
#     print(i)

# for i in range(5):
#     if i == 3:
#         break
#     print(i)

#Example .03 Continue Statement : Skipping an iteration

for i in range(5):
    if i == 3:
        # continue
     print(i)


# Example .04 Infinie loop

# count = 5

# while count > 0:
#     if count == 3:
#          continue
#          count -= 1
       
#     else:
#         print(count)

#     count -= 1
