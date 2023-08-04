import sys
def main():
    if len(sys.argv) > 2:
        sys.exit('Too many command-line arguments')
    name,type = sys.argv[1]

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
        sys.exit('File does not exist')
    except IndexError:
        sys.exit('Too few command-line arguments')

    print(lines)
if __name__ == '__main__':
    main()