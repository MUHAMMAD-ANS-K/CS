def main():
    number = input("Number: ")
    if card(number) == "INVALID":
        print("INVALID")
    numbers = list()
    for i in number:
        numbers.append(int(i))
    sum = 0
    range_stop = -len(numbers) - 1
    for j in range(-2, range_stop, -2):
        num = numbers[j] * 2
        if num > 9:
            sum += int((num / 10)) + (num % 10)
        else:
            sum += num
    for k in range(-1, range_stop, -2):
        sum += numbers[k]

    if sum % 10 == 0:
        print(card(number))
    else:
        print("INVALID")


def card(number):
    if number.startswith(("34", "37")) and len(number) == 15:
        return "AMEX"
    if number.startswith(("51", "52", "53", "54", "55")) and len(number) == 16:
        return "MASTERCARD"
    if number.startswith("4") and (len(number) == 13 or len(number) == 16):
        return "VISA"
    else:
        return "INVALID"


if __name__ == "__main__":
    main()
