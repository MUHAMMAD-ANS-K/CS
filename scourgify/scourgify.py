import sys
def main():
    if len(sys.argv) > 2:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    try:

    except FileNotFoundError:
        sys.exit('Could not read invalid_file.csv')


if __name__ == '__main__':
    main()