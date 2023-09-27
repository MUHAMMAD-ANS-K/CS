def main():
    cents = 50
    while cents > 0:
        print(f"Amount Due: {cents}")
        coin = int(input("Insert Coin: ").strip())
        if coin == 5 or coin == 10 or coin == 25:
            cents -= coin
    print(f"Change Owed: {abs(cents)}")
if __name__ == "__main__":
    main()