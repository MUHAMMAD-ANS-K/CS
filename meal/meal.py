def main():
    t = input('What time is it?')
    print(convert(t))


def convert(time):
    hours, minutes = time.split(':')
    minutes = float(minutes) / 60
    hours = round(float(hours) + minutes, 1)
    return hours


#if __name__ == "__main__":

main()