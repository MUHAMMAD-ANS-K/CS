def main():
    camel = input("camelCase: ")
    for chr in camel:
        if chr.isupper():
            print(f"_{chr.lower()}",end='')
        else:
            print(chr,end='')
    print()

if __name__ == "__main__":
    main()