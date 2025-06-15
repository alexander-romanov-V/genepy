"""HARD - Magic Square"""

import numpy as np


# Solution 1 - my first
def fill_magic_square(square: np.array) -> None:
    ...


if __name__ == "__main_":
    easy_square = np.array([
        [2, 7, 6],
        [9, 0, 1],
        [4, 3, 8],
    ])
    fill_magic_square(easy_square)
    print(easy_square)
    # Output:
    # array([[ 2, 7, 6 ],
    #    [ 9, 5, 1 ],
    #    [ 4, 3, 8 ]]])

    harder_square = np.array([
        [ 4,  0, 15,  0],
        [ 9,  0,  6, 12],
        [ 5, 11, 10,  0],
        [16,  0,  0, 13],
    ])
    fill_magic_square(harder_square)
    print(harder_square)
    # Output:
    # array([[4, 14, 15,  1],
    #    [9,  7,  6, 12],
    #    [5, 11, 10,  8],
    #    [16, 2,  3, 13]])
