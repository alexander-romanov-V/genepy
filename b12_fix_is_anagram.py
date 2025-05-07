"""BASIC - Fix is_anagram"""

# Solution 1
def is_anagram(left, right):
    """Returns True if left word is an anagram of right"""
    left_letters = sorted(left)
    right_letters = sorted(right)
    return left_letters == right_letters

if __name__ == "__main__":
    print(is_anagram("rope", "pore"))
