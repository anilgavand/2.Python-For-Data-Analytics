#String ,list and Number Functions

# Readymade functions are available in python

# 1. String Function _ Count

# Name =input("Enter The Name :")
# print(" Total A Count :",Name.lower().count("a"))

# 2. String Function _ endswith

# Name =input("Enter the python file Name :")
# print(" Ends with py :",Name.endswith(".py"))
      
# #Ans= True / False

# 3. String Function _ endswith

# Name =input("Enter the data file Name :")
# print("Starts with Sales:",Name.startswith("Sales"))

##Ans= True / False

# 4. String Function _ isdigit,isalpha.isalnum

# Name=(input("Enter The Variable :"))
# print("Name is :",Name.isdigit())
# print("Name is :",Name.isalphat())
# print("Name is :",Name.isalnum())

# Name = input("Enter The Variable: ")

# print("Name is digit:", Name.isdigit())
# print("Name is alpha:", Name.isalpha())
# print("Name is alnum:", Name.isalnum())

# 5. String Function _ \n_New Line

# Name = input("Enter The Variable: ")
# print("Line1\nLine2\nLine3",Name)

# 6. String Function _ Splitline()

Name = input("Enter The Variable: ")
print("Line1\nLine2\nLine3".splitlines()) 
# Calling splitlines() on a string containing newline characters (\n)
# Alternatively, if you want to use the input variable:
print(Name.splitlines())
