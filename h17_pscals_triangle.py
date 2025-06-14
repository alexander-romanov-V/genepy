"""HARD - Pascal's triangle"""


# Solution 1 - my first
def print_pascal_triangle(height):
    t = []
    for h in range(height):
        tt = [1] * (h + 1)
        for x in range(1, h):
            tt[x] = t[h - 1][x] + t[h - 1][x - 1]
        t.append(tt)
    l = len(str(max(t[height - 1]))) + 1
    l += l % 2
    ll = l // 2

    for h in range(height):
        print(" " * (ll * (height - h - 1)), end="")
        for x in range(h + 1):
            print(f"{t[h][x]:^{l}}", end="")
        print()


if __name__ == "__main__":
    for i in range(1, 10):
        print_pascal_triangle(i)
