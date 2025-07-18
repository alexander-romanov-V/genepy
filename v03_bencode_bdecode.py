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


def bencode(obj: str | int | list | dict) -> bytes:
    """take one object as a parameter and returns bytes
    objects may be of type: str (UTF-8), int, list, dict"""

    def bencode_helper(obj: str | int | list | dict) -> str:
        """bencode helper"""
        if isinstance(obj, str):
            return f"{len(obj)}:{obj}"
        if isinstance(obj, int):
            return f"i{obj}e"
        if isinstance(obj, list):
            return f"l{''.join(bencode_helper(b) for b in obj)}e"
        if isinstance(obj, dict):
            return f"d{''.join(bencode_helper(k) + bencode_helper(v) for k, v in sorted(obj.items()))}e"
        raise ValueError

    return bencode_helper(obj).encode(encoding="utf-8")


def bdecode(b: bytes) -> str | int | list | dict:
    """take bytes as a parameter and returns an object
    objects may be of type: str (UTF-8), int, list, dict"""

    s = b.decode(encoding="utf-8")

    def bdecode_helper(inner=False) -> str | int | list | dict:
        """bdecode helper"""
        nonlocal s
        if (l := len(s)) > 1:
            if s[0].isdecimal():
                l = int(s[: (n := s.find(":"))])
                res, s = s[n + 1 : n + l + 1], s[n + l + 1 :]
                if len(res) == l and (not s or inner):
                    return res
            elif s[0] == "i" and (n := s.find("e")):
                res, s = int(s[1:n]), s[n + 1 :]
                if not s or inner:
                    return res
            elif (c := s[0]) in "ld":
                res, s = [], s[1:]
                while s[0] != "e":
                    res.append(bdecode_helper(inner=True))
                s = s[1:]
                if c == "l":
                    return res
                if len(res) % 2 == 0:
                    return dict(zip(res[::2], res[1::2]))
        raise ValueError

    return bdecode_helper()


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
    assert bencode({"wiki": "bencode", "meaning": 42}) == b"d7:meaningi42e4:wiki7:bencodee"
    # inner
    assert bencode({"outter": {"inner": "hello"}}) == b"d6:outterd5:inner5:helloee"
    # ENCODE all passed
    print(f"{bencode.__name__:24} \033[92m[ PASS ]\033[0m")

    # DECODE
    # int
    assert bdecode(b"i0e") == 0
    assert bdecode(b"i42e") == 42
    assert bdecode(b"i-42e") == -42
    # str
    assert bdecode(b"0:") == ""
    assert bdecode(b"7:bencode") == "bencode"
    # list
    assert bdecode(b"le") == []
    assert bdecode(b"l7:bencodei-20ee") == ["bencode", -20]
    # dict
    assert bdecode(b"de") == {}
    assert bdecode(b"d7:meaningi42e4:wiki7:bencodee") == {"wiki": "bencode", "meaning": 42}
    # inner
    assert bdecode(b"d6:outterd5:inner5:helloee") == {"outter": {"inner": "hello"}}
    assert bdecode(b"d7:outter1d5:inner5:helloe7:outter25:worlde") == {"outter1": {"inner": "hello"}, "outter2": "world"}
    # DECODE all passed
    print(f"{bdecode.__name__:24} \033[92m[ PASS ]\033[0m")

    print("\nTest function with incorrect parameters:")
    for data in [
        "",
        "ie",
        "i0e1",  # "i+5e", "i-5e",
        "1:",
        "3:test",  # "4:test",
        "l e",
        "lie",
        "liee",
        "lie0:e",  # "le", "l0:e", "li1e4:teste",
        "d e",
        "die",
        "diee",
        "die0:e",
        "d0:e",  # "de", "d7:meaningi42e4:wiki7:bencodee",
    ]:
        try:
            r = bdecode(data.encode("utf-8"))
        except ValueError:
            print(f"{'\'' + data + '\'':>10} -> {'exception':10} \033[92m[ PASS ]\033[0m")
        else:
            print(f"{'\''+ data + '\'':>10} -> {r.__str__():10} \033[91m[ FAIL ]\033[0m")
