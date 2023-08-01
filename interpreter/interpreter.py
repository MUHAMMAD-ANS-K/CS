expression = input('Expression: ')
x, y , z = expression.split()
if y.startswith('+'):
    print(f'{float(x) + float(z) : .1f}')
elif y.startswith('-'):
    print(f'{float(x) - float(z) : .1f}')
elif y.startswith('*'):
    print(f'{float(x) * float(z) : .1f}')
elif y.startswith('/'):
    print(f'{float(x) / float(z) : .1f}')