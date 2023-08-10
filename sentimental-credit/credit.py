number = input("Number: ")
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



print(sum)



def card(list_num):
    if 