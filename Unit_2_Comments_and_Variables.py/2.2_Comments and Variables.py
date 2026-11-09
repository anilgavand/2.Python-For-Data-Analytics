#Comments and Variable

#Variables

# 1. A variable is used to store a value.
# 2. A variable is a named memory location used to store data.
# 3. Use id() function to display the address of memory location.
# 4. Python uses dynamic typing, so no need to declare type explicitly.
# 5. Variables do not store values directly, they store references.

# #Notes

# 1. Python automatically determines whether a value is int, float, str, etc.
# 2. Variables store references to objects in memory, not the actual values.
# 3. If two variables refer to the same object, they may have the same memory address (id() value).
# 4. id() returns the unique identity (memory reference) of an object during its lifetime.

#print("Welcome to Pyt")
#print("Go along with Way")
#print("that the perfect way")

# following Programe is for Variable
#here we used variable to stored the data
# Variable is Name and this time we save data Anil we can save anything here.

#Example.1 Python detemine value is int, float, str, etc.Automatically

# pi = 3.14
# print(type(pi)) #ans will be <class 'float'> because we stored float value in variable pi.

#Example.2 Python Variable store reference to object in memory, not the actual values.

a = 10
b = 10
print(id(a))
print(id(b)) # python will give same id for both a and b
# because both are referring to same object in memory.

# Example .1 Running variable Name with keywords
# Name="Anil"
# print("Good Morning")
# print("Welcome to Rovema Gmbh",Name)
# print("Have a nice day")
# print=("keywords")
