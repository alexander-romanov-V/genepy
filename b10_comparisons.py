"""BASIC - Comparisons"""

the_list = [
    143266561,
    1738152473,
    312377936,
    1027708881,
    1871655963,
    1495785517,
    1858250798,
    1693786723,
    374455497,
    430158267,
]


# Solution 1
max_value = the_list[0]
for e in the_list:
    if e > max_value:
        max_value = e
print(max_value)


# Solution 2
print(max(the_list))
