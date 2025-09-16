"""MEDIUM - Sum of every prime number below n"""



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

def sum_primes(n: int) -> int:
    """Sum of every prime number below n"""
    return sum(i for i in range(n) if is_prime(i))



# Solution 2
def sum_primes2(n: int) -> int:
    """Sum of every prime number below n"""
    return sum(i for i in range(2, n) if not any(i % z == 0 for z in range(2, int(i**0.5) + 1)))


# Solution 3
def sum_primes3(n: int) -> int:
    """Sum of every prime number below n"""
    if n < 2:
        return 0
    sieve = [True] * (n // 2)
    for i in range(3, int(n**0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = [False] * ((n - i * i - 1) // (2 * i) + 1)
    return 2 + sum((2 * i + 1) for i in range(1, n // 2) if sieve[i])


# Solution 4
def sum_primes4(n: int) -> int:
    """Sum of every prime number below n"""
    primes = [2]
    prime_sum = 2 * (n > 1)
    i = 3
    while i < n:
        if all(i % p > 0 for p in primes):
            primes.append(i)
            prime_sum += i
        i += 2
    return prime_sum


if __name__ == "__main__":
    print(sum_primes(10))
    print(sum_primes2(10))
    print(sum_primes3(10))
    print(sum_primes4(10))
