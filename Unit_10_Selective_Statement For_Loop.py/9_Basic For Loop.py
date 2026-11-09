# Basic for Loop Programing.( For looping or While Looping)

#Condition 1.Priny your own name 5 times

#print("My name is lakhan")  
    
#We must have to write 5 time with unnecessary Sapce and  irreelevnt used of print function

#Condition 2.Replication Operator

# print("Hello"*5) # Here we get same print in single line


#Type 1. For looping

# For + Loop Variable(i) + in + Sequence (Range) #range is Sequence Generator


#Type 2. While looping
# a=0  # Here a is Loop Variable with value zero.
# while +  Condition(a>5):       As condition comes to (True/False) i.e true it print the output.
#print(Output)--When Condition is true
# loop variable a=a+1
#Program stop - When condition is False.



#1.Looping 

#For multiple printing we can used

#1.Replication Operator

print("Hello"*5) # Here we get same print in single line

# Example 1.Using For loop

for i in range(1,11):
    print(i)

# for i in range(1,11):
#     print("The range is : ",i)

# #Example 2.

# word="python"

# for Alphabet in word:
#     print(Alphabet)

# word="SQL"
# for J in range(1,11):
#     print(word)

# #Loop through List
# iteam  =["Pen","Book","Laptop"]
# for i in iteam:
#     print(i)

# #Loop through List
# iteams  =["Pen","Book","Laptop"]
# for iteam in iteams:
#     print(iteam)

#     #Example 4 Printing Evennumbers

# range(start,end,step)

# for n in range(0,21,2): # for single value in range  says Stop.   
#         print(n)

        
#   #Example 4 Printing Even numbers

# for n in range(0,21,3):   # range(start,end,step)
#         print(n)

for n in range(0,21):  # range(start,end)
        print(n)
else:
    print("For loop end")

#   #Example 4 Printing odd numbers
  
# for n in range(1,21,2):
#           print(n)  



# Example 6.Clean cities names.

# cities=[   "Mumbai","PUNE","dELHI","bANGLORE","CHENNAI,","cULCUTTA"]
# Cleaned=[]
# for City in cities:
#         Cleaned.append(City.strip().title())
# print(Cleaned)

# #if ..loop Condition

# num=[12,31,52,45,12,14,12,95,1,3,2]
# for n in num:
#         if n>10:
#             print(n,"is greater than 10")
#         else:
#          print(n,"is lesser tham 10")

# Example .08 if ..loop Condition for odd and Even

# num=[12,31,52,45,12,14,12,95,1,3,2]
# for n in num:
#         if n%2==0:
#             print(n,"is even Number")
#         else:
#          print(n,"is odd Number")

# #example  10.

# ids=["EMP-002266","EMP-006644","EMP-001234"]     
# for emp in ids:
#     print(emp[-4:])
    