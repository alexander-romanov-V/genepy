"""HARD - Sequence Mining"""

from collections import Counter

# Solution 1 - my first
def seq_mining(l: list[str,], min_p: float, max_l: int) -> Counter:
    """
    Find number of sequences according passed patterns

    Args:
        l (list[str,]): list of strings (representing the sequences), such as:
        min_p (float): The minimum proportion of the number of sequences that must
            have this pattern for being taken into account (float between 0 and 1)
        max_l (int): The maximum pattern length that must be considered (int)

    Returns:
        dict[str, int]: a Counter, containing:
                            The found patterns as keys
                            The number of sequences containing this pattern as values

    """
    ...


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
