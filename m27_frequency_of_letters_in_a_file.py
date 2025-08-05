"""MEDIUM - Frequency of letters in a file"""

# Solution 1 - my first
import string

with open("words.txt", "r", encoding="UTF-8") as file:
    text = file.read()
n, f = 0, {}
for c in text:
    if c in string.ascii_lowercase:
        f[c] = f.get(c, 0) + 1
    n += 1
for c in f:
    print(f"{c}: {f[c]/sum(f.values()):.02f}")


# Solution 2 - my second
with open("words.txt", "r", encoding="UTF-8") as file:
    text = file.read()
    f = {
        c: text.count(c)
        for c in __import__("string").ascii_lowercase
        if text.count(c) > 0
    }
    print(*(f"{c}: {f[c]/sum(f.values()):.02f}" for c in f), sep="\n")


# Solution 3 - my third
with open("words.txt", "r", encoding="UTF-8") as file:
    text = file.read()
    print(*(f"{c}: {text.count(c)/len(text):.02f}" for c in {*filter(str.islower, text)}), sep="\n")


# Solution 4
import collections

with open("words.txt", "r", encoding="UTF-8") as file:
    counter = collections.Counter(file.read())
l = sum(counter.values())
for c, n in counter.items():
    print(f'{c}: {n/l:.2f}')
