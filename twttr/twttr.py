def main():
    input = input('Input: ')
    output = input.lower()
    j = 0
    for i in output:
        if i != 'a' or i != 'e' or i != 'i' or i != 'o' or i != 'u':
            print(input[j])
        j += 1

main()