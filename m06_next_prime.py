"""MEDIUM - Next prime"""

# Provide a script that computes, then prints the first prime number greater than 100_000_000.

# Solution 1 - too slow for large numbers
def next_prime():
    """Returns next prime"""
    yield 2
    primes = [2]
    i = 3
    while True:
        if all(i % p > 0 for p in primes):
            primes.append(i)
            yield i
        i += 2


# Solution 2
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
    # Solution 1 - too slow for large numbers
    # for p in next_prime():
    #     if p > 100000000:
    #         print(p)
    #         break

    # Solution 2
    n = 100000001
    while not is_prime(n):
        n += 2
    print(n)
