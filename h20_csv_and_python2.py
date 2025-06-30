"""HARD - CSV and Python"""

# Solution 1 - my first

import csv
import datetime


def format_value(v):
    if isinstance(v, (tuple, list)):
        return ",".join(map(str, v))
    if isinstance(v, datetime.date):
        return v.strftime("%m/%d/%Y")
    return v


def generate_csv(rows):
    fields = [f for f, _ in rows[0]]
    with open("results.csv", "w") as f:
        writer = csv.DictWriter(f, fields)
        writer.writeheader()
        for row in rows:
            row = {k: format_value(v) for k, v in row}
            writer.writerow(row)


def parse_csv():
    rows = []
    with open("students.csv") as f:
        for row in csv.DictReader(f):
            row["Birthdate"] = datetime.datetime.strptime(
                row["Birthdate"], "%m/%d/%Y"
            ).date()
            row["Marks"] = [int(x) for x in row["Marks"].split(",")]
            rows.append(row)
    return rows


if __name__ == "__main__":
    # from <your_solution> import generate_csv
    meteo = [
        (
            ("temperature", 42),
            ("date", datetime.date(2017, 1, 22)),
            ("locations", ("Berlin", "Paris")),
            ("weather", "sunny"),
        ),
        (
            ("temperature", -42),
            ("date", datetime.date(2017, 1, 22)),
            ("locations", ("Marseille", "Moscow")),
            ("weather", "cloudy"),
        ),
    ]
    # m2 = [dict(m) for m in meteo]
    generate_csv(meteo)

    # from <your_solution> import parse_csv
    students = [
        {
            "Birthdate": datetime.date(1815, 12, 10),
            "Comments": "The first one",
            "Firstname": "Ada",
            "Lastname": "Lovelace",
            "Marks": [4242, 1010],
        },
        {
            "Birthdate": datetime.date(1969, 12, 28),
            "Comments": "Have a problem with penguin",
            "Firstname": "Linus",
            "Lastname": "Torvald",
            "Marks": [42, 21],
        },
        {
            "Birthdate": datetime.date(1968, 5, 19),
            "Comments": "This guy is just crazy",
            "Firstname": "Theo",
            "Lastname": "De Raadt",
            "Marks": [18, 19, 20],
        },
        {
            "Birthdate": datetime.date(1941, 9, 9),
            "Comments": "Like a boss",
            "Firstname": "Dennis",
            "Lastname": "Ritchie",
            "Marks": [20, 20, 20],
        },
        {
            "Birthdate": datetime.date(1912, 6, 23),
            "Comments": "Shouldn't eat apple",
            "Firstname": "Alan",
            "Lastname": "Turing",
            "Marks": [42, 42, 42],
        },
    ]

    assert parse_csv() == students
