"""BASIC - Temperatures"""


# Solution 1
def fahrenheit_to_celsius(temp):
    """Converts F into C"""
    return (temp - 32) * 5 / 9


def celsius_to_fahrenheit(temp):
    """Converts C into F"""
    return temp * 9 / 5 + 32


# Solution 2 - as lambdas, just for fun
fahrenheit_to_celsius2, celsius_to_fahrenheit2 = (
    lambda temp: 5 / 9 * (temp - 32),
    lambda temp: 9 / 5 * temp + 32,
)


if __name__ == "__main__":
    print(celsius_to_fahrenheit(100))
    print(fahrenheit_to_celsius(100))

    print(celsius_to_fahrenheit2(100))
    print(fahrenheit_to_celsius2(100))
