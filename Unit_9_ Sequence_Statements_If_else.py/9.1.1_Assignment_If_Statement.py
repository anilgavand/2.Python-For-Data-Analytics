# Admission criteria

# Solution :01

# Input marks for each subject

# math = int(input("Enter the Math Marks: "))
# phy = int(input("Enter the Physics Marks: "))
# chem = int(input("Enter the Chemistry Marks: "))

# # Calculate total marks combinations

# total_marks_all = math + phy + chem
# total_marks_math_phy = math + phy

# # Check eligibility criteria

# if (math >= 65 and phy >= 55 and chem >= 50) and (total_marks_all >= 180 or total_marks_math_phy >= 140):
#     print("You qualified based on individual scores!")
#     print("Welcome! You qualified for the second stage. You are in!")
# else:
#     print("Better luck next time!")
#     print("You do not have the valid total marks or individual scores required.")


#Solution 02:

# Input marks for each subject

Maths_marks = int(input("Enter the Math Marks: "))
physics_marks = int(input("Enter the Physics Marks: "))
Chemistry_marks = int(input("Enter the Chemistry Marks: "))

total_marks_all = Maths_marks+physics_marks+Chemistry_marks
total_marks_math_phy = Maths_marks+physics_marks

# Eligibility check logic matching the image structure
if (Maths_marks >= 65 and 
    physics_marks >= 55 and 
    Chemistry_marks >= 50 and 
    (total_marks_all) >= 180 and 
    (total_marks_math_phy) >= 140):
    
    print("You're eligible!")
else:
    print("You're not eligible!")


# Input marks for each subject
Maths_marks = int(input("Enter the Math Marks: "))
physics_marks = int(input("Enter the Physics Marks: "))
Chemistry_marks = int(input("Enter the Chemistry Marks: "))

# Solution: 03 

# Step-by-step evaluation using only if-else conditions

if Maths_marks >= 65:
    if physics_marks >= 55:
        if Chemistry_marks >= 50:
            if (Maths_marks + physics_marks + Chemistry_marks) >= 180:
                if (Maths_marks + physics_marks) >= 140:
                    print("You're eligible!")
                else:
                    print("You're not eligible!")
            else:
                print("You're not eligible!")
        else:
            print("You're not eligible!")
    else:
        print("You're not eligible!")
else:
    print("You're not eligible!")


# Solution : 04

# Input marks for each subject

Maths_marks = int(input("Enter the Math Marks: "))
physics_marks = int(input("Enter the Physics Marks: "))
Chemistry_marks = int(input("Enter the Chemistry Marks: "))

# Check for failure conditions one by one using if-elif
if Maths_marks < 65:
    print("You're not eligible!")
elif physics_marks < 55:
    print("You're not eligible!")
elif Chemistry_marks < 50:
    print("You're not eligible!")
elif (Maths_marks + physics_marks + Chemistry_marks) < 180:
    print("You're not eligible!")
elif (Maths_marks + physics_marks) < 140:
    print("You're not eligible!")
else:
    # If none of the failure conditions above match, they must be eligible
    print("You're eligible!")
