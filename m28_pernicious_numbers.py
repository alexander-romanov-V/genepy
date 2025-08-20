"""MEDIUM - Pernicious numbers"""


# Solution 1 - my first
def is_prime(n):
    """True if n is prime"""
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))

for n in range(222281, 222381):
    if is_prime(bin(n).count("1")):
        print(n)


# Solution 1b - my second
print(*(n for n in range(222281, 222381) if is_prime(bin(n).count("1"))), sep="\n")


# Solution 2 - my third
print(*(n for n in range(222281, 222381)
        if bin(n).count("1") > 1
        and all(bin(n).count("1") % i for i in range(2, int(bin(n).count("1") ** 0.5) + 1))),
    sep="\n")
