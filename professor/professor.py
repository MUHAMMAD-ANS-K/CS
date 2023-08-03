import sys
def main():
    level = get_level()



def get_level():
    while True:
        try:
            n = int(input('Level: ').strip())
            if n == 1 or n == 2 or n == 3:
                sys.exit()
        except ValueError:
            pass

if __name__ == '__main__':
    main()
