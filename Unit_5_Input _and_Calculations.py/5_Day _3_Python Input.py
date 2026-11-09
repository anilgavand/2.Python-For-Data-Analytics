# Q.1: What happens if a user inputs 3.14 when the code executed is
#num = int(input())
# 1.It raises a ValueError
# 2.It rounds the number to 3
# 3.It raises a TypeError
# 4.It stores the string "3.14"
# #Answer: 1.It raises a ValueError

# num = int(input("Enter The Number :")) #Here we are taking input from user 
# print("The number is:", num)    #and converting it into integer by using int() function.

# We get error when we input 3.14 because 
#int() function can only convert whole numbers (integers) and not decimal numbers (floats).

#Q.2
x=input("Enter the value of x :") #Here we are taking input from user
print("The value of x is:",x*2) #Here we are printing the value of x
