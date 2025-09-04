"""MEDIUM - Reverse Roman Numerals"""



# Solution 1
def from_roman_numeral1(roman_numeral: str) -> int:
    """Returns the value of a given roman numeral"""
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ns = list(map(nums.get, roman_numeral.strip().upper()))
    for i in range(len(ns) - 1):
        if ns[i] < ns[i + 1]:  # type: ignore
            ns[i] *= -1  # type: ignore
    return sum(ns)  # type: ignore



# Solution 2
def from_roman_numeral2(roman_numeral: str) -> int:
    """Returns the value of a given roman numeral"""
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ns = [nums[c] for c in roman_numeral.strip().upper()]
    for i in range(len(ns) - 1):
        if ns[i] < ns[i + 1]:
            ns[i] *= -1
    return sum(ns)



# Solution 3
def from_roman_numeral3(roman_numeral: str) -> int:
    """Returns the value of a given roman numeral"""
    nums = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4, 
            "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = 0
    for roman, decimal in nums.items():
        res += roman_numeral.count(roman) * decimal
        roman_numeral = roman_numeral.replace(roman, "")
    return res



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

    for d, r in check_roman.items():
        assert from_roman_numeral1(r) == d
    print("from_roman_numeral1 - OK")

    for d, r in check_roman.items():
        assert from_roman_numeral2(r) == d
    print("from_roman_numeral2 - OK")

    for d, r in check_roman.items():
        assert from_roman_numeral3(r) == d
    print("from_roman_numeral3 - OK")
