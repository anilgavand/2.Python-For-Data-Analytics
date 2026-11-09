#Variables in pythons 

# A.Keywords :Keywords cannot treated as variables

# #Python variable rules:

# A.1 Rules and best practices for naming variables
# Rule_2.It cannot start with a number.
# Rule_3.It cannot contain spaces.
# Rule_4.Python Variable  is case-sensitive (age and Age are different).
# Rule_5.Do not use Python keywords such as if, for, class, or def. 

#Rules Explanation:

# A.1 Rules and best practices for naming variables

# Rule_1.A variable name can contain : letters, numbers, and underscores(_).

# a="Anil"
# Anil=122245
# _113= "Sydney"

# Rule_2.It cannot start with a number.

# 123="Anil"
# print(123)

# Rule_3.It cannot contain spaces.

# My Name = "Anil"
# print(My Name)


# Rule_4.Python Variable  is case-sensitive (age and Age are different).

# Name= "Rickey Pointing"
# print(name)

# Rule_5.Do not use Python keywords such as if, for, class, or def. 

# for=20
#     print(for) # Variable name cannot be reserved words

# i.e Keywords cannot be used as variable names.

# help("keywords")

# Example.1 Running variable Name with keywords

# else=10
# print(else) # We get Ans SyntaxError: invalid syntax 

#because else is a keyword in Python and cannot be used as a variable name.
#we get Ans SyntaxError: invalid syntax

# Example.2 Running variable Name without keywords

# v=10
# print(v)

#We get Ans 10 because v is not a keyword in Python and can be used as a variable name.

# Example.3 Running variable Name without Number Starting

# 123_abc=33
# print(123_abc) #SyntaxError: invalid decimal literal

# Here we get Ans SyntaxError: invalid decimal literal
# #because variable name cannot start with a number in Python.

# # Example.3 Running variable Name with underscore Starting

# _123=55
# print(_123) #We get Ans 55 because variable name can start with an underscore in Python.

 # Example.4 Declaring Variable using Variable

# b=Anil
# print(b)

 # Corrections

# Anil=12
# b=Anil
# print(b) #Here we get output

 # Example.5 Asigning multiple variable

# p,q,r=10,11,12
# print(p+1,q+5,r+8) # Variable with Arithmatic Operations

# A.2 Way to declare Variable

#In Python, there are different naming conventions (cases) used for variables, functions, classes, and constants.

MyName="Anil"      # Pascal Case
myName="Anil"      # camel Case
myname="Anil"      # flat case
my_name="Anil"     # Snake case   

# Example.4 Running variable Name with Spaces

# radius of circle=5
# area of circle=3.14*radius*radius
# print("The Area of Circle is :",area of circle) #We get Ans SyntaxError: invalid syntax
# Spaces are not allowed in variable names in Python.
# We get Ans SyntaxError: invalid syntax


# Example.4 Running variable Name without Spaces

# radius_of_circle=float(input("Enter the Radius of Circle :"))
# area_of_circle=3.14*radius_of_circle*radius_of_circle
# print("The Area of Circle is :",area_of_circle) 

#We get Ans 78.5 because variable name can contain underscores in Python.