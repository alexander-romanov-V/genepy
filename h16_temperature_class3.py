"""HARD - Temperature class"""


# Solution 3
class TemperatureAttr:
    def __init__(self, from_kelvin, to_kelvin):
        self.from_kelvin = from_kelvin
        self.to_kelvin = to_kelvin

    def __get__(self, obj, owner=None):
        return self.from_kelvin(obj.kelvin)

    def __set__(self, obj, value):
        obj.kelvin = self.to_kelvin(value)


class Temperature:
    def __init__(self):
        self.kelvin = 0

    celsius = TemperatureAttr(
        to_kelvin=lambda c: c + 273.15,
        from_kelvin=lambda k: k - 273.15,
    )
    fahrenheit = TemperatureAttr(
        to_kelvin=lambda f: (f + 459.67) * 5 / 9,
        from_kelvin=lambda k: k * 9 / 5 - 459.67,
    )


if __name__ == "__main__":
    t = Temperature()
    t.celsius = -1
    print(t.celsius)
    t.celsius += 1
    print(t.celsius)
    print(t.kelvin)
    print(t.fahrenheit)
