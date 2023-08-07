import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start, end = s.split(' to ')
    s = re.search(r'(:[0-5][0-9])',start)
    if s:
        return True
    else:
        return False




...


if __name__ == "__main__":
    main()