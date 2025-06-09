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
        res = choices(ascii_lowercase + digits * with_digits + ascii_uppercase * with_uppercase, k=length)
        if (
            set(res).intersection(ascii_lowercase)
            and (not with_digits or set(res).intersection(digits))
            and (not with_uppercase or set(res).intersection(ascii_uppercase))
        ):
            return "".join(res)


if __name__ == "__main__":
    print(pwgen(6, False, False))
    print(pwgen(6, False, True))
    print(pwgen(6, True, False))
    print(pwgen(6, True, True))
