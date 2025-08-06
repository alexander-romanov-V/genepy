"""MEDIUM - Count the lower 'e' in the 'words' file"""


# Solution 1 - my
with open("words.txt", "r", encoding="UTF-8") as file:
    print(file.read().count("e"))


# Solution 2 - short version
print(open("words.txt").read().count("e"))


# Solution 3
print(__import__("pathlib").Path("words.txt").read_text().count("e"))
