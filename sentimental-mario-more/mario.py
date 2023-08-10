while True:
    try:
        height = int(input("Height: "))
        if 9 > height > 0:
            break
    except ValueError:
        pass
# A for loop in range from 1 to height.
for i in range(1, height + 1):
    # Printing all the stuff by setting sep parameter to empty.
    print(" " * (height - i), "#" * i, "  ", "#" * i, sep="")
