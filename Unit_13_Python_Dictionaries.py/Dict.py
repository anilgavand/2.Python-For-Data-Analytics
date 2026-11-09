# Dictionaries

student={"Name":"Anil","age":30,"City":"Pune"}
# # print(student)
# # #Accesing Values
# print(student["Name"])
# print(student["City"])

# # #adding and updating
# student["Marks"]=85
# student["City"]="Baramati"
# print(student)

# # #Removing Age
# student.pop("age")
# print(student)

# #Printing student key
# print(student.keys())
# print(student.values())
# print(student.items())
# print(student.get("Name"))

## Looping
for k in student:
    print(k,student[k])

# #Nested dictionary
# employee={
#     "EMP_01":{"Name":"Anil","City":"Pune"},
#     "EMP_02":{"Name":"Sachin","City":"Baramati"}
# }
# print(employee["EMP_01"]["Name"])

#mapping Wrong correct
mapper={
    "momboi":"Mumbai",
    "kolkatta":"Culcutta"
}
print(mapper["momboi"])
