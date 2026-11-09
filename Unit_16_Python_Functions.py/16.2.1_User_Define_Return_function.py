             
                        # return Function

'''
Return function: it used n function o send a result back to the place where 
the function was called.

When return is exeuted ,the function stop running and immidetiely returns the specfic Value.

'''

# Example 1. Function with return Statement

def add(a,b):
    return a+b               # After return statement function ends.
def multiple(X):
    return X*2               #here we used output value again due to return 

result=multiple(add(10,20))
print("Print the result :",result)

# Example 2. Function with return Statement (cesious and Ferenhit)

def celsius_Fahrenhit(celsius):
    Fahrenhit=(celsius*(9/5))+32
    return Fahrenhit

tmp_f=celsius_Fahrenhit(25)
print=(" Temparature in Fahrenhit is :",tmp_f)







# # Example 4.

# def clean_text(Value):
#     return Value.strip().title()

# output=clean_text("   BAramati   ")
# print(output)

# Example 5.

# def fix_city(city):
#     city=city.lower().strip()
#     city=city.replace("mombai","Mumbai")
#     city=city.replace("kolkatta","Calcutta")
#     return city.title

# fix_city("PUne")
# print(fix_city)

# def fix_city(city):
#     city = city.lower().strip()
#     city = city.replace("mombai", "mumbai")
#     city = city.replace("kolkatta", "calcutta")
#     return city.title()  # Added () to execute the title method


# # Print the result of invoking the function
# print(fix_city("  PUne "))  # Output: Pune