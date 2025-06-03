"""HARD - Print the first parameter"""

# Solution 1 - my
from sys import argv
if len(argv) == 2:
    print(argv[1])
else:
    print(f"usage: python3 {argv[0]} PARAM")


# Solution 2
# from sys import argv
print(argv[1] if len(argv) > 1 else "usage: python3 solution.py PARAM")


# Solution 3
# from sys import argv
try:
    print(argv[1])
except IndexError:
    print("usage: python3 solution.py PARAM")
