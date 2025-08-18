"""HARD - Calculator"""

# Solution 4 (but 5 / 2 is 2, not 2.5)

from sys import argv

prog, *arg = argv
if len(arg) != 3:
    print(f"usage: {prog} a_number (an_operator +-*/%^) a_number")
else:
    for o, po in zip("/^", ("//", "**")):
        arg[1] = arg[1].replace(o, po)
    try:
        print(eval(" ".join(arg)))
    except:
        print("input error")
