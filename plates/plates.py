def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if !(7 > len(s) > 1):
        return False
    if s[0].isalpha() and s[1].isalpha():
        r_two = True
    else:
        return False

    r_three = True
    for i in range(len(s)):
        if s[i].isdecimal():
            while i > len(s):
                if s[i].isalpha():
                    return False
                i += 1
    return True
main()
