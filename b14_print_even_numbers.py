"""BASIC - Print even numbers"""


# Solution 1
def print_even_numbers(start, stop):
    """Print even numbers"""
    for i in range(start + start % 2, stop, 2):
        print(i)


# Solution 2 - unpack range list
def print_even_numbers2(start, stop):
    """Print even numbers"""
    print(*range(start + start % 2, stop, 2), sep="\n")


# Solution 3 - just for example
def print_even_numbers3(start, stop):
    """Print even numbers"""
    l = [print(i) for i in range(start, stop) if i % 2 == 0]


if __name__ == "__main__":
    print_even_numbers(0, 10)
    print_even_numbers2(0, 10)
    print_even_numbers3(0, 10)
