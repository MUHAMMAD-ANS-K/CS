def main():
    camelCase = input('camelCase: ')
    i = 0
    while i < len(camelCase):
        if camelCase[i].isupper():
            camelCase[i] = '_' + camelCase[i].lower()
        i += 1
    print('snake_case:', camelCase)
main()