def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isalpha() and s[1].isalpha():
        r_one = True
    if 7 > len(s) > 2:
        r_two = True
    for i in range(len(s)):
        if s[i].isdecimal():
            while i 
main()
