"""HARD - Simple adder"""

# Solution 1
from sys import argv
if len(argv) == 3:
    print(int(argv[1]) + int(argv[2]))
    print(sum([int(i) for i in argv[1:]]))
    print(sum(map(int, argv[1:])))
else:
    print("usage: python3 solution.py OP1 OP2")


# Solution 2
print(
    sum(map(int, __import__("sys").argv[1:]))
    if len(__import__("sys").argv) == 3
    else "usage: python3 solution.py OP1 OP2"
)
