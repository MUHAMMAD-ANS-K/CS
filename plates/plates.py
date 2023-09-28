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
    for char in s:
        if char == "." or char == " " or char == "," or char == "!":
            return False
    for i in range(len(s) - 2):
        if s[i + 1].isnumeric():
            if s[i + 1] == "0":
                return False
            while (i + 1) < len(s):
                if s[i + 1].isalpha():
                    return False
                i += 1
            return True
    return True

main()