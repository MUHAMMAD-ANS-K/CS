import random
from prompt import get_level
def main():
    level = get_level()
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

main()