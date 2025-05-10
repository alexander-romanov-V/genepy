"""MEDIUM - Print every prime numbers in a range"""


# Solution 1
def is_prime(n: int) -> bool:
    """Primarily test using 6k+-1 optimization."""
    if n <= 3:
        return n > 1
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i**2 <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


if __name__ == "__main__":
    print(*[i for i in range(10000, 10051) if is_prime(i)], sep=", ")
