"""MEDIUM - The Fibonacci sequence"""


# Solution 0 - my
def fibonacci_gen():
    """Fibonacci sequence generator"""
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a + b


# Solution 1 - my first
def fibonacci(n):
    """Fibonacci sequence generator"""
    f = [1, 1]
    for i in range(n - 2):
        f.append(f[i] + f[i + 1])
    return f[:n]


# Solution 1 - my second
def fibonacci2(n):
    """Fibonacci sequence generator"""
    f = [1, 1]
    for _ in range(n - 2):
        f.append(sum(f[-2:]))
    return f[:n]


if __name__ == "__main__":
    for fn in fibonacci_gen():
        print(fn)
        if fn > 100:
            break

    print(fibonacci(1))
    print(fibonacci(2))
    print(fibonacci(5))

    print(fibonacci2(1))
    print(fibonacci2(2))
    print(fibonacci2(5))
