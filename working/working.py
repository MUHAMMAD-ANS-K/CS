import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    time = re.search(
        r"^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M to (1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$", s
        )
    if not (time):
        raise ValueError()
    hours_24s = int(time.group(1))
    hours_24e = int(time.group(4))
    minutes_s = time.group(2)
    minutes_e = time.group(5)
    if minutes_s == None:
        minutes_s = ":00"
    if minutes_e == None:
        minutes_e = ":00"
    if time.group(3) == "P":
        hours_24s += 12
    if time.group(6) == "P":
        hours_24e += 12
    if time.group(1) == '12':
        hours_24s -= 12
    if time.group(4) == '12':
        hours_24e -= 12
    return f"{hours_24s:02d}{minutes_s} to {hours_24e:02d}{minutes_e}"


if __name__ == "__main__":
    main()
