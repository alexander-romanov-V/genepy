"""UNIT TEST - Py Master Mind"""

from v06_py_master_mind import gen_colors, gen_code, check_guess, score_guess


def test_gen_colors():
    """Unit test gen_colors() function"""
    assert gen_colors(-1) == ""
    assert gen_colors(0) == ""
    assert gen_colors(1) == "A"
    assert gen_colors(6) == "ABCDEF"
    assert gen_colors(25) == "ABCDEFGHIJKLMNOPQRSTUVWXY"
    assert gen_colors(26) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    assert gen_colors(295) == "ABCDEFGHIJKLMNOPQRSTUVWXYZ"


def test_gen_code():
    """Unit test gen_code() function"""
    for i in [(5, "ABCDEF"), (5, "A"), (1, "ABCDE"), (2, "AB")]:
        x = gen_code(i[0], i[1])
        assert len(x) == i[0]
        for n in range(i[0]):
            assert x[n] in i[1]


def test_check_guess():
    """Unit test check_guess() function"""
    assert check_guess("ZZZZ", 4, "ABCDEF") is False
    assert check_guess("EEBBAA", 4, "ABCDEF") is False
    assert check_guess("AABB", 4, "ABCDEF") is True
    assert check_guess("AB", 4, "ABCDEF") is False
    assert check_guess("Z", 1, "ABCDEF") is False
