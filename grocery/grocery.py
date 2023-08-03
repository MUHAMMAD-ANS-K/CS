def main():
    items = {}
    while True:
        try:
            item = input().strip().upper()
            found = False
            for key in items:
                if item == key:
                    items[item] += 1
                    found = True
            if found == False:
                items[item] = 1
        except EOFError:
            break
    sorted_names = sorted(items)
    for j in range(len(sorted_names)):
        for key_item in items:
            if sorted_names[j] == key_item:
                print(f"{items[key_item]} {sorted_names[j]}")


main()
