"""HARD - Password Generator"""

# Solution 1 - my
from random import choices
from string import ascii_lowercase, ascii_uppercase, digits
def pwgen(length: int, with_digits=True, with_uppercase=True) -> str:
    """
    Returns a password with lowercase letters
    """
    while True:
        res = choices(ascii_lowercase + digits * with_digits + ascii_uppercase * with_uppercase, k=length)
        if (
            set(res).intersection(ascii_lowercase)
            and (not with_digits or set(res).intersection(digits))
            and (not with_uppercase or set(res).intersection(ascii_uppercase))
        ):
            return "".join(res)


# Solution 2 - my second
from random import choices, choice, shuffle
from string import ascii_lowercase, ascii_uppercase, digits
def pwgen2(length, with_digits=True, with_uppercase=True):
    """Returns a password with lowercase letters"""
    res = choices(ascii_lowercase + digits * with_digits + ascii_uppercase * with_uppercase, k=length - with_digits - with_uppercase - 1)
    res += choice(ascii_lowercase)
    if with_digits:
        res += choice(digits)
    if with_uppercase:
        res += choice(ascii_uppercase)
    shuffle(res)
    return "".join(res)


if __name__ == "__main__":
    print(pwgen(6, False, False))
    print(pwgen(6, False, True))
    print(pwgen(6, True, False))
    print(pwgen(6, True, True))

    print(pwgen2(6, False, False))
    print(pwgen2(6, False, True))
    print(pwgen2(6, True, False))
    print(pwgen2(6, True, True))
