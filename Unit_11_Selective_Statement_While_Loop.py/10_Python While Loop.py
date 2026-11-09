
# Python While Loop

'''
Loops enable you to perform repetitive 
tasks efficiently without writing redundant code.
They iterate over a sequence (like a list, tuple, string, or range)
or execute a block of code as long as a specific condition is met.

Types of Loops in Python

1.While Loop
2.For Loop
3.Nested Loop

While loop repetedly executes a block of codes as
long as given condition remains true.
It check the condition before each iteration

Syntax: 
    while condition:
        code block to execute

While Loop = I C U

I → Initialization
C → Condition
U → Updation

Rule:

Use while when repetition depends on a condition.
Use for when iterating through a sequence or a known number of times.

'''

#Type 1. For looping

# For + Loop Variable(i) + in + Sequence (Range) #range is Sequence Generator

'''a = start_value     #Initialization

while condition:    # Condition
    # work
    a = update_value  #Updation
'''

#Type 2. While looping :printing numbers 1 to 5

# a=1       # The loop control variable.       

# while (a<6):       # As condition comes to (True/False) i.e true it print the output.

#     print(a)      #--When Condition is true

#     a+=1         # loop variable

#Program stop - When condition is False.

#Type 2.1 While looping :printing numbers 5 to 1

a=5  #the loop control variable.

while a>0:
    print(a)
    a-=1
else:
    print("While loop ended")







# Example 1. Basic 

# Count=0
# while Count<5:
#     print("The Value is :",Count)
#     Count=Count+1

# Count=0
# while Count<5:
#     print("The Value is :",Count)
#     Count+=1

# # Example 2. Basic 

# n=5
# while n>0:
#     print(n)
#     n-=1

# # Example.3 Input valid input number

# num=" "
# while not  num.isnumeric():
#     num=input("Enter any Value : ")

# print("NumberAccepted :",num)


# # Example.3.1 Input valid input number

# num=" "
# while not  num.isnumeric():
#     num=input("Enter any Value : ")
#     print("Enter number only : ")
# print("NumberAccepted :",num)

# #Example 4.Loop through List using While

# iteams=["Banana","Apple","Grapes","Potato","Onion"]
# i=0
# while i<len(iteams):
#     print(iteams[i])
#     i+=1

#example 5. using Break function

# x=1
# while   x<=10:
#     if x==5:
#         break
#     print(x)
#     x+=1

#While in Continued

# y=0
# while y<10:
#     y+=1
#     if y % 2 == 0:
#         continue
#     print(y)

# #Example no 9 Pasward Match

# password=" "
# attempts= 0
# while password !="admin123" and attempts < 3:
#         passward=input("Enter the Password : ")
#         attempts+=1

#         if password == "admin123":
#          print(" Pasward mathch")
#         else:
#          print("Password doesnot Match","Attempt count:",attempts)


# # print(" 3 Attempt Complited")

# attempts = 0    
# password = ""

# while password != "admin123" and attempts < 3:
#     password = input("Enter the Password: ")
#     attempts += 1

#     if password == "admin123":
#         print("Password matched")
#     else:
#         print("Password does not match. Attempt count:", attempts)
#         if  attempts==3:
#             print("3 attempts completed")

