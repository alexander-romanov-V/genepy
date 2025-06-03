"""HARD - Consecutive Sum"""


# Solution 1 - my
def find_consecutive_sum(n):
    """Takes an integer n and returns a triplet of consecutive integers
    (a, b, c) such that a + b + c == n."""
    return None if n % 3 else (n // 3 - 1, n // 3, n // 3 + 1)


if __name__ == "__main__":
    assert find_consecutive_sum(15) == (4, 5, 6)
    assert find_consecutive_sum(10) is None
