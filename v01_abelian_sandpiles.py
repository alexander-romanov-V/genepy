"""HARD - Abelian sandpiles"""

import numpy as np


# Solution 1 - my first


def apply_gravity(sandpile):
    """ "apply gravity" on it (and returns nothing):
    * Each element of the array is an integer representing the height of the sandpile
    * Any "pile" that has 4 or more sand particles on it collapses, resulting in four
      particles being subtracted from the pile and distributed among its neighbors.
    """
    while np.any(sandpile >= 4):
        for x, y in list(zip(*np.where(sandpile > 4))):
            sandpile[x, y] -= 4
            for xx, yy in [
                (xx, yy)
                for xx in range(max(x - 1, 0), min(x + 2, sandpile.shape[0]))
                for yy in range(max(y - 1, 0), min(y + 2, sandpile.shape[1]))
            ]:
                if (x!=xx and y!=yy):
                    sandpile[xx, yy] += 1


import matplotlib.pyplot as plt

if __name__ == "__main__":
    sandpile = np.zeros((5, 5), dtype=np.uint32)
    sandpile[2, 2] = 16

    apply_gravity(sandpile)
    print(sandpile)

    plt.imshow(sandpile)
    plt.show()
