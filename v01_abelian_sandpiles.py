"""VERY HARD - Abelian sandpiles"""

import numpy as np


# Solution 1 - my first
def apply_gravity(sandpile):
    """ "apply gravity" on it (and returns nothing):
    * Each element of the array is an integer representing the height of the sandpile
    * Any "pile" that has 4 or more sand particles on it collapses, resulting in four
      particles being subtracted from the pile and distributed among its neighbors.
    """
    while idxs := tuple(zip(*np.where(sandpile >= 4))):
        for x, y in idxs:
            sandpile[x, y] -= 4
            for xx, yy in ((x - 1, y), (x + 1, y), (x, y - 1), (x, y + 1)):
                sandpile[xx, yy] += 1


# Solution 2
def apply_gravity2(grid):
    """apply gravity"""
    while np.max(grid) > 3:
        tops = grid > 3
        grid[tops] -= 4
        grid[1:, :][tops[:-1, :]] += 1
        grid[:-1, :][tops[1:, :]] += 1
        grid[:, 1:][tops[:, :-1]] += 1
        grid[:, :-1][tops[:, 1:]] += 1


import matplotlib.pyplot as plt

if __name__ == "__main__":
    sandpile = np.zeros((5, 5), dtype=np.uint32)
    sandpile[2, 2] = 16

    apply_gravity(sandpile)
    print(sandpile)

    plt.imshow(sandpile)
    plt.show()
