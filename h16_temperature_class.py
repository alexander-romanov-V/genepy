"""HARD - Temperature class"""


# Solution 1 - my first
class Celsius:
    """Basic descriptor for Celsius degree"""

    def __get__(self, obj, objtype=None):
        return obj._celsius

    def __set__(self, obj, value):
        obj._celsius = value


class Kelvin:
    """Descriptor for Kelvin degree (based on Celsius)"""

    def __get__(self, obj, objtype=None):
        return obj._celsius + 273.15

    def __set__(self, obj, value):
        obj._celsius = value - 273.15


class Fahrenheit:
    """Descriptor for Fahrenheit degree (based on Celsius)"""

    def __get__(self, obj, objtype=None):
        return obj._celsius * 9 / 5 + 32

    def __set__(self, obj, value):
        obj._celsius = (value - 32) * 5 / 9


class Temperature:
    """Temperature class can work with Celsius, Kelvin, and Fahrenheit degrees"""

    celsius = Celsius()
    kelvin = Kelvin()
    fahrenheit = Fahrenheit()

    def __init__(self):
        self.celsius = 0


if __name__ == "__main__":
    t = Temperature()

    t.celsius = -1
    print(t.celsius)

    t.celsius += 1
    print(t.celsius)
    print(t.kelvin)
    print(t.fahrenheit)

    t.fahrenheit += 1
    print(t.fahrenheit)
    
    t.kelvin += 1
    print(t.kelvin)
