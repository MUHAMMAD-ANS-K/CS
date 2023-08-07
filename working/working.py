import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start, end = s.strip().split(' to ')
    time1 = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',start)
    time2 = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',end)
    if time1 and time2:
        raise ValueError()





...


if __name__ == "__main__":
    main()