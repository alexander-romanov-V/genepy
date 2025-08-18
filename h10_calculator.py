"""HARD - Calculator"""

# Solution 1 - my first

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
