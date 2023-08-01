def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not(7 > len(s) > 1):
        return False
    if not(s[0].isalpha() and s[1].isalpha()):
        return False

    for i in range(len(s)):
        if s[i].isdecimal():
            j = i + 1
            break
    while int(j) > len(s):
        if s[j].isalpha():
            return False
        j += 1

    return True
main()
