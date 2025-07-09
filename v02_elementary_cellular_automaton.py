"""VERY HARD - Elementary cellular automaton"""

from sys import argv


# Solution 1 - my first
def solution1():
    """Build a program taking an integer as single parameter, .
    This integer is a rule number in the Wolfram code.
    Your program will display a 79×40 table filled with # for ones (1s) and . for zeroes (0s), as a result
    of running an elementary automata for the given rule number (the int parameter).
    The first line will always be filled with zeroes except for a single cell with a 1 right in the middle.
    The "board" is a cylinder: on the left of the leftmost column is the rightmost column, and vice-versa.
    """
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
    """Elementary cellular automaton"""
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


# Solution 3
def solution3():
    """Elementary cellular automaton"""
    try:
        rules_number = int(argv[1])
        # rules_number = 90
    except (ValueError, IndexError):
        print(f"Wrong parameter, usage : {argv[0]} NUMBER")
        exit(1)

    WIDTH = 79
    HEIGH = 40

    rules = [int(f"{rules_number:08b}"[7 - i]) for i in range(8)]

    cells = [0] * WIDTH
    cells[WIDTH // 2] = 1

    for _ in range(HEIGH):
        print("".join(".#"[c] for c in cells))
        cells = [
            rules[4 * cells[i - 1] + 2 * cells[i] + cells[(i + 1) % WIDTH]]
            for i in range(WIDTH)
        ]


# Solution 4 - my best
def solution4():
    """Elementary cellular automaton"""
    try:
        n = int(argv[1])
    except (ValueError, IndexError):
        print(f"usage: {argv[0]} N\n\tN - rule number = 0..255")
        exit(1)

    line = [0] * 39 + [1] + [0] * 39
    rule = [int(f"{n:08b}"[7 - i]) for i in range(8)]

    for _ in range(40):
        print("".join(".#"[c] for c in line))
        line = [rule[4 * line[i - 1] + 2 * line[i] + line[(i + 1) % 79]] for i in range(79)]


if __name__ == "__main__":
    solution1()
    solution2()
    solution3()
    solution4()
