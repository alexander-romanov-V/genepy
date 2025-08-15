"""BASIC - First function"""


# Solution 1
import math
def circle_perimeter(radius: float) -> float:
    """Returns the perimeter of a circle of the given radius"""
    return 2 * math.pi * radius


# Solution 2
def circle_perimeter2(radius: float) -> float:
    """Returns the perimeter of a circle of the given radius"""
    return __import__("math").tau * radius


if __name__ == "__main__":
    print(circle_perimeter(1))
    print(circle_perimeter(10))
    print(circle_perimeter(100))

    print(circle_perimeter2(1))
    print(circle_perimeter2(10))
    print(circle_perimeter2(100))
