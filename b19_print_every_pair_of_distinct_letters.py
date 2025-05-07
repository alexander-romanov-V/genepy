"""BASIC - Print every pair of distinct letters"""

# Solution 1
from string import ascii_lowercase

for a in ascii_lowercase:
    for b in ascii_lowercase:
        if a != b:
            print(a + b)

# Solution 2
from itertools import product
from string import ascii_lowercase

for a, b in product(ascii_lowercase, repeat=2):
    if a != b:
        print(a + b)


# Solution 3
from string import ascii_lowercase
from itertools import starmap, permutations
from operator import add

print(*starmap(add, permutations(ascii_lowercase, 2)), sep="\n")


# Solution 4
from string import ascii_lowercase

print(
    "\n".join(
        ["%s%s" % (i, j) for i in ascii_lowercase for j in ascii_lowercase if i != j]
    )
)
