
#              If-elif-else Conditional Statement In Python(Sequence statement)

#Syntax As per Following:

# if Condition 1:
#              Code to execute if the condition is true

#     elif Condition 2:
#              Code to execute if the condition is true 

#     elif Condition *:
#              Code to execute if the condition is true 
# else:
#              Code to execute if the condition 1 is false.

#Example : Grading System

marks=int(input("Enter your percentage"))

if marks>=90:
    print("Grade : A")
elif marks>=75:
    print("Grade : B")
elif marks>=65:
    print("Grade : c")  
elif marks>=55:   
    print("Grade : D")
else:
    print(" You are fail")

#Example 1. we have to find out given number is divisible by 5,3 or none

n=int(input("Enter the value of a :"))

if n%5==0 and n%3==0:
    print("n is divisble by 5 and 3")
elif n%5==0:
    print("n is divisble by 5")
elif n%3==0:
    print("n is divisble by 3")
else:
    print("n is not divisble by 5 and 3")


#Example 2.we have to find out given number is between 9 to 99 i.e Two digit

a=int(input("Enter the number : "))

if a>=0 and a<=10:
    print("Number is single digit :",a)
elif a>=10 and a<=100:
    print("Number is two Digit",a)
else:
    print("Number is't belong this digit catogery",a)


# Example 3. we are finding Sales Performer

print("-----Sales Performer---------------")
sales=int(input("Enter the sales Amount :"))
if sales>65006:
    print("High performer")
elif sales>56000:
    print("Medium Performer")
elif sales>32004:
    print("Low Performer")
else:
    print("Need Improvement")


# Example .4 Data related example

print("----------------------------------------------------------")
print("Grades as per Following for Bachlors degree in Engineering")
print("----------------------------------------------------------")
Marks=int(input("Enters the marke :"))
if Marks>=66:
    print("first Class with Dist")
elif Marks>=60:
    print("First class")
elif Marks>=56:
    print("Second Class")
elif Marks>=40:
    print("Pass")
else:
    print("Failed")
    
