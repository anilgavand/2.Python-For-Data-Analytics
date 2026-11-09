# # Number Separation Logic: Splitting Digits

# n=int(input("Enter the Value : "))
# m=1
# while n > 0:
#     r =n % 10
#     m =m * r
#     n = n // 10
# print("The multiplication is :", m )



# n = int(input("Enter the Value : "))
# m = 1
# while n > 0:
#     r = n % 10
#     m = m * r
#     n = n // 10  # Fixed: updates the value of n
# print("The multiplication of the digits is :", m)




# Example : Armstrong number

#An Armstrong number (or narcissistic number) is a number that is equal to the sum of its own digits each raised to 
# the power of the total number of digits.For example, $153$ is a 3-digit number where:$1^3 + 5^3 + 3^3 = 1 + 125 + 27 = 153$

# n=input("Enter the Number :")
# cnt=len(n)
# n=int(n)
# dn=n
# sm=0
# while n>0:
#     r= n % 10
#     sm=sm+r**cnt
#     n= n // 10
#     if sm==dn:
#         print("The number is Armstrong :",dn)
# print("The number is not Armstrong :",dn)

# # method 2:

# n = int(input("Enter the Value : "))
# temp = n
# num_digits = len(str(n))
# sum_val = 0

# # Extracting and raising digits using a while loop
# while n > 0:
#     r = n % 10
#     sum_val += r ** num_digits
#     n = n // 10

# # Checking if the sum equals the original number
# if temp == sum_val:
#     print(temp, "is an Armstrong number.")
# else:
#     print(temp, "is not an Armstrong number.")


# Example : 03 We have to find Armstrong number in 10000

for n in range(0,10001,1):
      cnt=len(str(n))
      n=int(n)
      dn=n
      sm=0
      while n>0:
       r= n % 10
       sm=sm+r**cnt
       n= n // 10
      if sm==dn:
        print("The number is Armstrong :",dn)

# Example : 04 Printing number in reverse direction.
