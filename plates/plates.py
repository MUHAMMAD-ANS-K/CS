def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2:
        return False
    for chr in s[:2]:
        if chr.isnumeric():
            return False
    for i in range(len(s) - 2):
        if s[i + 1].isnumeric():
            temp = s[i + 1]
            return False

    return True

main()