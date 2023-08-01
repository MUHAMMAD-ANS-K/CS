def main():
    in_put = input('Input: ')
    out = in_put.lower()
    j = 0
    for i in out:
        match i:
            case 'a':
            case 'e':
            case 'i':
            case 'o':
            case 'u':
            case _ :
                print(in_put[j],end = '')
        j += 1
    print()
main()