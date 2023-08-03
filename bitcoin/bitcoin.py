import requests
import json
import sys

def main():
    try:
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json').json()
        bpi = response['bpi']
        USd = bpi['USD']
        rate = USd['rate_float'] * float(sys.argv[1])
        print(f'${rate:,.4f}')
    except ValueError:
        sys.exit('Command-line argument is not a number')
    except IndexError:
        sys.exit('Missing command-line argument')

if __name__ == '__main__':
    main()