"""BASIC - Square numbers"""

# Solution 1
for i in range(10):
    print(i**2)

# Solution 2 - form a list and unpack it
print(*(i * i for i in range(10)), sep="\n")

# Solution 3 - for a list with side effects - calling print func
l = [print(i * i) for i in range(10)]
