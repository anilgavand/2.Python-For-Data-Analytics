
#              If-else Conditional Statement In Python(Sequence statement)

# Syntax As per Following:

# if Condition:
#              Code to execute if the condition is true
# else:
#              Code to execute if the condition is false


# Example 1.Finding Out Spring Based on Temparature

Temp_T=int(input("Enter the temparature :"))

if Temp_T<24:
    print("Its Winter Spring")
else:
    print("It's Summer Spring")

# Example 2. Email Validation

email=input("Enter your mail :")

if "@" in email and "." in email:
    print(" Email is valid")
else:
    print("Invalid Email")

# Example 3.Missing Data Checking

Value=""   #here we can add or delete word or number like "Samay","1"

if Value==" ":
    print("Data is Missing")
else:
    print("Data is Available")