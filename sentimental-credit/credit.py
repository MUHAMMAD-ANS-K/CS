import re

number = int(input('Number: '))
numbers = list()
for _ in range(len(number)):
    numbers.append(number % 10)
    number = number / 10

print(numbers)
