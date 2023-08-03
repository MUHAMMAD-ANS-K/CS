def main():
    fraction = input('Fraction: ')
    percent = convert(fraction)
    print(gauge(percent))

def convert(fract):
    while True:
        try:
            x,y = fract.split('/')
            x = int(x)
            y = int(y)
            if x <= y:
                return round((x / y) * 100)
        except ValueError:
            fract = input('Fraction: ')
            pass
        except ZeroDivisionError:
            fract = input('Fraction: ')
            pass

def gauge(percentage):
    if percentage <= 1:
        return 'E'
    elif percentage >= 99:
        return 'F'
    else:
        return (f'{percentage}%')

if __name__ == '__main__':
    main()
