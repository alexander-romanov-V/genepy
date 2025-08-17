"""BASIC - Print sorbet flavors"""

FLAVORS = [
    "Banana",
    "Chocolate",
    "Lemon",
    "Pistachio",
    "Raspberry",
    "Strawberry",
    "Vanilla",
]

# Solution 1
from itertools import starmap, combinations
print(*starmap(lambda a, b: a + ", " + b, combinations(FLAVORS, 2)), sep="\n")


# Solution 2
print(*(", ".join(c) for c in __import__("itertools").combinations(FLAVORS, 2)), sep="\n")
