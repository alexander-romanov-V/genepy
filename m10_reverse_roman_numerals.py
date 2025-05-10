"""MEDIUM - Reverse Roman Numerals"""


# Solution 1
def from_roman_numeral1(roman_numeral: str):
    """Returns the value of a given roman numeral"""
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ns = list(map(nums.get, roman_numeral.strip().upper()))
    for i in range(len(ns) - 1):
        if ns[i] < ns[i + 1]: # type: ignore
            ns[i] *= -1 # type: ignore
    return sum(ns) # type: ignore


# Solution 2
def from_roman_numeral2(roman_numeral: str):
    """Returns the value of a given roman numeral"""
    nums = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
    ns = [nums[c] for c in roman_numeral.strip().upper()]
    for i in range(len(ns) - 1):
        if ns[i] < ns[i + 1]:
            ns[i] *= -1
    return sum(ns)


# Solution 3
def from_roman_numeral(roman_numeral: str):
    """Returns the value of a given roman numeral"""
    nums = {"CM": 900, "CD": 400, "XC": 90, "XL": 40, "IX": 9, "IV": 4,
    "M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
    res = 0
    for roman, decimal in nums.items():
        res += roman_numeral.count(roman) * decimal
        roman_numeral = roman_numeral.replace(roman, "")
    return res


if __name__ == "__main__":
    print(from_roman_numeral("I"))
    print(from_roman_numeral("II"))
    print(from_roman_numeral("III"))
    print(from_roman_numeral("IV"))
    print(from_roman_numeral("V"))  # == 5
    print(from_roman_numeral("VI"))
    print(from_roman_numeral("VII"))
    print(from_roman_numeral("VIII"))
    print(from_roman_numeral("IX"))
    print(from_roman_numeral("X"))
    print(from_roman_numeral("XI"))
    print(from_roman_numeral("XII"))
    print(from_roman_numeral("XIII"))
    print(from_roman_numeral("XIV"))
    print(from_roman_numeral("XV"))
    print(from_roman_numeral("XVI"))
    print(from_roman_numeral("XX"))  # == 20
    print(from_roman_numeral("DCCC"))  # == 800
    print(from_roman_numeral("MMMM"))  # == 4000
