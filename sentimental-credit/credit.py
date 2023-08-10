import re

number = input('Number: ')
numbers = list()
for i in number:
    numbers.append(int(i))
for j in range(len(numbers)/2):
    print(numbers[-2])


