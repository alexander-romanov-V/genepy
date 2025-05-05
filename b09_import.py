"""BASIC - Import"""

# Solution 1 - basic
import math
print(math.factorial(27))

# Solution 2 - import with rename
import math as m
print(m.factorial(27))

# Solution 3 - dynamic import
print(__import__("math").factorial(27))
