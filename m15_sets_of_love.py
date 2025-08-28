"""MEDIUM - Sets of love"""



# Solution 1
def love_meet(bob, alice):
    """Taking bob and alice's daily paths as two lists
    and returning a set of the districts they both visit during the day."""
    return set(bob).intersection(alice)


def affair_meet(bob, alice, silvester):
    """takes Bob, Alice and Silvester daily path in Paris,
    and returns a set of all places where Alice and Silvester can meet 
    and be sure Bob won't be."""
    return set(alice).intersection(silvester).difference(bob)



# Solution 2 - using set operators
def love_meet2(bob, alice):
    """Taking bob and alice's daily paths as two lists
    and returning a set of the districts they both visit during the day."""
    return set(bob) & set(alice)


def affair_meet2(bob, alice, silvester):
    """takes Bob, Alice and Silvester daily path in Paris,
    and returns a set of all places where Alice and Silvester can meet
    and be sure Bob won't be."""
    return set(alice) & set(silvester) - set(bob)



if __name__ == "__main__":
    for p in (love_meet, love_meet2):
        assert p(
            ["IV", "III", "II", "XX", "II", "XX"],
            ["II", "IV", "II", "XIX", "XV", "IV", "II"],
        ) == {"II", "IV"}
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")

    for p in (affair_meet, affair_meet2):
        assert p(
            ["IV", "III", "II", "XX", "II", "XX"],
            ["II", "IV", "II", "XIX", "XV", "IV", "II"],
            ["XVIII", "XIX", "III", "I", "III", "XVIII"],
        ) == {"XIX"}
        print(f"{p.__name__:20} \033[92m[ PASS ]\033[0m")
