# # # Python _Operators

# #1.Arithmatic Operator_Binary Operator

# num1= 12
# num2 =24

# print(num1-num2)     #Substraction
# print(num1*num2)     #multiplication
# print(num2/num1)     #Division
# print(num1**num2)    #power



# ##2. Comparision Operator
# p1=56
# p2=42
# p3=15
# print(p1<p2)
# print(p3>p1)
# print(p1==p2==p3)

# # # 3. Assignment Operator
# value=50
# print(value)
# value-=10   #subtraction and assign
# print(value)

# ## 4. Logical operator

# x1=12
# x2=23
# x3=15
# x4=26
# print("And result is :",x1<x3 and x2>x4) #AND Condition
# print("And result is :",x1<x3 and x2<x4) #AND Condition
# print("or result is :",x1<x2 or x3<x4)  #OR Condition

# #5. Identity operator
# m1=100
# m2=100
# print(m1 is m2)

#6. Membership Operators

print("Chech e s in te Mango :",'e'in 'mango')
print("Chech a s in te Mango :",'a'in 'mango')

# 7.Modulus Operator
# it gives the remainder when we divide two numbers

a=10
b=3
print("The Modulus of two values is :",a%b) 

#We get Ans 1 because 10/3=3 and remainder is 1

# # 8. Floor Division Operator (For + ve Values)
# # it gives the quotient when we divide two numbers
# a=10
# b=3 
# print("The Floor Division of two values is :",a//b) 
# # here we get Ans 3 because 10/3=3 and quotient is 3

#8.1 Floor Division Operator (For - ve Values)

# a=-10
# b=3 
# print("The Floor Division of two values is :",a//b) 

# here we get Ans -4 because -10/3=-3.33 and quotient is -4
# Lowest quotient is -3.33 and -4 is the lowest integer value so we get Ans -4
# this is opposite for +ve values because for +ve values we get the lowest integer value is 3.33 
# # and 3 is the lowest integer value so we get Ans 3

#9 Exponential Operator
# it gives the power of a number
a=2
b=3     
print("The Exponential of two values is :",a**b)
