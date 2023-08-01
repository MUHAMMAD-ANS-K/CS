def main():
    total_cents = 50
    while(total_cents > 0):
        print(f'Amount Due: {total_cents}')
        s = get_input()
        if s == 25 or s == 10 or s == 5:
            total_cents -= s
        if(total_cents <= 0):
            print(f'Change Owed: {abs(total_cents)}')
def get_input():
    while True:
        n = int(input('Insert Coin: '))
        if n > 0:
            return n
main()