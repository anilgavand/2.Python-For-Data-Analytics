# STRINGS Methods

# String is sequence and immutable(No change) data type.

# 1. Single Quote ' '             ---It's hence we avoid
# 2. Double Quote  '' ''          ---IT's is valid here
# 3. Tripple Quote """"  """"     --- This is multi line string

# string is sequence type 
#          -5    -3  -1   ---- Backword Indexing
#           P Y T H O N
#           0 1 2 3 4 5   ---- Forward Indexing

'''
Method	Purposelen()	Length of string
upper()	Convert to uppercase
lower()	Convert to lowercase
strip()	Remove leading/trailing spaces
count()	Count occurrences
find()	Find position of substring
title()	Capitalize each word
split()	Convert string into list
replace()	Replace substring

Important: Except len(),
all of the above are string methods and are called using the dot (.)
operator on a string object.
'''
# #Example 1. Removing Spacea from Leading and trailing

# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Remove Spaces output : ",Text.strip())

#Eaxmple 2. Upper Letters

# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Remove Spaces output : ",Text.strip())
# print("Upper Letter output:",Text.upper())

#Here we used strip function otherwise it leading and trailing space is remain same as pe the
# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.upper().strip())

# #or
# Text="     Hello learners Python    "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.upper()
#                                 .strip())

# strip = All Space from left and right removing.
# rsrtip = Space from right side removing.
# lstrip = Space from left side removing.

#Eaxmple 3. Proper Letters

# Text="     hello python learners   "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.title()
#                                 .strip())

#Eaxmple 4. Lowers Letters

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Upper Letter output:",Text.lower()
#                                 .strip())

# #Eaxmple 5. replace Word

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Replace Python Word by SQL:",Text.replace("Python","SQL")
#                                 .strip())

# #Eaxmple 6.Count occurance of word

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Replace Python Word by SQL:",Text.replace("Python","SQL")
#                                 .strip())
# print("Count of O is:",Text.count("o"))

# #Eaxmple 7.Start with some Word

# Text="     Hello Python Learners   "
# print("Original Text :",Text)
# print("Replace Python Word by SQL:",Text.replace("Python","SQL")
#                                 .strip())
# print("Count of O is:",Text.count("o"))
# print("Start with Word ?:",Text.strip().startswith("Hello")) #Here we used strip function to remove space before the word.

# # #Eaxmple 8.Data is Numeric

# mobile="9823565726"
# print("Data is numeric ?:",mobile.isnumeric())
# mobile1=" Masters in data science"
# print("Data is numeric ?:",mobile1.isnumeric())

# #Eaxmple 9.Split function used

# Word="Welcome to goa Sinhgam"
# print("Word is as per following:",Word.split())
# Joined_Text="".join(Word)
# print("Joined Texts:",Joined_Text)

# # #Eaxmple 10.Joined back with hyphen
# Word="Welcome to goa Sinhgam"
# Joined_Text="".join(Word)
# print("Joined Texts:",Joined_Text)

# ## Example .11 finding position of g
# Word="Welcome to goa Sinhgam"
# print("Find the position of g :",Word.find("g"))

## Example .12 Extract diomain

email="student@example.com"
domain = email[email.find("@")+1:]
print=("The domain Name is:",domain)


















