"""HARD - Longest Collatz sequence"""


# Solution 1 - my
def collatz_length(n):
    """Collatz sequence"""
    c = 0
    while n > 1:
        n = n * 3 + 1 if n % 2 else n // 2
        c += 1
    return c


# Solution 2 - my second
def collatz_length2(n):
    """Collatz sequence"""
    return 1 + collatz_length2(n * 3 + 1 if n % 2 else n // 2) if n > 1 else 0


if __name__ == "__main__":
    assert collatz_length(10) == 6
    assert collatz_length2(10) == 6
