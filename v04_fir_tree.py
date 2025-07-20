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
    fir_tree(n)
