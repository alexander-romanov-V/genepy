"""MEDIUM - Distance"""



# Solution 1
def dist(points):
    """Returns max distance"""
    return max(points) - min(points)


# Solution 2
def dist2(points):
    """Returns max distance"""
    mini, *_, maxi = sorted(points)
    return maxi - mini


# Solution 3 (just for fun)
dist3 = lambda points: max(points) - min(points)


if __name__ == "__main__":
    print(dist([1, 2, 3]))
    print(dist([1, 2, 3, 2.5]))
    print(dist([1, 2, 3, 2.5, 3.5]))
    print(dist([1, 2, 3, 2.5, 3.5, 120]))
    print(dist([1, 2, 3, 2.5, 3.5, 120, -1000]))

    print(dist2([1, 2, 3]))
    print(dist2([1, 2, 3, 2.5]))
    print(dist2([1, 2, 3, 2.5, 3.5]))
    print(dist2([1, 2, 3, 2.5, 3.5, 120]))
    print(dist2([1, 2, 3, 2.5, 3.5, 120, -1000]))

    print(dist3([1, 2, 3]))
    print(dist3([1, 2, 3, 2.5]))
    print(dist3([1, 2, 3, 2.5, 3.5]))
    print(dist3([1, 2, 3, 2.5, 3.5, 120]))
    print(dist3([1, 2, 3, 2.5, 3.5, 120, -1000]))
