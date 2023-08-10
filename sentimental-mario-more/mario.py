while True:
    try:
        height = int(input('Height: '))
        if 9 > height > 0:
            break
    except ValueError:
        pass
for i in range(height):
    print