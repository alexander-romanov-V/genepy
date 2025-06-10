"""HARD - Change for 42€"""

# Solution 0 - my (too slow)
# outer = set()
# inner = []
# def changes(amount, coins):
#     """Returns how many set of change can be made for a given amount and a set of coins"""
#     e = sorted([c for c in coins if c <= amount], reverse=True)
#     if len(e) > 0:
#         for c in list(e):
#             inner.append(c)
#             changes(amount - c, coins)
#             inner.pop()
#     else:
#         outer.add(tuple(sorted(inner)))
#         # inner.clear()
#         return
#     return len(outer)


# Solution 1 - my first
def changes(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""
    e = sorted([c for c in coins if c <= amount], reverse=True)
    res = 0
    if len(e) <= 1:
        return 1
    for c in range(0, amount + 1, e[0]):
        res += changes(amount - c, e[1:])
    return res


# Solution 2 - my second - condensed & improved
def changes2(amount, coins):
    """Returns how many set of change can be made for a given amount and a set of coins"""
    res = 0
    for c in range(0, amount + 1, coins[-1]):
        res += 1 if len(coins) <= 2 else changes2(amount - c, coins[:-1])
    return res


if __name__ == "__main__":
    for y in range(2, 43):
        x = changes2(y, (1, 2, 5, 10, 20, 50, 100, 200, 500))
        print(f"{y}: {x}")
