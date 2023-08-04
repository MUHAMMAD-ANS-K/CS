import sys
def main():
    lines = 0
    #file_name = sys.argv[1]
    with open('figlet.py') as file:
        for line in file:
            #line = line.lstrip()
            if line.startswith(' '):
                pass
            else:
                lines += 1

    print(lines)
if __name__ == '__main__':
    main()