def main():
    camelCase = input('camelCase: ')
    for i in camelCase:
        if i.isupper():
            i.lower()
    print('snake_case:', camelCase)
main()