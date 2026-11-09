# 2.Formatted String-str.format() method:


# Syntax :"string{}".format(value)

name="Anil"
age= 35
# print("My name is {} and I'm {}".format (name,age))


# print("My name is {0} and I'm {1}".format(name,age))  # index=Variable position 0,1

# # # Index always start with 0 then 1

# print("My name is {1} and I'm {0}".format(name,age))

# we get wrong output :My name is 35 and I'm Anil

print("My name is {name} and I'm {age}".format(name="Anil",age=29))

