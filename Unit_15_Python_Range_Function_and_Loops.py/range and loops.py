# Range and Loops

#1.Range:

#Range(Start,end,Step)
#range(end)----Here start is 0 by default and step are optional which is 1.
#range(start,end)--Here step is not givenits by default 1.
#range(Start,end,+Ve Increment) -- Here Start< end and increment is positive
#range(Start,end,-ve decrement) -- Here Start> end and decrement is negative

 # 1. end value alwaus Excluded.
 # 2. If end is used then start from zero and step is 1 by default with exclude end .
 # 3. For step increment Start must be less than end.   
 # 3. For Step decrement Start must be greater than end.
 # 4. Range is lazy sequence generator ex range(1,10000000) ex 1=28 byte =280m byte.if divide 1024 then MB ten GB then TB
        #for fast generation =list(range(1,10000000))

#2.For loop:(For Syntax)

#for i



# 1. for always used for sequence iteration.

# print("\n Print 1 to 5")
# for i in range(1,6):
#     print(i)


# print("\n Print Even Number :0-18")

# for i in range(0,18,2):
#     print(i)

# print("\n Print odd Number :0-20")

# for i in range(0,20,1):
#     print(i)

# ##Example Countdown
# print("\nCountdown from 10 to 1")
# for i in range(10,0,-1):
# #     print(i)

# iteam=["Pen","Book","Notebook","Rubber","Pencil"]
# for i in range(len(iteam)): #len Measuring iteams 
#     print(i,iteam[i])

# #Generate employee Id
# employee_id=[]
# for i in range(1,6):
#     print("Emp_Id:",i)

# print("\n List of Years :" )
# years=[]
# for y in range(2015,2026):
#     years.append(y)
#     print(years)  #we ahve to find out difference of print function


# print("\n List of Years :" )
# years=[]
# for y in range(2015,2026):
#     years.append(y)
# print(years)

# # # Using range function clean cities names

# cities=["mUMBAI","PunE","DELhi","ChEnnai"]    
# for i in range(len(cities)):
#     cities[i]=cities[i].strip().title()
# print(cities)

# print("\n7) Clean city names using range")
# cities = [" mUMbai", " DELhi", "pune "]
# for i in range(len(cities)):
#     cities[i] = cities[i].strip().title()
# print(cities)

#Finding out Last Four didgit
ids=["Emp-001233","Emp-001234","Emp-001235"]
for i in range(len(ids)):
    print(ids[i][-4:])

for i in range(1,4):
    for j in range(1,4):
        print(f"Print i :{i} Print j : {j}")
        
    