"""BASIC - Powers of two"""

# Solution 1
for i in range(10):
    print(2**i)


# Solution 2 - form a list and unpack it
print(*(2**i for i in range(10)), sep="\n")


# Solution 3 - for a list with side effects - calling print func
l = [print(2**i) for i in range(10)]
