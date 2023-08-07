import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start, end = s.split(' to ')
    s = re.search(r'(1[0-2]|0[0-9]){1}',start)
    if s:
        return True
    else:
        return False




...


if __name__ == "__main__":
    main()