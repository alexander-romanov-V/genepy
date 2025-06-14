"""HARD - Pascal's triangle"""


# Solution 1
def print_pascal_triangle(height):
    t = []
    for h in range(height):
        tt = [1] * (h + 1)
        for x in range(1, h):
            tt[x] = t[h - 1][x] + t[h - 1][x - 1]
        t.append(tt)
    for h in range(height):
        print(" "*(height-h),*t[h])
    # l = len(str(max(t[height - 1])))
    # for h in range(height):
    #     if h % 2 == 0:
    #         print("-" * (l // 2), end="")
    #     print("+" * (l * (height - h - 2)), end="")
    #     for x in range(h+1):
    #         print(f"{t[h][x]:^{l}}", end=" ")
    #     print()


if __name__ == "__main__":
    print_pascal_triangle(10)
