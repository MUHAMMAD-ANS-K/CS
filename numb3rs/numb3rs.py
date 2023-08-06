import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    if re.search(r'^[0-255]{1,3}\.[0-9]+\.[0-9]+\.[0-9]+$',ip):
        return 'Valid'
    else:
        return 'Invalid'





if __name__ == "__main__":
    main()