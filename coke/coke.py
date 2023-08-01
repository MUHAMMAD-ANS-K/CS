def main():
    total_cents = 50
    while(total_cents > 0):
        print(f'Amount Due: {total_cents}')
        s = int(input('Insert Coin: '))
        total_cents -= s
        if(total_cents =< 0):
            print(f'Change Owed: {abs(total_cents)}')

main()