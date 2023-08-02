def main():
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
    ]
    while True:
        try:
            month,day,year = input('Date: ').split('/')
            month = int(month)
            day = int(day)
            if month <= 12 and day <= 31:
                break
        except ValueError:
            pass
    print(f'{year}-{month:02}-{day:02}')

main()