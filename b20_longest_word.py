"""BASIC - Longest word"""


# Solution 1
def longest_word(text: str) -> str:
    """Giving the longest word in a given text"""
    l = text.split()
    l.sort(key=lambda s: len(s))
    return l.pop()


# Solution 2
def longest_word2(text: str) -> str:
    """Giving the longest word in a given text"""
    return sorted(text.split(), key=len)[-1]


# Solution 3
def longest_word3(text):
    """Giving the longest word in a given text"""
    return max(text.split(), key=len, default="")


if __name__ == "__main__":
    print(longest_word("We want a SHRUBBERY"))
    print(longest_word("Shrubberies are great"))

    print(longest_word2("We want a SHRUBBERY"))
    print(longest_word2("Shrubberies are great"))

    print(longest_word3("We want a SHRUBBERY"))
    print(longest_word3("Shrubberies are great"))

