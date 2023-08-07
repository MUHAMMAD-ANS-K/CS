import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        start, end = s.strip().split(' to ')
        time1 = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',start)
        time2 = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',end)
        if not(time1 and time2):
            raise ValueError()
            #return False
    except ValueError:
        return True




...


if __name__ == "__main__":
    main()