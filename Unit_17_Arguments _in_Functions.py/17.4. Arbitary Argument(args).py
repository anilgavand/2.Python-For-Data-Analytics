# Arbitrary Arguments

# Arbitarary positional Arguments (*args 
#  
# Note : Stores arguments as tuple

# Example 1.

# def addition2numbers(a,b):
#     return (a+b)

# result=addition2numbers(11,78)
# print(result)

# # Example 2.

# def addition2numbers(a,b,c):  # here we dwfined Paramater
#     return (a+b+c)

# result=addition2numbers(11,78,12)
# print(result)


# Example 3.

# def addnumbers(*args):  # Here we defined 
#     print(type(args))
#     return sum(args)
# result=addnumbers(13,12,45,15,78,95,45218,5314)  #Variable no of arguments
# print(result)


# Example 4.

def greetings(*names):  # Here we defined 
    for name in names:
     print(f"Hello {name}")

result=greetings("Anil","Sneha","Sachin")  #Variable no of arguments
print(result)

