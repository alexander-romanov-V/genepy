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


# Solution 2 - my second
def fill_magic_square2(square: np.array) -> None:  # type: ignore
    """Fill 0's in magic square"""
    m = max(
        *np.sum(square, axis=0),
        *np.sum(square, axis=1),
        sum(np.diag(square)),
        sum(np.flipud(square).diagonal()),
    )
    
    indices = list(zip(*np.where(square == 0)))
    
    while 0 in square:
        for x, y in indices:
            if square[x, y] == 0:
                if np.count_nonzero(square[x, :] == 0) == 1:
                    square[x, y] = m - sum(square[x, :])
                elif np.count_nonzero(square[:, y] == 0) == 1:
                    square[x, y] = m - sum(square[:, y])
                elif x == y and np.count_nonzero(np.diag(square) == 0) == 1:
                    square[x, y] = m - sum(np.diag(square))
                elif (
                    x + y == square.shape[0] - 1
                    and np.count_nonzero(np.flipud(square).diagonal() == 0) == 1
                ):
                    square[x, y] = m - sum(np.flipud(square).diagonal())


# Solution 3
def search_magic_constant(square):
    """Find magic square number"""
    n = square.shape[0]
    
    for view in square, np.rot90(square):
        for row in view:
            if np.count_nonzero(row) == n:
                return row.sum()
        if np.count_nonzero(np.diag(view)) == n:
            return np.diag(view).sum()
        
    raise ValueError("Square has too many holes!")


def fill_magic_square3(square: np.array) -> None:  # type: ignore
    """Fill 0's in magic square"""
    m = search_magic_constant(square)
    n = square.shape[0]
    diag_mask = np.diag(np.full((n,), True))

    while np.any(square == 0):
        for view in square, np.rot90(square):
            for row in view:
                if np.count_nonzero(row) == n - 1:
                    row[row == 0] = m - row.sum()
            if np.count_nonzero(np.diag(view)) == n - 1:
                view[(view == 0) & diag_mask] = m - np.diag(view).sum()


if __name__ == "__main__":
    easy_square = np.array(
        [
            [
                [2, 7, 6],
                [9, 0, 1],
                [4, 3, 8],
            ],
            [
                [2, 7, 6],
                [9, 5, 1],
                [4, 3, 8],
            ],
        ]
    )

    harder_square = np.array(
        [
            [
                [4, 0, 15, 0],
                [9, 0, 6, 12],
                [5, 11, 10, 0],
                [16, 0, 0, 13],
            ],
            [
                [4, 14, 15, 1],
                [9, 7, 6, 12],
                [5, 11, 10, 8],
                [16, 2, 3, 13],
            ],
        ]
    )

    hard_square1 = np.array(
        [
            [
                [1, 14, 14, 0],
                [11, 7, 0, 0],
                [8, 0, 10, 0],
                [13, 2, 3, 0],
            ],
            [
                [1, 14, 14, 4],
                [11, 7, 6, 9],
                [8, 10, 10, 5],
                [13, 2, 3, 15],
            ],
        ]
    )

    hard_square2 = np.array(
        [
            [
                [2087, 0, 2803, 0, 3389],
                [2843, 2729, 0, 0, 2647],
                [3359, 2113, 0, 2819, 0],
                [2663, 2777, 2699, 3373, 2153],
                [2713, 3413, 0, 2621, 0],
            ],
            [
                [2087, 2633, 2803, 2753, 3389],
                [2843, 2729, 3347, 2099, 2647],
                [3359, 2113, 2687, 2819, 2687],
                [2663, 2777, 2699, 3373, 2153],
                [2713, 3413, 2129, 2621, 2789],
            ],
        ]
    )

    for p in [
        fill_magic_square,
        fill_magic_square2,
        fill_magic_square3,
    ]:
        for arr in [
            easy_square.copy(),
            harder_square.copy(),
            hard_square1.copy(),
            hard_square2.copy(),
        ]:
            p(arr[0])
            assert (arr[0] == arr[1]).all()
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")
