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
