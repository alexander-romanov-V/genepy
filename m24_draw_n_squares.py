"""MEDIUM - Draw N Squares"""


# Solution 1
def draw_n_squares(n):
    """Returns a string of squares"""
    a = "+" + "---+" * n + "\n"
    b = "|" + "   |" * n + "\n"
    return a + (b + a) * n


# Solution 2
def draw_n_squares2(n):
    """Returns a string of squares"""
    return ("+" + "---+" * n + "\n|" + "   |" * n + "\n") * n + "+" + "---+" * n


if __name__ == "__main__":
    for p in (draw_n_squares, draw_n_squares2):
        print(f"{p.__name__:20}")
        for n in (1, 3, 5):
            print(p(n))
