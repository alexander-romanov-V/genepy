"""MEDIUM - Playing with anagrams"""

import unicodedata



# Solution 1 - my first
def normalize(s):
    """Removes diacritics, combining characters, and non letters chars and sort"""
    return sorted([c for c in unicodedata.normalize("NFKD", s.lower())
                if c.isalpha() and not unicodedata.combining(c)])
    # Actually unicodedata.combining(c) is not necessary, because c.isalpha() also removes combining chars
def is_anagram(left, right):
    """Returns True if the letters of one word are a rearrangement of the letters of the other"""
    return normalize(left) == normalize(right)


# Solution 1 - my second
def is_anagram2(left, right):
    """Returns True if the letters of one word are a rearrangement of the letters of the other"""
    return sorted([c for c in unicodedata.normalize("NFD", left.lower()) if c.isalpha()]) \
        == sorted([c for c in unicodedata.normalize("NFD", right.lower()) if c.isalpha()])


if __name__ == "__main__":
    print(is_anagram("funeral", "real fun"))
    print(is_anagram("Madam Curie", "Radium came"))
    print(is_anagram("crâné", "crane"))

    print(is_anagram2("funeral", "real fun"))
    print(is_anagram2("Madam Curie", "Radium came"))
    print(is_anagram2("crâné", "crane"))
