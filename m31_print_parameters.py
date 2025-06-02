"""MEDIUM - Print parameters"""

# Solution 1 - my [but actually it needs to print only script name]
# print(*(p for p in __import__("sys").argv), sep="\n")


# Solution 2 - my second
print(__import__("sys").argv[0])
