def main():
    in_put = input('Input: ')
    out = in_put.lower()
    j = 0
    for i in out:
        if i != 'a' or i != 'e' or i != 'i' or i != 'o' or i != 'u':
            print(in_put[j])
        j += 1

main()