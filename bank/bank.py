def main():
    greet = input("Greeting: ").casefold().strip()
    print('$' + value(greet))
def value(greeting):
    if greeting.startswith('hello'):
        return '0'
    elif greeting.startswith('h'):
        return '20'
    else:
        return '100'

if __name__ == '__main__':
    main()

