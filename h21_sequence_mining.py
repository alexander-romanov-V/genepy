"""HARD - Sequence Mining"""

# Solution 1 - my first
def seq_mining(l: list[str,], min_p: float, max_l: int) -> dict[str, int]:
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
    data = ['ABCD', 'ABABC', 'BCAABCD']
