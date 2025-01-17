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
            month = int(month)
            day = int(day)
            if month <= 12 and day <= 31:
                print(f'{year}-{month:02}-{day:02}')
                break
        except ValueError:
            try:
                month,day,year = date.split(' ')
                day,j = day.split(',')
                for i in range(len(months)):
                    if month == months[i]:
                        month = i + 1
                        break
                month = int(month)
                day = int(day)
                if month <= 12 and day <= 31:
                    print(f'{year}-{month:02}-{day:02}')
                    break
            except ValueError:
                pass


main()