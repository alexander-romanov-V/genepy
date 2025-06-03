"""HARD - Break a safe"""

# Solution 1 - my
import itertools
n = set()
for a in [1, 5, 8]:
    for b in itertools.permutations([1, 5, 8, a], 4):
        n.add(b)
for c in n:
    print(*c)


# Solution 2
import itertools
digits = (1, 5, 8)
for d in digits:
    for p in itertools.permutations(digits + (d,)):
        print(*p)


# Solution 3
import itertools
print(
    "\n".join(
        " ".join(d for d in p)
        for p in itertools.product("158", repeat=4)
        if len(set(p)) == 3
    )
)
