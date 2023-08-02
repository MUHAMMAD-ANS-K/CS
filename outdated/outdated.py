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
                    month = i
            if int(month) <= 12 and int(day) <= 31:
                break
        except ValueError:
            pass
    print(f'{month} {day} {year}')

main()