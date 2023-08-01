def main():
    camelCase = input('camelCase: ')
    i = 0
    while i < len(camelCase):
        if camelCase[i].isupper():
            camelCase[i] = ''
main()