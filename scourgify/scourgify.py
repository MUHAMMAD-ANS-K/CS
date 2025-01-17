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
                last, first = dic["name"].split(",")
                students.append(
                    {"first": first.lstrip(), "last": last, "house": dic["house"]}
                )
    except FileNotFoundError:
        sys.exit(f"Could not read {sys.argv[1]}")
    with open(file_write, "w") as file2:
        field_names = ["first", "last", "house"]
        writer = csv.DictWriter(file2, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(students)


if __name__ == "__main__":
    main()
