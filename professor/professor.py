import random

def main():
    level = get_level('Level: ')
    score = 0
    for _ in range(10):
        x = random.randint(1,9) * 10 ** (level - 1)
        y = random.randint(1,9) * 10 ** (level - 1)
        total = x + y
        for i in range(3):
            print(f'{x} + {y} = ', end = '')
            try:
                user_input = int(input())
            except ValueError:
                print('EEE')
            if user_input != total:
                print('EEE')
            elif user_input == total:
                score += 1
                break
        if user_input != total:
            print(total)
    print(score)


def get_level(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n == 1 or n == 2 or n == 3:
                return n
        except ValueError:
            pass


main()