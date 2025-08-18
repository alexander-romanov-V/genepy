"""HARD - Calculator"""

# Solution 3

from sys import argv
# import operator
# operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv, "^": operator.pow, "%": operator.mod}
operators = {"+": int.__add__, "-": int.__sub__, "*": int.__mul__, "/": int.__truediv__, "%": int.__mod__, "^": int.__pow__}
if len(argv) == 4:
    try:
        print(operators[argv[2]](int(argv[1]), int(argv[3])))
    except (KeyError, ValueError, ZeroDivisionError):
        print("input error")
else:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
