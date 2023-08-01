def main():
    t = convert(input('What time is it?'))
    if 7.0 <= t <= 8.0:
        print('breakfast time')
    elif 12.0 <= t <= 13.0:
        print('lunch time')
    elif 18.0 <= t <= 19.0:
        print('dinner time')

def convert(time):
    hours, minutes = time.split(':')
    minutes = float(minutes) / 60
    hours = round(float(hours) + minutes, 1)
    return hours


#if __name__ == "__main__":

main()