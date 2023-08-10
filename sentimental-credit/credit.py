

number = input('Number: ')
numbers = list()
for i in number:
    numbers.append(int(i))
sum = 0
for j in range(-2,-len(numbers) - 1,-2):
    num = numbers[j] * 2
    sum += (num / 10) + (num % 10) if num > 9 else
print(sum)





