import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'https?://(www\.)?youtube.com/embed',s)





if __name__ == "__main__":
    main()