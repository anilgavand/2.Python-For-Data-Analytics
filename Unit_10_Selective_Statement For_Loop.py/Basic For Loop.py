# Loops in Python

'''
Loops enable you to perform repetitive 
tasks efficiently without writing redundant code.
They iterate over a sequence (like a list, tuple, string, or range)
or execute a block of code as long as a specific condition is met.

Types of Loops in Python

1.While Loop
2.For Loop
3.Nested Loop

'''
'''
2.For Loop:

A for loop is used when you want to iterate over a sequence like:

1.String
2.List
3.Tuple
4.Dictionary
5.Set

Instead of checking a condition manually (like while),
Python automatically takes each element one by one.

Rule:

Use while when repetition depends on a condition.
Use for when iterating through a sequence or a known number of times.

Comparison

While loop:

1.While loop works on a condition.
2.While loop is preferred when the number of repetitions is unknown.
3.While loop requires manual control of the loop variable.
4.While loop is more flexible for condition-based problems.

For loop:

1.For loop works on a sequence or range.
2.For loop is preferred when the number of repetitions is known.
3.For loop automatically manages the loop variable.
4.For loop is simpler and more readable for iteration tasks.
'''
# Example1. For Loop

language = "Python"

for x in language:
    print(x)

