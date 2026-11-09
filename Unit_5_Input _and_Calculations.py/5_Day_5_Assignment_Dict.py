
                  # multiple type Data input

# Prob .02_Takes multiple types of input from the user.Name,Height,age and Student Status
# Stores the data in a dictionary.Displays the collected data.

user_Data={}

user_Data['Name']=input("Enter the Student Name :")
user_Data['Age']=int(input("Enter the age of Student :"))
user_Data['Height']=int(input("Enter heght of student in CM :"))#here we can used float for Height in inch 
user_Data['Student_Status']=input("Enter the student Status (Yes/No):")

print(user_Data)
