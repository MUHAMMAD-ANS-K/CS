import random

def main():
    level = get_level('Level: ')
    for _ in range(10):
        x = rand_int()
        y = rand_int()
        total = x + y
        print(f'{x} + {y} = ', end = '')
        for i in range(3):
            try:
                user_input = int(input())
            except ValueError:
                print('EEE')
            if user_input != total:
                print('EEE')


def get_level(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n == 1 or n == 2 or n == 3:
                return n
        except ValueError:
            pass

def rand_int():
    return random.randint(1,10) * 10 ** level
main()