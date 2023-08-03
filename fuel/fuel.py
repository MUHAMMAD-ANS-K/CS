def main():
    fraction = input('Fraction: ')
    fraction = convert(fraction)


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
    if fraction <= 1:
        return 'E'
    elif fraction >= 99:
        return 'F'
    else:
        print(f'{fraction}%')

main()
