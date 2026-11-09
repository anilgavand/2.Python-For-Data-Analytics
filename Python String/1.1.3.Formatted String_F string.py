# F_String_fromated String 

# Syntax: f"strings {variable}"


# 1.Basic Example

Name="Lakhan"
City="Pune"
Age=32
print(f"My name is {Name} and I'm {Age}")
print(f"My age after five year will be {Age + 5}")

# print(f"My name is:{Name} I'm From :{City} & I'm :{Age}")

# print("My Name is :",Name ,"I'm from :",City ,"& I'm :",Age,)


# 2.Basic Example

# topic = "python"
# print(f"Learning {topic.upper()}!")  # Output: Learning PYTHON!

# 3.Basic Example

# pi = 3.14159
# print(f"Pi to two decimal places: {pi:.2f}")  # Output: Pi to two decimal places: 3.14

# 4.Basic Example

# ❌ INCORRECT (SyntaxError: Python gets confused by matching nested quotes)
# print(f"Hello {"Bob"}") 

#  CORRECT (Mix double and single quotes)
# print(f"Hello {'Bob'}") 
