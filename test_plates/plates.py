def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (7 > len(s) > 1):
        return False
    #if not (s[0].isalpha() and s[1].isalpha()):
     #   return False
    for k in range(len(s)):
        if s[k] == " " or s[k] == "." or s[k] == "," or s[k] == "!":
            return False
    for i in range(len(s)):
        if s[i].isdecimal():
            if s[i] == "0":
                return False
            while i < len(s):
                if s[i].isalpha():
                    return False
                i += 1
            return True
    return True


if __name__ == "__main__":
    main()
