"""VERY HARD - Py Master Mind"""

# Solution 1

from random import choices


def gen_colors(code_size: int) -> str:
    """Generate colors"""
    return "".join([chr(ord("A") + i) for i in range(min(26, max(0, code_size)))])


def gen_code(code_size: int, colors: str) -> str:
    """Generate the code"""
    return "".join(choices(colors, k=code_size))


def check_guess(guess: str, code_size: int, colors: str) -> bool:
    """Check guess"""
    return len(guess) == code_size and set(guess).issubset(colors)


def score_guess(code: str, guess: str) -> tuple:
    """Score guess"""
    exact = sum(1 for i in range(len(code)) if code[i] == guess[i])
    partial = sum(
        1 for i in range(len(code)) if code[i] != guess[i] and guess[i] in code
    )
    return (exact, partial)


print("Possible colors are ABCDEF\nCode is size 4.\nCODE = BFEB")
