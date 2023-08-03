import random
import sys
def main():
    level = get_int('Level: ')
    number = random.randint(1,level)

    while True:
        guess = get_int('Guess: ')
        if guess > number:
            print('Too large!')
        elif guess < number:
            print('Too small!')
        else:
            sys.exit('Just right!')

def get_int(prompt):
    while True:
        try:
            n = int(input(prompt))
            if n > 0:
                return n
        except ValueError:
            pass





main()