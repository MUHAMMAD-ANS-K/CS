import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    start, end = s.strip().split(" to ")
    time1 = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$", start)
    time2 = re.search(r"^(1[0-2]|[0-9])(:[0-5][0-9])? ([AP])M$", end)
    if not (time1 and time2):
        raise ValueError()
    hours_24s = int(time1.group(1))
    hours_24e = int(time2.group(1))
    minutes_s = time1.group(2)
    minutes_e = time2.group(2)
    if minutes_s == None:
        minutes_s = ":00"
    if minutes_e == None:
        minutes_e = ":00"
    if time1.group(3) == "P":
        time_24as += 12
    if time2.group(3) == "P":
        time_24e += 12
    return f"{hours_24s:02d}{minutes_s} to {hours_24e}{minutes_e}"


if __name__ == "__main__":
    main()
