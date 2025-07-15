"""HARD - Pascal's triangle"""


# Solution 1 - my first
def print_pascal_triangle(height):
    """Print Pascal's triangle"""
    t = []
    for h in range(height):
        tt = [1] * (h + 1)
        for x in range(1, h):
            tt[x] = t[h - 1][x] + t[h - 1][x - 1]
        t.append(tt)
    l = len(str(max(t[height - 1]))) + 1
    l += l % 2

    for h in range(height):
        print(" " * (l // 2 * (height - h - 1)), end="")
        for x in range(h + 1):
            print(f"{t[h][x]:^{l}}", end="")
        print()


# Solution 2 - my second
def print_pascal_triangle2(height):
    """Print Pascal's triangle"""
    t = [[1]]
    for h in range(1, height):
        t.append([1] + [sum(t[h - 1][x - 1 : x + 1]) for x in range(1, h)] + [1])
    l = (len(str(max(t[height - 1]))) + 2) // 2
    for h in range(height):
        print(" " * (l * (height - h - 1)), *[f"{t[h][x]:^{l*2}}" for x in range(h + 1)], sep="")


# # Solution - not aligned
# def print_pascal_triangle2(height):
#     if height == 1:
#         print(1)
#         return [1]
#     prev = print_pascal_triangle2(height - 1)
#     bottom = [1] + [a + b for a, b in zip(prev[:-1], prev[1:])] + [1]
#     print(*bottom)
#     return bottom


if __name__ == "__main__":
    for p in (print_pascal_triangle, print_pascal_triangle2):
        for i in range(1, 11):
            print(f"\n{p.__name__}({i})")
            p(i)
