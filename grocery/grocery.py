def main():
    item = {}
    while True:
        try:
            for i in range(5):
                item[i] = input().upper
        except EOFError:
            pass
            return





main()