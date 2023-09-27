def main():
    time = input("What time is it? ").strip()
    time = convert(time)
    if 8.0 => time => 7.0:
        print

def convert(time):
    hours, minutes = time.split(":")
    return (int(hours) + int(minutes) / 60.0)

if __name__ == "__main__":
    main()