def main():
    in_put = input('Input: ')
    out = in_put.lower()
    j = 0
    for i in out:
        match i:
            case 'a' | 'e'| 'i' | 'o' | 'u':
                None
            case _ :
                print(in_put[j],end = '')
        j += 1
    print()
main()