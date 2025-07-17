"""VERY HARD - bencode, bdecode

Expose two functions bencode and bdecode.

    bencode take one object as a parameter and returns bytes.
    bdecode take bytes as a parameter and returns an object.

objects may be of type:

    str
    int
    list
    dict

You have to follow the bencode encoding and decoding algorithm,
see Wikipedia bencode page. https://en.wikipedia.org/wiki/Bencode
You'll have to encode and decode strings, use "UTF-8" everywhere
and explicitly.

Hints
You may code other helper functions in your module, functions to help
bencode and bdecode in their work. You also can store module variables
and use them but only for you to use.

"""


# Solution 1 - my first


def bencode_helper(obj: str | int) -> str:
    """bencode helper for str and int"""
    if isinstance(obj, str):
        return f"{len(obj)}:{obj}"
    return f"i{obj}e"


def bencode(obj: str | int | list[int | str] | dict[int | str, int | str]) -> bytearray:
    """take one object as a parameter and returns bytes
    objects may be of type: str (UTF-8), int, list, dict"""
    if isinstance(obj, list):
        res = f"l{''.join(bencode_helper(b) for b in obj)}e"
    elif isinstance(obj, dict):
        res = f"d{''.join(bencode_helper(k) + bencode_helper(v) for k, v in sorted(obj.items()))}e"
    else:
        res = bencode_helper(obj)
    return bytearray(res, encoding="utf-8")


def bdecode_helper(s: str, inner=False) -> tuple[str | int, str]:
    """bdecode helper for str and int"""
    if s:
        if s[0] == "i" and (n := s.find("e")):
            res = int(s[1:n])
            if not (s := s[n + 1 :]) or inner:
                return res, s
        elif n := s.find(":"):
            l = int(s[:n])
            res = s[n + 1 : n + l + 1]
            if len(res) == l and (not (s := s[n + l + 1 :]) or inner):
                return res, s
    raise ValueError


def bdecode(b: bytearray) -> str | int | list[int | str] | dict[int | str, int | str]:
    """take bytes as a parameter and returns an object
    objects may be of type: str (UTF-8), int, list, dict"""
    if not (s := b.decode(encoding="utf-8")):
        raise ValueError
    if s[0] == "l" and s[-1] == "e":
        s = s[1:-1]
        res = []
        while s:
            e, s = bdecode_helper(s, inner=True)
            res.append(e)
        return res
    elif s[0] == "d" and s[-1] == "e":
        s = s[1:-1]
        res = dict()
        while s:
            k, s = bdecode_helper(s, inner=True)
            v, s = bdecode_helper(s, inner=True)
            res[k] = v
        return res
    else:
        return bdecode_helper(s)[0]


if __name__ == "__main__":

    print("\nTest function with correct parameters:")

    # ENCODE
    # int
    assert bencode(0) == b"i0e"
    assert bencode(42) == b"i42e"
    assert bencode(-42) == b"i-42e"
    # str
    assert bencode("") == b"0:"
    assert bencode("bencode") == b"7:bencode"
    # list
    assert bencode([]) == b"le"
    assert bencode(["bencode", -20]) == b"l7:bencodei-20ee"
    # dict
    assert bencode({}) == b"de"
    assert (
        bencode({"wiki": "bencode", "meaning": 42}) == b"d7:meaningi42e4:wiki7:bencodee"
    )
    # ENCODE all passed
    print(f"{bencode.__name__:24} \033[92m[ PASS ]\033[0m")

    # DECODE
    # int
    assert bdecode(bytearray("i0e", "utf-8")) == 0
    assert bdecode(bytearray("i42e", "utf-8")) == 42
    assert bdecode(bytearray("i-42e", "utf-8")) == -42
    # str
    assert bdecode(bytearray("0:", "utf-8")) == ""
    assert bdecode(bytearray("7:bencode", "utf-8")) == "bencode"
    # list
    assert bdecode(bytearray("le", "utf-8")) == []
    assert bdecode(bytearray("l7:bencodei-20ee", "utf-8")) == ["bencode", -20]
    # dict
    assert bdecode(bytearray("de", "utf-8")) == {}
    assert bdecode(bytearray("d7:meaningi42e4:wiki7:bencodee", "utf-8")) == {
        "wiki": "bencode",
        "meaning": 42,
    }
    # DECODE all passed
    print(f"{bdecode.__name__:24} \033[92m[ PASS ]\033[0m")
