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


def bencode(obj: str | int | list[int|str] | dict[int|str, int|str]) -> bytearray:
    """take one object as a parameter and returns bytes
    objects may be of type: str (UTF-8), int, list, dict"""
    if isinstance(obj, list):
        res = f"l{''.join(bencode_helper(b) for b in obj)}e"
    elif isinstance(obj, dict):
        res = f"d{''.join(bencode_helper(k) + bencode_helper(v) for k, v in sorted(obj.items()))}e"
    else:
        res = bencode_helper(obj)
    return bytearray(res, encoding="utf-8")


def bdecode(b: bytearray):
    """take bytes as a parameter and returns an object
    objects may be of type: str (UTF-8), int, list, dict"""

    return b


if __name__ == "__main__":

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
    
    # all passed
    print(f"{bencode.__name__:20} \033[92m[ PASS ]\033[0m")

