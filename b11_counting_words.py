"""BASIC - Counting Words"""

whetting_your_appetite = "Python is an easy to learn, powerful programming language. It has efficient high level data structures and a simple but effective approach to object oriented programming. This tutorial introduces the reader informally to the basic concepts and features of the Python language and system. For a description of standard objects and modules..."

# Solution 1
print(len(whetting_your_appetite.split()))

# Solution 2 - use RegEx
print(len(__import__("re").findall(r"\w+", whetting_your_appetite)))
