def main():
    camelCase = input('camelCase: ')
    for i in camelCase:
        print(f'_{i.lowe()}') if i.isupper() else print(i)
main()