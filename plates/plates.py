def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0].isalpha() and s[1].isalpha():
        return True
    #for char in s:



main()
