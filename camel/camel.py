def main():
    camelCase = input('camelCase: ')
    print('snake_case: ',end = '')
    for i in camelCase:
        print(f'_{i.lower()}', end = '') if i.isupper() else print(i, end ='')
    print()

main()