import sys
def main():
    lines = 0
    file_name = sys.argv[1]
    with open(file_name) as file:
        for line in file:
            line = line.lstrip()
            if line

print(lines)
if __name__ == '__main__':
    main()