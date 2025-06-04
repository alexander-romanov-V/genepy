"""HARD - Roman Numerals"""


# Solution 1 - my
def to_roman_numeral(n):
    """Returns roman numeral by a given decimal number"""
    nums = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    res = ""
    for decimal, roman in nums.items():
        while decimal <= n:
            n -= decimal
            res += roman
    return res


# Solution 2
def to_roman_numeral2(n):
    """Returns roman numeral by a given decimal number"""
    nums = {1000: "M", 900: "CM", 500: "D", 400: "CD", 100: "C", 90: "XC",
            50: "L", 40: "XL", 10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I" }
    res = ""
    for decimal, roman in nums.items():
        count, n = divmod(n, decimal)
        res = f"{res}{roman * count}"
    return res


# Solution 3
def to_roman_numeral3(data):
    """Returns roman numeral by a given decimal number"""
    basic = "M" * (data // 1000) + "D" * (data % 1000 // 500) + "C" * (data % 500 // 100) + "L" * (data % 100 // 50) + "X" * (data % 50 // 10) + "V" * (data % 10 // 5) + "I" * (data % 5)
    return basic.replace("DCCCC", "CM").replace("CCCC", "CD").replace("LXXXX", "XC").replace("XXXX", "XL").replace("VIIII", "IX").replace("IIII", "IV")


if __name__ == "__main__":
    check_roman = {
        1: "I",
        2: "II",
        3: "III",
        4: "IV",
        5: "V",
        6: "VI",
        7: "VII",
        8: "VIII",
        9: "IX",
        10: "X",
        11: "XI",
        12: "XII",
        13: "XIII",
        14: "XIV",
        15: "XV",
        16: "XVI",
        17: "XVII",
        18: "XVIII",
        19: "XIX",
        20: "XX",
        30: "XXX",
        40: "XL",
        50: "L",
        60: "LX",
        70: "LXX",
        80: "LXXX",
        90: "XC",
        100: "C",
        200: "CC",
        222: "CCXXII",
        800: "DCCC",
        4000: "MMMM",
    }

    for p in [
        to_roman_numeral,
        to_roman_numeral2,
        to_roman_numeral3,
    ]:
        for d, r in check_roman.items():
            assert p(d) == r
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")
