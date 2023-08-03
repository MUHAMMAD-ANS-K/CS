def main():
    level = get_level('Level: ')






def get_level(prompt):
    while True:
        try:
            n = int(input(prompt).strip())
            if n == 1 or n == 2 or n == 3:
                return n
        except ValueError:
            pass

main()