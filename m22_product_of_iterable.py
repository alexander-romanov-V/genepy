"""MEDIUM - Product of iterable"""



# Solution 1 - my
def mul(numbers):
    """Product of iterable"""
    return __import__("math").prod(numbers)



# Solution 2
def mul2(numbers):
    """Product of iterable"""
    return __import__("functools").reduce(__import__("operator").mul, numbers)



# Solution 3
def mul3(numbers):
    """Product of iterable"""
    return __import__("functools").reduce(lambda m, n: m * n, numbers)



# Solution 4
def mul4(numbers):
    """Product of iterable"""
    return eval("*".join(str(el) for el in numbers))



if __name__ == "__main__":
    for p in [mul, mul2, mul3, mul4]:
        assert p([1, 2, 3]) == 6
        print(f"{p.__name__:20} \033[92m[ PASS 1 ]\033[0m")

        assert p([0, 1, 2, 3]) == 0
        print(f"{p.__name__:20} \033[92m[ PASS 2 ]\033[0m")

        assert p([2, 3, 4]) == 24
        print(f"{p.__name__:20} \033[92m[ PASS 3 ]\033[0m")
        
        assert p([2, 3, 4]) + p([1, 2]) == 26
        print(f"{p.__name__:20} \033[92m[ PASS 4 ]\033[0m\n")
