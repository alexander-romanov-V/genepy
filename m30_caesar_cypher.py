"""MEDIUM - Caesar Cypher"""


# Solution 1 - my
def caesar_cypher_encrypt(s, key):
    """Encrypt Caesar cypher"""
    r = ""
    for c in s:
        if c.isupper():
            r += chr((ord(c) - ord("A") + 26 + key % 26) % 26 + ord("A"))
        elif c.islower():
            r += chr((ord(c) - ord("a") + 26 + key % 26) % 26 + ord("a"))
        else:
            r += c
    return r


def caesar_cypher_decrypt(s, key):
    """Decrypt Caesar cypher"""
    return caesar_cypher_encrypt(s, -key)



if __name__ == "__main__":
    assert caesar_cypher_encrypt("a", 2) == "c"
    assert caesar_cypher_decrypt("c", 2) == "a"
    assert (
        caesar_cypher_encrypt("Python is super disco !", 31)
        == "Udymts nx xzujw inxht !"
    )
    assert (
        caesar_cypher_decrypt("Udymts nx xzujw inxht !", 31)
        == "Python is super disco !"
    )
