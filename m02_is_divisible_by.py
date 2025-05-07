"""MEDIUM - Is divisible by ?"""

# Find and print all numbers between from 0 to 1000 (both included),
# that are divisible by 7 and whose digits sum are divisible by 3.


# Solution 1
def digit_sum(n):
    """Returns digits sum of n"""
    return n if n < 10 else digit_sum(n // 10) + n % 10
print(*(n for n in range(0, 1001, 7) if digit_sum(n) % 3 == 0), sep="\n")

# Solution 1b
digit_sum = lambda n: n if n < 10 else digit_sum(n // 10) + n % 10
print(*(n for n in range(0, 1001, 7) if digit_sum(n) % 3 == 0), sep="\n")

# Solution 2
print(*(n for n in range(0, 1001, 7) if sum(map(int, str(n))) % 3 == 0), sep="\n")

# Solution 2
print(*(n for n in range(0, 1001, 21)), sep="\n")

# Solution 2b
print("\n".join(f"{n}" for n in range(0, 1001, 21)))
