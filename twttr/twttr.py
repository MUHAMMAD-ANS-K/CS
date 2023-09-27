def main():
    user_input = input("Input: ").strip().lower()
    for chr in user_input:
        match(chr):
            case 'a' | 'e' | 'i' | 'o' | 'u':
                pass
            case _:
                print(chr,end='')
    print()
if __name__ == "__main__":
    main()