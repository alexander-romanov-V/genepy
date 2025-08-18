"""HARD - Calculator"""

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
