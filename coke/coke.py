def main():
    total_cents = 50
    while(total_cents > 0):
        print(f'Amount Due: {total_cents}')
        s = int(input)
        total_cents -= s
        if(total_cents <= 0):
            print(f'Change Owed: {abs(total_cents)}')
def get_input():
    while True:
        n = int(input('Insert Coin: '))
        if n > 0:
            break

main()