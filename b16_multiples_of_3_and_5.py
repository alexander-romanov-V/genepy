"""BASIC - Multiples of 3 and 5"""

# Solution 1
print(sum(i for i in range(0, 1000) if i % 3 == 0 or i % 5 == 0))


# Solution 2
print(sum(i for i in range(0, 1000) if 0 in (i % 3, i % 5)))


# Solution 3
print(sum(i for i in range(0, 1000) if i % 3 * i % 5 == 0))
