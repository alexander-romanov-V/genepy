"""MEDIUM - Print the content of a file"""


# Solution 1
def print_file(file_name):
    """Print the content of a file"""
    with open(file_name, encoding="UTF-8") as file:
        print(file.read())


# Solution 2
def print_file2(file_name):
    """Print the content of a file"""
    print(__import__("pathlib").Path(file_name).read_text())


# Solution 3
def print_file3(file_name):
    """Print the content of a file"""
    print(open(file_name, encoding="UTF-8").read())


if __name__ == "__main__":
    print_file("README.md")
    print_file2("README.md")
    print_file3("README.md")
