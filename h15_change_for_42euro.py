"""HARD - Change for 42€"""

# Solution 0 - my (too slow)
outer = set()
inner = []
def changes(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""
    e = sorted([c for c in coins if c <= amount], reverse=True)
    if len(e) > 0:
        for c in list(e):
            inner.append(c)
            changes(amount - c, coins)
            inner.pop()
    else:
        outer.add(tuple(sorted(inner)))
        # inner.clear()
        return
    return len(outer)


if __name__ == "__main__":
    for y in range(2, 13):
        x = changes(y, (1, 2, 5, 10, 20, 50, 100, 200, 500))
        print(f"{y}: {x}")
