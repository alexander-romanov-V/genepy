"""BASIC - Print every two letters pairs"""

# Solution 1
from string import ascii_lowercase

for a in ascii_lowercase:
    for b in ascii_lowercase:
        print(a + b)


# Solution 2
from itertools import product
from string import ascii_lowercase

for x in product(ascii_lowercase, repeat=2):
    print("".join(x))


# Solution 3
from string import ascii_lowercase
from itertools import starmap, product
from operator import add

print(*starmap(add, product(ascii_lowercase, repeat=2)), sep="\n")
