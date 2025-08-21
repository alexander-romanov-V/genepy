"""MEDIUM - Product of iterable"""



# Solution 1 - my
def battery_charge(p: int) -> None:
    """Graphically represents a battery's charge"""
    print(f"[{'❚' * round(p / 10):<10}]\n{p}%")



if __name__ == "__main__":
    for n in (0, 5, 6, 9, 11, 100):
        battery_charge(n)
