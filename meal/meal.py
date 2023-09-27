def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if time

def convert(time):
    hours, minutes = time.split(":")
    return (int(hours) + int(minutes) / 60.0)

if __name__ == "__main__":
    main()