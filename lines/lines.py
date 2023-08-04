import sys
def main():
    lines = 0
    try:
        file_name = sys.argv[1]
        with open(file_name) as file:
            for line in file:
                line = line.lstrip()
                if line.startswith('#'):
                    pass
                else:
                    lines += 1
    except FileNotFoundError:
        pass
    except IndexError:
        sys.exit('T')

    print(lines)
if __name__ == '__main__':
    main()