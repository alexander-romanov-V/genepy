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
    for p in (print_even_numbers, print_even_numbers2, print_even_numbers3):
        print(f"{p.__name__:20}")
        p(0, 10)
