# Input functiom :

#Input, Procesing , Output- Which must be known before writing any program

#Example 1. Input Function_ Input always by defaul String. 

# a=input("Enter the Value of a :")
# b=input("Enter the Value of b :")
# print(a+b)


# Birth_year=(input("Enter your Birth Year :"))  #
# Age=2026-Birth_year
# print("Your Age is :",Age)

#  Example 1.1 Correction in String to integer by Explicit Type(Manually)

a=input("Enter the Value of a :")
b=input("Enter the Value of b :")
print(int(a)+int(b))  #-------------------- String to int Conversion Manually------ 
print(a+b)


# Birth_year=int(input("Enter your Birth Year :"))  #converting age in integer
# #input function by default string value is taken from user,
# # so we have to convert it into integer by using int() function
# Age=2026-Birth_year
# print("Your Age is :",Age)





# #Example 2. Input Function:Data Type

# Data=input("Enter your data  :") #By default input function takes string value from user
# print("Your Name is :",type(Data))

#Example .3

# a=input("Enter the First Value")
# b=input("Enter Second Value")
# ans=a+b
# print("The Addition of two values is :",ans)

# Here we get ans 25 when we add the a=2 and b=5 Sting value with concatenate
# #because input function takes string value from user by default,
# # so we have to convert it into integer by using int() function

#Example 4.

# a=int(input("Enter the First Value"))
# b=int(input("Enter Second Value"))
# ans=a+b
# print("The Addition of two values is :",ans)

#Here we get ans 7 when we add the a=2 and b=5

a=int(input("Enter the First Value"))
b=(input("Enter Second Value"))
ans=a+int(b) #even we can convert the string value into integer by using int() function.
print("The Addition of two values is :",ans)

# Data=int(input("Enter your data  :"))
# print("Your Name is :",type(Data))
