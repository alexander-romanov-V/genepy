"""MEDIUM - The missing card"""



# Solution 1
def missing_card(cards):
    """Returns the missing card"""
    deck = []
    for c in "SHDC":
        for v in [*range(2, 11), "J", "Q", "K", "A"]:
            deck.append(c + str(v))
    for c in cards.split(" "):
        deck.remove(c)
    return deck[0]


# Solution 2
def missing_card2(cards):
    """Returns the missing card"""
    deck = [c + str(v) for c in "SHDC" for v in [*range(2, 11), "J", "Q", "K", "A"]]
    return list(set(deck) - set(cards.split(" "))).pop()


# Solution 3
def missing_card3(cards):
    """Returns the missing card"""
    colors, values = zip(*((c[:1], c[1:]) for c in cards.split()))
    return f"{min(colors, key=colors.count)}{min(values, key=values.count)}"


# Solution 4
def missing_card4(cards):
    """Returns the missing card"""
    for c in "SHDC":
        for v in "2 3 4 5 6 7 8 9 10 J Q K A".split():
            if c + v not in cards:
                return c + v


CARDS = (
    "S2 S3 S4 S5 S6 S7 S8 S9 S10 SJ SQ SK SA "
    "H2 H3 H4 H5 H6 H7 H8 H9 H10 HJ HQ HK HA "
    "D2 D3 D4 D5 D6 D7 D8 D9 D10 DJ DQ DK DA "
    "C2 C3 C4 C5 C6 C7 C8 C9 C10 CJ CQ CK"
)

if __name__ == "__main__":
    print(missing_card(CARDS))
    print(missing_card2(CARDS))
    print(missing_card3(CARDS))
    print(missing_card4(CARDS))
