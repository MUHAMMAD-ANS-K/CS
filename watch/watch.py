import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'https?://(www\.)?youtube.com/embed(/xvFZjo5PgG0)',s)
    if match:
        return 'https://youtu.be' + match.group(2)
    else:
        return None




if __name__ == "__main__":
    main()