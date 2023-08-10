import re

number = input('Number: ')
numbers = list()
for i in number:
    numbers.append(int(i))
for j in range(-2,-len(numbers) - 1,-2):
    print(numbers[j],end = '')



