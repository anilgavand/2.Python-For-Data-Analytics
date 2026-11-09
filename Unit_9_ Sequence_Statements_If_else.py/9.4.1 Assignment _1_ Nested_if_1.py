# Nested_If

# Problem Statement:1 System login with password 

usrname="Sneha@321"
password="India@123"

I_user=input(" Enter your username :")
I_password=input(" Enter your Password :")

if I_user==usrname:
    if I_password==password:
        print("Welcome, Login Sucessful")
    else:
        print("Wrong Password")
else:
    print(" Wrong Username ")


# Problem Statement:2 We have to approve permission to te student.

print("-----------------------------------------------------------")
print("          Validating of Student Entry                      ")
print("-----------------------------------------------------------")
Student=input("Enter Student Name :")
age=int(input("Enter student age :"))
if age>=18 and age<=26:
    id_number=int(input("Enter Id Number : "))
    print("Student Id Number :",id_number)
    if id_number>=1100 and id_number<=5000:
        print("Congratulation:You Can enter the Student hall")
    else:
        print("Better Luck for Next time")
else:
    print("Your age criteria doesen't Match")
print("-----------------------------------------------------------")


# Problem Statement:3  Secure Meeting Room Access System  
 
#1.The user must enter a security code.
#2.Ask the user to enter their department name.
#3.If the access level is 5 or higher

Security_Code=int(input("Enter the security Code :"))
Department=input("Enter your department :")
Acess_level=int(input("Enter Your Acesss Level:"))

if Security_Code>=1 and Security_Code<=22567:
    print("Security Code acess Sucessfully")
    if Department.lower()== "finance":
        print(" Welcome to finanace department")
        if Acess_level<=10:
            print(" Acess Granted")
        else:
            print("Acess not Granted")
    else:
        print("you entered wrong department")
else:
    print("Acess Denied")

