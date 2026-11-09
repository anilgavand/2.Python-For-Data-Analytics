# Leap Year

# Method 1.Leap Year Checker

# Year = int(input("Enter the Year: "))

# # A year is a leap year if it is divisible by 400, 
# # OR divisible by 4 but NOT by 100.

# if (Year % 400 == 0):
#     print("Its a Leap Year")
# elif (Year % 100 == 0):
#     print("Its Not a Leap Year")
# elif (Year % 4 == 0):
#     print("Its a Leap Year")
# else:
#     print("Its Not a Leap Year")

# Method 2.Leap Year Checker

# # user input
# year = int(input("Enter a Year (e.g. 2024): "))

# # check leap year
# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0): #for or anyone is true is give true output
#     print(f"{year} is leap year")
# else:
#     print(f"{year} is not leap year")

# Method 3.Leap Year Checker

# user input
year = int(input("Enter a Year (e.g. 2024): "))

# check leap year ------ For new line use \

if (year % 4 == 0 and year % 100 != 0) or \
      (year % 400 == 0): #for or anyone is true is give true output
    print(f"{year} is leap year")
else:
    print(f"{year} is not leap year")
