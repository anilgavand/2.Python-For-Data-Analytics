
#              Nested_If Conditional Statement In Python(Sequence statement)

#Syntax As per Following:

# if Condition 1:
#              Code to execute if the condition 1 is true

#         if Condition 2:
#              Code to execute if the condition 2 is true 

#         else Condition *:
#              Code to execute if the condition 2 is False 
# else:
#              Code to execute if the condition 1 false.



# Example 1. Check Number positive, even odd or Negative

Number=int(input("Enter the Number: "))

if Number>0:                       # Number is positive
  if Number % 2==0:
    print("Number is Even")
  else:
    print("Number is odd")
else:                              # Number is Negative
    if Number==0:
     print("Number is Zero")
    else:
     print("Number is Negative")
