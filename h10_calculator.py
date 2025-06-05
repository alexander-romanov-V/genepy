"""HARD - Calculator"""


# Solution 1 - my first
"""
from sys import argv
if len(argv) == 4:
    try:
        match argv[2]:
            case "+":
                print(int(argv[1]) + int(argv[3]))
            case "-":
                print(int(argv[1]) - int(argv[3]))
            case "*":
                print(int(argv[1]) * int(argv[3]))
            case "/":
                print(int(argv[1]) / int(argv[3]))
            case "%":
                print(int(argv[1]) % int(argv[3]))
            case "^":
                print(int(argv[1]) ** int(argv[3]))
            case _:
                raise ValueError
    except ValueError:
        print("input error")
else:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")
"""


# Solution 2 - my second
from sys import argv
if len(argv) == 4:
    try:
        if argv[2] not in "+-*/%^":
            raise SyntaxError
        if argv[2] == "^":
            argv[2] = "**"
        print(eval(''.join(argv[1:])))
    except:
        print("input error")
else:
    print("usage: ./solution.py a_number (an_operator +-*/%^) a_number")


"""
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

"""