def main():
    fraction = input('Fraction: ')
    fraction = convert(fraction)
    if fraction <= 1:
        print('E')
    elif fraction >= 99:
        print('F')
    else:
        print(f'{fraction}%')

def get_fraction(fract):
    while True:
        try:
            x,y = fract.split('/')
            x = int(x)
            y = int(y)
            if x <= y:
                return round((x / y) * 100)
        except ValueError:
            pass
        except ZeroDivisionError:
            pass



main()
