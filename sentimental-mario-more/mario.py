while True:
    try:
        height = int(input('Height: '))
        if height > 0:
            break
    except ValueError:
        pass