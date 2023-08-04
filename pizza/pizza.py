import sys
import csv
from tabulate import tabulate


def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    try:
        file_name = sys.argv[1]
        if not file_name.endswith(".csv"):
            sys.exit("Not a CSV file")
        with open(file_name) as file:
            reader = csv.reader(file)
            print(tabulate(reader, headers="firstrow", tablefmt="grid"))

    except FileNotFoundError:
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
