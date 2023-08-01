def main():
    t = convert(input('What time is it?'))
    if 7.0 <= t <= 8.0:
        print('Breakfast')

def convert(time):
    hours, minutes = time.split(':')
    minutes = float(minutes) / 60
    hours = round(float(hours) + minutes, 1)
    return hours


#if __name__ == "__main__":

main()