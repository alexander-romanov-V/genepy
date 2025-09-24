"""MEDIUM - Sort students"""



# Represent student as a pair of (mark, full_name), so a tuple of two elements.
students = [(85, "Susan"), (6, "Joshua"), (37, "Jeanette")]


# Solution 1
def sort_by_mark(my_class):
    """Take a list of students and returns a copy of it sorted by mark in descending order"""
    return sorted(my_class, reverse=True)


def sort_by_name(my_class):
    """Take a list of students and returns a copy of it sorted by name in ascending order"""
    return sorted(my_class, key=lambda s: s[1])


# Solution 2
def sort_by_mark2(my_class):
    """Take a list of students and returns a copy of it sorted by mark in descending order"""
    return sorted(my_class, key=lambda s: -s[0])


if __name__ == "__main__":
    print(sort_by_mark(students))
    print(sort_by_name(students))
    print(sort_by_mark2(students))
