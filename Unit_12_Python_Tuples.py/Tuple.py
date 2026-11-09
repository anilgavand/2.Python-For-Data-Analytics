# Creating tupple

# fruits=("Banana","Apple","Mango","Papaya","Potatao")
# print(fruits)
# print(fruits[:3])
# print(fruits[-3:]) #indexing
# print(fruits[1:4]) #Slicing
# # Looping in the tupple
# for i in fruits:
#     print(i)
# #Tuple length
# print(" Tupple lenth is : ",len(fruits))

# #concatenate
# a=(3,4)
# b=(5,6)
# print(a+b)

# #packing and unpacking
# data=("Laptop",4500,"Black")
# Product,price,colour=data
# print(Product,price,colour)

# #Applying F string
# print(f"Product :{Product} Price :{price} and Colour :{colour}")

#Nested Tupple
employee=[("EMP_01","Sachin","Wagholi"),("EMP_02","Maruti","Hadpsar")]
for eid,name,city in employee:
        print(eid,name,city)

