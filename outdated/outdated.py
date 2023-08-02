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
            date = input('Date: ').strip()
            month,day,year = date.split('/')
            break
        except ValueError:
            try:
                month,day,year = date.split(' ')
                day = day.rstrip(',')
                for i in range(len(months)):
                    if month == months:
                        month = i + 1
                        break
            except ValueError:
                pass
    month = int(month)
    day = int(day)
    if month <= 12 and day <= 31:
    print(f'{year}-{month:02}-{day:02}')

main()