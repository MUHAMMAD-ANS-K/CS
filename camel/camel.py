def main():
    camelCase = input('camelCase: ')
    for i in camelCase:
        print(f'_{i.lower()}') if i.isupper() else print(i)
main()