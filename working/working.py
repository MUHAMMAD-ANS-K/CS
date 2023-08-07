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
    time_24a = int(time1.group(1))
    time_24b = int(time2.group(1))
    if time1.group(3) == 'P':
        time_24a += 12
    if time2.group(3) == 'P':
        time_24b += 12
    return f'{time_24a:02d} to {time_24b}'


...


if __name__ == "__main__":
    main()