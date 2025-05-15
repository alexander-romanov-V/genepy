"""MEDIUM - Draw N Squares"""


# Solution 1 - my first
def is_a_dyck_word(word: str) -> bool:
    """A Dyck word have to be "well-parenthesized"""
    if word == "":
        return True
    a = word[0] + word[-1]
    if len(set(word)) != 2 or len(word) % 2 != 0 or a[0] == a[1]:
        return False
    while len(word) > 0:
        n = word.find(str(a))
        if n >= 0:
            word = word[:n] + word[n + 2 :]
        else:
            return len(word) == 0
    return True


# Solution 2 - my second
def is_a_dyck_word2(word: str) -> bool:
    """A Dyck word have to be "well-parenthesized"""
    if word and (len(set(word)) != 2 or len(word) % 2 != 0 or word[0] == word[-1]):
        return False
    x = 0
    for i in word:
        x += 1 if i == word[0] else -1
        if x < 0:
            return False
    return x == 0


# Solution 3
def is_a_dyck_word3(word: str) -> bool:
    """A Dyck word have to be "well-parenthesized"""
    if not word:
        return True
    opening, to_close = word[0], 1
    for char in word[1:]:
        to_close += (-1, 1)[char == opening]    # tricky addressing in a tuple via bool (a,b)[True] == (a,b)[1] = b
        if to_close < 0:
            return False
    return to_close == 0


if __name__ == "__main__":
    for p in [is_a_dyck_word, is_a_dyck_word2, is_a_dyck_word3]:
        assert p("") is True
        assert p("()") is True
        assert p("(((())))") is True
        assert p("()()()()") is True
        assert p("()(())()") is True
        assert p("(((") is False
        assert p("((()") is False
        assert p("()))") is False
        assert p("()()()(") is False
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")
