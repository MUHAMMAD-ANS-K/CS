def main():
    user_input = input("Input: ").strip()
    for chr in user_input:
        c = chr.lower()
        match(c):
            case 'a' | 'e' | 'i' | 'o' | 'u':
                pass
            case _:
                print(chr,end='')
    print()
if __name__ == "__main__":
    main()