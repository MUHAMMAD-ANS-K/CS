expression = input('Expression: ')
x, y , z = expression.split()
if y.startswith('+'):
    print(float(x) + float(z))
elif y.startswith('-'):
    print(float(x) - float(z))
elif y.startswith('*'):
    print(float(x) * float(z))
elif y.startswith('/'):
    print(float(x) / float(z))