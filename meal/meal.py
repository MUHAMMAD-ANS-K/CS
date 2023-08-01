def main():
    t = input('What time is it?')
    print(convert(t))


def convert(time):
    hours, minutes = float(split(':'))
    minutes = minutes / 60
    hours = round(hours + minutes, 1)
    return hours


#if __name__ == "__main__":

main()