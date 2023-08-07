import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start, end = s.strip().split(' to ')
    time1 = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',start)
    time2 = re.search(r'^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$',end)
    if not(time1 and time2):
        raise ValueError()
    if time1.group(3) == 'P':
        time1.group(1) = int(time1.group(1)) + 12
    if time2.group(3) == 'P':
        time2.group(1) = int(time2.group(1)) + 12
    return f'{time1.group(1)} to {time2.group(1)}'


...


if __name__ == "__main__":
    main()