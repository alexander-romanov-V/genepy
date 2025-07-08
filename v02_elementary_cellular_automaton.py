"""VERY HARD - Elementary cellular automaton"""

from sys import argv


# Solution 1 - my first
def solution1():
    """Build a program taking an integer as single parameter, .
    This integer is a rule number in the Wolfram code.
    Your program will display a 79×40 table filled with # for ones (1s) and . for zeroes (0s), as a result 
    of running an elementary automata for the given rule number (the int parameter).
    The first line will always be filled with zeroes except for a single cell with a 1 right in the middle.
    The "board" is a cylinder: on the left of the leftmost column is the rightmost column, and vice-versa."""
    try:
        n = int(argv[1])
        if n < 0 or n > 255:
            raise ValueError
    except (ValueError, IndexError):
        print(f"usage: {argv[0]} N\n\tN - rule number = 0..255")
        exit()
    # n = 30
    w = 79
    line, line_2 = [0] * w, [0] * w
    line[w // 2] = 1

    rule = dict()
    for i in range(8):
        r = n % 2
        n //= 2
        rule[i // 4 % 2, i // 2 % 2, i % 2] = r

    for _ in range(40):
        print("".join(("#" if c else ".") for c in line))
        line_2[0] = rule[(line[w - 1], line[0], line[1])]
        line_2[w - 1] = rule[(line[w - 2], line[w - 1], line[0])]
        for i in range(1, w - 1):
            line_2[i] = rule[tuple(line[i - 1 : i + 2])]
        line, line_2 = line_2, line


# Solution 2 - my second
def solution2():
    try:
        n = int(argv[1])
        if n < 0 or n > 255:
            raise ValueError
    except (ValueError, IndexError):
        print(f"usage: {argv[0]} N\n\tN - rule number = 0..255")
        exit()
    # n = 90
    line = [0] * 39 + [1] + [0] * 39

    rule = dict()
    for i in range(8):
        rule[i // 4 % 2, i // 2 % 2, i % 2] = n % 2
        n //= 2

    for _ in range(40):
        print("".join(("#" if c else ".") for c in line))
        line = [line[-1]] + line + [line[0]]
        line = [rule[tuple(line[i - 1 : i + 2])] for i in range(1, 80)]


