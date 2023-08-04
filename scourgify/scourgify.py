import sys
import csv
def main():
    if len(sys.argv) > 3:
        sys.exit("Too many command-line arguments")
    elif len(sys.argv) == 1:
        sys.exit("Too few command-line arguments")
    students = []
    try:
        file_read = sys.argv[1]
        file_write = sys.argv[2]
        with open(file_read) as file1:
            reader = csv.DictReader(file1)
            for dic in reader:
                students.append(dic)
        with open(file_write) as file2:
            
    except FileNotFoundError:
        sys.exit(f'Could not read {sys.argv[1]}')

if __name__ == '__main__':
    main()