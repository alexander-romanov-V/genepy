"""MEDIUM - Currency"""


# Solution 1 - my first
def how_to_pay(amount, currency):
    """Returns a dict describing the easiest way to pay amount with the given currency"""
    pay = {}
    for c in sorted(currency, reverse=True):
        pay[c] = amount // c
        amount %= c
    return pay


# Solution 2 - my second
def how_to_pay2(amount, currency):
    """Returns a dict describing the easiest way to pay amount with the given currency"""
    return {
        c: (amount // c, amount := amount % c)[0]
        for c in sorted(currency, reverse=True)
        if amount // c > 0
    }


EURO = [1, 2, 5, 10, 20, 50, 100, 200, 500]

if __name__ == "__main__":
    # {500: 1}  # means: To pay 500€: give one bill of 500€
    print(how_to_pay(500, EURO))
    # {10: 1}  # means: To pay 10€: give one bill of 10€
    print(how_to_pay(10, EURO))
    # {100: 1, 20: 1, 2: 1, 1: 1}  # give 1 bill of 100€, one bill of 20€, one coin of 2€, and one coin of 1€.
    print(how_to_pay(123, EURO))

    print(how_to_pay2(500, EURO))
    print(how_to_pay2(10, EURO))
    print(how_to_pay2(123, EURO))
