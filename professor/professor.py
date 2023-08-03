import random


def main():
    level = get_level()
    score = 0
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        total = x + y
        for i in range(3):
            print(f"{x} + {y} =", end="")
            try:
                user_input = int(input(" "))
            except ValueError:
                print("EEE")
            if user_input != total:
                print("EEE")
            elif user_input == total:
                score += 1
                break
        if user_input != total:
            print(f"{x} + {y} = {total}")
    print(f"Score: {score}")


def get_level():
    while True:
        n = input("Level: ").strip()
        if n == "1" or n == "2" or n == "3":
            return n


def generate_integer(level):
    while True:
        try:
            level = int(level)
            if level == 1:
                number = random.randint(0, 9)
                return number
            elif level == 2:
                number = random.randint(10, 99)
                return number
            else:
                number = random.randint(100, 999)
                return number
        except ValueError:
            get_level()


if __name__ == "__main__":
    main()
