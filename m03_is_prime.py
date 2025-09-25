"""MEDIUM - Check if a number is prime"""



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



# Solution 2
def is_prime2(n):
    """Primarily test with less optimization."""
    if n <= 3:
        return n > 1
    i = 2
    while i * i <= n:
        if n % i == 0:
            return False
        i += 1
    return True


# Solution 3
def is_prime3(n):
    """True if n is prime"""
    return n > 1 and all(n % i != 0 for i in range(2, int(n**0.5) + 1))


if __name__ == "__main__":
    
    for p in (is_prime, is_prime2, is_prime3):
        assert p(1) is False
        assert p(2) is True
        assert p(3) is True
        assert p(4) is False
        assert p(271) is True
        assert p(272) is False
        assert p(5) is True
        assert p(29) is True
        
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")
