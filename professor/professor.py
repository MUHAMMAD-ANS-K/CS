import random

def main():
    level = get_level('Level: ')
    for i in range(10):
        x =
        y = random.randint(1,10) * 10 ** level
        total = x + y
        print(f'{x} + {y} = ', end = '')
        try:
            user_input = int(input())
        except ValueError:
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
    random.randint(1,10) * 10 ** level
main()