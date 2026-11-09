## Example 4. Forwarding and backwording
fruits=["Banana","Apple","pear","Coconut"]
print(fruits)
fruits[1]="Graphes"
print(fruits)
print(fruits[0])  #Indexing forward
print(fruits[-1]) #indexing define with Backord
fruits.append("Papaya") #Appends addding papaya at the end
print(fruits)
fruits.insert(1,"Potato")  #inserting ptato in the position1
print(fruits)
fruits.remove("pear")
print(fruits)
fruits.pop(0) #this will remove zeroth position Banana
print(fruits)
print(fruits[:3]) #sicing Operation
print(fruits[-3:])
for f in fruits:     #For looping
    print("Fruit:",f)

