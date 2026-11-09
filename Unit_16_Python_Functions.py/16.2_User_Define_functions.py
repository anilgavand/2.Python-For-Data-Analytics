          
                 # Define functions (def,return)

''' Function : Its block of code that perform a Specfic Task.

Basic Concept:
1. Create :  used keyword def_
2. Call :    Function name()
3. Parameter : Variable listed inside
4. Arguments : Actual value passed to function 

 def my_funttion(parameer) :
 instruction-1
 instruction-2
    ......
 return result

'''
# def : To define function we used keyword def

# Example 1.Function without Parameter

# def greet():     #Variable or Parameter is blank in greet Function.
#     print("Hello python Learner")
#     print("Learning Function")
# greet()

# Example 1.Function with Parameter

# def welcome(Name):
#         print("Welcome to Goa : ",Name)
#         print(type(Name))
#         print(Name[0:13:2])

# welcome("Anil_Gavand")

def add(a,b):          # here a and b is Parameter
    print("Addition of a and b is :",a+b)  # Here print value we cannot reused.
    print("Substraction of a and b is :",a-b)
    print("Multiplication of a and b is :",a*b)
    print(a//b)
add(5,7)  # Here 5 and 7 is arguments
add(b=8,a=5) # Here sequence of a and b can be change









