"""HARD - Format your output"""


# Solution 1
def list_pretty_print(items):
    """5 ints per line"""
    for i in range(0, len(items), 5):
        print(*items[i : i + 5], sep=", ")


if __name__ == "__main__":
    list_pretty_print([42] * 6)
