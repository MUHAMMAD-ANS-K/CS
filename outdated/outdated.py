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
            for i in range(len(months)):
                if months[i] == month:
                    month = i + 1
            month = int(month)
            day = int(day)
            if month <= 12 and day <= 31:
                break
        except ValueError:
            pass
    print(f'{year}-{month:.1f}-{day}')

main()