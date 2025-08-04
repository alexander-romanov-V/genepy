"""MEDIUM - Select students"""


# Solution 1
def de_flat(a_list):
    """Yield items from any nested iterable"""
    for e in a_list:
        if isinstance(e, list):
            yield from de_flat(e)
        else:
            yield e


def flatten(a_list):
    """Returns a list of lists (of any depth) returns a flattened version of it"""
    return list(de_flat(a_list))


# Solution 2
def flatten2(a_list):
    """Returns a list of lists (of any depth) returns a flattened version of it"""
    return sum(([x] if not isinstance(x, list) else flatten2(x) for x in a_list), [])


# Solution 3
def flatten3(a_list):
    """Returns a list of lists (of any depth) returns a flattened version of it"""
    if not isinstance(a_list, list):
        return [a_list]
    return [y for x in a_list for y in flatten3(x)]


if __name__ == "__main__":
    param = [[1], 2, [[3, 4], 5], [[[]]], [[[6]]], 7, 8, []]
    res = [1, 2, 3, 4, 5, 6, 7, 8]

    for p in [
        flatten,
        flatten2,
        flatten3,
    ]:
        assert p(param) == res
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")
