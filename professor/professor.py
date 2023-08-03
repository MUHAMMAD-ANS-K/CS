def main():
    while True:
        try:
            n = int(input('Level: ').strip())
            if n == 1 or n == 2 or n == 3:
                break
        except ValueError:
            pass

main()