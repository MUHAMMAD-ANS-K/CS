def main():
    s = input()
    print(convert(s))


def convert(n):
    n = n.replace(':)', '🙂')
    n = n.replace(':(','🙁')
    return n
main()