              
                      # Conditional Expression

# Its shortest way to write simple if-else statement.also known as ternary Operator.

#Syntax As per Following:

# Value_if_true_if condition else Value_if_false

age=int(input("Enter your age : "))

status= "Yoy are Valid for Voting" if age>=18 else  "Better Luck \nNot valid for voting"

print(status)

# 1. Pass or Fail Status
marks = int(input("Enter your marks: "))
result = "Pass" if marks >= 40 else "Fail"
print(result)

# 2. Even or Odd
num = int(input("Enter a number: "))
type_of_num = "Even" if num % 2 == 0 else "Odd"
print(type_of_num)

# 3. Discount Checker
bill = float(input("Enter total bill amount: "))
discount = bill * 0.10 if bill >= 500 else bill * 0.0
print(f"Your discount is: ${discount}")

# 4. Login Access
role = input("Enter your role: ")
access = "Full Access Granted" if role.lower() == "admin" else "Limited Guest Access"
print(access)

# 5. Temperature Warning
temp = float(input("Enter temperature in Celsius: "))
weather_alert = "Stay Indoors - It's too hot!" if temp > 35 else "Weather is pleasant"
print(weather_alert)

