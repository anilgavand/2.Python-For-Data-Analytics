             
#Escape characters

'''
Escape characters are special character sequences used inside strings to represent 
characters that are difficult or impossible to type directly.

An escape character always starts with a backslash (\) followed by another character.

Common Escape Characters in Python Escape Character	Meaning

\n	New Line
\t	Horizontal Tab
\\	Backslash
\'	Single Quote
\"	Double Quote
\b	Backspace
\r	Carriage Return
\a	Alert/Bell Sound
\f	Form Feed
\v	Vertical Tab
'''

#Example 1.2 when the text contains an apostrophe (').

# print(' It's baby boy')  # Eroor=unterminated string literal (detected at line 35)

# print(" It's baby boy")  

# print(" It\'s baby boy")   # Here we used Escape Sequence\' before




# Example 1.3 Double Quotes

# We want output that : You are "Pass"

# print(" You are "Pass"") #SyntaxError: invalid syntax. Perhaps you forgot a comma?

# print(''' You are "Pass" ''')

# Example 1.3 Escape Sequence / Charaters_Double Quotes

# print("You are \"Pass\" ")  # Here we used \" before and after the required output word.


print("Hello \nWorld ") # Next Line \n 
print("Hello \tWorld ") # Tab for Spacing \t

