"""MEDIUM - Common Lines"""

# Solution 1 - my

from sys import argv, stderr
from functools import reduce

if __name__ == "__main__":
    if len(argv) < 3:
        stderr.write(f"usage: {argv[0]} file1.txt file2.txt [...]")
        exit(1)
    try:
        files = [set(open(argv[i], "r", encoding="UTF-8").read().split()) for i in range(1, len(argv))]
    except FileNotFoundError:
        stderr.write("Error reading input file!")
        exit(2)
    if r := reduce(lambda a, b: a & b, files):
        print(*r, sep="\n")
    else:
        exit(3)
