while True:
    try:
        height = int(input("Height: "))
        if 9 > height > 0:
            break
    except ValueError:
        pass
for i in range(1, height + 1):
    print(" " * (height - i), "#" * i, "  ", "#" * i, sep="")
