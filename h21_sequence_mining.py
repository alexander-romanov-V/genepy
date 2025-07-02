"""HARD - Sequence Mining"""

from collections import Counter


# Solution 1 - my first
def seq_mining(data: list[str,], min_p: float, max_l: int) -> Counter:
    """
    Find number of sequences according passed patterns
    Args:
        l (list[str,]): list of strings (representing the sequences), such as:
        min_p (float): The minimum proportion of the number of sequences that must
            have this pattern for being taken into account (float between 0 and 1)
        max_l (int): The maximum pattern length that must be considered (int)
    Returns:
        Counter: a Counter, containing: The found patterns as keys and
            The number of sequences containing this pattern as values
    """
    res = Counter()
    for e in data:
        c = Counter()
        for le in range(min(max_l, len(e))):
            for i in range(len(e) - le):
                c[e[i : i + le + 1]] = 1
        res += c

    for r in res:
        if res[r] < len(data) * min_p:
            res[r] = 0

    return +res


if __name__ == "__main__":
    data = ["ABCD", "ABABC", "BCAABCD"]
    result1 = {
        "A": 3,
        "AB": 3,
        "ABC": 3,
        "B": 3,
        "BC": 3,
        "BCD": 2,
        "C": 3,
        "CD": 2,
        "D": 2,
    }
    result2 = {
        "A": 3,
        "AB": 3,
        "ABC": 3,
        "ABCD": 2,
        "B": 3,
        "BC": 3,
        "BCD": 2,
        "C": 3,
        "CD": 2,
        "D": 2,
    }
    result3 = {"A": 3, "AB": 3, "B": 3, "BC": 3, "C": 3, "CD": 2, "D": 2}

    assert seq_mining(data, 0.34, 3) == result1
    assert seq_mining(data, 0.34, 4) == result2
    assert seq_mining(data, 0.50, 2) == result3
