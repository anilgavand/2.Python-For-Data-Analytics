# # Sets

# #repeated values are automatically deleted

# Fruits={"Banana","Apple","Coconut","Pear","Apple"}
# print(Fruits)

# #working on the sets

# Fruits.add("Grapes")
# print(Fruits)

# #removing Fruit
#difference between Pop and Discard Function

# Fruits.discard("Banana") 
# print(Fruits)

# #Set operations
# a={1,2,3}
# b={3,4,5}

# print("union :",a|b)
# print("Intersection :",a&b)
# print("Difference :",a-b)
# print("Difference :",b-a)
# print("Symmetric Difference :",a^b)

# #Remove duplicate
# cities=["Mumbai","Pune","Delhi","Mumbai"] #This is the list in Squre Bracket
# unique=set(cities) #set remove duplicate values
# print("Unique Cities :",unique)

# ## Missing Values

# list_1={"SQL","Python","Power BI"} #set1
# list_2={"SQL","Python"} #set2
# missing=list_1-list_2
# print("Missing :",missing)

## Common Skill

Dept_1={"SQL","Python","Power BI"} #set1
Dept_2={"SQL","Python"} #set2

print("Common Skill is :",Dept_1&Dept_2)


