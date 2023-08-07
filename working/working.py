import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    #start, end = s.split(' to ')
    s = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',s)
    if s:
        return True
    else:
        return False




...


if __name__ == "__main__":
    main()