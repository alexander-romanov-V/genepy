"""VERY HARD - Fir tree"""


# Solution 2

import sys

try:
    n = int(sys.argv[1])
    if n == 0:
        sys.exit()
except (IndexError, ValueError):
    print(f"Wrong or missing parameter!\nUsage: {sys.argv[0]} INTEGER")
    sys.exit()


r = []
l = 0
d = 0

for i in range(n):
    for j in range(4 + i):
        r += ["*" * (l - l % 2 + 1 + j * 2)]
    l = len(r[-1]) - int(d * 2 + 2)
    d += 0.5


for i in range(n):
    r += ["|" * (n + 1 - n % 2)]

lmax = max(map(len, r))

for l in r:
    print(l.center(lmax).rstrip())
