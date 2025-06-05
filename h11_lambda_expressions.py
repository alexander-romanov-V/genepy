"""HARD - Lambda expressions"""

# def is_even(x):
#     """True if x is even"""
#     return x % 2 == 0


# def is_odd(x):
#     """True if x is odd"""
#     return x % 2 == 1


# def test():
#     """Test filtered function"""
#     items = [1, 2, 3, 4, 5, 6]
#     print(filtered(items, lambda x: x % 2 == 0))
#     print(filtered(items, lambda x: x % 2 == 1))
#     print(filtered(items, is_even))
#     print(filtered(items, is_odd))


# Solution 1 - my
def filtered(items, key):
    """Filter items using key function"""
    return [i for i in items if key(i)]


# Solution 2
def filtered2(items, key):
    """Filter items using key function"""
    return filter(key, items)


if __name__ == "__main__":
    # Solution 1 - my
    print(", ".join([str(x) for x in filtered(range(101), lambda x: x % 3 == 0)]))
    print(", ".join([str(x) for x in filtered(range(101), lambda x: x % 5 == 0)]))
    print(", ".join([str(x) for x in filtered(range(101), lambda x: x % 15 == 0)]))

    # Solution 1b - my
    for d in (3, 5, 15):
        print(*filtered(range(101), lambda x: x % d == 0), sep=", ")

    # Solution 2
    print(", ".join(map(str, filtered2(range(101), lambda i: i % 3 == 0))))
    print(", ".join(map(str, filtered2(range(101), lambda i: i % 5 == 0))))
    print(", ".join(map(str, filtered2(range(101), lambda i: i % 15 == 0))))
