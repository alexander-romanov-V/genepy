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

N                           1   2   3   4   5   6   7   8       = N

число участков              1   2   3   4   5   6   7   8       = N
число строк на N-й участок  4   5   6   7   8   9   10  11      = N+3
ширина первой строки N-го   1   5   11  17  25  33  43  53      = x ????
(prev-1)/2                  0   2   5   8   12  16  21  26
prev+                           +2  +3  +3  +4  +4  +5  +5
N+                          -1  0   3   4   7   10  14  18
ширина последней строки Nго 7   13  21  29  39  49  61  73      = x+2*(N+2)
ширина ствола               1   3   3   5   5   7   7   9       = N//2*2+1
высота ствола               1   2   3   4   5   6   7   8       = N


"""

# Solution 1 - my first

from sys import argv


def fir_tree(n: int): ...


if __name__ == "__main__":
    try:
        n = int(argv[1])
    except (IndexError, ValueError):
        print(f"Usage: {argv[0]} N\n    N - size of fir tree\n")
        exit()
    if n > 0:
        fir_tree(n)
