import sys
def main():
    
    file_name = sys.argv[1]
    with open(file_name) as file:
        for line in file:
            print(line.rstrip())
if __name__ == '__main__':
    main()