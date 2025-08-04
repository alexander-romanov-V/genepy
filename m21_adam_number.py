"""MEDIUM - Adam Number"""


# Solution 1 - my
def check_adam_number(num):
    """Check if num is an Adam number"""
    return str(num**2) == str(int(str(num)[::-1]) ** 2)[::-1]


# Solution 2
def check_adam_number2(num):
    """Check if num is an Adam number"""
    return num**2 == int(str(int(str(num)[::-1]) ** 2)[::-1])


if __name__ == "__main__":
    for p in [
        check_adam_number,
        check_adam_number2,
    ]:
        assert p(31) is True
        print(f"{p.__name__:20} \033[92m[ PASS 1 ]\033[0m")

        assert p(22) is True
        print(f"{p.__name__:20} \033[92m[ PASS 2 ]\033[0m")

        assert p(15) is False
        print(f"{p.__name__:20} \033[92m[ PASS 3 ]\033[0m\n")
