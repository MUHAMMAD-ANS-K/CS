def main():
    camel = input("camelCase: ")
    for chr in camel:
        if chr.isupper():
            print(f"_{chr.lower()}")

if __name__ == "__main__":
    main()