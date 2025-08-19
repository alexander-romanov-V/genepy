"""HARD - Password Generator"""

# Solution 1 - my
from random import choices
from string import ascii_lowercase, ascii_uppercase, digits

def pwgen(length: int, with_digits=True, with_uppercase=True) -> str:
    """
    Returns a password with lowercase letters
        AND digits if with_digits == True
        AND uppercase letters if with_uppercase == True

    :param length: the length of the generated password
    :type length: int
    :param with_digits: Defaulting to True, to allow or disallow digits
    :type with_digits: bool
    :param with_uppercase: Defaulting to True, to allow or disallow capital letters
    :type with_uppercase: bool

    :return: A string with random password
    :rtype: str
    """

    while True:
        res = choices(
            ascii_lowercase + digits * with_digits + ascii_uppercase * with_uppercase,
            k=length,
        )
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
    """
    Returns a password with lowercase letters
        AND digits if with_digits == True
        AND uppercase letters if with_uppercase == True

    :param length: the length of the generated password
    :type length: int
    :param with_digits: Defaulting to True, to allow or disallow digits
    :type with_digits: bool
    :param with_uppercase: Defaulting to True, to allow or disallow capital letters
    :type with_uppercase: bool

    :return: A string with random password
    :rtype: str
    """
    res = choices(
        ascii_lowercase + digits * with_digits + ascii_uppercase * with_uppercase,
        k=length - with_digits - with_uppercase - 1,
    )
    res += choice(ascii_lowercase)
    if with_digits:
        res += choice(digits)
    if with_uppercase:
        res += choice(ascii_uppercase)
    shuffle(res)
    return "".join(res)


if __name__ == "__main__":
    for p in [pwgen,pwgen2]:
        print(p(6, False, False))
        print(p(6, False, True))
        print(p(6, True, False))
        print(p(6, True, True))
        print()
