"""MEDIUM - Perfect deck shuffle"""


# Solution 1
def perfect_shuffle(deck: list):
    """Splitting a deck of cards into equal halves, and perfectly interleaving them."""
    l = len(deck) // 2
    res = []
    for i in range(l):
        res += deck[i], deck[l + i]
    return res


# Solution 2
def perfect_shuffle2(deck: list):
    """Splitting a deck of cards into equal halves, and perfectly interleaving them."""
    return list(__import__("itertools").chain(*zip(deck[: len(deck) // 2], deck[len(deck) // 2 :])))


# Solution 3
def perfect_shuffle3(deck: list):
    """Splitting a deck of cards into equal halves, and perfectly interleaving them."""
    return [c for x in zip(deck[: len(deck) // 2], deck[len(deck) // 2 :]) for c in x]


# Solution 4
def perfect_shuffle4(deck: list):
    """Splitting a deck of cards into equal halves, and perfectly interleaving them."""
    shuffled, m = deck[:], len(deck) // 2
    shuffled[::2], shuffled[1::2] = deck[:m], deck[m:]
    return shuffled


# Solution 5
def perfect_shuffle5(deck: list):
    """Splitting a deck of cards into equal halves, and perfectly interleaving them."""
    return [deck[i] for r in range(len(deck) // 2) for i in (r, r + len(deck) // 2)]


if __name__ == "__main__":
    assert perfect_shuffle([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert perfect_shuffle2([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert perfect_shuffle3([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert perfect_shuffle4([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
    assert perfect_shuffle5([1, 2, 3, 4, 5, 6]) == [1, 4, 2, 5, 3, 6]
