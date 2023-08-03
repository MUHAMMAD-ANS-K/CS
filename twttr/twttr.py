def main():
    in_put = input('Input: ')
    print(shorten(in_put))


def shorten(word):
    out = word.lower()
    short = ''
    j = 0
    for i in out:
        match i:
            case 'a' | 'e'| 'i' | 'o' | 'u':
                pass
            case _ :
                short += word[j]
        j += 1
    return short

if __name__ == "__main__":
    main()