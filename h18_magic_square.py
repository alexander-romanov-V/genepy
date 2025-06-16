"""HARD - Magic Square"""

import numpy as np


# Solution 1 - my first
def fill_magic_square(square: np.array) -> None:  # type: ignore
    """Fill 0's in magic square"""
    n = square.shape[0]
    # m = n * (n**2 + 1) // 2 # Only for normal magic square
    m = 0
    for j in range(n):
        if np.count_nonzero(square[j, :]) == n:
            m = sum(square[j, :])
            break
        elif np.count_nonzero(square[:, j]) == n:
            m = sum(square[:, j])
            break
    if m == 0:
        if np.count_nonzero(square.diagonal()) == n:
            m = sum(square.diagonal())
        elif np.count_nonzero(np.flipud(square).diagonal()) == n:
            m = sum(np.flipud(square).diagonal())
        else:
            raise ValueError("Can't find magic square number - too many blanks")

    while np.count_nonzero(square) != n**2:
        for j in range(n):
            for i in range(n):
                if square[j, i] == 0:
                    if np.count_nonzero(square[j, :]) == n - 1:
                        square[j, i] = m - sum(square[j, :])
                    elif np.count_nonzero(square[:, i]) == n - 1:
                        square[j, i] = m - sum(square[:, i])
                    elif i == j and np.count_nonzero(square.diagonal()) == n - 1:
                        square[j, i] = m - sum(square.diagonal())
                    elif (
                        i == n - 1 - j
                        and np.count_nonzero(np.flipud(square).diagonal()) == n - 1
                    ):
                        square[j, i] = m - sum(np.flipud(square).diagonal())


