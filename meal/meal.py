def main():
    time = input("What time is it? ").strip()


def convert(time):
    hours, minutes = int(time.split(":"))
    return hours + minutes/60

if __name__ == "__main__":
    main()