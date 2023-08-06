import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    match = re.search(r'<iframe(.+)? src="https?://(www\.)?youtube.com/embed(/xvFZjo5PgG0)"(.+)?></iframe>',s)
    if match:
        return 'https://youtu.be' + match.group(3)
    else:
        return None




if __name__ == "__main__":
    main()