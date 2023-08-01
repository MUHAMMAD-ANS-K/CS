def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if 7 > len(s) > 1:
        r_one = True
    else:
        return False
    if s[0].isalpha() and s[1].isalpha():
        r_two = True

    r_three = True
    for i in range(len(s)):
        if s[i].isdecimal():
            while i > len(s):
                if s[i].isalpha():
                    r_three = false
                    break
                i += 1
    if r_one == True and r_two == True and r_three == True:
        return True
main()
