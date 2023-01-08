# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]
# lst1=[2, 3, 4, 5, 6]
# lst1=[2, 3, 5, 6]
import random
number = int(input('Введите размер списка '))
lst1 = []
lst = []
for i in range(number):
    lst1.append(random.randint(0, 9))
for i in range(len(lst1)):
    while i < len(lst1)/2 and number > len(lst1)/2:
        number = number - 1
        a = lst1[i] * lst1[number]
        lst.append(a)
        i += 1

print(lst1)
print(lst)