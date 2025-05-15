"""MEDIUM - Hearts emojis"""


# Solution 1 - my first
for i in range(1 + 0x10FFFF):
    if "HEART" in __import__("unicodedata").name(chr(i), ""):
        print(chr(i))


# Solution 2 - my second
print(*[chr(i) for i in range(230000) if "HEART" in __import__("unicodedata").name(chr(i), "")], sep="")


# Solution 3
print(*(char for i in range(0x110000) if "HEART" in __import__("unicodedata").name((char:=chr(i)), "")), sep="")
