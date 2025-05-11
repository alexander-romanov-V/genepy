"""MEDIUM - Friday the 13th"""

import datetime


# Solution 1 - my first one
def inc_month(d):
    """Increment a month"""
    return datetime.date(d.year + d.month // 12, d.month % 12 + 1, d.day)
def friday_the_13th(today=datetime.datetime.today().date()):
    """Returns the date of the next friday the 13th."""
    if today.day > 13:
        today = inc_month(today)
    today += datetime.timedelta(days=13 - today.day)
    while today.weekday() != 4:
        today = inc_month(today)
    return str(today)


# Solution 2 - tricky (sometimes can fail?)
def friday_the_13th2(today=datetime.date.today()):
    """Returns the date of the next friday the 13th."""
    d = today.replace(day=13)
    while d < today or d.weekday() != 4:
        d = (d + datetime.timedelta(days=30)).replace(day=13)
    return format(d, "%Y-%m-%d")


# Solution 3 - easy
def friday_the_13th3(today=datetime.datetime.now().date()):
    """Returns the date of the next friday the 13th."""
    while today.weekday() != 4 or today.day != 13:
        today += datetime.timedelta(1)
    return str(today)


# Solution 4 - good enough
def friday_the_13th4(today=datetime.datetime.today().date()):
    """Returns the date of the next friday the 13th."""
    while today.weekday() is not 4:
        today += datetime.timedelta(1)
    while today.day is not 13:
        today += datetime.timedelta(7)
    return str(today)


if __name__ == "__main__":
    print(friday_the_13th())
    print(friday_the_13th2())
    print(friday_the_13th3())
    print(friday_the_13th4())
