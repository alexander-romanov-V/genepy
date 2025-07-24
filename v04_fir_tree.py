"""VERY HARD - Fir tree

You'll write a Python 3 program drawing a fir tree.

The size of the drawed fir tree will depend on the single parameter given to
your program. As always, print a human error message if no parameter are
given to your program.

Given 0, your program should display nothing.

Advice
You can test is for several values of the parameter here:
https://sapin.hackinscience.org/?n=10
https://sapin.hackinscience.org/?n=5
etc...


N                           1   2   3   4   5   6   7   8   9   10
Blocks                      1   2   3   4   5   6   7   8   9   10      = N
Lines in Nth block          4   5   6   7   8   9   10  11  12  13      = N+3
Wfirst_lines in 1th block  [1]  5   11  17  25  33  43  53  65  77  = x = y[-1] - N//2*2  (x = 1 for N==1, y[-1] -> y of previous block)
Wlast_lines in Nth block    7   13  21  29  39  49  61  73  87  101 = y = x + 2*(N+2)
Wbar                        1   3   3   5   5   7   7   9   9   11      = 1 + N//2*2
Hbar                        1   2   3   4   5   6   7   8   9   10      = N

"""

# Solution 1 - my first

from sys import argv


def fir_tree(n: int):
    w1 = []
    y = 1
    for i in range(n):
        x = y - (i + 1) // 2 * 2
        y = x + 2 * (i + 3)
        w1.append((x, y))
    for b in range(n):
        for bl in range(w1[b][0], w1[b][1] + 1, 2):
            print(f"{'*'*bl:^{w1[-1][1]}}")
    for b in range(n):
        print(f"{'|'*(1 + n // 2 * 2):^{w1[-1][1]}}")


if __name__ == "__main__":
    fir_tree(1)
    fir_tree(2)
    fir_tree(3)
    # try:
    #     n = int(argv[1])
    # except (IndexError, ValueError):
    #     print(f"Usage: {argv[0]} N\n    N - size of fir tree\n")
    #     exit()
    # if n > 0:
    #     fir_tree(n)
