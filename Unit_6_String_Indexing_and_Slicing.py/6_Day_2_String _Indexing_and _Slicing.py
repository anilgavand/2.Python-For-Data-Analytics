# #6.1 string Indexing and Slicing

# Syntax : string[start:end:step]
# Start : the index start slicing (inclusive).Default value is 0.
# Start : the index start slicing (exclusive).Default value is length of string.

Name="DataAnalytics"

print("First Word strait is :",Name[:4])
print("First Word strait is :",Name[2:4:2])
print("Second Word Strait is :",Name[4:13])               #Here we didnot need to define end due to last word still we defined
print("Second Word Strait is :",Name[4:])                 #Here we didnot need to define end due to last word
print("Second Word Reverse is :",Name[-9:])               #Here we didnot need to define end due to last word by -1
print("Second Word is Reverse is :",Name[-13:-9])
print(Name[:])
print(Name[::])



# Example :String Slicing

Name_name ="Anil Gavand"



