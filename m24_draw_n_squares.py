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
    print(draw_n_squares(1))
    print(draw_n_squares(3))
    print(draw_n_squares(5))

    print(draw_n_squares2(1))
    print(draw_n_squares2(3))
    print(draw_n_squares2(5))
