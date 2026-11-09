# Arbitrary Arguments

# Arbitarary keyword Arguments (**kwargs)
#  
# Note : The arguments are Stores as dictionary

# Example 1.

def print_details(**kwargs):
  
    for key,value in kwargs.items():
        #   print(type(kwargs))
          print(f"{key}:{value}")

print_details(Name="Sneha",age=34,city="Pune")
print_details(Name="Anil",age=36)

