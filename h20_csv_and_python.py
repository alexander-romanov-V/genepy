"""HARD - CSV and Python"""

# Solution 1 - my first

import csv


def generate_csv(a_list):
    """Create a csv file called results.csv from a list of tuples"""
    ...


def parse_csv():
    """Read and parse a csv file called students.csv and return a list of dictionaries 
    which will contain the column name as key and the value as value"""
    ...


if __name__ == "__main__":
    import datetime

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
    generate_csv(meteo)
