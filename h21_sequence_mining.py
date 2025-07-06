"""HARD - Sequence Mining"""

from collections import Counter


# Solution 1 - my first
def seq_mining(data: list[str], min_p: float, max_l: int) -> Counter[str]:
    """
    Find number of sequences according passed patterns
    Args:
        l (list[str]): list of strings (representing the sequences), such as:
        min_p (float): The minimum proportion of the number of sequences that must
            have this pattern for being taken into account (float between 0 and 1)
        max_l (int): The maximum pattern length that must be considered (int)
    Returns:
        Counter[str]: a Counter, containing: The found patterns as keys and
            The number of sequences containing this pattern as values
    """
    res = Counter()
    for d in data:
        c = Counter()
        for seq_l in range(min(max_l, len(d))):
            for i in range(len(d) - seq_l):
                c[d[i : i + seq_l + 1]] = 1
        res += c

    for r in res:
        if res[r] < len(data) * min_p:
            res[r] = 0

    return +res


# Solution 2 - my second
def seq_mining2(data: list[str], min_p: float, max_l: int) -> Counter[str]:
    """Find number of sequences according passed patterns"""
    res = sum(
        [
            Counter(
                {
                    d[i : i + seq_l + 1]
                    for seq_l in range(min(max_l, len(d)))
                    for i in range(len(d) - seq_l)
                }
            )
            for d in data
        ],
        Counter(),
    )

    return Counter(c for c in res.elements() if res[c] >= len(data) * min_p)


# Solution 3
def seq_mining3(seqs: list, ratio: float, max_len: int):
    """Find number of sequences according passed patterns"""
    mine = []
    size = min(max(len(s) for s in seqs), max_len)

    for seq in seqs:
        entry = {seq[i : i + j] for j in range(1, size + 1) for i, _ in enumerate(seq)}
        mine.append(list(entry))
    count = Counter(s for seq in mine for s in seq)
    return Counter(c for c in count.elements() if count[c] >= ratio * len(seqs))


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

    for p in [
        seq_mining,
        seq_mining2,
        seq_mining3,
    ]:
        assert p(data, 0.34, 3) == result1
        print(f"{p.__name__:20} \033[92m[ PASS 1 ]\033[0m")

        assert p(data, 0.34, 4) == result2
        print(f"{p.__name__:20} \033[92m[ PASS 2 ]\033[0m")

        assert p(data, 0.50, 2) == result3
        print(f"{p.__name__:20} \033[92m[ PASS 3 ]\033[0m")

        print()
