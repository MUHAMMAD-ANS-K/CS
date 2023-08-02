def main():
    items = dict()
    while True:
        try:
            item = input().strip().upper()
            items[key] = item
        except EOFError:
            pass
            return
    print(items)




main()