"""HARD - Temperature class"""


# Solution 2 - my second - concisely
class Temperature:
    """Temperature class can work with Celsius, Kelvin, and Fahrenheit degrees"""

    def __init__(self):
        self.celsius = 0

    @property
    def kelvin(self):
        """Getter for Kelvin degree"""
        return self.celsius + 273.15

    @kelvin.setter
    def kelvin(self, val):
        self.celsius = val - 273.15

    @property
    def fahrenheit(self):
        """Getter for Fahrenheit degree"""
        return self.celsius * 9 / 5 + 32

    @fahrenheit.setter
    def fahrenheit(self, val):
        self.celsius = (val - 32) * 5 / 9


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
