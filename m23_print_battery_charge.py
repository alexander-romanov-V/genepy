"""MEDIUM - Product of iterable"""


# Solution 1 - my
def battery_charge(p: int) -> None:
    """Graphically represents a battery's charge"""
    print(f"[{'❚' * round(p / 10):<10}]\n{p}%")


if __name__ == "__main__":
    battery_charge(0)
    battery_charge(5)
    battery_charge(9)
    battery_charge(11)
    battery_charge(100)
