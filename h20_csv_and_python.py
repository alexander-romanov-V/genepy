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


    # from <your_solution> import parse_csv
    parse_csv()
    # [{'Birthdate': datetime.date(1815, 12, 10),
    # 'Comments': 'The first one',
    # 'Firstname': 'Ada',
    # 'Lastname': 'Lovelace',
    # 'Marks': [4242, 1010]},
    # {'Birthdate': datetime.date(1969, 12, 28),
    # 'Comments': 'Have a problem with penguin',
    # 'Firstname': 'Linus',
    # 'Lastname': 'Torvald',
    # 'Marks': [42, 21]},
    # {'Birthdate': datetime.date(1968, 5, 19),
    # 'Comments': 'This guy is just crazy',
    # 'Firstname': 'Theo',
    # 'Lastname': 'De Raadt',
    # 'Marks': [18, 19, 20]},
    # {'Birthdate': datetime.date(1941, 9, 9),
    # 'Comments': 'Like a boss',
    # 'Firstname': 'Dennis',
    # 'Lastname': 'Ritchie',
    # 'Marks': [20, 20, 20]},
    # {'Birthdate': datetime.date(1912, 6, 23),
    # 'Comments': "Shouldn't eat apple",
    # 'Firstname': 'Alan',
    # 'Lastname': 'Turing',
    # 'Marks': [42, 42, 42]}]
